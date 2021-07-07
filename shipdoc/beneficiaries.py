import datetime

from googleapi.gdrive import Drive
from googleapi.gss import GSS
from PyPDF4 import PdfFileReader, PdfFileWriter, utils

import shipdoc.settings as settings
from shipdoc.scholarship_docs import ScholarshipDocs


class Beneficiaries(ScholarshipDocs):
    """ Handles beneficiaries. """

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
        self._solicitudes_beca_index = [b[2].strip() for b
                                        in self._solicitudes_beca_data

                                        if len(b) >= 3]

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
        self._reporte_sep_index = [d[2].strip() for d
                                   in self._reporte_sep_data]

    def _get_index(self, elemet, data_list):
        try:
            return data_list.index(elemet)
        except ValueError:
            return False

    def run(self):
        for beca in self._revision_becas_data:
            enrollment = beca[0]
            name = beca[1]
            career = beca[2]
            group = beca[3]
            scholarship = beca[8]
            situtation = beca[9]
            scholarship_type = beca[10]
            average = beca[11]

            if (not enrollment in self._reporte_sep_index
                and 'SEP' in scholarship_type):
                email_id = self._get_index(
                    enrollment,
                    self._solicitudes_beca_index
                )
                email = (self._solicitudes_beca_data[email_id][0]
                         if email_id
                         else False)
                docs = self._get_index(
                    email,
                    self._documentos_beca_data
                )
                boleta = self._get_index(
                    enrollment,
                    self._boletas_index_data
                )

                if boleta:
                    print(boleta)

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
                        1
                    ]
                else:
                    print(enrollment, email, name)
