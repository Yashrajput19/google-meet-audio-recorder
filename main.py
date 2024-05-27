import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

opt = Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(options=opt)


def join_meet():

    driver.get('https://accounts.google.com/')

    username = driver.find_element(By.ID, 'identifierId')
    username.click()
    username.send_keys('Your Gmail ID')

    next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
    next_button.click()
    time.sleep(5)
    
    password = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    password.click()
    password.send_keys('Your Password')

    next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
    next_button.click()
    time.sleep(5)

    driver.get('Google meet link')

    time.sleep(5)

    mic_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[26]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[7]/div[1]/div/div/div[1]')
    mic_button.click()

    time.sleep(5)

    camera_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[26]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[7]/div[2]/div/div[1]')
    camera_button.click()

    time.sleep(5)

    join_button = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div[26]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]')
    join_button.click()


def meeting():

	while True:
            
            try:
                join_now = driver.find_element(By.XPATH ,'//*[@id="yDmH0d"]/c-wiz/div/div/div[26]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button/span')

            except NoSuchElementException :
                
                try:
                    
                    members_in_meet = int(driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div[25]/div[3]/div[10]/div/div/div[3]/div/div[2]/div/div/div').text.strip())
                    
                    if members_in_meet < 2:
                        driver.quit()
                        break

                except:
                    pass
                 
            time.sleep(6)


join_meet()
meeting()

