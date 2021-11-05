import sqlalchemy

from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:D&J,qwe1@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('city', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([actor])
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

# result_set = result_proxy.fetchmany(5)
pprint(result_set)








