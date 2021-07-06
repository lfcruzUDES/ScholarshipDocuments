from googleapi.gss import GSS

import shipdoc.settings as settings


class Beneficiaries():
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

        self._revision_becas = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_REVISION_BECAS,
            settings.REVISION_BECAS_RANGE
        )
        self._revision_becas_data = self._revision_becas.get_data()
        self._revision_becas_index = [a[0] for a
                                      in self._revision_becas_data ]

        self._solicitudes_beca = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_SOLICITUDES_BECA,
            settings.SOLICITUDES_BECA_RANGE
        )
        self._solicitudes_beca_data = self._solicitudes_beca.get_data()
        self._solicitudes_beca_index = [b[3] for b
                                        in self._solicitudes_beca_data ]

        self._documentos_beca = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_DOCS_ID,
            settings.DOCS_RANGE_NAME
        )
        self._documentos_beca_data = self._documentos_beca.get_data()
        # Email as key reference.
        self._documentos_beca_index = [c[1] for c
                                       in self._documentos_beca_data]

        self._boletas_index = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_BOLETAS_INDEX,
            settings.BOLETAS_INDEX_RANGE
        )
        self._boletas_index_data = self._boletas_index.get_data()

        self._reporte_sep = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            settings.SPREADSHEET_REPORTE_SEP,
            settings.REPORTE_SEP_RANGE
        )
        self._reporte_sep_data = self._reporte_sep.get_data()
        self._reporte_sep_index = [d[2] for d
                                   in self._reporte_sep_data]

    def run(self):
        for beca in self._revision_becas_data:
            if not beca[0] in self._reporte_sep_index:
                print(beca)
