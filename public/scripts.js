
document.querySelector('.send-button').addEventListener('click', () => {
    const input = document.querySelector('.chat-input');
    const message = input.value.trim();
    if (message) {
        const chatWindow = document.querySelector('.chat-window');
        const messageElement = document.createElement('div');
        messageElement.textContent = message;
        chatWindow.appendChild(messageElement);
        input.value = '';
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
});
