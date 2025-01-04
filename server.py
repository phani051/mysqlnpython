from flask import Flask, render_template
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/")
def home():
    today = datetime.today()
    current_year = today.year
    f = open('jobs.json', )
    data = json.load(f)
    completed_jobs = 0
    failed_jobs = 0
    job_count = 0
    for i in range(0, (data['count'])):
        jobs = (data['jobs'][job_count])
        if (jobs.get("completionStatus")) == "Succeeded":
            completed_jobs += 1
        elif (jobs.get("completionStatus")) == "Failed":
            failed_jobs += 1
        job_count += 1
    return render_template('index.html', year=current_year, jobscount=job_count, Successful=completed_jobs, failed=failed_jobs)



if __name__=="__main__":
    app.run(debug=True)