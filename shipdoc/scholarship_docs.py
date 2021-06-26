""" This file has the class that executes al process."""


import datetime
import re
import uuid

from googleapi.gdrive import Drive
from googleapi.gss import GSS
from PyPDF4 import PdfFileReader, PdfFileWriter

import shipdoc.settings as settings
from shipdoc.logger import LogHandler

#from dataclasses import dataclass




class ScholarshipDocs:
    """ This class executes all process. """

    _ss = None
    _drive = None

    _rows_doc = None
    _rows_scholarship = None

    _execution_id = None

    def __init__(self, ss_id=None, range_name=None):
        self._ss = GSS(settings.SECRETG, settings.SS_SCOPES)
        self._drive = Drive(settings.SECRETG, settings.DRIVE_SCOPES)
        date = datetime.date.today()
        self._execution_id = f'{date.year}_{date.month}'

        if not settings.SAVE_PATH.exists():
            settings.SAVE_PATH.mkdir()

        self._rows_doc = self._ss.get_data(
            ss_id if ss_id else settings.SPREADSHEET_DOCS_ID,
            range_name if range_name else settings.DOCS_RANGE_NAME
        )
        self._rows_scholarship = self._ss.get_data(
            settings.SPREADSHEET_SCHOLARSHIP_ID,
            settings.SCHOLARSHIP_RANGE_NAME
        )

    def _get_enrollment_by_email(self, email):
        """ Get enrollment by email. """

        for row in self._rows_scholarship:
            if email in row[0]:
                return row[2]

    def _get_id_file(self, http_file):
        """ Extract id from  """

        sub_str = re.search('[^=][\w-]+$', http_file);

        return sub_str.group();

    def _download_files(self, row):
        """ Download files and return a list of its paths. """

        documents_to_download = row[3:7]
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

    def _merge_documents(self, file_name, paths):
        """ Merge documents. """
        pdf_writer = PdfFileWriter()

        for file_path in paths:
            if file_path:
                pdf_reader = PdfFileReader(str(file_path))

                for page in range(pdf_reader.getNumPages()):
                    # Add each page to the writer object
                    pdf_writer.addPage(pdf_reader.getPage(page))

        # Write out the merged PDF
        output = settings.SAVE_PATH / file_name
        with open(output, 'wb') as out:
            pdf_writer.write(out)

        return output

    def _unlink_individual_docs(self, documents):
        for doc in documents:
            doc.unlink()

    def process(self):
        """ Executes all process. """

        LogHandler.execution_log(action='START')

        for row in self._rows_doc:
            student_name = row[7].strip().replace(' ', '_')
            enrollment = self._get_enrollment_by_email(row[1])
            documents = self._download_files(row)
            full_file = self._merge_documents(
                f'{enrollment}_{self._execution_id}_{student_name}_FULL.pdf'.upper(),
                documents
            )
            self._unlink_individual_docs(documents)
            LogHandler.execution_log(action=f'Created file: {full_file}')

        LogHandler.execution_log(action='END')
