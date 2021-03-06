from selenium import webdriver
import time
import datetime as date
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chromeoptions = Options()
chromeoptions.add_argument("start-maximized")
chromeoptions.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
    })

chromedriver = webdriver.Chrome(chrome_options = chromeoptions, executable_path="/home/kiaria/Documents/github_projects/lazyteems/chromedriver")
chromedriver.get("https://teams.microsoft.com")
team_to_join = ""
login_email = input("Enter your email here\n")
login_password = input("Enter your password")

def login(email, password):
    email_field = chromedriver.find_element_by_xpath('//*[@id="i0116"]')
    password_field = chromedriver.find_element_by_xpath('//*[@id="i0118"]')
    email_field.send_keys(email)
    chromedriver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    password_field.send_keys(password)
    time.sleep(3)
    chromedriver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(3)
    chromedriver.find_element_by_xpath('//*[@id="idBtn_Back"]').click()

def write_timetable():
    print("Enter exact team names of 8'o clock classes, starting from monday separated by commas. Enter \"none\" if there is no class")
    am8 = open("am8classes.txt", "a")
    am8class = input().split(",")
    for x in am8class:
        am8.write(x)
        am8.write("\n")
    am8.close()
    print("Enter exact team names of 9'o clock classes, starting from monday separated by commas. Enter \"none\" if there is no class")
    am9 = open("am9classes.txt", "a")
    am9class = input().split(",")
    for x in am9class:
        am9.write(x)
        am9.write("\n")
    am9.close()
    print("Enter exact team names of 10'o clock classes, starting from monday separated by commas. Enter \"none\" if there is no class")
    am10 = open("am10classes.txt", "a")
    am10class = input().split(",")
    for x in am10class:
        am10.write(x)
        am10.write("\n")
    am10.close()
    print("Enter exact team names of 11'o clock classes, starting from monday separated by commas. Enter \"none\" if there is no class")
    am11 = open("am11classes.txt", "a")
    am11class = input().split(",")
    for x in am11class:
        am11.write(x)
        am11.write("\n")
    am11.close()
    print("Enter exact team names of 2'o clock classes, starting from monday separated by commas. Enter \"none\" if there is no class")
    pm2 = open("pm2classes.txt", "a")
    pm2class = input().split(",")
    for x in pm2class:
        pm2.write(x)
        pm2.write("\n")
    pm2.close()
    print("Enter exact team names of 4'o clock classes, starting from monday separated by commas. Enter \"none\" if there is no class")
    pm4 = open("pm4classes.txt", "a")
    pm4class = input().split(",")
    for x in pm4class:
        pm4.write(x)
        pm4.write("\n")
    pm4.close()
    print("Enter exact team names of 5:30 pm classes, starting from monday separated by commas. Enter \"none\" if there is no class")
    pm530 = open("pm530classes.txt", "a")
    pm530class = input().split(",")
    for x in pm530class:
        pm530.write(x)
        pm530.write("\n")
    pm530.close()

def read_timetable():
    now = date.datetime.now()
    day = now.strftime("%A").lower()
    hour = int(now.hour)
    min = int(now.minute)
    curent_teamname = ""
    if hour == 8 and min<45:
        am8file = open("am8classes.txt", "r")
        if day == "monday":
            curent_teamname = am8file.read(0)
        elif day == "tuesday":
            curent_teamname = am8file.read(1)
        elif day == "wednesday":
            curent_teamname = am8file.read(2)
        elif day == "thursday":
            curent_teamname = am8file.read(3)
        elif day == "friday":
            curent_teamname = am8file.read(4)
    elif hour == 9 and min<45:
        am9file = open("am9classes.txt", "r")
        if day == "monday":
            curent_teamname = am9file.read(0)
        elif day == "tuesday":
            curent_teamname = am9file.read(1)
        elif day == "wednesday":
            curent_teamname = am9file.read(2)
        elif day == "thursday":
            curent_teamname = am9file.read(3)
        elif day == "friday":
            curent_teamname = am9file.read(4)
    elif hour == 10 and min<45:
        am10file = open("am10classes.txt", "r")
        if day == "monday":
            curent_teamname = am10file.read(0)
        elif day == "tuesday":
            curent_teamname = am10file.read(1)
        elif day == "wednesday":
            curent_teamname = am10file.read(2)
        elif day == "thursday":
            curent_teamname = am10file.read(3)
        elif day == "friday":
            curent_teamname = am10file.read(4)
    elif hour == 11 and min<45:
        am11file = open("am11classes.txt", "r")
        if day == "monday":
            curent_teamname = am11file.read(0)
        elif day == "tuesday":
            curent_teamname = am11file.read(1)
        elif day == "wednesday":
            curent_teamname = am11file.read(2)
        elif day == "thursday":
            curent_teamname = am11file.read(3)
        elif day == "friday":
            curent_teamname = am11file.read(4)
    elif hour == 14:
        pm2file = open("pm2classes.txt", "r")
        if day == "monday":
            curent_teamname = pm2file.read(0)
        elif day == "tuesday":
            curent_teamname = pm2file.read(1)
        elif day == "wednesday":
            curent_teamname = pm2file.read(2)
        elif day == "thursday":
            curent_teamname = pm2file.read(3)
        elif day == "friday":
            curent_teamname = pm2file.read(4)
    elif hour == 16:
        pm4file = open("pm4classes.txt", "r")
        if day == "monday":
            curent_teamname = pm4file.read(0)
        elif day == "tuesday":
            curent_teamname = pm4file.read(1)
        elif day == "wednesday":
            curent_teamname = pm4file.read(2)
        elif day == "thursday":
            curent_teamname = pm4file.read(3)
        elif day == "friday":
            curent_teamname = pm4file.read(4)
    elif hour == 17 and min>30:
        pm530file = open("pm530classes.txt", "r")
        if day == "monday":
            curent_teamname = pm530file.read(0)
        elif day == "tuesday":
            curent_teamname = pm530file.read(1)
        elif day == "wednesday":
            curent_teamname = pm530file.read(2)
        elif day == "thursday":
            curent_teamname = pm530file.read(3)
        elif day == "friday":
            curent_teamname = pm530file.read(4)
    
    return curent_teamname

def join_class(team_name):
    time.sleep(15)
    chromedriver.find_element_by_xpath('//*[@id="app-bar-2a84919f-59d8-4441-a975-2a8c2643b741"]').click()
    time.sleep(5)
    searchbox = chromedriver.find_element_by_xpath('//*[@id="controlbox-input-group"]')
    searchbox.click()
    time.sleep(2)
    searchbox_input = chromedriver.find_element_by_xpath('//*[@id="searchInputField"]')
    searchbox_input.send_keys(team_name)
    time.sleep(1)
    searchbox_input.send_keys(Keys.DOWN)
    time.sleep(1)
    searchbox_input.send_keys(Keys.ENTER)
    time.sleep(4)
    join1 = chromedriver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/middle-messages-stripe/div/messages-header/div[2]/div/message-pane/div/div[1]/div/div/message-list/div/virtual-repeat/div/div[15]/div/thread/div/div[2]/calling-thread-header/div/calling-join-button/button')
    join1.send_keys(Keys.ENTER)
    time.sleep(3)
    chromedriver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button').click()
    time.sleep(2)
    join = chromedriver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    join.send_keys(Keys.ENTER)


#if os.path.exists("am8classes.txt") == False:
#    write_timetable()
#else:
#    team_to_join = read_timetable()

login(login_email, login_password)
join_class("MAT1014-Winter 20-21-A1")
