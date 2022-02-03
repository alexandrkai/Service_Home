from sqlalchemy import *

engine = create_engine('sqlite:///:memory:')
metadata_obj = MetaData()

user = Table('user', metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(16), nullable=False),
    Column('email_address', String(60), key='email'),
    Column('nickname', String(50), nullable=False)
)

user_prefs = Table('user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)

idaddress=Table(
    'ipaddress', metadata_obj,
    Column('ipaddress_id', Integer)

)

def create_db():
    metadata_obj.create_all(engine)

def create_individual_table():
    employees = Table('employees', metadata_obj,
                      Column('employee_id', Integer, primary_key=True),
                      Column('employee_name', String(60), nullable=False, key='name'),
                      Column('employee_dept', Integer, ForeignKey("departments.department_id"))
                      )
    employees.create(engine)

def drop_table(table):
    table.drop(engine)

