import requests, os, json

# Load the client secrets
with open('credentials.json') as f:
    client_secrets = json.load(f)['installed']

# Load the refresh token
with open('refresh_token.json') as f:
    refresh_info = json.load(f)

data = {
   'refresh_token': refresh_info['refresh_token'],
   'client_id': client_secrets['client_id'],
   'client_secret': client_secrets['client_secret'],
   'grant_type': 'refresh_token'
}

token = requests.post('https://www.googleapis.com/oauth2/v4/token', data=data).json()
response = requests.get('https://photoslibrary.googleapis.com/v1/mediaItems?pageSize=10', headers={"Authorization": "Bearer %s" % token["access_token"]})
photos = response.json()

for photo in photos['mediaItems']:
   if photo['mimeType']=='image/jpeg':
       print(photo)
       
       
# 上のコードを続ける
for photo in photos['mediaItems']:
    if photo['mimeType'] == 'image/jpeg':
        # Get the url of the photo
        url = photo['baseUrl']

        # Get the photo data
        response = requests.get(url)

        # Check if the request is successful
        if response.status_code == 200:
            # Get the file name from the photo metadata
            file_name = photo['filename']

            # Create the directory if it does not exist
            if not os.path.exists('image'):
                os.makedirs('image')

            # Write the photo data to a file
            with open(os.path.join('image', file_name), 'wb') as f:
                f.write(response.content)