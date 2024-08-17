import datetime
from functions import internal
import json
import requests




class logs:
    def writeToLogs(message, username="phoibe"):
        now1 = datetime.datetime.now()
        time = now1.strftime('%Y-%m-%d %H:%M:%S')
        date = now1.strftime('%Y-%m-%d')
        file = "./logs/" + date + ".log"
        with open(file, "a+") as f:
            f.write(str(time) + " - " + username + " - " + message + "\n")
            internal.hashes.hashfile(file)
class basics:
    def checkVersion():
        x = requests.get('https://pages-theta-blond.vercel.app/api/hello')
        data = json.loads(x.text)
        with open("json-files/settings.json") as f:
            data2 = json.load(f)
        installedVersion = data2['core']['version']

        if data['version'] != installedVersion:
            return "an update is needed"
        if data['version'] == installedVersion:
            return "version is up to date"
