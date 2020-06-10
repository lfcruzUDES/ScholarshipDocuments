""" Spreadsheets """
from __future__ import print_function

import pickle
from os import path

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class GSS:
    """ This functions manages conexion and data manipulation. """

    def __init__(self, ss_id, range_name, secrets_path, scopes):
        self._secrets_path = secrets_path
        self._SCOPES = scopes
        self.ss_id = ss_id
        self.range_name = range_name

    def conn(self):
        """Se conecta al libro de cálculo de Google.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if path.exists(path.join(self._secrets_path, 'token.pickle')):
            with open(path.join(self._secrets_path, 'token.pickle'), 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    path.join(self._secrets_path, 'client_secret.json'),
                    self._SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(path.join(self._secrets_path, 'token.pickle'), 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)
        return service

    def get_datas(self, ss_id='', range_name=''):
        # Call the Sheets API
        sheet = self.conn().spreadsheets()
        result = sheet.values().get(spreadsheetId=self.ss_id,
                                    range=self.range_name).execute()
        return result.get('values', [])
