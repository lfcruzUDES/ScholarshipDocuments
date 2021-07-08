import datetime
import re

from googleapi.gdrive import Drive
from googleapi.gss import GSS
from PyPDF4 import PdfFileReader, PdfFileWriter, utils

import shipdoc.settings as settings
from shipdoc.logger import LogHandler
from shipdoc.scholarship_docs import ScholarshipDocs


class Beneficiaries(ScholarshipDocs):
    """ Handles beneficiaries. """

    _data_to_save = []

    _revision_becas = None
    _revision_becas_data = []
    _revision_becas_index = []

    _solicitudes_beca = None
    _solicitudes_beca_data = []
    _solicitudes_beca_index = []

    _documentos_beca = None
    _documentos_beca_data = []
    _documentos_beca_index = []

    _boletas_index = None
    _boletas_index_data = []
    _boletas_index_index = []

    _reporte_sep = None
    _reporte_sep_data = []
    _reporte_sep_index = []

    def __init__(self):

        self._create_start_configs()

        self._drive = Drive(settings.SECRETG, settings.DRIVE_SCOPES)

        self._revision_becas = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_REVISION_BECAS,
            settings.REVISION_BECAS_RANGE
        )
        self._revision_becas_data = self._revision_becas.get_data()
        self._revision_becas_index = [a[0].strip() for a
                                      in self._revision_becas_data]

        self._solicitudes_beca = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_SOLICITUDES_BECA,
            settings.SOLICITUDES_BECA_RANGE
        )
        self._solicitudes_beca_data = self._solicitudes_beca.get_data()

        for b in self._solicitudes_beca_data:
            try:
                self._solicitudes_beca_index.append(b[2])
            except IndexError:
                print(b)
                self._solicitudes_beca_index.append('')

        self._rows_scholarship = self._solicitudes_beca_data

        self._documentos_beca = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_DOCS_ID,
            settings.DOCS_RANGE_NAME
        )
        self._documentos_beca_data = self._documentos_beca.get_data()
        # Email as key reference.
        self._documentos_beca_index = [c[1].strip() for c
                                       in self._documentos_beca_data]

        self._boletas_index = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_BOLETAS_INDEX,
            settings.BOLETAS_INDEX_RANGE
        )
        self._boletas_index_data = self._boletas_index.get_data()
        self._boletas_index_index = [e[0].strip() for e
                                     in self._boletas_index.get_data()]

        self._reporte_sep = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_REPORTE_SEP,
            settings.REPORTE_SEP_RANGE
        )

        self._reporte_sep_data = self._reporte_sep.get_data()

        if len(self._reporte_sep_data) > 0:
            self._reporte_sep_index = [d[2] for d
                                       in self._reporte_sep_data]
        else:
            self._reporte_sep_data = []

    def _get_index(self, element, data_list):
        try:
            return data_list.index(element)
        except ValueError:
            return False

    def run(self, mode='pypdf'):
        LogHandler.execution_log(action='BENEFICIARIES START')

        for beca in self._revision_becas_data:
            enrollment = beca[0]
            name = beca[1]
            career = beca[2]
            group = beca[3]
            scholarship = beca[8]
            situtation = beca[9]
            scholarship_type = beca[10]
            average = beca[11]

            if enrollment in self._reporte_sep_index:
                continue

            if not 'SEP' in scholarship_type:
                continue

            email_id = self._get_index(
                enrollment,
                self._solicitudes_beca_index
            )
            email = (self._solicitudes_beca_data[email_id][0]
                     if email_id
                     else False)

            if email:
                dataToSave = [
                    str(datetime.datetime.now()),
                    email,
                    enrollment,
                    name,
                    career,
                    group,
                    average,
                    scholarship_type,
                    '',
                    '',
                    scholarship,
                    '',
                    situtation,
                    '',
                    1,
                    '',
                ]

                observation_id = len(dataToSave) - 1

                docs_id = self._get_index(
                    email,
                    self._documentos_beca_index
                )


                if not enrollment in self._boletas_index_index:
                    print('Boleta IndexError', enrollment, email, name)
                    dataToSave[observation_id] += 'FALTA_BOLETA'
                    LogHandler.execution_log(
                        error=f'FALTA BOLETA {enrollment} {email} {name}'
                    )

                    continue

                boleta_id = self._get_index(
                    enrollment,
                    self._boletas_index_index
                )
                boleta = None
                boleta = self._boletas_index_data[boleta_id][1]

                docs = self._documentos_beca_data[docs_id]
                docs[3] = boleta
                self._rows_doc.append(docs)
                self._data_to_save.append(dataToSave)
            else:
                print(enrollment, email, name)

        # Save data to Spreadsheet
        self._reporte_sep.append(self._data_to_save)
        self.process(mode=mode, save_in_index=False)
        LogHandler.execution_log(action='BENEFICIARIES END')
