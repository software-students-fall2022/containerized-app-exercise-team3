# Machine Learning Client

**Code related to the machine learning client goes in this folder.**

# For Mac OS and Linux User only, before install all dependencies
## Install dependency for PyAudio (Mac OS)
    brew install portaudio
## Install dependency for PyAudio (Linux)
    sudo apt-get install portaudio19-dev libasound-dev python3-pyaudio

# To Run Unit Test
## Install all dependencies into the virtual environment
    pip3 install -r requirements.txt
## Run pytest
    python3 -m pytest

# To Run Locally in Vistual Environment
## Activate Virtual Env
    source venv/bin/activate    
##  Install pytest 
    pip3 install pytest
##  Re-activate Virtual Env
    deactivate && source venv/bin/activate