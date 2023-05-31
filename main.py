from selenium import webdriver
from fake_useragent import UserAgent
from os.path import isfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle # для сохранения дампа
import random
import time
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

url = 'https://ogo1.ru/personal/'

user_agent_list = {'PS5':'Mozilla/5.0 (PlayStation; PlayStation 5/2.26) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15',
                   'Amazon 4K Fire TV':'Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36',
                   'EDGE':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
                   'Linux':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
                   'iOS':'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1',
                   'Android':'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
                   'Chrome':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

fakeuseragent=UserAgent()


option = webdriver.ChromeOptions()
option.add_argument(f"user-agent={user_agent_list['Chrome']}")   #{user_agent_list[random.choice(list(user_agent_list))]}")
# option.add_argument('--proxy-server=5.161.186.127:8080')   # set proxy
option.add_argument('--disable-blink-features=AutomationControlled') # отключить WebDriver
# option.add_argument('--headless') # работа в фоновом режиме

# proxy_options = {
#     'proxy': {
#         'https': f'http://your_proxy_login:your_proxy_password@138.128.91.65:8000'
#     }
# }  # proxy с авторизацией


driver = webdriver.Chrome(options=option)  #executable_path = r'C:\Users\stbut\PycharmProjects\pythonProject\ChromeSeleniumDriver\chromedriver')


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com") установка драйвера


try:
    driver.get('https://www.avito.ru/moskva_i_mo?cd=1&q=%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D1%8F+2+%D1%80%D1%83%D0%B1%D0%B8%D0%BD')
    driver.implicitly_wait(2)

    items = driver.find_elements(By.XPATH, "//div[@data-marker='item-photo']")
    items[1].click()

    driver.switch_to.window(driver.window_handles[1])

    username = driver.find_element(By.CLASS_NAME, 'styles-module-size_ms-EVWML')
    print(username.text)
    driver.get_screenshot_as_file(f'{username.text}.png' )

    driver.implicitly_wait(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()



    # if isfile('ChromeSeleniumDriver/st.butcher'):
    #     for cookie in pickle.load(open('ChromeSeleniumDriver/st.butcher','rb')):
    #         driver.add_cookie(cookie)
    #     driver.refresh()
    #
    #
    # else:
    #
    #     email_input = driver.find_element(By.NAME,'USER_LOGIN')
    #     email_input.clear()
    #     email_input.send_keys('st.butcher@mail.ru')
    #
    #     password_input = driver.find_element(By.NAME,'USER_PASSWORD')
    #     password_input.clear()
    #     password_input.send_keys('963963')
    #     password_input.send_keys(Keys.ENTER)
    #
    #     pickle.dump(driver.get_cookies(), open('ChromeSeleniumDriver/st.butcher','wb'))
    time.sleep(3)

