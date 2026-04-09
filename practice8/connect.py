import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",   # ← ВАЖНО (у тебя dbname, не database)
    user="nursultannasipkali",
    password=""
)

cursor = conn.cursor()