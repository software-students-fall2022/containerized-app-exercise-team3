import pyaudio
import wave
import keyboard
import os
from time import time


def record(name="untitled", duration=None):
    """
    Record audio from user's default microphone

    return: str 
        path to .wav file output 
    -------------------------------------------

    Parameters:
    - name: str 
        name of the output file, default is "untitled". 
    - duration: int  
        length of the recording, in seconds, default is None. i.e. keyboard interupt to stop unless timeout (optional)

    --------------------------------------------
    Boundaries: 
    - 1s < duration <= 60s 

    """

    # argument error handling
    # name
    if not isinstance(name, str):
        raise TypeError("Name of the file should be a string.")
    if len(name) > 255:
        raise OverflowError("File name should be shorter than 255 characters.")

    # duration
    if(duration is not None and duration <= 0):
        raise ValueError("Duration should be integer larger than zero.")
    elif(duration is not None and duration > 60):
        raise NotImplementedError(
            "Duration larger than 60 seconds is not supported.")

    # Name of sub-directory where WAVE files are placed
    subdir_recording = 'recording'

    # Variables for Pyaudio
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100

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
    if duration is None:
        timeout = 60000
    else:
        timeout = duration * 1000

    # start recording
    print("* Recording. Press [Ctrl + C] to stop recording. Max Length: %dseconds.\n" %
          (int(timeout) / 1000))
    frames = []
    start_time = int(time()*1000)
    current_time = int(time()*1000)

    while (current_time - start_time) < timeout:
        try:
            data = stream.read(chunk)
            frames.append(data)
            current_time = int(time()*1000)
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
    print('Audio generated at: ' + record(name="test1"))
