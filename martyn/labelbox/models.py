

class Recording(object):
    """audio recording"""

    def __init__(self, filename=None, fs=None):
        self.filename = filename
        self.fs = fs
