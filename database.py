from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("postgresql://postgres:ali.1234@localhost/pizza_delivery",
                       echo = True
                       )

base = declarative_base()

session = sessionmaker()