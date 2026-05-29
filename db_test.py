import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="testdb",
    user="postgres",
    password="secret"
)

cursor = conn.cursor()
cursor.execute("SELECT version();")
version = cursor.fetchone()
print(version)

conn.close()