from bs4 import BeautifulSoup
import requests

class WebScraper:
    def __init__(self,url):
        self.url = url
        
    def extract_text(self):
        html = requests.get(self.url)
        soup = BeautifulSoup(html.content, 'html5lib')
        head = soup.find('h1').get_text()
        text = ""
        for i in range(len(soup.find_all('p'))):
            text += soup.find_all('p')[i].get_text()
            
        return head, text

