function startCamera() {
    const videoElement = document.getElementById("video");

    // Request access to the webcam
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            videoElement.srcObject = stream;
            // Optionally, use a facial recognition API here to verify the user's face
            // E.g., use TensorFlow.js or a third-party API like Microsoft Face API
        })
        .catch(err => {
            console.error("Camera access denied", err);
        });
}

function submitOTP() {
    const otpInput = document.getElementById("otp").value;

    if (otpInput === "") {
        alert("Please enter a valid OTP");
        return;
    }

    // Make API call to verify OTP (replace with your backend endpoint)
    fetch('/verify-otp', {
        method: 'POST',
        body: JSON.stringify({ otp: otpInput }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = "dashboard.html"; // Redirect to the dashboard or app home page
        } else {
            alert("Invalid OTP. Please try again.");
        }
    })
    .catch(err => {
        alert("Error verifying OTP: " + err);
    });
}
