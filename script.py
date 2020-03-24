import requests
from bs4 import BeautifulSoup
URL = "https://www.mohfw.gov.in/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find_all(class_="icount")
print("Active Values are:")
print(result[1].text)
print("Recovered Patients:")
print(result[2].text)
print("Deaths:")
print(result[3].text)



