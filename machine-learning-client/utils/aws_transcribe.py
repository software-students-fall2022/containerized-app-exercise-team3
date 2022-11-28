import time
import json
import uuid
import boto3
import pymongo
from urllib import request
from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values(".env")

client = boto3.client('transcribe')

cxn = pymongo.MongoClient(config['MONGO_URI'], serverSelectionTimeoutMS=5000)
try:
    # verify the connection works by pinging the database
    # The ping command is cheap and does not require auth.
    cxn.admin.command('ping')
    db = cxn[config['MONGO_DBNAME']]  # store a reference to the database
    # if we get here, the connection worked!
    print(' *', 'Connected to MongoDB!')
except Exception as e:
    # the ping command failed, so the connection is not available.
    # render_template('error.html', error=e) # render the edit template
    print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
    print('Database connection error:', e)  # debug


def start_transcription_job(s3_file_url: str, language_code: str = "en-US"):
    job_name = str(uuid.uuid4())

    response = client.start_transcription_job(
        TranscriptionJobName=job_name,
        LanguageCode=language_code,
        Media={
            'MediaFileUri': s3_file_url
        }
    )

    return job_name, response


def get_transcription_job(job_name: str):
    job_status = -1

    while job_status not in ["COMPLETED", "FAILED"]:
        response = client.get_transcription_job(
            TranscriptionJobName=job_name
        )

        if response["TranscriptionJob"]["TranscriptionJobStatus"] in ["COMPLETED", "FAILED"]:
            print("----- Transcription Job Finished -----")
            return response
        else:
            print("Current Job Status:", response["TranscriptionJob"]["TranscriptionJobStatus"])
            print("Waiting for 5 seconds...\n")

            time.sleep(5)


if __name__ == '__main__':
    s3_file_url = "s3://software-eng-project-4/2022v-body-stuff-season-002-episode-005-yeast-video-002-180k.mp4"

    job_name, start_response = start_transcription_job(s3_file_url=s3_file_url)
    print("----- Transcription Job Submitted -----")
    print(start_response, "\n")

    if start_response["TranscriptionJob"]["TranscriptionJobStatus"] in ["IN_PROGRESS", "QUEUED"]:
        get_response = get_transcription_job(job_name)
        print(get_response, "\n")

        if get_response["TranscriptionJob"]["TranscriptionJobStatus"] == "COMPLETED":
            results_response = request.urlopen(get_response["TranscriptionJob"]["Transcript"]["TranscriptFileUri"])
            results_str = results_response.read()
            results_dict = json.loads(results_str)

            print("***** Transcript ******")
            print(results_dict["results"]["transcripts"][0]["transcript"])
