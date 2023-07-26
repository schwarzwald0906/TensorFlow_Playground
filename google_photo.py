import requests
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os
import io
import requests
from PIL import Image

creds_path = 'credentials.json'
token_path = 'refresh_token.json'

with open(creds_path) as f:
    creds_data = json.load(f)['installed']
with open(token_path) as f:
    token_data = json.load(f)

client_id = creds_data['client_id']
client_secret = creds_data['client_secret']
refresh_token = token_data['refresh_token']

scopes = ['https://www.googleapis.com/auth/photoslibrary.readonly']

def get_service():
    creds = Credentials.from_authorized_user_info({
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token
    }, scopes)
    return build('photoslibrary', 'v1', credentials=creds)

def save_photos(service, num_photos):
    results = service.mediaItems().list(pageSize=num_photos).execute()
    items = results.get('mediaItems', [])

    if not items:
        print('No photos found.')
    else:
        print('Photos:')
        for item in items:
            print(item['name'])

            image_response = requests.get(item['baseUrl'])
            image_content = image_response.content

            image = Image.open(io.BytesIO(image_content))
            image.save(os.path.join('./', f"{item['filename']}"))

def main():
    service = get_service()
    save_photos(service, 30)

if __name__ == '__main__':
    main()
