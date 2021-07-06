""" Spreadsheets """

from shipdoc.logger import LogHandler

from googleapi.base_api import ServiceAPI


class GSS(ServiceAPI):
    """ This functions manages conection and data manipulation. """


    def __init__(self, secrets_path, scopes, ss_id, range_name):
        super().__init__(secrets_path, scopes)
        self._api_service = 'sheets'
        self._api_version = 'v4'
        self._ss_id = ss_id
        self._range_name = range_name


    @staticmethod
    def create(secrets_path, scopes, ss_id, range_name):
        """ Creates a new instance of GSS. """

        return GSS(secrets_path, scopes, ss_id, range_name)

    def get_data(self):
        """ Call sheet API """

        service = self.conn()
        result = None

        try:
            sheet = service.spreadsheets()
            result = sheet.values().get(
                spreadsheetId=self._ss_id,
                range=self._range_name
            ).execute()
        except Exception as error:
            LogHandler.execution_log(error=error)
        finally:
            service.close()

        return result.get('values', [])

    def append(self, values):
        """ Append values in Spreadsheet. """

        service = self.conn()

        try:
            body = {
                'values': values,
            }
            sheet = service.spreadsheets()
            result = sheet.values().append(
                spreadsheetId=self._ss_id,
                range=self._range_name,
                valueInputOption='USER_ENTERED',
                body=body,
            ).execute()

            updatedCells = result.get('updates').get('updatedCells')
        except Exception as error:
            LogHandler.execution_log(error=error)
        finally:
            service.close()

        return updatedCells
