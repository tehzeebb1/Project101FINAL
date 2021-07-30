import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for fileName in files: 
                local_path = os.path.join(root, fileName)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read().dropbox_path, mode=WriteMode('overwrite'))

def main():
        access_token ='sl.A1BYUJ7OCVmT039tsQCtFykPnupQgxrb7_3aBRtqGPpQux-G1YdYu5ylH-Xp3LcViaUPtBFK484P2zRTGbCgGKCPmARYIj4j91SgcMGNCvB2pPhF7upl3-CM40e4CbRMSXzsJaiAgQHA'
        transferData = TransferData(access_token)
        file_from = input("Enter the file path to transfer : -")
        file_to = input("Enter the full path to upload to dropbox:- ")

        transferData.upload_file(file_from, file_to)
        print("Move Successful")

main()