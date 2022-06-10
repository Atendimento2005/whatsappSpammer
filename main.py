from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com')

wait = WebDriverWait(driver, 100)

with open('links.txt', 'r+') as f:
	links = f.readlines()
	for link in links:
		driver.get(link)
		textField = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '._1LbR4 > div:nth-child(2)')))

		textField.clear()
		textField.send_keys(
'''
Hi,
We're grateful for your demonstrated interest in our program, and we're happy to tell you that you've been offered a place in the Summer Camp, organised by DPSRPK's Tech Club!

Included in this email are two links, one for the WhatsApp group, and the other for the Discord server. All members are required to join the groups on both platforms. If you haven't used Discord before, you could use the following YouTube video to familiarize yourself with the application:
https://www.youtube.com/watch?v=nPmdafMo1b8

Moreover, we share your enthusiasm for the program, and we're looking forward to meeting you!

Discord Server Invite: https://discord.gg/fnWq9TdZwz

Whatsapp Group Invite: https://chat.whatsapp.com/G7ytufqES1Q2BsddWiyqQP
'''
		)
		sleep(1)
		textField.send_keys(Keys.RETURN)
		print(link)
		sleep(3)

driver.close()
