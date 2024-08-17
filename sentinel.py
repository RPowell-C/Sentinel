# imports

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# non function, but still important imports
import time
import random
import json
import threading

# function imports
from functions import settings
from functions import filesay
from functions import internalFunctions
from functions import moderation
from functions import UCAL
from functions import Api



# selenium shit


opts = Options()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)
browser.get("https://y99.in/web/login/")
a = ActionChains(browser)


# find the button to login to an account
access_y99_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'blue--text.login-instead')))
# click the button found above
access_y99_button.click()

# input the username
browser.find_element(By.CLASS_NAME, 'input-username').send_keys(settings.core.username)
# input the password
browser.find_element(By.CLASS_NAME, 'input-username.mt-1').send_keys(settings.core.password)
# click the button to login
browser.find_element(By.CLASS_NAME, 'mx-0.btn.btn--large.btn--depressed.e4jtrd').click()
print("Logged in")

# get past the staging page

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="welcome-page"]/div/div[3]/button'))).click()
print("past the staging page")

# Firefox options go here

# Get rid of the popup

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[12]/div/div/div[3]/button[1]'))).click()

print("got rid of the popup")
print("entering the chat")

# lookup the room by room code
searchRoom = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[26]/div[1]/div[2]/div[9]/div/div[2]/input')))
searchRoom.click()
time.sleep(.1)
searchRoom.send_keys(settings.core.room)

# enter the chatroom with the code from settings.json
chatroom = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[26]/div[1]/div[2]/div[9]/div/div[3]/div[2]/div[2]/div/div[1]/div/div/div[3]/button[1]')))
chatroom.click()
time.sleep(.5)
print("entered the chat")





# reading and stripping down the messages so that they can be proccesses by the bot
def read_messages():
    time.sleep(.2)
    WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@class="log-container may-transform"]')))
    LastMessage = browser.find_elements(By.XPATH, '//*[@class="log-container may-transform"]')[-1]
    try:
        message_text = LastMessage.find_element(By.CLASS_NAME, 'text').text
    except Exception:
        message_text = ""
    username_text = LastMessage.find_element(By.CLASS_NAME, 'username').text
    return username_text, message_text




def send_message(message):
    time.sleep(.2)
    global userBuffer
    userBuffer = settings.core.username
    text_area = browser.find_element(By.XPATH, '/html/body/div[1]/div[26]/div[1]/div[2]/div[8]/div[3]/div[1]/div[5]/div[2]/div/div/textarea')
    text_area.click()
    text_area.send_keys(message)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[26]/div[1]/div[2]/div[8]/div[3]/div[1]/div[5]/div[2]/div/div/div[4]').click()
# API shit
def runAPI():
    Api.shitfuck()

def update_username(username):
    Api.update_username(username)

def update_message(message):
    Api.update_message(message)
x = threading.Thread(target=runAPI)
x.daemon = True
x.start()
print("successfully threaded API server")






# Tools
muteChat = False
trustedUsers = settings.core.trustedUsers


userBuffer = settings.core.username
send_message(str(internalFunctions.basics.checkVersion()))
mesBuffer = ""
time.sleep(.3)
# send_message(settings.core.entrances)
while True:
    try:
        username, message = read_messages()
        if message == "":
            message = "(No Message)"
        if username == "":
            username = userBuffer
        if username != "":
            userBuffer = username
        if message != mesBuffer:
            moderation.moderator.add_strikes(username, 0)
            internalFunctions.logs.writeToLogs(message, username)
            mesBuffer = message
            print("[" + username + "]")
            print(message)
            update_username(username)
            update_message(message)
            if muteChat:
                if UCAL.ucal.check(username, 10):
                    moderation.moderator.delete_message(browser)
            if UCAL.ucal.check(username, 5):
                moderation.moderator.delete_message(browser)
            for thing in settings.moderation.triggers:
                if thing in message:
                    moderation.moderator.delete_message(browser)
                    moderation.moderator.add_strikes(username, 1)
            if moderation.moderator.strikes(username) >= settings.moderation.strikes:
                moderation.moderator.ban_user(username, browser)


        if message.startswith(".version"):
            send_message(str(settings.core.version))
# Moderation shit
        if message.startswith(".mute-chat"):
            if settings.funcSettings.useModerationTools:
                if username in trustedUsers:
                    send_message("/notice A chat wide mute has been activated")
                    muteChat = True
                    internalFunctions.logs.writeToLogs(username + " muted the chat")
        if message.startswith(".unmute-chat"):
            if settings.funcSettings.useModerationTools:
                if username in trustedUsers:
                    send_message("/notice The chat has been unmuted")
                    muteChat = False
                    internalFunctions.logs.writeToLogs(username + " unmuted the chat")

# commands


        if message.startswith(".ban"):
            if settings.funcSettings.useBan:
                if UCAL.ucal.check(username, settings.ucalLevels.ban):
                    try:
                        cmd, user = message.split(" ")
                    except:
                        send_message("an error has occured with banning")
                    moderation.moderator.ban_user(user, browser)
                    internalFunctions.logs.writeToLogs(username + " banned " + user)
                    send_message("/notice " + user + " has been banned")
                else:
                    send_message("You do not have a high enough level to ban people")
# filesay
        if message.startswith(".filesay"):
            if settings.funcSettings.useFilsay is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Filsay) is True:
                        command, url = message.split(" ")
                        internalFunctions.logs.writeToLogs(username + " used filesay with this link: " + str(url))
                        contents = filesay.filesay.filesay(url)
                        for thing in contents:
                            time.sleep(3)
                            send_message(thing)
            else:
                send_message("this command has been disabled")
# raise level
        if message.startswith(".raiseLevel"):
            if settings.funcSettings.useRaiseLevel is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.raiseLevel) is True:
                        com, target, level = message.split(" ")
                        UCAL.ucal.raiseLevel(target, level)
                        send_message(target + "'s level has been raised by " + level)
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    send_message("UCAL is not used in this room")
            else:
                send_message("UCAL is not used in this room, you must like killing puppies")
    except KeyboardInterrupt():
        print("interrupt recieved")

