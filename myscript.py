import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='postgres',
    user='postgres',
    password='postgres',
)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test1 (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test1 (num, data) VALUES (%s, %s)", (100, "abcdefg"))
cur.execute("INSERT INTO test1 (num, data) VALUES (%s, %s)", (1000, "abcdefg"))
cur.execute("SELECT * FROM test1;")
result = cur.fetchone()
print(result)
conn.commit()
cur.close()
conn.close()