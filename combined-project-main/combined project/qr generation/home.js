$(document).ready(function() {
    const storedData = localStorage.getItem('laundryData');
    if (storedData) {
        const data = JSON.parse(storedData);
        // Set the status for each bag
        $('#bag1-status').text('Pending');
        $('#bag2-status').text('Pending');
    }

    $('#show-qr-codes').click(function() {
        window.location.href = 'index.html'; // Navigate to the registration interface
    });
});
