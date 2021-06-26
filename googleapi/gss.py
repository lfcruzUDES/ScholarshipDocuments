""" Spreadsheets """

from googleapi.base_api import ServiceAPI


class GSS(ServiceAPI):
    """ This functions manages conection and data manipulation. """


    def __init__(self, secrets_path, scopes, ss_id=None, range_name=None):
        super().__init__(secrets_path, scopes)
        self._api_service = 'sheets'
        self._api_version = 'v4'

        if ss_id:
            self.ss_id = ss_id

        if range_name:
            self.range_name = range_name

    def get_data(self, ss_id='', range_name=''):
        """ Call sheet API """

        _ss_id = ss_id if ss_id else self.ss_id
        _range_name = range_name if range_name else self.range_name

        if not _ss_id:
            raise Exception('Spreadsheet ID is required.')

        if not _range_name:
            raise Exception('Range name is required.')
        service = self.conn()
        sheet = service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=_ss_id,
            range=_range_name
        ).execute()
        service.close()

        return result.get('values', [])
