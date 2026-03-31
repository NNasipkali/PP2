import psycopg2

conn = psycopg2.connect(
    dbname="phonebook_db"
)

print("CONNECTED")

conn.close()