import requests
import re
from bs4 import BeautifulSoup
from csv import writer
import socket
import json
import ast
import pandas as pd
import sys
import datetime
import js2xml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#url = "https://afx.kwayisi.org/ngx/access.html"
url = "https://afx.kwayisi.org/chart/ngx/access"
#url = "https://www.worldweatheronline.com/canberra-weather-averages/australian-capital-territory/au.aspx"
# url = "https://www.investsmart.com.au/invest-with-us/investsmart-growth-portfolio"

driver = webdriver.Chrome()
driver.get(url)

ids = driver.find_elements_by_xpath('//*')
#element = driver.find_elements(By.TAG_NAME, 'body')
for ii in ids:
    print(ii.text)
    #print(element) 

driver.close()


# try:
#     soup = BeautifulSoup(requests.get(url).content, "html.parser")
#     print("content gotten")

# #script = soup.find("script", text=re.compile("Highcharts.charts")).string
# #all_scripts = soup.find_all('script')
#     print(soup.contents)
# except:
#     #r.status_code = "Connection refused"
#     print("Connection refused")


# #print(len(all_scripts))
#script_text = all_scripts[0].text
#print(script_text)
# parsed = js2xml.parse(script)

# print(js2xml.pretty_print(parsed))
## print(script)
