// Logique du chatbot
document.getElementById('chatbot-send-btn').addEventListener('click', function() {
    sendMessage();
});

document.getElementById('chatbot-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});


function sendMessage() {
    var inputEl = document.getElementById('chatbot-input');
    var message = inputEl.value;
    if (message.trim() !== '') {
        appendMessage('user', message);
        inputEl.value = '';
        scrollToBottom();

        // Ici, vous pouvez ajouter la logique de traitement du message du chatbot
        // et générer une réponse en conséquence

        var reply = generateReply(message); // Appel à une fonction pour générer la réponse du chatbot
        appendMessage('bot', reply); // Ajout de la réponse du chatbot dans la boîte de dialogue
        scrollToBottom();
    }
}

function appendMessage(sender, text) {
    var messagesEl = document.getElementById('chatbot-messages');
    var messageEl = document.createElement('div');
    messageEl.className = 'message-' + sender;
    messageEl.textContent = text;
    messagesEl.appendChild(messageEl);
}

function scrollToBottom() {
    var messagesEl = document.getElementById('chatbot-messages');
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

function generateReply(message) {
    var reply = '';

    // Logique de traitement du message de l'utilisateur
    switch (message.toLowerCase()) {
        case 'bonjour':
            reply = 'Bonjour ! Comment puis-je vous aider ?';
            break;
        case 'aide','help':
            reply = "Je suis là pour vous aider. Consultez la page des questions : ";
            break;
        case 'informations':
            reply = 'Quelles informations souhaitez-vous obtenir ?';
            break;
        default:
            reply = "Je ne comprends pas. Pouvez-vous reformuler votre question ?";
            break;
    }

    return reply;
}
