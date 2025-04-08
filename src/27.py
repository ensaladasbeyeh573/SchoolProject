# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage containing the project list
url = "https://www.example.com/projects"

# Send a GET request to the URL and parse the HTML content using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <a> tags containing the link to the projects page
projects_links = soup.find_all('a', href=True)

# Loop through each project link and print its text
for link in projects_links:
    if link['href'].endswith('/project'):
        print(link['href'])
