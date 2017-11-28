from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

objectName = "iss"

driver = webdriver.Chrome("C://Dev//chromedriver_win32//chromedriver.exe")
driver.get("http://www.satflare.com/iss/?q=" + objectName)

csvPath = "C://Dev//data//" + objectName + "//temp.csv"
if not os.path.exists(csvPath):
    f = open(csvPath, "w+")
    f.close()

while True:
    lat = driver.find_element_by_id("DisplayWorkingSatLatitude").text
    if lat == "":
        time.sleep(5)
        continue
    else:
        break

while True:
    lat = driver.find_element_by_id("DisplayWorkingSatLatitude").text
    lon = driver.find_element_by_id("DisplayWorkingSatLongitude").text
    alt = driver.find_element_by_id("DisplayWorkingSatAltitude").text
    currentTime = time.gmtime()

    line = {
        float(lat),
        float(lon),
        float(alt),
        time.time()
    }

    with open(csvPath, "a", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(line)

    time.sleep(1)
