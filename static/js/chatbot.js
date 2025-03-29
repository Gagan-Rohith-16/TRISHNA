document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    const chatbotToggle = document.querySelector('.chatbot-toggle');
    const chatbotBox = document.querySelector('.chatbot-box');
    const chatbotMessages = document.querySelector('.chatbot-messages');
    const chatbotInput = document.querySelector('.chatbot-input input');
    const chatbotSendButton = document.querySelector('.chatbot-input button');
    const closeChatbotButton = document.querySelector('.close-chatbot');
    
    // Initialize chatbot state
    let isChatbotOpen = false;
    let isWaitingForResponse = false;
    
    // Open/close chatbot functions
    function openChatbot() {
        chatbotBox.classList.add('active');
        isChatbotOpen = true;
        // Display welcome message if this is the first time
        if (chatbotMessages.children.length === 0) {
            displayBotMessage("Hello! I'm ExamSeek Assistant. How can I help you with your exam preparation today?");
        }
    }
    
    function closeChatbot() {
        chatbotBox.classList.remove('active');
        isChatbotOpen = false;
    }
    
    // Toggle chatbot visibility
    if (chatbotToggle) {
        chatbotToggle.addEventListener('click', function() {
            if (isChatbotOpen) {
                closeChatbot();
            } else {
                openChatbot();
            }
        });
    }
    
    // Close chatbot when close button is clicked
    if (closeChatbotButton) {
        closeChatbotButton.addEventListener('click', closeChatbot);
    }
    
    // Send message function
    function sendMessage() {
        // Get user message
        const message = chatbotInput.value.trim();
        
        // Skip if message is empty or already waiting for response
        if (!message || isWaitingForResponse) {
            return;
        }
        
        // Display user message
        displayUserMessage(message);
        
        // Clear input field
        chatbotInput.value = '';
        
        // Show loading indicator
        showLoadingIndicator();
        
        // Send message to server
        fetchChatbotResponse(message);
    }
    
    // Display user message in chat
    function displayUserMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'message user-message';
        messageElement.textContent = message;
        chatbotMessages.appendChild(messageElement);
        scrollToBottom();
    }
    
    // Display bot message in chat
    function displayBotMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'message bot-message';
        
        // Convert URLs to clickable links
        message = message.replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank">$1</a>');
        
        // Process markdown-like formatting
        message = message.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>'); // Bold
        message = message.replace(/\*(.*?)\*/g, '<em>$1</em>'); // Italic
        
        // Handle bullet points
        message = message.replace(/^- (.*)/gm, '<li>$1</li>');
        message = message.replace(/<li>(.*)<\/li>/g, '<ul><li>$1</li></ul>');
        
        messageElement.innerHTML = message;
        chatbotMessages.appendChild(messageElement);
        scrollToBottom();
    }
    
    // Show loading indicator
    function showLoadingIndicator() {
        isWaitingForResponse = true;
        const loadingElement = document.createElement('div');
        loadingElement.className = 'message bot-message loading-message';
        loadingElement.innerHTML = '<div class="loading-spinner"></div> <span>Thinking...</span>';
        loadingElement.id = 'loading-indicator';
        chatbotMessages.appendChild(loadingElement);
        scrollToBottom();
    }
    
    // Hide loading indicator
    function hideLoadingIndicator() {
        isWaitingForResponse = false;
        const loadingElement = document.getElementById('loading-indicator');
        if (loadingElement) {
            loadingElement.remove();
        }
    }
    
    // Fetch response from server or use client-side chatbot
    function fetchChatbotResponse(message) {
        // Check if client-side chatbot is available
        if (window.clientChatbot && window.clientChatbot.initialized) {
            console.log("Using client-side chatbot");
            // Use client-side chatbot
            try {
                const response = window.clientChatbot.getResponse(message);
                // Hide loading indicator
                hideLoadingIndicator();
                
                // Display bot response
                if (response.status === 'success') {
                    displayBotMessage(response.text);
                } else {
                    displayBotMessage("I'm sorry, I encountered an error. Please try again later.");
                    console.error('Client chatbot error:', response.error);
                }
            } catch (error) {
                // Hide loading indicator
                hideLoadingIndicator();
                
                // Display error message
                displayBotMessage("I'm sorry, something went wrong with the chatbot. Please try again later.");
                console.error('Client chatbot error:', error);
            }
        } else {
            console.log("Using server-side chatbot");
            // Fall back to server-side chatbot
            fetch('/chatbot', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => {
                // Hide loading indicator
                hideLoadingIndicator();
                
                // Display bot response
                if (data.status === 'success') {
                    displayBotMessage(data.text);
                } else {
                    displayBotMessage("I'm sorry, I encountered an error. Please try again later.");
                    console.error('Chatbot error:', data.error);
                }
            })
            .catch(error => {
                // Hide loading indicator
                hideLoadingIndicator();
                
                // Display error message
                displayBotMessage("I'm sorry, I'm having trouble connecting to the server. Please try again later.");
                console.error('Chatbot fetch error:', error);
            });
        }
    }
    
    // Scroll chat to bottom
    function scrollToBottom() {
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }
    
    // Event listeners for sending messages
    if (chatbotSendButton) {
        chatbotSendButton.addEventListener('click', sendMessage);
    }
    
    if (chatbotInput) {
        chatbotInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        });
    }
});
