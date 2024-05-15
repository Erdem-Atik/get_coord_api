function uploadPDF() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error uploading file');
        }
        return response.json();
    })
    .then(data => {
        const messageDiv = document.getElementById('message');
        messageDiv.textContent = 'Coordinates: ' + data.coordinates;
    })
    .catch(error => {
        const messageDiv = document.getElementById('message');
        messageDiv.textContent = 'Error: ' + error.message;
    });
}
