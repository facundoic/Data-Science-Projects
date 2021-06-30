from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import requests
import time
import json


from config import link,driver_path

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--ignore-certificate-errors')
chromeOptions.add_argument('--start-maximized')
chromeOptions.add_argument('--incognito')
#chromeOptions.add_argument('--headless')

desired_capabilities = DesiredCapabilities.CHROME.copy()
desired_capabilities['chrome.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'

driver = webdriver.Chrome(
    executable_path=driver_path,
    options=chromeOptions,
    desired_capabilities=desired_capabilities
)

driver.get(link)
time.sleep(1)
req = requests.post(
    url = link
)
data = json.load(req.content.decode('utf8'))
print(data)
driver.quit()
