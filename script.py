import requests
from BS4 import BeautifulSoup4
URL = "https://www.mohfw.gov.in/"
page = requests.get(URL)
soup = BeautifulSoup4(page.content, 'html parser')
results = soup.find(class_='icount')
print(results.text)
