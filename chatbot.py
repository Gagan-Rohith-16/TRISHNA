import os
import logging
from typing import List, Dict, Any

# Import Google Cloud libraries
try:
    from google.cloud import aiplatform
    from vertexai.preview.generative_models import GenerativeModel, Part
except ImportError:
    logging.error("Vertex AI libraries not available. Chatbot will not function.")

class ExamSeekChatbot:
    def __init__(self):
        self.initialized = False
        self.model = None
        
        # Try to initialize Vertex AI
        try:
            # Initialize Vertex AI API
            # If API_KEY is not provided, this will use the default authentication
            # method using Application Default Credentials (ADC)
            api_key = os.environ.get("VERTEX_AI_API_KEY")
            
            if api_key:
                # Initialize with API key if provided
                aiplatform.init(project=os.environ.get("GOOGLE_CLOUD_PROJECT", ""), 
                                location=os.environ.get("VERTEX_AI_LOCATION", "us-central1"),
                                api_key=api_key)
            else:
                # Initialize with default credentials
                aiplatform.init(project=os.environ.get("GOOGLE_CLOUD_PROJECT", ""), 
                                location=os.environ.get("VERTEX_AI_LOCATION", "us-central1"))
            
            # Load the model
            self.model = GenerativeModel("gemini-pro")
            self.initialized = True
            logging.info("Vertex AI chatbot initialized successfully")
        except Exception as e:
            logging.error(f"Failed to initialize Vertex AI chatbot: {e}")
            self.initialized = False

    def get_response(self, message: str) -> Dict[str, Any]:
        """
        Get a response from the chatbot for a user message.
        
        Args:
            message: The user's message
            
        Returns:
            A dictionary containing the response text and status
        """
        if not self.initialized or not self.model:
            return {
                "text": "I'm sorry, but the AI assistant is currently unavailable. Please try again later.",
                "status": "error",
                "error": "Chatbot not initialized"
            }
        
        try:
            # Create a system instruction that defines the role and scope of the assistant
            system_instruction = """
            You are ExamSeek Assistant, a helpful AI designed to provide accurate information about Indian public exams. 
            You can help users with:
            - Information about entrance exams in India (engineering, medical, law, management, etc.)
            - Details about government job exams (UPSC, SSC, Banking, Railways, etc.)
            - Guidance on eligibility criteria, exam patterns, syllabus, and application procedures
            - Tips for exam preparation
            
            Please provide concise, accurate information. If you're unsure about any details, 
            let the user know and suggest checking the official exam website for the most up-to-date information.
            
            Always maintain a helpful, professional tone.
            """
            
            # Get response from the model with context
            response = self.model.generate_content(
                [system_instruction, message],
                generation_config={
                    "max_output_tokens": 1024,
                    "temperature": 0.2,
                    "top_p": 0.8,
                    "top_k": 40
                }
            )
            
            return {
                "text": response.text,
                "status": "success"
            }
            
        except Exception as e:
            logging.error(f"Error getting response from Vertex AI: {e}")
            return {
                "text": "I'm sorry, but I encountered an error processing your request. Please try again later.",
                "status": "error",
                "error": str(e)
            }

# Create a global instance of the chatbot
chatbot = ExamSeekChatbot()
