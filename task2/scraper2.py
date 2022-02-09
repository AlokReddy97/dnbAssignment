from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
from urllib import parse

import os.path

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


#create and add service attribute to supress warnings
s=Service(r"C:\Users\Alok\Downloads\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=s,options=options)
driver.maximize_window()


#driver = webdriver.Chrome(r"C:\Users\Alok\Downloads\chromedriver_win32\chromedriver.exe")
# passing the url to be parsed in get method
driver.get("https://www.certipedia.com/search/certified_companies?locale=en")


# allowing the chromium browser to load the page before accessing and parsing the content
time.sleep(2)

try:
    wait = WebDriverWait(driver, 5)
    wait.until(EC.element_to_be_clickable((By.ID, 'tarteaucitronPersonalize'))).click()
except:
    print("Cannot find the Accept cookie button, Ignoring")



content = driver.page_source
soup = BeautifulSoup(content,'html5lib') # add html5lib to supress html warnings


# using the class name tablebord to get the object and parse further
certificates_list = soup.find("ul",{ "class" : "search-results"}).find_all("span",{"class" : "certificate_links"})

list_header = []
  

for certificates in certificates_list:
    try:
        list_header.append("https://www.certipedia.com/"+certificates.find("a").get("href"))
    except:
        continue


main_window_handle = driver.current_window_handle

certificate_header = ["Certificate Number","Certificate Holder","Scope","Certificate Type"]

row_data = []

print("Scraping through each certificate and storing in a csv file")

for certificate in list_header:
    #certificate links for each
    try:
        driver.get(certificate)
        #driver.execute_script("window.open(certificate, 'new window')")
        time.sleep(2)
        content = driver.page_source
        soup = BeautifulSoup(content,'html5lib') # add html5lib to supress html warnings
        rows = soup.find("tbody",{"class" : "search-results"}).find_all("tr")
        for row in rows:
            try:
                url = row.find("td",{"class" : "last"}).find("a").get("href")
                certi_no = url.split("certificate_number=",1)[1]
                driver.get("https://www.certipedia.com/certificates/"+certi_no)
                time.sleep(1)
                content = driver.page_source
                soup = BeautifulSoup(content,'html5lib') # add html5lib to supress html warnings
                # using the class name certificate to get the object and parse further
                data = soup.find("div",{ "class" : "certificate"}).find("tbody").find_all("tr")
                certificate_data = []
                for item in data:
                    try:
                        value = item.find("td",{"class" : "last"}).get_text()
                        final_value = " ".join(value.split())
                        certificate_data.append(final_value)
                    except:
                        continue
                row_data.append(certificate_data)
            except:
                continue
    except:
        continue


dataFrame = pd.DataFrame(row_data)
   
dataFrame.to_csv('assignment_2.csv', index=False, header=certificate_header)

if os.path.isfile('assignment_2.csv'):
    print ("CSV file successfully created")
else:
    print ("Error creating the csv file")

driver.close()


