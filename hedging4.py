import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import os, sys, subprocess
from time import time, sleep
import datetime
options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('start-maximized') # 
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
#####Telegram_Part
def telegram_bot_sendtext(bot_message):
    bot_token = '1749640480:AAF7s2naeeHm3AmUsGM6jtptKE3GwFDrs_Q'
    bot_chatID = '-597351300'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=MarkdownV2&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

PATH="D:\Royal\Automation\chromedriver.exe"
driver = webdriver.Chrome(options=options)#PATH)
# this below 3 code only for clor game###
driver.get("https://www.royal999.win/lottery-bet/SELF_COLOR_GAME")
#draw = driver.find_element_by_xpath("//div[@id='root']//div[@class='bet-box']/div[@class='head']//div[@class='last-draw']/div[@class='right']/p[contains(@class,'result')]/span[contains(@class,'ball')]").text
#print(draw)
driver.get("https://www.royal999.win/lottery-bet/SELF_STAIR")

#Fetching value from chrome:


while True:
    sleep(75 - time() % 60)
    
    p1= driver.find_element_by_xpath("(//div[@id='root']//div[@class='bet-box']/div[@class='content']/div[@class='right']//div[@class='inner']/div[@class='bd']/ul//p[@class='result']/span[contains(@class,'ball')])[5]").text
    p2= driver.find_element_by_xpath("(//div[@id='root']//div[@class='bet-box']/div[@class='content']/div[@class='right']//div[@class='inner']/div[@class='bd']/ul//p[@class='result']/span[contains(@class,'ball')])[3]").text
    p3= driver.find_element_by_xpath("(//div[@id='root']//div[@class='bet-box']/div[@class='content']/div[@class='right']//div[@class='inner']/div[@class='bd']/ul//p[@class='result']/span[contains(@class,'ball')])[1]").text
    s1= driver.find_element_by_xpath("(//div[@id='root']//div[@class='bet-box']/div[@class='content']/div[@class='right']//div[@class='inner']/div[@class='bd']/ul//p[@class='result']/span[contains(@class,'ball')])[6]").text
    s2= driver.find_element_by_xpath("(//div[@id='root']//div[@class='bet-box']/div[@class='content']/div[@class='right']//div[@class='inner']/div[@class='bd']/ul//p[@class='result']/span[contains(@class,'ball')])[4]").text
    s3= driver.find_element_by_xpath("(//div[@id='root']//div[@class='bet-box']/div[@class='content']/div[@class='right']//div[@class='inner']/div[@class='bd']/ul//p[@class='result']/span[contains(@class,'ball')])[2]").text
    p0= driver.find_element_by_xpath("(//div[@id='root']//div[@class='bet-box']/div[@class='content']/div[@class='right']//div[@class='inner']/div[@class='bd']/ul//p[@class='result']/span[contains(@class,'ball')])[7]").text
    s0= driver.find_element_by_xpath("(//div[@id='root']//div[@class='bet-box']/div[@class='content']/div[@class='right']//div[@class='inner']/div[@class='bd']/ul//p[@class='result']/span[contains(@class,'ball')])[8]").text
    pl= driver.find_element_by_xpath("(//div[@id='root']//div[@class='bet-box']/div[@class='content']/div[@class='right']//div[@class='inner']/div[@class='bd']/ul//p[@class='result']/span[contains(@class,'ball')])[9]").text
    sl= driver.find_element_by_xpath("(//div[@id='root']//div[@class='bet-box']/div[@class='content']/div[@class='right']//div[@class='inner']/div[@class='bd']/ul//p[@class='result']/span[contains(@class,'ball')])[10]").text

    pairlast = pl+sl
    pair1 = p0+s0
    pair2 = p1+s1
    pair3 = p2+s2
    pair4 = p3+s3
    
    pairall = pairlast+pair1+pair2+pair3+pair4
    print(pairall)
    print("\n................................")
    if pairall == "ACACACBDBD":
        draw = driver.find_element_by_xpath("//div[@id='root']//div[@class='bet-box']/div[@class='head']//div[@class='current']/p[@class='hd']/span[@class='issue']/em").text
        telegram_bot_sendtext("Alert 4 loss, Bet on" + ' ' + str(draw) + ' ' + "AD C")
        print("Bet on BD")

    elif pairall == "ADADADBCBC":
        draw = driver.find_element_by_xpath("//div[@id='root']//div[@class='bet-box']/div[@class='head']//div[@class='current']/p[@class='hd']/span[@class='issue']/em").text
        telegram_bot_sendtext("Alert 4 loss, Bet on" + ' ' + str(draw) + ' ' + "AC D")
        print("Bet on BC")

    elif pairall == "BCBCBCADAD":
        draw = driver.find_element_by_xpath("//div[@id='root']//div[@class='bet-box']/div[@class='head']//div[@class='current']/p[@class='hd']/span[@class='issue']/em").text
        telegram_bot_sendtext("Alert 4 loss, Bet on" + ' ' + str(draw) + ' ' + "AC B")
        print("Bet on AD")
    elif pairall == "BDBDBDACAC":
        draw = driver.find_element_by_xpath("//div[@id='root']//div[@class='bet-box']/div[@class='head']//div[@class='current']/p[@class='hd']/span[@class='issue']/em").text
        telegram_bot_sendtext("Alert 4 loss, Bet on" + ' ' + str(draw) + ' ' + "AD B")
        print("Bet on AC")
