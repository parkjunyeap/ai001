from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request


# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# 오류 안뜨게 하는키

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogb")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("조코딩") # 키보드 입력값 전송 가능
elem.send_keys(Keys.RETURN)

# 스크롤 쭉 내릴거임
SCROLL_PAUSE_TIME = 1
# Get scroll height 
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height: # 끝까지 내려갔을 때
        try:
            driver.find_element(By.CSS_SELECTOR,".mye4qd").click()
        except:
            break
       
    last_height = new_height


images = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd") #작은이미지들을
count=1
for image in images:
    try:
        image.click() 
        time.sleep(2)
        url = driver.find_element(By.XPATH,"/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img").get_attribute("src")
        urllib.request.urlretrieve(url, str(count) + ".jpg")
        count = count +1
    except:
        pass
# driver.implicitly_wait(10)  안꺼지게 할려했는데 안됨.

while(1):
    pass

    
driver.close( )
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close() 

