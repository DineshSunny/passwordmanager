from flask import Flask, request, jsonify
import random
import smtplib

app = Flask(__name__)

# Simulating a valid keyfob ID for demonstration
valid_keyfob_id = "your-unique-keyfob-id"

# Store OTP temporarily for demo purposes
stored_otp = None

def send_otp_via_email(otp, email):
    try:
        # Example: sending OTP via email (use a real email service like SendGrid or Twilio for SMS)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your-email@example.com', 'your-email-password')
        message = f"Your OTP code is: {otp}"
        server.sendmail('your-email@example.com', email, message)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

@app.route('/keyfob-login', methods=['POST'])
def keyfob_login():
    data = request.json
    keyfob_id = data.get('key_fob_id')

    if keyfob_id == valid_keyfob_id:
        # Generate a random OTP
        otp = str(random.randint(100000, 999999))  # 6-digit OTP

        # Send OTP via email (for example purposes)
        send_otp_via_email(otp, "user-email@example.com")  # Replace with the user's actual phone/email

        # Store OTP temporarily for comparison (in a real app, you'd use a more secure method)
        global stored_otp
        stored_otp = otp

        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False, "message": "Invalid keyfob ID"}), 400

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.json
    otp = data.get('otp')

    if otp == stored_otp:
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False, "message": "Invalid OTP"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
