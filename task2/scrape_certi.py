

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
driver.get("https://www.certipedia.com/certificates/01+400+1610377")

# allowing the chromium browser to load the page before accessing and parsing the content
time.sleep(2)

content = driver.page_source
soup = BeautifulSoup(content,'html5lib') # add html5lib to supress html warnings


# using the class name tablebord to get the object and parse further
data = soup.find("div",{ "class" : "certificate"}).find("tbody").find_all("tr")

certificate_header = ["Certificate Number","Certificate Holder","Scope","Certificate Type"]


certificate_data = []
  
for item in data:
    try:
        value = item.find("td",{"class" : "last"}).get_text()
        final_value = " ".join(value.split())
        certificate_data.append(final_value)
    except:
        continue
#print(header)

final_data1 = []


print(certificate_data)
print("-------------------------------")

final_data1.append(certificate_data)
final_data1.append(certificate_data)

#print(list_header)
#print(final_data)


dataFrame = pd.DataFrame(final_data1)
   


dataFrame.to_csv("text_certi.csv", index=False, header=certificate_header)


driver.close()



"""

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
dataFrame.to_csv('assignment_final.csv',index=False)

print(row_data)

driver.close()

"""