from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your service account key file
SERVICE_ACCOUNT_FILE = 'omkar-406915-668e2c37a47f.json'

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

# Authenticate and construct service
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

# Function to list all files in Google Drive
def list_files():
    results = service.files().list(pageSize=100, fields="nextPageToken, files(id, name, mimeType, size, createdTime, modifiedTime)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        return items

# Call the function
list_files()
