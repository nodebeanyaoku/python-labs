# Add the code for the file counter script that you wrote in the course.

from datetime import datetime
import pathlib
from sqlalchemy import Column, Integer, String,  create_engine, MetaData, Table, DateTime, func, text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# locate path of my Desktop
dir = pathlib.Path("/mnt/c/users/nodebechukwu.anyaoku/desktop")

ext_lst = []
file_list = []
ext_dict = {}
file_dict = {}

# list out all the files in desktop location
for file in dir.iterdir():
    file_list.append(file.suffix)

# store extension not in this list
[ext_lst.append(ext) for ext in file_list if ext not in ext_lst]

ext_dict = dict.fromkeys(ext_lst, None)

for ext in file_list:

    for key, val in ext_dict.items():
        if ext == key:
            ext_dict[key] = file_list.count(ext)


print(ext_dict)

file_dict = {'PNG': 8, 'JPG' : 3, 'WORD': 13 }

class File(Base):
   __tablename__ = 'file'
   id = Column(Integer, primary_key=True)
   file_type = Column(String(50))
   number_of_files = Column(Integer)
   created_at = Column(DateTime(timezone=True), server_default=func.now())
   updated_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

engine = create_engine('mysql+pymysql://root:D&J,qwe1@localhost/filecounter')
connection = engine.connect()
Base.metadata.create_all(engine)
session = sessionmaker()
session.configure(bind=engine)

s = session()

for key, value in file_dict.items():
    np = File(file_type=key, number_of_files=value)
    s.add(np)

s.commit()

"""connection.execute(File.file.update(),ext_dict.values)
session.commit()"""


