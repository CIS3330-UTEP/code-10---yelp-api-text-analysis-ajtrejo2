from bs4 import BeautifulSoup
import requests

web_url= 'https://www.utep.edu/business/people/faculty-profiles.html'

page_to_scrape = requests.get(web_url)

soup = BeautifulSoup(page_to_scrape.text,'html.parser')

emails = soup.findAll('span',attrs={'class':'email'})
numbers = soup.findAll('span',attrs={'class':'phone'})
location = soup.findAll('span',attrs={'class':'address'})
title = soup.findAll('span',attrs={'class':'Title'})
section_title = soup.findAll('span',attrs={'class':'sectionTitle'})


# emails
for tag in emails:
    print(tag)  

# phones
for number in numbers:
    print(number)

# Location
for tag in location:
    print(tag)

# Title
for tag in title:
    print(tag)

# section title
for tag in section_title:
    print(tag)