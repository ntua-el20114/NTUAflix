// Search form
document.getElementById('searchForm').addEventListener('submit', function(event) {
    // Prevent the form from submitting normally
    event.preventDefault();

    // Get the search query
    var query = document.getElementById('searchInput').value;

    // Redirect to the search results page
    window.location.href = '/SearchResults?query=' + encodeURIComponent(query);
});

// Close flash messages
var flashesElement = document.querySelector('.flashes');
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

//DropDown - NavBar
document.addEventListener('DOMContentLoaded', function () {
    var moreContainer = document.getElementById('moreContainer');
    var moreButton = document.getElementById('moreButton');
    var moreDropdown = document.getElementById('moreDropdown');

    //Hardcoded Genre List
    var genreList = [
      'Action',
      'Adult',
      'Adventure',
      'Animation',
      'Biography',
      'Comedy',
      'Crime',
      'Documentary',
      'Drama',
      'Family',
      'Fantasy',
      'History',
      'Horror',
      'Music',
      'Musical',
      'Mystery',
      'News',
      'Romance',
      'Sci-Fi',
      'Short',
      'Sport',
      'Thriller',
      'War',
      'Western'
    ]

    document.addEventListener('click', function (event) {
      if (
        !moreContainer.contains(event.target) &&
        !event.target.matches('#moreButton')
      ) {
        // Close the dropdown if the user clicks outside of it
        moreDropdown.classList.remove('show');
      }
    });
  
    moreContainer.addEventListener('click', function (event) {
      if (event.target === moreButton || event.target.closest('#moreButton')) {
        event.preventDefault(); // Prevent form submission
        moreDropdown.classList.toggle('show');
      }
    });

    genreList.forEach(function (genre) {
      var genreLink = document.createElement('a');
      genreLink.href = '/ByGenre?qgenre=' + encodeURIComponent(genre);
      genreLink.textContent = genre;
    
      // Attach an event listener to each genre link
      genreLink.addEventListener('click', function (event) {
        event.preventDefault();
        handleGenreClick(genre);
      });
    
      moreDropdown.appendChild(genreLink);
    });
    
    // Function to handle genre click
    function handleGenreClick(genre) {
      console.log('Genre clicked:', genre);
      // Add your logic to handle genre click, for example, redirect to a new page
      window.location.href = '/ByGenre?qgenre=' + encodeURIComponent(genre);
    }


  });
  