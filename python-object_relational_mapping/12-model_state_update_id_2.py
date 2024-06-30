#!/usr/bin/python3
"""
    The `Update a state` module.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, db),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State)\
                   .where(State.id == 2)\
                   .first()
    state.name = "New Mexico"
    session.commit()
    print(state.id)
    session.close()
