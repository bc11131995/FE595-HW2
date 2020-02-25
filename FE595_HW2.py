import requests
import urllib.request
import html.parser
import time
import json
from bs4 import BeautifulSoup

website = ['http://18.207.92.139:8000/random_company']
names = []
purposes = []

for x in range(50):
    response = requests.get('http://18.207.92.139:8000/random_company')
    
    response
    soup = BeautifulSoup(response.text, "html.parser")
    soup
    
    for elem in soup.find_all('li'):
        words = elem.text.split()
        if words[0] == "Purpose:":
            purposes.append(" ".join(words[1:]))
        elif words[0] == "Name:":
            names.append(" ".join(words[1:]))

companies = []
for (name, purpose) in zip(names, purposes):
    companies.append({'name': name, 'purpose': purpose})

with open('output.json', 'w+') as J:
    json.dump(companies, J)
