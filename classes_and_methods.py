import requests
import json
from datetime import date

"""
What does this do?
1. apiRequest is a class that takes a database name and API URL endpoint as arguments
2. When we instantiate a class, the API request method is looped until an output is successful, i.e. we get our data.
        Why is it looped?:
   This prevents the application from failing in the instance of a bad API request.
   Sometimes data extracted from API contains risky data such as unique characters that our application cannot read.
3. When we get our data from the API, the data is also converted into a string and stored with a timestamp.
        Why is the data stored with a timestamp?:
   This means we can aggregate data into a small, loosely-structured database. This provides us with additional functionality.
   For example: If the user wanted to know what the yoga pose was a week ago, we have the data stored to perform this action.
   This also effectively means we could create an API for our application if desired.
"""

#Note: I couldn't find reliable, open-sourced APIs for the quote or yoga pose - but you get the point.

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


#Couldn't find an open-sourced yoga API.
temp_pose = None
while temp_pose == None:
    try:
        #pose = apiRequest("poseData","https://yoga-api-nzy4.onrender.com/v1/poses" )
        #temp_pose = pose.getRequest()
        temp_pose = "Downwards Dog"
    except: pass

temp_quote = None
while temp_quote == None:
    try:
        #quote = apiRequest("quoteData", "https://philosophy-quotes-api.glitch.me/quotes/philosophy/stoicism")
        #temp_quote = quote.getRequest()
        temp_quote = "Life can be only understood backwards, but must be lived forwards."
    except: pass