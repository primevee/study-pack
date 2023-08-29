#!/usr/bin/python3
""" get form db and filter """

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, database_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (session.query(State)
              .filter(State.name.like('%a%'))
              .order_by(State.id).all())
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
