import pyaudio
import wave
import keyboard
import os
from time import time


def get_time():
    ms = int(time()*1000)
    return ms


def record(name, duration=None, fs=44100):
    """
    Record audio from user's default microphone

    return: str 
        path to .wav file output 
    -------------------------------------------

    Parameters:
    - name: str 
        name of the output file
    - duration: int  
        length of the recording, in seconds, default is None. i.e. keyboard interupt to stop unless timeout (optional)
    - fs: int
        Sample rate, default is 44100 (optional) 

    --------------------------------------------
    Boundaries: 
    - 1s < duration < 60s 

    --------------------------------------------
    TODO:
    - tests
    """

    # Name of sub-directory where WAVE files are placed
    subdir_recording = 'recording'

    # Variables for Pyaudio
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = fs

    # set filename
    wave_output_filename = '%s.wav' % name

    # setup recording
    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    # set duration
    if duration == None:
        timeout = 60000
    else:
        timeout = duration * 1000

    # start recording
    print("* Recording. Press [Ctrl + C] or [Cmd + .] to stop recording. Max Length: %dseconds.\n" %
          (int(timeout) / 1000))
    frames = []
    start_time = get_time()
    current_time = get_time()

    while (current_time - start_time) < timeout:
        try:
            data = stream.read(chunk)
            frames.append(data)
            current_time = get_time()
        except KeyboardInterrupt:
            data = stream.read(chunk)
            frames.append(data)
            break
    else:
        data = stream.read(chunk)
        frames.append(data)

    # stop recording
    print("* done recording \n")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # write
    file_path = os.path.join(
        os.getcwd(), subdir_recording, wave_output_filename)
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    return file_path


if __name__ == "__main__":
    print('Audio generated at: ' + record("test1"))
