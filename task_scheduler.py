'''

>>>>>>>>>>>>CONTEXT

Luigi is a popular data pipeline tool.
Similar tools include Apache-Airflow and Azure Data Factory.
In the context of this repo, Luigi orchestrates HTTP GET requests against open-sourced APIs.
Luigi also ensures platform stability against unexpected behavior.

'''

import luigi
from classes_and_methods import *

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
        pass
class GetPose(luigi.Task):
    def requires(self):
        return None
    def output(self):
        return luigi.LocalTarget("poseData.txt")
    def run(self):
        pass
if __name__ == '__main__':
    luigi_run_results = luigi.build([GetPose(),GetQuote(),GetAffirmation()],detailed_summary=True,
                local_scheduler=False)
