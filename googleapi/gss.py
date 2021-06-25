""" Spreadsheets """

from googleapi.base_api import ServiceAPI


class GSS(ServiceAPI):
    """ This functions manages conection and data manipulation. """

    api_service = 'sheets'
    api_version = 'v4'

    def __init__(self, secrets_path, scopes, ss_id, range_name,):
        super().__init__(secrets_path, scopes)

        if ss_id:
            self.ss_id = ss_id

        if range_name:
            self.range_name = range_name

    def get_data(self, ss_id='', range_name=''):
        # Call the Sheets API

        if not ss_id and not self.ss_id:
            raise Exception('Spreadsheet ID is required.')

        if not range_name and not self.range_name:
            raise Exception('Range name is required.')

        sheet = self.conn().spreadsheets()
        result = sheet.values().get(
            spreadsheetId=self.ss_id,
            range=self.range_name
        ).execute()

        return result.get('values', [])
