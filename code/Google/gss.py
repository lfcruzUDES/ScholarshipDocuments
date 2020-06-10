""" Spreadsheets """
from __future__ import print_function

import pickle
from os import path

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from base_api import ServiceAPI


class GSS(ServiceAPI):
    """ This functions manages conexion and data manipulation. """

    api_service = 'sheets'
    api_version = 'v4'

    def __init__(self, secrets_path, scopes, ss_id, range_name,):
        super().__init__(secrets_path, scopes)
        self.ss_id = ss_id
        self.range_name = range_name

    def get_datas(self, ss_id='', range_name=''):
        # Call the Sheets API
        sheet = self.conn().spreadsheets()
        result = sheet.values().get(spreadsheetId=self.ss_id,
                                    range=self.range_name).execute()
        return result.get('values', [])
