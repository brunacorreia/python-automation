from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.amazon.com.br/')
messageField = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
messageField.send_keys('Kindle')
showMessageButton = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
showMessageButton.click()