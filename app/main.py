from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests
from app.google_news import scrape_google_news
from app.telegram_api import fetch_telegram_messages

app = Flask(__name__)

@app.route('/app')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_keyword():
    data = request.get_json()
    keyword = data['keyword']

    google_url = f"https://www.google.com/search?q={keyword}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(google_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for title in soup.find_all('h3'):
        results.append(title.get_text())

    return jsonify(results)
