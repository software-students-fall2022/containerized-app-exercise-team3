import pytest
from utils import aws_s3

class Tests:
    @pytest.fixture
    def example_fixture(self):
        '''
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        '''

        # place any setup you want to do before any test function that uses this fixture is run

        yield # at th=e yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed


    #
    # Test functions
    #

    def test_sanity_check(self, example_fixture):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True # the value we expect to be present
        actual = True # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    
    def test_upload_file(self, example_fixture):
        """
        Test the upload_file function from the aws_s3 module
        """
        expected = "s3://software-eng-project-4/video_sample.mp4"
        actual = aws_s3.upload_file('video_sample.mp4', 'software-eng-project-4')
        assert actual == expected, "Expected s3://software-eng-project-4/video_sample.mp4 to be equal to s3://software-eng-project-4/video_sample.mp4!"
