import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    port='5432',
    user='postgres',
    password='muha2003'
)

current=config.cursor()

config.commit()
samp_query='SELECT phone from phonebook where name= "Mukhtarhan" '
current.execute(samp_query)
records=current.fetchall()

print(records)