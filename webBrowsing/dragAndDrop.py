# http://www.dhtmlgoodies.com/scripts/drag-drop-nodes/drag-drop-nodes-demo3.html

from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-nodes/drag-drop-nodes-demo3.html')
source = driver.find_element_by_xpath('//*[@id="dragContent"]')
destination = driver.find_element_by_xpath('//*[@id="box1"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()



