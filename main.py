from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com')

wait = WebDriverWait(driver, 100)

# Message to send goes here
message = '''
Test Message OP
'''

'''Remember to copy the image to be sent
before executing the script'''

with open('links.txt', 'r+') as f:
	links = f.readlines()
	for link in links:
		driver.get(link)
		textField = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fd365im1')))
		textField.clear()

		a = ActionChains(driver)

		for i in message:
			a.send_keys(i)
		sleep(1)
		a.key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()
		sleep(2)
		a.reset_actions()
		a.send_keys(Keys.RETURN).perform()
		print(link)
		sleep(5)

driver.close()
