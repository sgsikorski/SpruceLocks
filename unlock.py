import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import RPi.GPIO as gpio

url = 'https://sgsikorski.github.io/SpruceLocks'
doc = requests.get(url)

gpio.setup(17, gpio.out)
gpio.setup(18, gpio.out)
gpio.setup(19, gpio.out)
gpio.setup(20, gpio.out)
gpio.setup(21, gpio.out)
gpio.setup(22, gpio.out)
gpio.setup(23, gpio.out)
gpio.setup(24, gpio.out)
gpio.setup(25, gpio.out)
gpio.setup(26, gpio.out)

driver = webdriver.Chrome("C:\\Users\\Scott Sikorski\\CS.Workspace\\SideProjects\\chromedriver")
driver.get(url)

action = ActionChains(driver)
ele = driver.find_element_by_id("status")
action.click()

def GPIOoutput(pin1, pin2, direction):
    dir1 = True if direction == 'lock' else False
    gpio.output(pin1, dir1)
    gpio.output(pin2, False if dir1==True else True)

for line in (bs4.BeautifulSoup(doc.text, "html.parser")):
    if (line.contains('</p>')):
        if (line.contains('u1')):
            GPIOoutput(17,18,'unlock') if line.contains('Un') else GPIOoutput(17,18,'lock')
        elif (line.contains('u2')):
            GPIOoutput(19,20,'unlock') if line.contains('Un') else GPIOoutput(19,20,'lock')
        elif (line.contains('u3')):
            GPIOoutput(21,22,'unlock') if line.contains('Un') else GPIOoutput(21,22,'lock')
        elif (line.contains('u4')):
            GPIOoutput(23,24,'unlock') if line.contains('Un') else GPIOoutput(23,24,'lock')
        elif (line.contains('u4')):
            GPIOoutput(25,26,'unlock') if line.contains('Un') else GPIOoutput(25,26,'lock')




