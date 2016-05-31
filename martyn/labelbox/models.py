from scipy.io import wavfile

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Recording(Base):
    """audio recording"""

    __tablename__ = 'recordings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(Text)
    fs = Column(Integer)
    events = relationship('Event')

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


class Event(Base):
    """audio event"""

    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start = Column(Integer)
    stop = Column(Integer)
    recording_id = Column(Integer, ForeignKey('recordings.id'))
    recording = relationship('Recording')

    def __init__(self, start, stop, recording=None):
        self.start = start
        self.stop = stop
        self.recording = recording

    def __repr__(self):
        return ('{self.__class__.__name__}: '
                '{self.id} ({self.start}, {self.stop})').format(self=self)
