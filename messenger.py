import time
import selenium.webdriver
import selenium.webdriver.common.keys as KEYS
import pyautogui
import requests
import bs4
import urllib
import account


def main():
    # 使用Chrome進入Messenger的登入頁面
    option = selenium.webdriver.ChromeOptions()
    driver = selenium.webdriver.Chrome(chrome_options=option)
    driver.get('https://www.messenger.com/login/')
    time.sleep(1)

    # 在Messenger輸入帳號密碼登入
    element_username = driver.find_element_by_css_selector('input[name="email"]')
    element_username.send_keys(account.acc())
    element_password = driver.find_element_by_css_selector('input[name="pass"]')
    element_password.send_keys(account.pwd())
    element_persist = driver.find_element_by_css_selector('label.uiInputLabelLabel')
    element_persist.click()
    pyautogui.press('enter')
    time.sleep(2)

    # 設定聊天機器人的陣列，目前2個。
    url_list=['t/twTrainChatBot','t/WeatherRisk.Co']

    # 進入第一個機器人：台鐵時刻通
    # driver.get('https://www.messenger.com/'+url_list[0])
    # time.sleep(2)

    # 輸入查詢資料，以"查詢台北到台中今天班次"為例
    # element_text = driver.find_element_by_css_selector('div.notranslate')
    # element_text.send_keys('查詢台北到台中今天班次')
    # pyautogui.press('enter')
    # time.sleep(5)
    # driver.get('https://www.messenger.com/'+url_list[0])
    # time.sleep(2)

    # 讀取圖片、網路訂票和列車動態
    # element_child_1 = list([])
    # element_pic_1 = list([])
    # element_child_1 = driver.find_elements_by_css_selector('#js_1 div._1t_p:last-child div._2zgz div._4y9n')
    # for i in range(0,len(element_child_1),1)
    #     element_pic_1 = element_pic_1.append(element_child_1[i])
    
    # element_child_0.click()

    


    # 進入第二個機器人：天氣風險
    driver.get('https://www.messenger.com/'+url_list[1])
    time.sleep(2)

    # 輸入查詢資料，以"查詢台北天氣"為例
    element_text_1 = driver.find_element_by_css_selector('div.notranslate')
    element_text_1.send_keys('查詢高雄天氣')
    pyautogui.press('enter')
    time.sleep(5)
    driver.get('https://www.messenger.com/'+url_list[1])
    html_dr1 = driver.page_source
    print(html_dr1)
    time.sleep(3)
    
    # 讀取台北的一周天氣
    # element_parent_1 = driver.find_element_by_css_selector('#js_1')
    element_child_1 = driver.find_element_by_css_selector('#js_1 > div:last-child a._3cnp')
    element_pic_1 = element_child_1.get_property('href')
    print(element_pic_1)
    time.sleep(2)
    element_child_1.click()
    
    # 儲存圖片-使用selenium
    driver.get(str(element_pic_1))
    time.sleep(2)
    html_1 = driver.page_source
    driver.get('https://www.messenger.com/'+url_list[1])  
    print(html_1)
    time.sleep(3)

    # 儲存圖片-使用header(未完成)
    # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.0 Safari/537.36'}
    # r = requests.get(url=str(element_pic),headers=headers)
    # r.encoding = 'utf-8'
    # html = r.text
    # print(html)
    # time.sleep(2)

    d = bs4.BeautifulSoup(html_1,'lxml')
    im = d.find('img').get('src')
    print(str(im))
    urllib.request.urlretrieve(im,'im.png')
    print('success!')

    time.sleep(1200)

if __name__ == '__main__':
    main()
