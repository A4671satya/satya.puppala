sudo apt update
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker


sudo usermod -aG docker $USER newgrp docker

sudo apt install docker-compose -y

mkdir docker-python-postgres-app
cd docker-python-postgres-appnano app.py


creating new file

nano app.py

past this code in it
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
	
	
	
	
	echo "psycopg2-binary" > requirements.txt

creating docker file

nano Dockerfile

inset another file

FROM python:3.10-slim

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]

docker build -t my-python-app .


docker network create mynetwork

docker run -d \
  --name my-postgres \
  --network mynetwork \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=pass \
  -e POSTGRES_DB=mydb \
  postgres

docker run --rm --network mynetwork my-python-app

You should see:

Row: (1, 'Alice')

# Stop and remove PostgreSQL container
docker stop my-postgres
docker rm my-postgres

# Remove Docker image
docker rmi my-python-app

# Remove the Docker network
docker network rm mynetwork


# Install Docker
sudo apt update && sudo apt install docker.io -y
sudo usermod -aG docker $USER
newgrp docker

# Create project
mkdir docker-python-postgres-app && cd docker-python-postgres-app

# Create files
nano app.py     # Paste Python code
echo "psycopg2-binary" > requirements.txt
nano Dockerfile # Paste Dockerfile content

# Build image
docker build -t my-python-app .

# Create network
docker network create mynetwork

# Run PostgreSQL
docker run -d --name my-postgres --network mynetwork \
-e POSTGRES_USER=user -e POSTGRES_PASSWORD=pass -e POSTGRES_DB=mydb postgres

# Run app
docker run --rm --network mynetwork my-python-app






