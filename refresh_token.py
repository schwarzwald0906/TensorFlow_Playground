import requests, ast, urllib, json

# ここで auth を定義
filepath = 'credentials.json'
with open(filepath) as f:
    txt = f.read()
auth = ast.literal_eval(txt)['installed']

code = '4/0AZEOvhWjSG5f7jDvx-AjQj0LseC9CaKrW-GA6CoFvkq3l7Z-C8X2Ks4MrvX1tvprinqZTQ'
tokenpath = 'refresh_token.json' #保存したい場所

data = {
   'code': urllib.parse.unquote(code),
   'client_id': auth['client_id'],
   'client_secret': auth['client_secret'],
   'redirect_uri': auth['redirect_uris'][0],
   'grant_type': 'authorization_code',
   'access_type': 'offline'
}
response = requests.post('https://www.googleapis.com/oauth2/v4/token', data = data).json()
print(response)
if 'refresh_token' in response.keys():
   with open(tokenpath, "w") as f:
       f.write(json.dumps(response))




