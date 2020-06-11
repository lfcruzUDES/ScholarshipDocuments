""" This file has the class that executes al process."""


from os import path, system

import googleapiclient

import settings
from Google.gdrive import Drive
from Google.gss import GSS


class Executor:
    """ This class executes all process. """

    ss = GSS(settings.SECRETG, settings.SS_SCOPES,
             settings.SPREADSHEET_ID, settings.RANGE_NAME)
    drive = Drive(settings.SECRETG, settings.DRIVE_SCOPES)

    def __init__(self):
        self.retrive_docs()

    def retrive_docs(self):
        datas = self.ss.get_datas()
        for data in datas:
            student_name = data[-1].replace(' ', '-')
            docs = [item.split('id=')[1] for item in data[2:-1]]
            for i, doc in enumerate(docs):
                try:
                    self.drive.donwload_file(
                        doc,
                        path.join(settings.SAVE_PATH,
                                  f'{student_name}_{i}.pdf')
                    )
                except googleapiclient.errors.HttpError as e:
                    print('File not found.')
                    print(e)

            full_pdf_name = path.join(settings.SAVE_PATH,
                                      student_name.replace("-", "_"))
            files_pdf_remove = path.join(settings.SAVE_PATH,
                                         student_name)
            system(
                f'convert {files_pdf_remove}* {full_pdf_name}_FULL.pdf'
            )
            system(
                f'rm {files_pdf_remove}*'
            )

    def join_docs(self):
        pass


if __name__ == "__main__":
    Executor()
