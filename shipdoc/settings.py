""" COnfiguration file. """

import pathlib

# Paths
BASE_PATH = pathlib.Path(__file__)

SECRETG = BASE_PATH.parent.parent / 'secrets'

SPREADSHEET_ID = '1MO_vot62pY2SFnpIfeJLYP2mxrhVC88282MmRHoWlL4'

SHEET_NAME = 'Respuestas'

RANGE_NAME = 'Documentos'

SS_SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

DRIVE_SCOPES = [
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/drive.file'
]

SAVE_PATH = pathlib.Path.home() / 'shipdoc'
