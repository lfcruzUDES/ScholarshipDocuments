""" Se conecta a Drive """

import io
import pathlib

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from shipdoc.logger import LogHandler

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

        request = None
        service = self.conn()

        try:
            request = service.files().get_media(fileId=file_id)
        except HttpError as error:
            LogHandler.drive_logs(error)
            service.close()

            return False

        fh = io.FileIO(str(_file_path), mode='wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False

        while done is False:
            status, done = downloader.next_chunk()
            # print(f"{int(status.progress() * 100)}")

        service.close()
        fh.close()

        return file_path

    def upload_file(self,
                    name,
                    local_path,
                    mimetype='application/pdf',
                    folders=[],
                    owner_email='lfcruz@udes.edu.mx'
                    ):
        """ Upload file. """

        service = self.conn()

        file_metadata = {
            'name': name,
            'parents': folders
        }

        media = MediaFileUpload(local_path, mimetype=mimetype)
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        file_id = file.get('id')

        # https://stackoverflow.com/questions/58080962/google-api-file-permissions-using-python
        # https://developers.google.com/drive/api/v3/reference/permissions/create

        permissions1 = {
            'type': 'user',
            'role': 'writer',
            'emailAddress': owner_email,
        }

        service.permissions().create(
            fileId=file_id,
            body = permissions1,
        ).execute();

        permissions2 = {
            'type': 'anyone',
            'role': 'writer',
        }

        service.permissions().create(
            fileId=file_id,
            body = permissions2,
        ).execute();

        service.close()

        return file_id
