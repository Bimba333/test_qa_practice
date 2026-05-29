import psycopg2
def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="testdb",
        user="postgres",
        password="secret"
    )

def setup_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY,
            city VARCHAR(100) NOT NULL,
            price DECIMAL NOT NULL,
            status VARCHAR(50) DEFAULT 'new'
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_db()
    print("Таблица создана")