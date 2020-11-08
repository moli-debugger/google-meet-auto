# Libraries what we need for our program are imported below
import datetime
import time
from selenium import webdriver
import cv2
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui as pg
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument('--ignore-ssl-errors=yes')
opt.add_argument('--ignore-certificate-errors')
#opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("–disable-notifications")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(options=opt,executable_path='D:\webdrivers\chromedriver.exe')
now=datetime.datetime.now()
print(now)
current_time = now.strftime("%H:%M / %A")
j=datetime.date.today()
print(j)
justtime = now.strftime("%H:%M")
print(justtime)
print (current_time)






def login():
    driver.get("https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F1%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F1%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("YOUR MAIL ID HERE")
    time.sleep(2)
    # Next Button:
    next=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
    next.click()
    time.sleep(5)
    #Password:
    driver.find_element_by_xpath("//input[@name='password']").send_keys("YPUR PASSWORD HERE")
    time.sleep(2)
    #next button:
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
    time.sleep(5)
def java():
    driver.get('https://classroom.google.com/u/1/c/MTE0NDY3ODM3MTAx')
    time.sleep(5)
    l=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[1]/div/div[1]')
    driver.find_elements_by_class_name('QRiHXd')
    driver.find_element_by_partial_link_text('http').click()
    time.sleep(4)





def ml():
    driver.get('https://classroom.google.com/u/1/c/OTk5OTI4NzYwMDla')
    time.sleep(5)
    l=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[1]/div/div[1]')
    driver.find_elements_by_class_name('QRiHXd')
    driver.find_element_by_partial_link_text('http').click()

def os():
    driver.get('https://classroom.google.com/u/1/c/MTE1NDQ4OTAyNjE4')
    time.sleep(5)
    l=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[1]/div/div[1]')
    driver.find_elements_by_class_name('QRiHXd')
    driver.find_element_by_partial_link_text('http').click()

def Or():
    driver.get('https://classroom.google.com/u/1/c/MTEzNTM1MjMzMjcz')
    time.sleep(5)
    l=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[1]/div/div[1]')
    driver.find_elements_by_class_name('QRiHXd')
    driver.find_element_by_partial_link_text('http').click()



classroom_id=input('''enter the classroom name:
os 
or
java
ml''')
if(classroom_id=='java'):
    login()
    time.sleep(3)
    java()
elif(classroom_id=='ml'):
    login()
    time.sleep(3)
    ml()


elif(classroom_id=='os'):
    login()
    time.sleep(3)
    os()

elif(classroom_id=='or'):
    login()
    time.sleep(3)
    Or()



driver.refresh()
i=driver.get_window_position()
print(i)
time.sleep(5)

time.sleep(5)

pg.hotkey('ctrl','d')
pg.hotkey('ctrl','e')
for i in range(5):
    pg.press('tab')
time.sleep(2)
pg.press('enter')
