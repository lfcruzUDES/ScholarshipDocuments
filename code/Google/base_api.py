""" Clase base para conectarse a las APIs de Google. """

import pickle
from os import path

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class FatherAPI(object):

    def __init__(self, secrets_path, scopes):
        self._secrets_path = secrets_path
        self._SCOPES = scopes

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
