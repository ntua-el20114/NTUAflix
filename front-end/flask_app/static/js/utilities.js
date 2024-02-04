// Get the <ul class='flashes'> element
var flashesElement = document.querySelector('.flashes');

// Check if the element exists
if (flashesElement) {
    // Event delegation
    flashesElement.addEventListener('click', function(event) {
        // Check if the clicked element has an id that starts with "flashClose"
        if (event.target.id.startsWith('flashClose')) {
            // Extract the number from the id
            var number = event.target.id.replace('flashClose', '');

            // Construct the id of the flash message
            var flashId = 'flash' + number;

            // Get the flash message element
            var flashElement = document.getElementById(flashId);

            // Hide the flash message element
            if (flashElement) {
                flashElement.style.display = 'none';
            }
        }
    });
}