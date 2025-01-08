from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'mysql-container',  # Use the MySQL container name
    'user': 'flaskuser',
    'password': 'flaskpassword',
    'database': 'flaskdb'
}

@app.route('/')
def home():
    try:
        # Establish connection to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT 'Hello from MySQL!'")
        result = cursor.fetchone()
        return jsonify(message=result[0])
    except mysql.connector.Error as err:
        return jsonify(error=str(err))
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
