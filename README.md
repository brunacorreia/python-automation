# Python Automation

## Web Scraping
Make sure to install the libraries below:
- ``pip install requests``
- ``pip install lxml``
- ``pip install beautifulsoup4``

Steps
1. Sending a GET query to the desired website
2. Parsing the HTML using the referred libraries

To prepare a webpage for scraping, you first need to convert the HTML code into a navigable object in Python:
``response = requests.get(url)``

## Multi-Page Web Scraping
E-commerce Store - Link: https://scrapingclub.com/exercise/list_basic

Tips:
- When you encounter a webpage with pagination, it is important to avoid capturing multiple links that go to the same page, which will create duplicate data in the scraped output when scraping the data.

## Web Browsing Automation
Why automate?<br>
*Test Website Functionality*
- Decreases cost and time
- Provides round the clock testing
- Makes cross-browser proofing easier

*Botting Processes:* A piece of software that executes commands or performs routine tasks without the users intervention
- Script any repetitive tasks
- Filling out forms
- Logging in
