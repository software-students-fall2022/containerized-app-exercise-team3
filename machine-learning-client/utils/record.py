import sounddevice as sd
import os
from scipy.io.wavfile import write


def record(name, duration=5, fs=44100):
    """
    Record audio from user's default microphone

    return: str 
        path to .wav file output 
    -------------------------------------------

    Parameters:
    - name: str 
        name of the output file
    - duration: int  
        length of the recording, in seconds, default is 10 (optional)
    - fs: int
        Sample rate, default is 44100 (optional) 

    --------------------------------------------
    Boundaries: 
    - 1s < duration < 60s 
    - valid sample rate: _______

    --------------------------------------------
    TODO:
    - stop/pause action? (unspecified duration) 
    - tests
    """

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished

    write(str(name + ".wav"), fs, recording)  # Save as WAV file

    return os.path.abspath(str(name + ".wav"))


if __name__ == "__main__":
    print(record("test"))
