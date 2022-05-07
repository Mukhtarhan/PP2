import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    port='5432',
    user='postgres',
    password='muha2003'
)

current=config.cursor()
update_query='''Update phonebook set phone = 87056254565 where name = 'Sabyrjan' '''

current.execute(update_query)
config.commit()
current.execute('SELECT * from phonebook')
records=current.fetchall()

print(records)