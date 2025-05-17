import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

project_links = []
for link in soup.find_all('a'):
    href = link['href']
    project_name = href.split('/')[-1]
    project_links.append(f"{url}/{project_name}")

print(project_links)
