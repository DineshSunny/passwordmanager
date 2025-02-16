import random
import string

def generate_otp(length=6):
    # Generate a random OTP of specified length
    otp = ''.join(random.choices(string.digits, k=length))
    return otp

# Generate and print a one-time password
otp = generate_otp()
print(f"Your one-time password is: {otp}")
