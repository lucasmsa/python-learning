from bs4 import BeautifulSoup
import requests

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# Prints out all the html
print(soup.prettify())

# Each new '.' is a different layer, the line below
# will get the text part of the title
matchTitle = soup.title.text
print(matchTitle)

# Finds the first instance with find method
# There's also the find_all method
matchText = soup.find('h3', class_='text').text
print(matchText)