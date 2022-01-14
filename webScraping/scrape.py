import requests
from bs4 import BeautifulSoup
url = 'https://quotes.toscrape.com/'
response = requests.get(url) #creating the request
soup = BeautifulSoup(response.text, 'lxml') #parsing the html doc
quotes = soup.find_all('span', class_= 'text') #creates a list with all the elements on the HTML website w/ tag span and class 'text'
authors = soup.find_all('small', class_ = 'author')
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
