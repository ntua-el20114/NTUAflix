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