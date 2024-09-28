document.addEventListener('DOMContentLoaded', () => {
    const optOutButton = document.getElementById('opt-out-btn');
    const optOutMessage = document.getElementById('opt-out-message');

    optOutButton.addEventListener('click', async () => {
        try {
            const response = await fetch('/opt-out', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (response.ok) {
                const message = await response.text();
                optOutMessage.textContent = message;
            } else {
                optOutMessage.textContent = 'Failed to opt out. Please try again.';
            }
        } catch (error) {
            console.error('Error:', error);
            optOutMessage.textContent = 'An error occurred. Please try again.';
        }
    });
});
