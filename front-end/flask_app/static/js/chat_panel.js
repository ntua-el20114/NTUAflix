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

document.getElementById('inputBox').addEventListener('submit', function(event) {
    // Prevent the form from being submitted normally
    event.preventDefault();
    
    // Get the prompt from the form input
    const prompt = document.getElementById('textInput').value;
    
    // Create a new chat bubble for the user's input
    const userBubble = document.createElement('div');
    userBubble.className = 'chat-bubble';
    
    const userBubbleContent = `
    <div class="bubble">
    <div class="overline-text">You</div>
    <div class="text">${prompt}</div>
    </div>
    `;
    userBubble.innerHTML = userBubbleContent;
    
    // Append the user's chat bubble to the chat container
    document.getElementById('chatContainer').appendChild(userBubble);

    // Clear the text input
    document.getElementById('textInput').value = '';
    
    const url = new URL('http://127.0.0.1:9876/ntuaflix_api/chatbot');
    url.searchParams.append('Sentence', prompt);

    fetch(url, {
        method: 'GET',
        headers: {
            'X-OBSERVATORY-AUTH': userToken, //This is defined in base.html
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        console.log("Response ok");
        return response.json();
    })
    .then(data => {
        var result = data.Response || [];

        // Make the result message a little more human-readable
        result = result.replace(/{/g, '<br>');
        result = result.replace(/}/g, '');

        // Create a new chat bubble for the server's response
        const serverBubble = document.createElement('div');
        serverBubble.className = 'chat-bubble2';

        const serverBubbleContent = `
            <div class="bubble2">
                <div class="overline-text">NTUAflix chatbot</div>
                <div class="text">${result}</div>
            </div>
        `;
        serverBubble.innerHTML = serverBubbleContent;

        // Append the server's chat bubble to the chat container
        document.getElementById('chatContainer').appendChild(serverBubble);
        
        // Scroll to the bottom of the chat container
        var div = document.getElementById('chatContainer');
        div.scrollTop = div.scrollHeight - div.clientHeight;

        console.log(result);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});