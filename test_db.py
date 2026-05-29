import pytest
import psycopg2
from db_setup import get_connection, setup_db

@pytest.fixture(scope="module")
def db():
    setup_db()
    conn = get_connection()
    yield conn          # тесты выполняются здесь
    conn.close()        # после всех тестов — закрываем соединение

@pytest.fixture(autouse=True)
def clean_table(db):
    yield
    db.cursor().execute("DELETE FROM orders")  # после каждого теста чистим таблицу
    db.commit()

def test_insert_order(db):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO orders (city, price) VALUES (%s, %s) RETURNING id",
        ("Москва", 1500)
    )
    db.commit()
    order_id = cursor.fetchone()[0]
    assert order_id > 0

def test_order_default_status(db):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO orders (city, price) VALUES (%s, %s) RETURNING status",
        ("Казань", 800)
    )
    db.commit()
    status = cursor.fetchone()[0]
    assert status == "new"

def test_find_order_by_city(db):
    cursor = db.cursor()
    cursor.execute("INSERT INTO orders (city, price) VALUES (%s, %s)", ("Москва", 1500))
    cursor.execute("INSERT INTO orders (city, price) VALUES (%s, %s)", ("Казань", 800))
    cursor.execute("INSERT INTO orders (city, price) VALUES (%s, %s)", ("Москва", 2000))
    db.commit()

    cursor.execute("SELECT * FROM orders WHERE city = %s", ("Москва",))
    result = cursor.fetchall()
    assert len(result) == 2

def test_empty_table_on_start(db):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM orders")
    count = cursor.fetchone()[0]
    assert count == 0