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
SPREADSHEET_SCHOLARSHIP_ID = '1RM-N99V2gs6hmNXebi-7lt2CR2kNNP4aaUgNDw0xgWw'

SCHOLARSHIP_SHEET_NAME = 'alumnos_datos'

SCHOLARSHIP_RANGE_NAME = 'alumnos_datos!A2:C'

SCHOLARSHIP_COLUMN_ORDER = {
    'email': 0,
    'date': 1,
    'enrollment': 2,
}

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
