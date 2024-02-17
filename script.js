document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.getElementById('chat-container');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-btn');

    // Function to add a message to the chat container
    function addMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', sender);
        messageElement.innerText = message;
        chatContainer.appendChild(messageElement);
        chatContainer.scrollTop = chatContainer.scrollHeight; // Scroll to bottom
    }

    // Function to handle user input
    function handleUserInput() {
        const inputText = userInput.value.trim();
        if (inputText === '') return;

        addMessage('user', inputText);
        userInput.value = '';

        // Send the user input to the backend
        fetch('/api/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ input: inputText })
        })
        .then(response => response.json())
        .then(data => {
            addMessage('ai', data.response);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Event listener for the send button
    sendButton.addEventListener('click', handleUserInput);

    // Event listener for pressing Enter key
    userInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            handleUserInput();
        }
    });
});
