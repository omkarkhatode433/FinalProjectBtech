from googleapiclient.discovery import build
from google.oauth2 import service_account
import tkinter as tk
from tkinter import simpledialog

SERVICE_ACCOUNT_FILE = 'omkar-406915-668e2c37a47f.json'
parent_folder_id = '1IGc1ADVQBsnDhWCwCJ64jFAEFhA791By'
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_to_drive(file_path):
    creds=authenticate()
    service = build('drive', 'v3', credentials=creds)
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    name = simpledialog.askstring("Input", "What is your name?")
    if name:
        name=name
    else:
        name="Encrypted"
    root.destroy()
    
    file_metadata = {
        'name': name,  
        'parents': [parent_folder_id]
    }
    
    
    file = service.files().create(
        body=file_metadata,
        media_body=file_path,
    ).execute()

    print(f"File uploaded successfully! File ID: {file.get('id')}")

    return

# # Example usage

# file_path = 'C:/Users/omkar/OneDrive/Desktop/Secure Text Transfer Protocol/Secure Text Transfer Protocol/src/web-application/media/text-files/3fb95c57b44c130bb261c699e0dfd681c268208e6b02ce6f.txt'  
# upload_to_drive(file_path)
