from scipy.io import wavfile

from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Recording(Base):
    """audio recording"""

    __tablename__ = 'recordings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(Text)
    fs = Column(Integer)

    def __init__(self, filename=None, fs=None):
        self.filename = filename
        self.fs = fs

    def __repr__(self):
        return '{self.__class__.__name__}: {self.id}'.format(self=self)

    def read(self):
        """read and return audio from file, is available"""

        if self.filename is None:
            return

        self.fs, sound = wavfile.read(self.filename)
        return sound
