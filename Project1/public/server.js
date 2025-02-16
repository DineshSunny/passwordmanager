const express = require('express');
const path = require('path');
const otpGenerator = require('otp-generator');

const app = express();
const port = 3000;

// Serve static files from the frontend directory
app.use(express.static(path.join(__dirname, '../frontend')));

// Endpoint to generate OTP
app.post('/generate-otp', (req, res) => {
  const otp = otpGenerator.generate(6, { upperCase: false, specialChars: false });
  console.log("Generated OTP:", otp);
  res.json({ otp });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
