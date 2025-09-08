import psycopg2
import time

# Wait a bit for PostgreSQL to be ready
time.sleep(5)

try:
    conn = psycopg2.connect(
        host="my-postgres",
        database="mydb",
        user="user",
        password="pass"
    )

    cur = conn.cursor()

    # Create table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        );
    """)

    # Insert a row
    cur.execute("INSERT INTO students (name) VALUES (%s) RETURNING id;", ("Alice",))
    conn.commit()

    # Read and print
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()
    for row in rows:
        print("Row:", row)

    cur.close()
    conn.close()

except Exception as e:
    print("Database error:", e)
	
	
