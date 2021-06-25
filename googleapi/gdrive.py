""" Se conecta a Drive """

import io
import pathlib

from googleapiclient.http import MediaIoBaseDownload

from googleapi.base_api import ServiceAPI


class Drive(ServiceAPI):

    def __init__(self, secrets_path, scopes):
        super().__init__(secrets_path, scopes)

        self._api_service = 'drive'
        self._api_version = 'v3'

    def download_file(self, file_id, file_path):
        """Descarga un documento de Drive, pero no un
        documento de la suit de Google.

        Args:
            file_id (string): ID del documento a descargar.
            file_path (path or string): Path to the file.
        """

        if not file_id:
            raise Exception("File ID is required")

        if not file_path:
            raise Exception("File path is required")

        _file_path = pathlib.Path(file_path)
        request = self.conn().files().get_media(fileId=file_id)
        fh = io.FileIO(str(_file_path), mode='wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False

        while done is False:
            status, done = downloader.next_chunk()
            # print(f"{int(status.progress() * 100)}")

        return downloader
