""" COnfiguration file. """

import pathlib

# Paths
BASE_PATH = pathlib.Path(__file__)

SECRETG = BASE_PATH.parent.parent / 'secrets/udes-manager-344d77f03c21.json'

SAVE_PATH = pathlib.Path.home() / 'shipdoc'

DRIVE_SCOPES = [
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/drive.file',
]

SS_SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
]

LOG_FILE = SAVE_PATH / 'shipsdoc.log'

# DRIVE
# ------------------------------------------------------------

DRIVE_DOCUMENTS_FOLDER = '1kWa4H7uG5R6aTdyJZRSM7ekxMLAhWn6U'

# Documents sheet.
# ------------------------------------------------------------
SPREADSHEET_DOCS_ID = '1MO_vot62pY2SFnpIfeJLYP2mxrhVC88282MmRHoWlL4'

DOCS_SHEET_NAME = 'Respuestas'

DOCS_RANGE_NAME = 'Documentos'

DOCS_COLUM_ORDER = {
    'date': 0,
    'email': 1,
    'doc_scholarship_request': 2,
    'doc_kardex': 3,
    'doc_economic': 4,
    'doc_address': 5,
    'doc_scholarship_receipt': 6,
    'name': 7,
    'status': 8,
}

# Scholarship sheet.
# ------------------------------------------------------------
# SPREADSHEET_SCHOLARSHIP_ID = '1RM-N99V2gs6hmNXebi-7lt2CR2kNNP4aaUgNDw0xgWw'
#
# SCHOLARSHIP_SHEET_NAME = 'alumnos_datos'
#
# SCHOLARSHIP_RANGE_NAME = 'alumnos_datos!A2:C'
#
# SCHOLARSHIP_COLUMN_ORDER = {
#     'email': 0,
#     'date': 1,
#     'enrollment': 2,
# }

# Index sheet.
# ------------------------------------------------------------
SPREADSHEET_INDEX_ID = '14zOmPR3947F82EvhuUIS-G6tbWmSgBGEUlhJC7pc2yA'

INDEX_SHEET_NAME = 'Índice'

INDEX_RANGE_NAME = 'index'

INDEX_COLUMN_ORDER = {
    'enrollment': 0,
    'email': 2,
    'name': 3,
    'document': 5,
    'url': 6,
}

# Solicitud de beca.
# ------------------------------------------------------------
SPREADSHEET_SOLICITUDES_BECA = '1RM-N99V2gs6hmNXebi-7lt2CR2kNNP4aaUgNDw0xgWw'

SOLICITUDES_BECA_RANGE = 'alumnos_datos'

SOLICITUDES_BECA_COLUMN_ORDER = {
    'email': 0,
    'date': 1,
    'enrollment': 2,
    'name': 3,
    'last_name': 4,
}

# Boletas.
# ------------------------------------------------------------
SPREADSHEET_BOLETAS_INDEX = '1IrqXZvkf0yMGUmRKG9xvcWP3NNU2so56dpBzOQZnaQ4'

BOLETAS_INDEX_RANGE = 'Boletas'

BOLETAS_INDEX_COLUMN_ORDER = {
    'enrollment': 0,
    'url': 1,
}

# Scholarship Revisión y resultados de la convocatoria de becas
# ------------------------------------------------------------
SPREADSHEET_REVISION_BECAS = '1Crr63rRVYFElx9a3K8Tk7edDizzFN8YlEKuNl1o-irA'

REVISION_BECAS_RANGE = 'request'

REVISION_BECAS_COLUMN_ORDER = {
    'enrollment': 0,
    'name': 1,
    'career': 2,
    'percentage_old': 6,
    'group': 7,
    'percentage_new': 8,
    'type': 9,
    'scholarship_type': 10,
    'average': 10,
}

# Scholarship Reporte SEP.
# ------------------------------------------------------------
SPREADSHEET_REPORTE_SEP = '1ytym5wvW4TYJ90DgEOuV07_eoAHDadj_oe8F5iXEJPI'

REPORTE_SEP_RANGE = 'Becas_asignadas'

REPORTE_SEP_COLUMN_ORDER = {
    'email': 1,
    'enrollment': 2,
    'name': 3,
    'career': 4,
    'group': 5,
    'average': 6,
    'scholarship_type': 7,
    'percentage_new': 10,
    'type': 12,
    'is_approved': 14,
}
