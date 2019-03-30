
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
print("Welecome to Voice Command Protal How can i help You:")
def openchrome():
	driver=webdriver.Chrome(executable_path="C:\Alexa\Exe\chromedriver.exe")

	while True:
		do=input("Enter command:")
			
		if do=='search':
			searchlink=input("Enter any link :")
			driver.get("https://"+searchlink)
		elif do=='scrolldown':
			driver.execute_script("window.scrollBy(0,500)","")
		elif do=='Maximize window':
			driver.maximize_window()
		elif do=='close':
			driver.close()
		elif do=='open':
			openchrome()
		elif do=='quit':
			driver.quit()
			break

openchrome()