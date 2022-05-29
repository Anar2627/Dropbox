import pathlib
import pandas as pd
import dropbox
from dropbox.exceptions import AuthError
from psutil import users

# Dropbox uygulamasını kurma ve Token alma

DROPBOX_ACCESS_TOKEN = 'sl.BHyEAe4KtxhRDjfxwFMPDFF5Aa_Ty1lK-QSZkSsgPJd5vDfOuRP3lkXANqViEMHqArgBSapSR8SI1qrxOYjS8_vzvXscSTxQaZPLwj0qDp3LJf9elgsZngXw0QJ5WcXJvGRfWiQ'


# Dropbox API'sine Bağlanma


def dropbox_connect():
    """Create a connection to Dropbox."""

    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    except AuthError as e:
        print('Error connecting to Dropbox with access token: ' + str(e))
    return dbx


# Dropbox'tan dosya indirme


def dropbox_download_file(dropbox_file_path, local_file_path):
    """Download a file from Dropbox to the local machine."""

    try:

        dbx = dropbox_connect()

        with open(local_file_path, 'wb') as f:

            metadata, result = dbx.files_download(path=dropbox_file_path)
            f.write(result.content)

    except Exception as e:
        print('Error downloading file from Dropbox: ' + str(e))


dropbox_download_file("/Documents/projeno_12.txt", "/Users/anarmammadov/Desktop/projeno_12.txt")