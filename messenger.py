import time
import selenium.webdriver
import selenium.webdriver.common.keys as KEYS
import selenium.webdriver.common.by as BY
import selenium.webdriver.support.ui as UI
import selenium.webdriver.support.expected_conditions as EC

def main():
    option = selenium.webdriver.ChromeOptions()
    driver = selenium.webdriver.Chrome(chrome_options=option)
    driver.get('https://www.messenger.com/login/')
    time.sleep(1)
    element_username = driver.find_element_by_css_selector('input[name="email"]')
    element_username.send_keys('project.aien0104@gmail.com')

    element_password = driver.find_element_by_css_selector('input[name="pass"]')
    element_password.send_keys('aien0104projectp')
    element_persist = driver.find_element_by_css_selector('label.uiInputLabelLabel')
    element_persist.click()
    element_password.submit()

    time.sleep(600)

if __name__ == '__main__':
    main()
