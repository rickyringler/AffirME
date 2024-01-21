'''

>>>>>>>>>>>>CONTEXT

This script defines and implements methods for:
1. API requests.
2. Installing local storage units.
3. Exception-handling.

'''

import requests
import json
from datetime import date

today = date.today()
class apiRequest():
    def __init__(self,name,url):
        self.name = name
        self.url = url
    def getRequest(self):
        try:
            data = requests.get(url = self.url)
            request_data = str(data.text)
            json_request_data = json.loads(request_data)

            date_data = {}
            date_data["date"] = str(today)

            data = {**json_request_data, **date_data}
            database = open(f"{self.name}.txt", "a")
            database.write(str(json_request_data))
            database.write("\n")

            return data
        except: f"Error with source site{self.url}"


temp_affirmation = None
while temp_affirmation == None:
    try:
        affirmation = apiRequest("affirmationsData", "https://www.affirmations.dev/")
        temp_affirmation = affirmation.getRequest()
        temp_affirmation = json.loads(str(temp_affirmation).replace("'", '"'))
        temp_affirmation = temp_affirmation["affirmation"]
    except: pass

temp_pose = None
while temp_pose == None:
    try:
        pose = apiRequest("poseData","https://yoga-api-nzy4.onrender.com/v1/poses" )
        temp_pose = pose.getRequest()
        temp_pose = "Downwards Dog"
    except: pass

temp_quote = None
while temp_quote == None:
    try:
        quote = apiRequest("quoteData", "https://philosophy-quotes-api.glitch.me/quotes/philosophy/stoicism")
        temp_quote = quote.getRequest()
        temp_quote = "Life can be only understood backwards, but must be lived forwards."
    except: pass
