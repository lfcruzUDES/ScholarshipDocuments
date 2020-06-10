""" Se conecta a Drive """

from base_api import ServiceAPI


class Drive(ServiceAPI):
    api_service = 'drive'
    api_version = 'v3'

    def __init__(self, secrets_path, scopes, ss_id, range_name,):
        super().__init__(secrets_path, scopes)
        self.ss_id = ss_id
        self.range_name = range_name
