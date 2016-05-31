from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from scipy.io import wavfile

from labelbox.models import Base, Recording

#==============================================================================
# constants
#==============================================================================
DATABASE = 'sqlite:///labelbox.db'
AUDIO_FILE = '../test.wav'

#==============================================================================
# database connection
#==============================================================================
# connection to database
engine = create_engine(DATABASE)
# factory for sessions
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# the actual session
session = scoped_session(session_factory)
# models base class: connect to enginer
Base.metadata.create_all(engine)
# query property: easier to generate queries ...
Base.query = session.query_property()

#==============================================================================
# populate database
#==============================================================================
# a recording
if not Recording.query.count():
    fs, sound = wavfile.read(AUDIO_FILE)
    recording = Recording(filename=AUDIO_FILE, fs=fs)
    session.add(recording)
    session.commit()
