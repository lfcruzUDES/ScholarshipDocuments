""" COnfiguration file. """

from os import path

# Paths
BASE_PATH = path.dirname((path.abspath('__file__')))
SECRETG = path.join(BASE_PATH, 'secrets')
SPREADSHEET_ID = '1MO_vot62pY2SFnpIfeJLYP2mxrhVC88282MmRHoWlL4'
SHEET_NAME = 'Respuestas'
RANGE_NAME = 'Documentos'
SS_SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
DRIVE_SCOPES = [
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/drive.file'
]
SAVE_PATH = '/home/quattroc/Descargas/test_docs'
