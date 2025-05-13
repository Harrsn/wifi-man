function sendMessage() {
  const userInput = document.getElementById('user-input').value;
  const chatLog = document.getElementById('chat-log');

  chatLog.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;
  document.getElementById('user-input').value = '';

  fetch('/chat', {
    method: 'POST',
    body: JSON.stringify({ message: userInput }),
    headers: { 'Content-Type': 'application/json' }
  })
  .then(res => res.json())
  .then(data => {
    chatLog.innerHTML += `<div><strong>Wi-Fi Wizard:</strong> ${data.response}</div>`;
    chatLog.scrollTop = chatLog.scrollHeight;
  });
}
