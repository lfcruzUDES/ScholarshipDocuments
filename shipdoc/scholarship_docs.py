""" This file has the class that executes al process."""


import datetime
import os
import re
import uuid

from googleapi.gdrive import Drive
from googleapi.gss import GSS
from PyPDF4 import PdfFileReader, PdfFileWriter, utils

import shipdoc.settings as settings
from shipdoc.logger import LogHandler

#from dataclasses import dataclass




class ScholarshipDocs:
    """ This class executes all process. """

    _ss_docs = None
    _ss_student_info = None
    _ss_index = None
    _drive = None

    _rows_doc = []
    _rows_scholarship = []
    _rows_index = None

    _execution_id = None

    _emails_processed = []

    # alter 'magick'
    _mode = 'pypdf'

    def __init__(self, mode='pypdf'):
        self._ss_docs = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_DOCS_ID,
            settings.DOCS_RANGE_NAME
        )
        self._ss_student_info = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_SOLICITUDES_BECA,
            settings.SOLICITUDES_BECA_RANGE
        )
        self._ss_index = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_INDEX_ID,
            settings.INDEX_RANGE_NAME
        )
        self._drive = Drive(settings.SECRETG, settings.DRIVE_SCOPES)

        self._create_start_configs()

        self._rows_doc = self._ss_docs.get_data()
        self._rows_scholarship = self._ss_student_info.get_data()
        self._rows_index = self._ss_index.get_data()
        self._emails_processed = [row[1] for row in self._rows_index]

        self._mode = mode

    def _create_start_configs(self):
        date = datetime.date.today()
        self._execution_id = f'{date.year}_{date.month}'

        if not settings.SAVE_PATH.exists():
            settings.SAVE_PATH.mkdir()


    def _get_enrollment_by_email(self, email):
        """ Get enrollment by email. """

        for row in self._rows_scholarship:

            if email.strip() == row[0].strip():
                return row[2]

        return None

    def _is_processed(self, email):
        """ Check if data student is already processed. """

        if email in self._emails_processed:
            return True

        return False


    def _get_id_file(self, http_file):
        """ Extract id from  """

        sub_str = re.search('[\w-]{10,}', http_file);

        return sub_str.group();

    def _download_files(self, row):
        """ Download files and return a list of its paths. """

        documents_to_download = row[2:7]
        documents_downloaded = []
        full_file = settings.SAVE_PATH / row[-1].replace(' ', '_')

        for doc in documents_to_download:
            if 'http' in doc:
                doc_id = self._get_id_file(doc)
                doc_path = settings.SAVE_PATH / f'{uuid.uuid4().hex}.pdf'
                doc_downloaded = self._drive.download_file(doc_id, doc_path)

                if doc_downloaded:
                    documents_downloaded.append(doc_downloaded)

        return documents_downloaded

    def _upload_file(self, name, file_path):
        """ Upload file. """

        file_id = self._drive.upload_file(
            name,
            file_path,
            folders=[settings.DRIVE_DOCUMENTS_FOLDER]
        )

        url = f'https://drive.google.com/open?id={file_id}'

        return url


    def _merge_documents_PyPDF4(self, file_name, paths):
        """ Merge documents. """
        output = settings.SAVE_PATH / file_name
        try:
            pdf_writer = PdfFileWriter()

            for file_path in paths:
                if file_path:
                    pdf_reader = PdfFileReader(str(file_path), strict=False)

                    for page in range(pdf_reader.getNumPages()):
                        # Add each page to the writer object
                        pdf_writer.addPage(pdf_reader.getPage(page))

            # Write out the merged PDF
            output = settings.SAVE_PATH / file_name
            with open(output, 'wb') as out:
                pdf_writer.write(out)

            return output
        except utils.PdfReadError as error:
            LogHandler.execution_log(error=error)
            LogHandler.execution_log(
                error=f'ERROR ON: {output.name.replace(".PDF", "")}'
            )

            return output

    def _merge_documents_imagemagick(self, file_name, paths):

        full_file = settings.SAVE_PATH / file_name

        documents = [str(path) for path in paths]

        command = f'convert {" ".join(documents)} {str(full_file)}'

        convert = os.system(command)

        return full_file

    def _unlink_individual_docs(self, documents):
        """ Remove files from local storage. """

        for doc in documents:
            doc.unlink()

    def _save_in_index(self, row):
        """ Save data in Index Sheet. """

        cells_updated = self._ss_index.append([row])

        return cells_updated

    def process(self, mode='pypdf', save_in_index=True):
        """ Executes all process. """

        if mode == 'magick':
            self._mode = mode

        LogHandler.execution_log(action='START')

        for row in self._rows_doc:

            if not self._is_processed(row[1]):
                student_name = row[7].strip().replace(' ', '_')

                enrollment = self._get_enrollment_by_email(row[1])

                documents = self._download_files(row)

                file_name = f'{enrollment}_{self._execution_id}_{student_name}_FULL.pdf'.upper()

                if self._mode == 'pypdf':
                    full_file = self._merge_documents_PyPDF4(file_name, documents)
                elif self._mode == 'magick':
                    full_file = self._merge_documents_imagemagick(file_name, documents)
                else:
                    raise Exception('No PDF merge method setted or is setted wrong key word.')

                # full_file_url = self._upload_file(file_name, full_file)

                self._unlink_individual_docs(documents)

                if full_file.exists():
                    LogHandler.execution_log(action=f'Created file: {full_file}')

                    if save_in_index:
                        self._save_in_index([
                            enrollment,
                            row[1],
                            row[7].upper(),
                            file_name,
                        ])

        LogHandler.execution_log(action='END')
