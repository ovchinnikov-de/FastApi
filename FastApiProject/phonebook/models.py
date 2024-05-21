
from sqlalchemy import MetaData, Table, Column, String, BigInteger

metadata = MetaData()



users = Table(
    "users",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("name", String, nullable=False),
    Column("surname", String, nullable=False),
    Column("phone_number", BigInteger,nullable=False),

)