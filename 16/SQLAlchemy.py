### ORM like  / without typical SQL

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String
import pandas as pd

engine = create_engine('sqlite:///lesson16.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users3'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Define and add new user
new_user = User(name='Alice', email='alice@example.com')
session.add(new_user)

# Get all users
users_results = session.query(User).all()
session.commit()


# Convert results to Panzdas
data = [{'id': u.id, 'name': u.name, 'email': u.email} for u in users_results]


df = pd.DataFrame(data)
print(df)


### with just typical SQL
"""
from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine('sqlite:///lesson16.db')

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users3"))
    df = pd.DataFrame(result.mappings().all())   
    print(df)
"""