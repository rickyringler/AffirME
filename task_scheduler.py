import luigi
from classes_and_methods import *

"""
What does this do?
1. Luigi imports all class and methods from classes_and_methods Python script.
2. Luigi asks the objects to execute their methods.
3. Tasks rely on an output in order to be classified as successful.
"""

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