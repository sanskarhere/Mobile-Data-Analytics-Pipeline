from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, TimeoutException



#Setting Configuration for webdriver
options=Options()

#essential arguments
# chrome_options.add_argument("--headless=new")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
options.add_experimental_option("excludeSwitches", ["enable-automation"])


#Instantiated WebDriver -> launch Chrome
driver=webdriver.Chrome(options=options)


#Search SmartPrix 
driver.get('https://www.smartprix.com/mobiles')

driver.maximize_window()

driver.implicitly_wait(5)

#Exclude OutofStock
driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()

#Exclude Upcoming Product
driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()




old_height =driver.execute_script('return document.body.scrollHeight')



while True:

    try :
        time.sleep(1)
        print(old_height)
        time.sleep(10)

        #load more product
        btn=driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div/div[3]')
        btn.click()

        time.sleep(5)
        new_height=driver.execute_script('return document.body.scrollHeight')
        

        if old_height == new_height:
            break


        old_height=new_height

    except Exception:
        continue

html=driver.page_source


#Save Html Page
path='data/html/mobile.html'
os.makedirs(os.path.dirname(path),exist_ok=True)

with open(path,'w',encoding='UTF-8') as f:
    f.write(html)

driver.quit()