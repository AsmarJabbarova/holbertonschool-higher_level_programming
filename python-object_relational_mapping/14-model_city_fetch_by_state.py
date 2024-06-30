#!/usr/bin/python3
"""
    The `Cities in state` module.
"""

from sys import argv
from model_state import State
from model_city import City
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
    cities = session.query(City, State.name.label('state'))\
                    .join(State, City.state_id == State.id)\
                    .all()

    for city in cities:
        print("{}: ({}) {}".format(city[1], city[0].id, city[0].name))
    session.close()
