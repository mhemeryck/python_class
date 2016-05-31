from sqlalchemy import and_, create_engine
#from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker
from tabulate import tabulate

from scipy.io import wavfile

from labelbox.models import Base, Recording, Event, Label

#==============================================================================
# constants
#==============================================================================
DATABASE = 'sqlite:///labelbox.db'
AUDIO_FILE = '../test.wav'
DEFAULT_LABELS = 'radio', 'werkloosheid'
EVENTS = [(31884, 55884), (101333, 138782)]
LABELS = [DEFAULT_LABELS[0], DEFAULT_LABELS[1]]

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
# generate default labels
for label_name in DEFAULT_LABELS:
    query = Label.query.filter(Label.name == label_name)
    if not query.count():
        session.add(Label(label_name))
session.commit()

# a recording
if not Recording.query.count():
    fs, sound = wavfile.read(AUDIO_FILE)
    recording = Recording(filename=AUDIO_FILE, fs=fs)
    session.add(recording)
    session.commit()

# events and labels
if not Event.query.count():
    for (start, stop), label_name in zip(EVENTS, LABELS):
        label = Label.query.filter(Label.name == label_name).first()
        session.add(Event(start, stop, label=label, recording=recording))
        session.commit()

#==============================================================================
# read from database
#==============================================================================
print("# print all events")
rows = []
for event in Event.query:
    rows.append([event.recording, event.start, event.stop, event.label.name])
headers = 'recording', 'start', 'stop', 'label'
print(tabulate(rows, headers=headers, tablefmt='pipe'))
print

print("# query all 'radio' events")
label = Label.query.filter(Label.name == 'radio').first()
query = Event.query.filter(Event.label == label)
for event in query:
    print event.id, event.start, event.stop, event.label
print

print("# find all events in second half of recording")
recording = Recording.query.first()
sound = recording.read()
half = sound.shape[0] / 2
clause = and_(Event.recording == recording,
              Event.start >= half)
query = Event.query.filter(clause)
for event in query:
    print event.id, event.start, event.stop, event.label
print

#session.close()
