""" Clase base para conectarse a las APIs de Google. """

import pathlib

import googleapiclient.discovery
from google.oauth2 import service_account


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
    _service_account_file = None
    _scopes = None

    _api_service = None
    _api_version = None

    def __init__(self, service_account_file, scopes):
        self._service_account_file = pathlib.Path(service_account_file)
        self._scopes = scopes

    def conn(self):
        """Se conecta al servicio de apis de Google
        y regresa un servicio.
        """
        credentials = service_account.Credentials.from_service_account_file(
            self._service_account_file,
            scopes=self._scopes
        )

        service = googleapiclient.discovery.build(
            self._api_service,
            self._api_version,
            credentials=credentials
        )

        return service
