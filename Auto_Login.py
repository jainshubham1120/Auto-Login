#AutoLogin_Brave
#Prerequisite - Install Selenium and Chromedriver


from selenium import webdriver 
import os
from selenium.webdriver.chrome.options import Options


def startBot(username, password, url):
    path = "D:/Apps/chromedriver_win32/chromedriver"
    
    options = Options()
    options.binary_location = 'C:/Users/shubh/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe'
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options = options, executable_path = path)
    driver.maximize_window()
    driver.get(url)
    driver.find_element(By.NAME,"username").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)
    

    #driver.find_element(By.XPATH,"//form[@class='login-form'][@type='submit']").click() #css-ifshk5  #[@class='login-form']
    driver.implicitly_wait()
    
username = "username" 
password = "password"
url = "website.com"
 
# Call the function
startBot(username, password, url)