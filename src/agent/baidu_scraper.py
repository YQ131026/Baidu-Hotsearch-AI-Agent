import requests
from bs4 import BeautifulSoup

class BaiduScraper:
    def __init__(self, url):
        self.url = url

    def get_hot_searches(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            hot_searches = self._parse_hot_searches(soup)
            return hot_searches
        else:
            raise Exception("Failed to fetch Baidu hotsearch page.")

    def _parse_hot_searches(self, soup):
        hot_searches = []
        items = soup.find_all("div", class_="c-single-text-ellipsis")
        for item in items:
            hot_searches.append(item.get_text(strip=True))
        return hot_searches

