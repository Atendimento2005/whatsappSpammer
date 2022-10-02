from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com')

wait = WebDriverWait(driver, 100)

message = '''
Test Message OP
'''

with open('links.txt', 'r+') as f:
	links = f.readlines()
	for link in links:
		driver.get(link)
		textField = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fd365im1')))

		textField.clear()
		for i in message:
			textField.send_keys(i)
		sleep(1)
		textField.send_keys(Keys.RETURN)
		print(link)
		sleep(3)

driver.close()
