# Machine Learning Client

## For Mac OS and Linux Users only, before install all dependencies

### Install Dependency for PyAudio (Mac OS)

    brew install portaudio

### Install Dependency for PyAudio (Linux)

    sudo apt-get install portaudio19-dev libasound-dev python3-pyaudio

## To Run the Machine Learning Client

### Create `.env`

In `machine-learning-client/`, create the `.env` file.

### Install All Dependencies

In `machine-learning-client/` run:

    pip3 install -r requirements.txt

### Run `main.py`

In `machine-learning-client/` run:

    python3 main.py

## To Run Unit Tests

### Run `pytest`

In `machine-learning-client/` run:
    
    python3 -m pytest
