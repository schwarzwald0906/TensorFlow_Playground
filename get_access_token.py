import requests, json

tokenpath = 'refresh_token.json'  # refresh_tokenが保存されたファイル

with open(tokenpath) as f:
    tokens = json.load(f)

data = {
   'client_id': tokens['client_id'],
   'client_secret': tokens['client_secret'],
   'refresh_token': tokens['refresh_token'],
   'grant_type': 'refresh_token',
}

response = requests.post('https://www.googleapis.com/oauth2/v4/token', data = data).json()

# 新しいaccess_tokenを表示
print(response['access_token'])
