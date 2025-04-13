from flask import Flask, request, jsonify
import sqlite3
from pathlib import Path

print("▶ Current working dir :", Path.cwd())
print("▶ __file__ dir         :", Path(__file__).resolve().parent)

app = Flask(__name__)


# @app.before_first_request
def initialize_db():
    conn = sqlite3.connect('transcripts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transcripts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            video_id TEXT UNIQUE,
            transcript TEXT
        )
    ''')

@app.route('/')
def home_page():
    return "<h1>Welcome to the YouTube Transcript Summarizer API!</h1>"

@app.route("/api/healthcheck", methods=["GET"])
def health_check():
    return jsonify({"status":"ok"}), 200

@app.route("/allusers", methods=["GET"])
def get_users():
    """
    Returns a JSON list of all users in the database.
    """
    with sqlite3.connect("database/users.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT name, email FROM users")
        rows = cur.fetchall()
        
        # Convert list of tuples into a list of dicts
        users = []
        for row in rows:
            users.append({
                "name": row[0],
                "email": row[1]
            })
    print(users)
    return jsonify(users), 200



@app.route("/users/<string:user_email>", methods=["GET"])
def get_user(user_email):
    """
    Returns a single user matching the provided user_email.
    If not found, returns a 404.
    """
    with sqlite3.connect("database/users.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT name, email FROM users WHERE email = ?", (user_email,))
        row = cur.fetchone()
        
        if row:
            user_data = {
                "name": row[0],
                "email": row[1]
            }
            return jsonify(user_data), 200
        else:
            return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    # For local dev only; production should use a WSGI server (gunicorn, etc.)
    app.run(debug=True, port=5000)