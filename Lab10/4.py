import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    port='5432',
    user='postgres',
    password='muha2003'
)

current=config.cursor()


del_row='''DELETE from phonebook where name = 'Sabyrjan' '''
current.execute(del_row)
config.commit()
current.execute('SELECT * from phonebook')
records=current.fetchall()

print(records)