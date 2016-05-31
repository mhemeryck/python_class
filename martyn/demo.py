from scipy.io import wavfile

import labelbox
from labelbox.models import Recording

AUDIO_FILE = '../test.wav'

print labelbox.__name__, labelbox.__author__, labelbox.__version__

fs, sound = wavfile.read(AUDIO_FILE)
recording = Recording(filename=AUDIO_FILE, fs=fs)

print recording.filename, recording.fs
