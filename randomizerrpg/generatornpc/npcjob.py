import random 
import json


def random_job(jobtype,gender):

    with open("./lib/jobs.json", "r", encoding="utf-8") as jobs_json:
        job_json = jobs_json.read()

    job = json.loads(job_json)

    job_select = jobtype

    return random.choice(job[job_select+gender])