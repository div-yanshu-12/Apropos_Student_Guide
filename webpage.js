document.addEventListener('DOMContentLoaded', function() {
    const chatbotIcon = document.getElementById('chatbot-icon');
    const tooltip = document.getElementById('tooltip');
    const chatbotContainer = document.querySelector('.chat-container');

    function showTooltip() {
        tooltip.classList.add('show');
        tooltip.classList.remove('hide');
    }

    function hideTooltip() {
        tooltip.classList.add('hide');
        tooltip.classList.remove('show');
    }

    function toggleChatbot() {
        if (chatbotContainer.style.display === 'none' || chatbotContainer.style.display === '') {
            chatbotContainer.style.display = 'block';
            tooltip.style.display = 'none';  // Hide the tooltip on click
        } else {
            chatbotContainer.style.display = 'none';
        }
    }

    chatbotIcon.addEventListener('mouseenter', showTooltip);
    chatbotIcon.addEventListener('mouseleave', hideTooltip);
    chatbotIcon.addEventListener('click', toggleChatbot);

    document.getElementById('toggleButton1').addEventListener('click', function() {
        const description = document.getElementById('slideOutDescription1');
        description.classList.toggle('show');
    });

    document.getElementById('toggleButton2').addEventListener('click', function() {
        const description = document.getElementById('slideOutDescription2');
        description.classList.toggle('show');
    });

    document.getElementById('toggleButton3').addEventListener('click', function() {
        const description = document.getElementById('slideOutDescription3');
        description.classList.toggle('show');
    });
});

async function sendMessage() {
    const messageInput = document.getElementById("message");
    const message = messageInput.value;

    const response = await fetch('http://127.0.0.1:5000/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById("response").innerText = "Bot: " + data.response;
    } else {
        console.error('Error:', response.statusText);
        document.getElementById("response").innerText = "Bot: There was an error communicating with the server.";
    }

    messageInput.value = '';  // Clear the input field
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}
