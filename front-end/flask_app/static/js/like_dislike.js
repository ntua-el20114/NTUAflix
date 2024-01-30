window.onload = function() {// Convert HTML string variables to boolean values
    let liked = html_liked === 'True';
    let disliked = html_disliked === 'True';

    document.getElementById('likeButton').addEventListener('click', toggleLike);

    document.getElementById('dislikeButton').addEventListener('click', toggleDislike);

    function toggleLike() {
        if (liked) { //unlike
            liked = false;
            document.getElementById('likeButton').style.fontVariationSettings = "'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24";
            rateMovie(0);
        } else { //like
            if (disliked) {
                disliked = false;
            document.getElementById('dislikeButton').style.fontVariationSettings = "'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24";
            }
            liked = true;
            document.getElementById('likeButton').style.fontVariationSettings = "'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24";
            rateMovie(1);
        }
    }

    function toggleDislike() {
        if (disliked) { //undislike
            disliked = false;
            document.getElementById('dislikeButton').style.fontVariationSettings = "'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24";
            rateMovie(0);
        } else { //dislike
            if (liked) {
                liked = false;
                document.getElementById('likeButton').style.fontVariationSettings = "'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24";
            }
            disliked = true;
            document.getElementById('dislikeButton').style.fontVariationSettings = "'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24";
            rateMovie(-1);
        }
    }
    
    function rateMovie(rating) {
        url='http://127.0.0.1:9876/ntuaflix_api/ratemovie';
        const data = new FormData();
        data.append('rating', rating);
        data.append('title_id', titleID);

        fetch(url, {
            method: 'POST',
            headers: {
                'X-OBSERVATORY-AUTH': userToken,
                },
            body: data,
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response data
            console.log(data);
        })
        .catch(error => {
            // Handle any errors
            console.error('Error:', error);
        });
    }
}