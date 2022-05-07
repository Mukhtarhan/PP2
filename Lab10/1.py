import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    port='5432',
    user='postgres',
    password='muha2003'
)

current=config.cursor()


current.execute('''INSERT INTO phonebook (name, phone) VALUES( 
    'Mukhtarhan','87052885795'), 
    ('Sabyrjan','77075996255')'''
    )
config.commit()
current.execute('SELECT * from phonebook')
records=current.fetchall()

print(records)