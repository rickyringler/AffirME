import luigi
import pandas
import requests
import json

class apiRequest():
    def __init__(self,url):
        self.url = url
    def getRequest(self):
        data = requests.get(url = self.url)
affirmation = apiRequest("https://www.affirmations.dev/")
print(affirmation.getRequest())