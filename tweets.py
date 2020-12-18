from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

headers = {
    'Authorization': f"Bearer {BEARER_TOKEN}"
}

twitter_api_url = "https://api.twitter.com/2/tweets/search/recent"

fcc_python = "?query=from:freecodecamp python"
psf_no_retweets = "?query=from:thepsf -is:retweet"
author_id = "&expansions=author_id"

@app.route("/")
def index():
    fcc_python_resp = get_tweets(twitter_api_url, fcc_python, author_id)
    psf_no_retweets_resp = get_tweets(twitter_api_url, psf_no_retweets, author_id)
    return render_template('index.html', fcc_python=fcc_python_resp, psf_no_retweets=psf_no_retweets_resp)

def get_tweets(url, query, option=''):
    api_url = url + query + option
    print(api_url)
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        print(response.status_code, response.text)
        return response.status_code, response.text

    body = response.json()
    print(body)


    return body

if __name__ == '__main__':
    app.run()