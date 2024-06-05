from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import os

# Path to your service account key file
SERVICE_ACCOUNT_FILE = 'omkar-406915-668e2c37a47f.json'

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

# Authenticate and construct service
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

def download_file(file_id, file_name):
    request = service.files().get_media(fileId=file_id)
    # Create a folder if it doesn't exist
    folder_path = 'CloudFiles'
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name)
    fh = open(file_path, "wb")
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")
    print(f"File downloaded to: {file_path}")
    return

# Example usage
# file_id = '1rNPH8v1XyHjljE9vSkZxkMcL04zfuj-c'
# file_name = 'your_file_name.txt'
# download_file(file_id, file_name)
