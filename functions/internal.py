# imports may be needed, maybe not
from gettext import install
import json
from tabnanny import check
import requests
import base64
import datetime
import hashlib


class checkVersion:
    def getVersion(self):
        file = open("json-files/settings.json", "r")
        data = json.load(file)
        content = data['core']['version']
        print(content)
        ver, version, codename = content.split(" ")
        return version

    def checkVersion(self):
        installedVersion = checkVersion.getVersion
        url = 'https://api.github.com/repos/teenchatbot/botversion/contents/version.txt'
        req = requests.get(url)
        if req.status_code == requests.codes.ok:
            req = req.json()
            content = base64.b64decode(req['content'])
            content = content.decode()
            ver, version, codename = content.split(" ")
            print("your version is ", installedVersion)
            if version == installedVersion:
                return "your version is up to date"
            else:
                return "your version (" + version + ") " + "needs to be updated"
        else:
            print("content not found")


class hashes:
    def check(self):
        try:
            now = datetime.datetime.now()
            now = now.strftime('%Y-%m-%d')
            file = './logs/' + now + '.log'
            hashpath = "./hashes/" + now + ".hash"
            try:
                hashpath = open(hashpath, "r")
            except Exception:
                hashpath = "woogly"
                return "there was a rare error that occured"
            prehash = hashpath.read()
            file = open(file, "rb")
            file = file.read()
            m = hashlib.sha3_512(file).hexdigest()
            print(str(m))
            print(prehash)
            # if prehash != str(m):
                # return "the log files were not validated correctly"
        except Exception:
            return "something has happened"

    def hashfile(self, file):
        file = open(file, "rb")
        file = file.read()
        now = datetime.datetime.now()
        now = now.strftime('%Y-%m-%d')
        hashpath = './hashes/' + now + '.hash'
        m = hashlib.sha3_512(file).hexdigest()
        with open(hashpath, "w+") as f:
            f.write(str(m))
