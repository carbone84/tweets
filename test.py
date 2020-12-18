import requests
import os

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

headers = {'Authorization': f"Bearer {BEARER_TOKEN}"}

search_api_url = "https://api.twitter.com/2/tweets/search/recent?query=from:freecodecamp python"
#search_api_url = "https://api.twitter.com/2/tweets/search/recent?query=free conference"

response = requests.get(search_api_url, headers=headers)

if response.status_code != 200:
    print(response.status_code, response.text)
else:
    body = response.json()
    print(body)