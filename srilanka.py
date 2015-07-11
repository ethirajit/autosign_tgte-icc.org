import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import string
import random

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        pass
	#self.driver = webdriver.Firefox()

    def test_login(self): 
	for i in range(0,1000):
		self.driver = webdriver.Firefox()
	        driver = self.driver
        	driver.get("http://tgte-icc.org")
	        #driver.implicitly_wait(50)
        	userName = driver.find_element_by_xpath("//input[@name='first_name']")
		userName.send_keys('Ramesh')
        	password = driver.find_element_by_xpath("//select[@id='Country']")
		password.send_keys('India')
		soup = BeautifulSoup(self.driver.page_source)
		code=''
		for img in soup.find_all('img'):
			num = img.get('src')
			if num[10] == 'w':
				continue
			code = code + num[10]
        	txtcode = driver.find_element_by_xpath("//input[@id='txtcode']")
		txtcode.send_keys(code)
	        btncode = driver.find_element_by_xpath("//input[@id='btncode']")
		btncode.click()
	        #driver.implicitly_wait(100)
		self.driver.quit()

if __name__ == "__main__":      
    unittest.main()
