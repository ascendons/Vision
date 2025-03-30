import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
import io
import config

def authenticate_drive():
    """Authenticates and returns Google Drive service."""
    creds = service_account.Credentials.from_service_account_file(
        config.SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/drive"]
    )
    return build("drive", "v3", credentials=creds)

def fetch_drive_files():
    """Fetches text and Google Docs files from Google Drive."""
    service = authenticate_drive()

    query = f"'{config.FOLDER_ID}' in parents"

    results = service.files().list(q=query, fields="files(id, name, mimeType)").execute()
    files = results.get("files", [])

    if not files:
        print("No text files found in the folder.")
        return []

    os.makedirs(config.DOWNLOAD_PATH, exist_ok=True)

    for file in files:
        file_id, file_name, mime_type = file["id"], file["name"], file["mimeType"]

        if mime_type == "text/plain":
            # Download normal text files
            request = service.files().get_media(fileId=file_id)
            file_path = os.path.join(config.DOWNLOAD_PATH, file_name)

            with open(file_path, "wb") as f:
                f.write(request.execute())

        elif mime_type == "application/vnd.google-apps.document":
            # Export Google Docs as plain text
            request = service.files().export(fileId=file_id, mimeType="text/plain")
            file_path = os.path.join(config.DOWNLOAD_PATH, file_name + ".txt")

            with open(file_path, "wb") as f:
                f.write(request.execute())

        else:
            print(f"Skipping unsupported file type: {file_name} ({mime_type})")
            continue

        print(f"Downloaded: {file_name}")

    return [file["name"] for file in files]