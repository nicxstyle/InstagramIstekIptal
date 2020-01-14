
"""


@author: burakgultekin
www.burakgultekin.com.tr
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

driver_path = r"CHROME BROWSER PATH"
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(10)
username = "INSTAGRAM KULLANICI ADI"
password = "INSTAGRAM ŞİFRE"

browser.find_element_by_xpath("//input[@name='username']").send_keys(username)
browser.find_element_by_xpath("//input[@name='password']").send_keys(password)
browser.find_element_by_xpath("//button[contains(.,'Giriş Yap')]").click()

time.sleep(10)
browser.find_element_by_xpath("//button[contains(.,'Şimdi Değil')]").click()

time.sleep(5)

def ac(dosya):
    with open('DOSYA PATH/'+str(dosya),encoding="utf8") as x:
        dizi = x.readlines()
    return [x.strip() for x in dizi]

kisiler = ac("DOSYA İSMİ.txt")

sozluk = []
for x in kisiler:
    sozluk.append(x)
    
for i in sozluk:
    time.sleep(3)
    kisi = "https://www.instagram.com/"+i
    browser.get(kisi)
    time.sleep(5)
    browser.find_element_by_xpath("//button[contains(.,'İstek Gönderildi')]").click()
    browser.find_element_by_xpath("//button[contains(.,'Takibi Bırak')]").click()
    time.sleep(3)
    
    
