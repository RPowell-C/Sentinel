import requests


class filesay:
    @staticmethod
    def filesay(url):
        contents = requests.get(url).text.split("\n")
        return contents
