""" This file has the class that executes al process."""


from os import environ

import settings


class Executor:
    """ This class executes all process. """

    def __init__(self):
        self.set_evironment()

    def set_evironment(self):
        environ['BASE_PATH'] = settings.BASE_PATH if settings.BASE_PATH else ''
        environ['SECRETG'] = settings.SECRETG if settings.SECRETG else ''
        environ['SPREADSHEET_ID'] = settings.SPREADSHEET_ID if settings.SPREADSHEET_ID else ''
        environ['SHEET_NAME'] = settings.SHEET_NAME if settings.SHEET_NAME else ''
        environ['RANGE_NAME'] = settings.RANGE_NAME if settings.RANGE_NAME else ''
        environ['SS_SCOPES'] = settings.SS_SCOPES if settings.SS_SCOPES else ''


if __name__ == "__main__":
    Executor()
