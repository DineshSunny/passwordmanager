from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import random
from twilio.rest import Client

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="FireN0de$!@#",
    database="padlock"
)

twilio_client = Client("AC14ae5be04d52903de08d31d8cce1515f", "e63e0d63cf2d49a01f2268148efbb174")

@app.route('/keyfob-login', methods=['POST'])
def keyfob_login():
    data = request.json
    key_fob_id = data.get("key_fob_id")

    cursor = db.cursor()
    cursor.execute("SELECT phone FROM users WHERE key_fob_id = %s", (key_fob_id,))
    user = cursor.fetchone()

    if user:
        otp = str(random.randint(100000, 999999))
        cursor.execute("UPDATE users SET otp = %s WHERE key_fob_id = %s", (otp, key_fob_id))
        db.commit()

        twilio_client.messages.create(
            body=f"Your OTP is {otp}",
            from_="+1234567890",
            to=user[0]
        )
        return jsonify({"success": True})
    return jsonify({"success": False})

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.json
    otp = data.get("otp")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE otp = %s", (otp,))
    if cursor.fetchone():
        return jsonify({"message": "OTP verified"})
    return jsonify({"message": "Invalid OTP"}), 400

if __name__ == '__main__':
    app.run(debug=True)
