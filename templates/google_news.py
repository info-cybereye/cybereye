import requests
from bs4 import BeautifulSoup

def scrape_google_news(keyword):
    url = f"https://www.google.com/search?q={keyword}&tbm=nws"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    news_titles = [title.get_text() for title in soup.find_all('h3')]

    return news_titles
