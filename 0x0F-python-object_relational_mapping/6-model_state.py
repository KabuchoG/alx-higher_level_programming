#!/usr/bin/python3
"""Create the engine"""

import sys
from model_state import Base
from sqlalchemy import create_engine


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True, echo=True)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
