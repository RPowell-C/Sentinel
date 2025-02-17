from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

class backlog:
    def assign(username):
        try:
            if username != "read":
                return "ok, " + username + " has been reported"
        except Exception:
            return "an error has occured"
    def read():
        usernames = open("./syscrit/people/backlog.txt", "r")
        usernames = str(usernames.read())
        usernames = usernames.replace("\n", " ")
        return usernames
class blacklist:
    def check(username):
        blacklist = open("./syscrit/people/blacklist.txt", "r")
        blacklist = str(blacklist.read)
        true_blacklist = blacklist.split("\n")
        if username in true_blacklist:
            return True
        else:
            return False
class minimods:
    def mMods():
        with open("./syscrit/people/minimods.txt") as f:
            lin = f.read()
            lines = lin.split("\n")
            return lines
    def test():
        return "your test has been successful"
class regUsers:
    def check(username):
        with open("./syscrit/people/regusers.txt", "r") as f:
            lin = str(f.read())
            users = lin.split("\n")
            if username in users:
                return True
            else:
                return False
class moderator:
    def get_muted_users():
        with open("syscrit/people/mute.txt", "r") as file:
            lines = file.read()
            lines = lines.split("\n")
            return lines
    def delete_message(browser, message):
        tripleDots = message.find_elements(By.XPATH, ".//div[contains(@class, 'message-tooltip') and contains(@class, "
                                              "'show-on-hover')]//button[contains(@class, 'btn--flat') and contains("
                                              "@class, 'btn--icon')]")[-1]
        browser.execute_script("arguments[0].click();", tripleDots)
        delete_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'list__tile') and contains(@class, 'list__tile--link')]//div[contains(@class, 'list__tile__title') and text()='Delete Message']")))

        delete_button.click()
    def ban_user(username, browser):
        settingsButton = browser.find_elements(By.XPATH, '//*[@class="tooltip tooltip--left"]')
        ActionChains(browser).move_to_element(settingsButton[2]).click().perform()
        e = browser.find_elements(By.XPATH, '//*[@class="tabs__container"]')
        securityButton = browser.find_element(By.XPATH, '/html/body/div[1]/div[31]/div[2]/div[1]/div[1]/div/div[1]/div/div/div[3]/a').click()
        banButton = browser.find_element(By.XPATH, '/html/body/div[1]/div[31]/div[2]/div[1]/div[1]/div/div[2]/div[3]/div/div/div[1]/button/div').click()
        inputField = browser.find_element(By.XPATH, '//*[@class="input-group__input"]')
        inptFld = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/input')
        inptFld.send_keys(username)
        time.sleep(1)
        continueButton = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[3]/button[2]/div').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@class="toolbar__content"]')
        e2 = browser.find_element(By.XPATH, '/html/body/div[1]/div[31]/div[2]/div[2]/div[1]/nav/div/button')
        ActionChains(browser).move_to_element(e2).click().perform()
    def strikes(username):
        with open("json-files/strikes.json", "r") as f:
            data = json.load(f)
        shitfuck = data[username]
        return shitfuck
    def add_strikes(username, strikes):
        with open("json-files/strikes.json", "r") as f:
            data = json.load(f)
        if username not in data.keys():
            data[username] = strikes
        if username in data.keys():
            data[username] += strikes
        with open("json-files/strikes.json", "w") as f:
            json.dump(data, f, indent=4)

