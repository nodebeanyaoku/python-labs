import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:D&J,qwe1@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()




newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)

#query = sqlalchemy.insert(newTable).values(Id=1, name='Software Ninjaneer', salary=60000.00, active=True)
#result_proxy = connection.execute(query)


# In the example above, we have inserted one record, however, 
# what if we want to insert multiple records at once? We need to create a list of dictionaries. For example: 

query = sqlalchemy.insert(newTable)
new_records = [{'Id':'2', 'name':'record1', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'record2', 'salary':70000, 'active':True}]
result_proxy = connection.execute(query,new_records)