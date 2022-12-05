import time
import uuid
import json
from urllib import request
from utils.record import record
from utils.aws_s3 import upload_file
from utils.aws_transcribe import start_transcription_job, get_transcription_job

if __name__ == '__main__':
    file_uuid = str(uuid.uuid4())

    audio_file_path = record(name=file_uuid)

    print("----- Uploading File to AWS S3 -----")
    s3_file_url = upload_file(audio_file_path, 'software-eng-project-4')
    time.sleep(5)

    job_name, start_response = start_transcription_job(s3_file_url=s3_file_url, job_name=file_uuid)
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
