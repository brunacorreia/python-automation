from urllib import response
from bs4 import BeautifulSoup
import requests
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_ = 'col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
    itemName = i.find('h4', class_ = 'card-title').text.strip('\n')
    itemPrice = i.find('h5').text
    print('%s Price: %s, Item Name: %s' % (count, itemPrice, itemName))
    count = count + 1


