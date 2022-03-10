from bs4 import BeautifulSoup
from utils.utils import common_words
from operator import itemgetter
import requests
import re


class WebAnalysis:

    def __init__(self):
        self.soup = None
        self.extract_dict = None
        self.highest_count = None

    def scrape_web(self, url):
        request = requests.get(url)
        self.soup = BeautifulSoup(request.text, 'html.parser')
        return self.soup

    def clean_data(self):
        new_extract = re.sub(r'[^\w\s]|[0-9]', '', self.soup.text.lower()).split()
        new_extract = [i for i in new_extract if i not in common_words and len(i) > 2]
        self.extract_dict = {i: new_extract.count(i) for i in set(new_extract) if new_extract.count(i)}
        return self.extract_dict

    def sort_data(self):
        self.highest_count = dict(sorted(self.extract_dict.items(), key=itemgetter(1), reverse=True)[:10])
        highest_keys = [i for i in self.highest_count.keys()]
        print(f'The top word is: {highest_keys[0]}')
        return self.highest_count
