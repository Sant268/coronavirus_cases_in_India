import requests
from bs4 import BeautifulSoup
URL = "https://www.mohfw.gov.in/"  #Indian Gov Website
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
active = soup.find(class_="bg-blue")
cure = soup.find(class_="bg-green")
death = soup.find(class_="bg-red")
print("Active Patients:")
print(active.text[:6])
print("Recovered Patients:")
print(cure.text[:5])
print("Deaths:")
print(death.text[:5])



