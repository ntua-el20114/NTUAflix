document.getElementById('chatbotFab').addEventListener('click', openPanel);

function openPanel() {
    document.getElementById("chatbotPanel").style.width = "30vw";
    document.getElementById("overlay").style.display = "block";
    document.body.style.overflow = 'hidden';
}

function closePanel() {
    document.getElementById("chatbotPanel").style.width = "0";
    document.getElementById("overlay").style.display = "none";
    document.body.style.overflow = 'auto';
}

// Add an event listener to the form submission
document.getElementById('inputBox').addEventListener('submit', function(event) {
    // Prevent the form from being submitted normally
    event.preventDefault();

    // Get the prompt from the form input
    const prompt = document.getElementById('textInput').value;
    console.log("Prompt: " + prompt);

    const url = new URL('http://127.0.0.1:9876/ntuaflix_api/chatbot');
    url.searchParams.append('Sentence', prompt);
    // const data = {'Sentence': prompt};

    console.log("Sending request");
    fetch(url, {
        method: 'GET',
        headers: {
            'X-OBSERVATORY-AUTH': userToken, //This is defined in base.html
        },
        // body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            console.log("Response not ok");
            throw new Error(`Error: ${response.status}`);
        }
        console.log("Response ok");
        return response.json();
    })
    .then(data => {
        console.log("Response: " + data)
        const result = data.Response || [];
        console.log(result);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});