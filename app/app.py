from flask import Flask
import mysql.connector
import os
import time

app = Flask(__name__)

# Read secrets from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Wait for DB (basic retry logic)
time.sleep(10)

db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

@app.route("/")
def home():
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(50))")
    cursor.execute("INSERT INTO users (name) VALUES ('Akshu')")
    db.commit()
    return "Hello,Secure App Running with MySQL!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

