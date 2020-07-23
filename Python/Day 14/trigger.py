import requests

ngrok_url = 'http://e1360c559f0d.ngrok.io'
endpoint = f'{ngrok_url}/box-office-mojo-scraper'

r = requests.post(endpoint, json={})
print(r.json()['data'])