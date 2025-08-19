## SQLAlchemy

The Python SQL Toolkit and Object Relational Mapper
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language. (source: www.sqlalchemy.org)

### **Install SQLAlchemy**

```bash
pip install sqlalchemy
```

---

### **Basic SQLAlchemy Concepts**

| Concept     | Purpose                                              |
| ----------- | ---------------------------------------------------- |
| **Engine**  | Core interface to the database (manages connections) |
| **Session** | Manages ORM transactions (unit of work)              |
| **Base**    | Declarative base class for ORM models                |
| **Model**   | Python class mapped to a table                       |

---

## ORM like  / without typical SQL
```python
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
```



### with just typical SQL

```python
from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine('sqlite:///lesson16.db')

with engine.connect() as conn:
    result = conn.execute(text("SELECT id, name, email FROM users3"))
    df = pd.DataFrame(result.mappings().all())   
    print(df)
```


###  **Summary**

* Use `create_engine()` with SQLite connection string.
* Define models by inheriting from `Base`.
* Use `Session` to interact with the DB.
* Call `Base.metadata.create_all(engine)` to create tables.
* Perform CRUD operations with `session`.

