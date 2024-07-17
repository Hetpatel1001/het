from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta


users = Table(
    'users', meta,
    Column('username', String(50),nullable=False),
    Column('firstname', String(50)),
    Column('lastname', String(50)),
    Column('pincode', Integer),
    Column('email', String(50))
)