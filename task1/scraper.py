from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd

#create and add service attribute to supress warnings
s=Service(r"C:\Users\Alok\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()


#driver = webdriver.Chrome(r"C:\Users\Alok\Downloads\chromedriver_win32\chromedriver.exe")
# passing the url to be parsed in get method
driver.get("https://www.epa.gov/greenpower/green-power-partnership-national-top-100")

# allowing the chromium browser to load the page before accessing and parsing the content
time.sleep(2)

content = driver.page_source
soup = BeautifulSoup(content,'html5lib') # add html5lib to supress html warnings


# using the class name tablebord to get the object and parse further
header = soup.find("table",{ "class" : "tablebord"}).find("thead").find("tr")

list_header = []
  
for item in header.find_all("th"):
    try:
        list_header.append(item.get_text())
    except:
        continue
#print(header)
#print(list_header)

row_data = []

HTML_data = soup.find("table",{ "class" : "tablebord"}).find("tbody")

rows = HTML_data.find_all("tr")

for row in rows:
    list_data = []
    try:
        for data in row.find_all("td"):
            try:
                list_data.append(data.get_text())
            except:
                continue
        row_data.append(list_data)
    except:
        continue


dataFrame = pd.DataFrame(data = row_data, columns = list_header)
   
# Converting Pandas DataFrame
# into CSV file
dataFrame.to_csv('assignment_1.csv',index=False)

print(row_data)

driver.close()

