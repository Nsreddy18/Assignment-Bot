from lib2to3.pgen2 import driver
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


username=""
password=""
path ="C:\Program Files (x86)\chromedriver.exe"
url="http://ngitonline.com/login/index.php"

driver=webdriver.Chrome(path)

def sendMail():
    driver.get("https://login.yahoo.com/?.src=ym&pspid=159600001&activity=mail-direct&.lang=en-IN&.intl=in&.done=https%3A%2F%2Fin.mail.yahoo.com%2Fd%2F")

    time.sleep(2)
    #mail
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[3]/input').send_keys("")
    #submit
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[2]/input').click()
    
    time.sleep(2)
    #password
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[2]/input').send_keys("")

    #submit
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[3]/button').click()

    time.sleep(5)

    #compose
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[1]/nav/div/div[1]/a').click()

    time.sleep(2)

    #to

    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/ul/li/div/div/input[1]').send_keys("")

    time.sleep(2)

    #subject

    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[3]/div/div/input').send_keys("test")

    time.sleep(2)

    #body

    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/div/div[1]').send_keys("The website has been updated since your last visit. Please visit the website to check the latest updates.")

    #send

    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/button').click()

    time.sleep(2)

    
def login():
    driver.get(url)
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("login").click()

login()

u=driver.current_url
timeout=time.time()+60*60

while True:

    page=requests.get(u)
    soup1=BeautifulSoup(page.content,"html.parser")

    time.sleep(2)

    driver.refresh()

    soup2=BeautifulSoup(page.content,"html.parser")

    if soup1==soup2:
        print("nothing changed")

    else:
        print("something changed")
        sendMail()
    if time.time()>timeout:
        break

driver.close()
print("logged in successfully")
