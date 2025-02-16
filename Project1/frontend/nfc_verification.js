function startNFC() {
    const statusElement = document.getElementById("status");

    // Check if NFC is supported in the browser (for desktop, this would use Web NFC API)
    if ('NFC' in window) {
        statusElement.innerText = "Waiting for NFC device...";

        // Start NFC reader logic (this will depend on whether your browser supports Web NFC API)
        navigator.nfc.scan().then(data => {
            // Assuming 'data' contains the NFC info
            if (data && data.isValid) {
                statusElement.innerText = "NFC Verified!";
                // Redirect to the next page after NFC verification
                window.location.href = "facial_otp_verification.html";
            } else {
                statusElement.innerText = "NFC verification failed. Please try again.";
            }
        }).catch(err => {
            statusElement.innerText = `Error: ${err}`;
        });
    } else {
        statusElement.innerText = "NFC is not supported in your browser.";
    }
}
