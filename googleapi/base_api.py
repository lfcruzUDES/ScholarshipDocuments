""" Clase base para conectarse a las APIs de Google. """

import pathlib
import pickle
from os import path

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class ServiceAPI:
    """ De esta clase heredan las demás clases referentes
    a servicios de Google.

    Atributos:

        - api_service {string}: es el servicio al que se va a conectar:
            drive, spreadsheets.

        - api_version {string}: es la versión de la api que se usará.

    Funciones:

        - conn : regresa la conexión al servicio, pero sólo
        al servicio de Google, para después conectarse a las APIs.
     """
    _secrets_path = None
    _scopes = None

    api_service = None
    api_version = None

    token_file = None

    def __init__(self, secrets_path, scopes):
        self._secrets_path = pathlib.Path(secrets_path)
        self._scopes = scopes
        self.token_file = (self._secrets_path
                           / f'{self.api_service}_token.pickle')

    def conn(self):
        """Se conecta al servicio de apis de Google
        y regresa un servicio.
        """
        creds = None

        # The file token.pickle stores the user's access and
        # refresh tokens, and is created automatically when
        # the authorization flow completes for the first time.

        if self.token_file.exists():
            with open(self.token_file, 'rb') as token:
                creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in.

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self._secrets_path / 'client_secret.json',
                    self._scopes
                )
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open(self.token_file, 'wb') as token:
                pickle.dump(creds, token)

        service = build(self.api_service, self.api_version, credentials=creds)

        return service
