from scipy.io import wavfile


class Recording(object):
    """audio recording"""

    def __init__(self, filename=None, fs=None):
        self.filename = filename
        self.fs = fs

    def read(self):
        """read and return audio from file, is available"""

        if self.filename is None:
            return

        self.fs, sound = wavfile.read(self.filename)
        return sound
