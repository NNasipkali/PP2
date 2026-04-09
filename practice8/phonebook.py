from connect import conn, cursor

# --- показать все ---
cursor.execute("SELECT * FROM contacts;")
print("All contacts:")
for row in cursor.fetchall():
    print(row)

# --- search ---
cursor.execute("SELECT * FROM search_contacts(%s);", ('Nurs',))
print("\nSearch result:")
for row in cursor.fetchall():
    print(row)

# --- upsert ---
cursor.execute("CALL upsert_contact(%s, %s);", ('Nurs', '999999999'))
conn.commit()

# --- bulk insert ---
cursor.execute("""
CALL insert_many_users(
    ARRAY['Ali', 'Bob', 'Tom'],
    ARRAY['1234567890', '123', '7777777777'],
    NULL
);
""")
conn.commit()

# --- pagination ---
cursor.execute("SELECT * FROM get_contacts(%s, %s);", (2, 0))
print("\nPagination:")
for row in cursor.fetchall():
    print(row)

# --- delete ---
cursor.execute("CALL delete_contact(%s);", ('Ali',))
conn.commit()

cursor.execute("SELECT * FROM contacts;")
print("\nAfter delete:")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()