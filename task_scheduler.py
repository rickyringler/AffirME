"""
What does this do?
1. Creates class for requests. Gets data from APIs.
2. Class method gets data, creats database, stores data.
3. Luigi pipeline executes and orchestrates getting data.
"""

import luigi
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

affirmation = apiRequest("affirmationsData","https://www.affirmations.dev/")
temp_affirmation = affirmation.getRequest()

pose = apiRequest("poseData","https://yoga-api-nzy4.onrender.com/v1")
temp_pose = pose.getRequest()

'''


quote = apiRequest("quoteData","https://philosophy-quotes-api.glitch.me")
print(quote.getRequest()




class GetAffirmation(luigi.Task):
    def requires(self):
        return None
    def output(self):
        return luigi.LocalTarget("affirmationsData.txt")
    def run(self):
        affirmation.getRequest()
class GetQuote(luigi.Task):
    def requires(self):
        return None
    def output(self):
        return luigi.LocalTarget("quoteData.txt")
    def run(self):
        quote.getRequest()
class GetPose(luigi.Task):
    def requires(self):
        return None
    def output(self):
        return luigi.LocalTarget("poseData.txt")
    def run(self):
        pose.getRequest()

if __name__ == '__main__':
    luigi_run_results = luigi.build([GetPose(),GetQuote(),GetAffirmation()],detailed_summary=True,
                local_scheduler=False)
'''
