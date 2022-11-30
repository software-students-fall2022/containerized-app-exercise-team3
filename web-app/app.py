from flask import Flask, render_template, request, redirect, url_for, make_response
from dotenv import dotenv_values

import pymongo
import datetime
from bson.objectid import ObjectId
import sys

# instantiate the app
app = Flask(__name__)

# load credentials and configuration options from .env file
# if you do not yet have a file named .env, make one based on the template in env.example
config = dotenv_values(".env")

# turn on debugging if in development mode
if config['FLASK_ENV'] == 'development':
    # turn on debugging, if in development
    app.debug = True # debug mnode


# connect to the database
cxn = pymongo.MongoClient(config['MONGO_URI'], serverSelectionTimeoutMS=5000)
try:
    # verify the connection works by pinging the database
    cxn.admin.command('ping') # The ping command is cheap and does not require auth.
    db = cxn[config['MONGO_DBNAME']] # store a reference to the database
    print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
except Exception as e:
    # the ping command failed, so the connection is not available.
    print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
    print('Database connection error:', e) # debug

# set up the routes

# route for the home page
@app.route('/')
def home():
    """
    Route for the home page
    """
    jobs = db.jobs.find()
    str_submitted = "Jobs in database: " + str(db.jobs.count_documents({})) + "\n"
    num_succeed = db.jobs.count_documents({"status": "COMPLETED"})
    str_succeed = "Jobs succeeded: " + str(num_succeed) + "\n"
    num_failed = db.jobs.count_documents({"status": "FAILED"})
    str_failed = "Jobs failed: " + str(num_failed) + "\n"
    str_processing = "Jobs processing: " + str(db.jobs.count_documents({"status": "IN_PROCESS"})) + "\n"
    if num_failed + num_succeed != 0:
        success_rate = round((num_succeed/(num_succeed+num_failed))*100)
    else:
        success_rate = 0
    str_success_rate = "Success rate: " + str(success_rate) + "%\n"
    success_doc = db.jobs.find({"status": "COMPLETED"})
    total_completion = datetime.timedelta()
    total_wait = datetime.timedelta()
    for each in success_doc:
        completion = each["completion_time"] - each["start_time"]
        wait = each["start_time"] - each["creation_time"]
        total_completion += completion
        total_wait += wait
    avg_completion = "Average completion time of jobs: " + str((total_completion / num_succeed).total_seconds()) + "s"
    avg_wait = "Average wait time of jobs: " + str((total_wait / num_succeed).total_seconds()) + "s"
    return render_template('index.html', jobs=jobs, submitted=str_submitted,
                           num_succeed=str_succeed, failed=str_failed, processing=str_processing,
                           success_rate=str_success_rate, avg_completion=avg_completion, avg_wait=avg_wait)
    # render the home template

@app.route('/job/<job_id>')
def job(job_id):
    """
    Route for the job page
    """
    job = db.jobs.find_one({'_id': ObjectId(job_id)})
    print(job)
    if job["status"] == "COMPLETED":
        total_time = 0
        total_confidence = 0
        count = 0
        for i in range(len(job["transcript_items"])):
            if job["transcript_items"][i]["type"] == "pronunciation":
                time_added = float(job["transcript_items"][i]["end_time"])\
                             - float(job["transcript_items"][i]["start_time"])
                confidence_added = float(job["transcript_items"][i]["alternatives"][0]["confidence"])
                total_time += time_added
                total_confidence += confidence_added
                count += 1
        avg_confidence = str(round((total_confidence/count)*100, 2)) + "%"
        avg_time = str(round(total_time/count, 3)) + "s"
    else:
        avg_confidence = "INVALID"
        avg_time = "INVALID"
    return render_template('job.html', job=job, avg_time=avg_time, avg_confidence=avg_confidence)


# route to handle any errors
@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


# run the app
if __name__ == "__main__":
    app.run(debug = True)