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

### **SQLite Connection String Example**

```python
from sqlalchemy import create_engine

# SQLite in-memory
engine = create_engine('sqlite:///:memory:')

# SQLite file database
engine = create_engine('sqlite:///my_database.db')
```

---

### **Declarative ORM Model Example**

```python
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
```

---

### **Create Tables and Session**

```python
# Create tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
```

---

### **CRUD Operations Example**

```python
# Create
new_user = User(name='Alice', email='alice@example.com')
session.add(new_user)
session.commit()

# Read
users = session.query(User).all()

# Update
user = session.query(User).filter_by(name='Alice').first()
user.email = 'alice@newdomain.com'
session.commit()

# Delete
session.delete(user)
session.commit()
```

---

###  **Summary**

* Use `create_engine()` with SQLite connection string.
* Define models by inheriting from `Base`.
* Use `Session` to interact with the DB.
* Call `Base.metadata.create_all(engine)` to create tables.
* Perform CRUD operations with `session`.

