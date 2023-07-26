import requests, ast, urllib, json

filepath = 'credentials.json'

with open(filepath) as f:
    txt = f.read()

data = ast.literal_eval(txt)

# 'web' の代わりに 'installed' を使用
auth = data['installed']

SCOPE ='https://www.googleapis.com/auth/photoslibrary'
url = "https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=%s&redirect_uri=%s&scope=%s&access_type=offline" % (auth['client_id'], auth['redirect_uris'][0], SCOPE)
print(url)