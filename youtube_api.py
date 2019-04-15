import os
import google.oauth2.credentials
import google_auth_oauthlib.flow

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = "client_secret.json"
YOUTUBE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, YOUTUBE_SCOPE)

    credentials = flow.run_console()

    # TODO: save credentials
    if credentials is None:
        credentials = flow.run_console()
        storage.put(credentials)

    return build(YOUTUBE_API_SERVICE_NAME,
            YOUTUBE_API_VERSION, credentials = credentials)
