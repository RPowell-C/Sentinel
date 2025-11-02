import requests


class filesay:
    def filesay(self, url):
        contents = requests.get(url).text.split("\n")
        return contents
