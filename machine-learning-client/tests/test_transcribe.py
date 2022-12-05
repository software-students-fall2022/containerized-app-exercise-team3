import os
import uuid
import boto3
import pytest
from utils.aws_transcribe import get_transcription_job, start_transcription_job


class Tests:
    #
    # Test functions
    #

    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_start_transcription_job(self):
        """
        Test the start_transcription_job function from the aws_transcribe module
        """
        self.job_name_expected = str(uuid.uuid4())

        job_name_actual, response = start_transcription_job(s3_file_url="s3://software-eng-project-4/sample_audio.mp3", job_name=self.job_name_expected)

        assert job_name_actual == self.job_name_expected, f"Expected {job_name_actual} to be equal to {self.job_name_expected}!"
        assert isinstance(response, dict)

    
    def get_transcription_job(self):
        """
        Test the get_transcription_job function from the aws_transcribe module
        """

        response = get_transcription_job(self.job_name_expected)

        assert isinstance(response, dict)
