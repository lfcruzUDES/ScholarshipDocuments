""" This module handle log calls. """

import datetime
import pathlib

import shipdoc.settings as settings


class LogHandler:

    _now = datetime.datetime.now()
    _log_file = settings.LOG_FILE

    @classmethod
    def execution_log(cls, error='', action=''):
        """ LOG execution. """
        txt = ''

        if error:
            txt = f'ERROR [{cls._now}]: shipdoc: {error}'

        if action:
            txt = f'LOG [{cls._now}]: shipdoc: {action}'

        if not txt:
            txt = f'LOG [{cls._now}]: shipdoc: execution'

        with cls._log_file.open('a') as f:
            f.write(txt + '\n')


    @classmethod
    def drive_logs(cls, error):
        """ Drive execution logs. """
        txt = f'ERROR [{cls._now}]: googleapi.gdrive: {error}'

        with cls._log_file.open('a') as f:
            f.write(txt + '\n')
