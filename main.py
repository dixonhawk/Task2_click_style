import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://www.arealme.com/colors/ru/')

start_button = driver.find_element('class name','pure-button-primary')
start_button.click()
wait_element = True

while True:
    try:
        get_elememts = driver.find_elements('xpath',
                                            '//span[contains(@style, "width: ")  and contains(@style, "background-color")]')

        array = {}
        for i in get_elememts:
            array[i] = i.value_of_css_property('background-color')

        flipped = {}
        for key, value in array.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                flipped[value].append(key)

        for key, value in flipped.items():
            if len(value) == 1:
                value[0].click()
    except:
        break