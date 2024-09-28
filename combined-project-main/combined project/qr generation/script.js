$(document).ready(function() {
    const storedData = localStorage.getItem('laundryData');
    if (storedData) {
        const data = JSON.parse(storedData);
        displayQRCode(data, 'Bag 1');
        $('#qr-code').removeClass('hidden');
        $('#registration-form').hide();
    }

    $('#registration-form').submit(function(event) {
        event.preventDefault();

        const name = $('#name').val();
        const mobile = $('#phone').val(); // Changed to mobile for clarity
        const room = $('#room').val();
        const tower = $('#tower').val();

        const qrData = { name, mobile, room, tower }; // Ensure 'mobile' is correctly set
        localStorage.setItem('laundryData', JSON.stringify(qrData));

        $('#registration-form').hide();
        $('#qr-code').removeClass('hidden');
        displayQRCode(qrData, 'Bag 1'); // Default to Bag 1 on first registration
    });

    $('#bag-selector').change(function() {
        const selectedBag = $(this).val();
        const data = JSON.parse(localStorage.getItem('laundryData'));
        displayQRCode(data, selectedBag);
    });

    $('#go-home').click(function() {
        window.location.href = 'home.html'; // Navigate to home page
    });

    function displayQRCode(data, bag) {
        $('#qr').empty();
        $('#selected-bag').text(bag);

        // Generate JSON with correct field names
        const qrData = JSON.stringify({ 
            name: data.name, 
            mobile: data.mobile, // Ensure mobile is used here
            room: data.room, 
            tower: data.tower 
        });

        new QRCode(document.getElementById("qr"), {
            text: qrData,
            width: 128,
            height: 128,
        });
    }
});

