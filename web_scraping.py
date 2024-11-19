from bs4 import BeautifulSoup
import requests

#url = "https://en.wikipedia.org/wiki/Ferrari"
url = str(input("Enter URL:"))
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html5lib')
head = soup.find('h1').get_text()
print(head)
text = ""
for i in range(len(soup.find_all('p'))):
    text += soup.find_all('p')[i].get_text()

