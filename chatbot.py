import os
import logging
import random
from typing import Dict, Any
from data import EXAM_CATEGORIES, EXAMS_DATA, get_exam_details, search_exams

class ExamSeekChatbot:
    def __init__(self):
        self.initialized = True
        logging.info("Simple chatbot initialized successfully")
        
        # Load exam data for reference
        self.exam_categories = EXAM_CATEGORIES
        self.exams_data = EXAMS_DATA
        
        # Define common responses and FAQs
        self.common_questions = {
            "help": "I can help you with information about entrance exams, government job exams, eligibility criteria, exam patterns, syllabus, and application procedures. Just ask me anything about Indian exams!",
            "greeting": ["Hello! How can I help you with your exam preparation today?", 
                       "Hi there! I'm ExamSeek Assistant. What would you like to know about exams?",
                       "Welcome to ExamSeek! I'm here to help with your exam-related questions."],
            "thanks": ["You're welcome! Feel free to ask if you have more questions.",
                      "Happy to help! Let me know if you need anything else.",
                      "Anytime! Good luck with your exam preparation!"],
            "capabilities": "I can provide information about various Indian exams, including details on eligibility, exam patterns, important dates, and preparation tips. I can also help you find the right exam based on your interests.",
            "bye": ["Goodbye! Good luck with your exam preparation!",
                   "See you later! Don't hesitate to return if you have more questions.",
                   "Bye! Wishing you success in your exams!"]
        }
        
        self.exam_tips = {
            "general": [
                "Create a structured study plan and stick to it.",
                "Take regular breaks during study sessions to maintain focus.",
                "Practice previous years' question papers to understand the exam pattern.",
                "Join study groups or find a study partner for motivation.",
                "Stay healthy by getting enough sleep, exercise, and proper nutrition."
            ],
            "engineering": [
                "Focus on understanding concepts rather than memorizing formulas.",
                "Practice numerical problems regularly to build speed and accuracy.",
                "For JEE/GATE, prioritize topics with higher weightage.",
                "Create short notes for quick revision before the exam.",
                "Solve mock tests under timed conditions to improve time management."
            ],
            "medical": [
                "For NEET, thoroughly master NCERT textbooks before moving to reference books.",
                "Practice diagram-based questions for Biology.",
                "Memorize important reactions and equations in Chemistry.",
                "Focus on understanding concepts in Physics rather than rote learning.",
                "Take regular mock tests to identify and improve weak areas."
            ],
            "upsc": [
                "Read newspapers daily to stay updated on current affairs.",
                "Make concise notes while studying for effective revision.",
                "Practice answer writing regularly for the Mains examination.",
                "Develop a multidisciplinary approach to issues.",
                "Focus on NCERT textbooks to build a strong foundation."
            ],
            "banking": [
                "Practice quantitative aptitude and reasoning questions daily.",
                "Stay updated with banking and financial current affairs.",
                "Improve your speed and accuracy for the preliminary exam.",
                "Take sectional tests to identify and work on weak areas.",
                "Learn shortcuts for quick calculations in quantitative sections."
            ]
        }

    def get_response(self, message: str) -> Dict[str, Any]:
        """
        Get a response from the chatbot for a user message.
        
        Args:
            message: The user's message
            
        Returns:
            A dictionary containing the response text and status
        """
        if not self.initialized:
            return {
                "text": "I'm sorry, but the AI assistant is currently unavailable. Please try again later.",
                "status": "error",
                "error": "Chatbot not initialized"
            }
        
        try:
            # Convert message to lowercase for easier matching
            message_lower = message.lower()
            
            # Check for greetings
            if any(word in message_lower for word in ["hello", "hi", "hey", "greetings", "namaste"]):
                greeting_responses = self.common_questions.get("greeting", ["Hello! How can I help you?"])
                return {
                    "text": random.choice(greeting_responses),
                    "status": "success"
                }
                
            # Check for thanks
            if any(word in message_lower for word in ["thank", "thanks", "appreciate", "helpful"]):
                thanks_responses = self.common_questions.get("thanks", ["You're welcome!"])
                return {
                    "text": random.choice(thanks_responses),
                    "status": "success"
                }
                
            # Check for goodbyes
            if any(word in message_lower for word in ["bye", "goodbye", "see you", "farewell"]):
                bye_responses = self.common_questions.get("bye", ["Goodbye! All the best!"])
                return {
                    "text": random.choice(bye_responses),
                    "status": "success"
                }
                
            # Check for help request
            if any(word in message_lower for word in ["help", "assist", "what can you do", "capabilities"]):
                return {
                    "text": self.common_questions.get("capabilities", "I can help you with information about various Indian exams, eligibility criteria, application procedures, and more."),
                    "status": "success"
                }
                
            # Check for exam category information
            for category in self.exam_categories:
                category_name = category.get("name", "").lower()
                category_id = category.get("id", "").lower()
                if category_name in message_lower or category_id in message_lower:
                    response = f"**{category.get('name', '')}**: {category.get('description', '')}\n\n"
                    # No subcategories information as per requirements
                    response += "You can ask me about specific exams in this category!"
                    return {
                        "text": response,
                        "status": "success"
                    }
                
            # Check for specific exam information
            for exam in self.exams_data:
                exam_name_lower = exam.get("name", "").lower()
                exam_full_name_lower = exam.get("full_name", "").lower()
                
                if exam_name_lower in message_lower or exam_full_name_lower in message_lower:
                    # Looking for specific aspects
                    if "eligibility" in message_lower:
                        return {
                            "text": f"**Eligibility for {exam.get('name', '')}**: {exam.get('eligibility', 'Information not available')}",
                            "status": "success"
                        }
                    elif "pattern" in message_lower or "structure" in message_lower:
                        return {
                            "text": f"**Exam Pattern for {exam.get('name', '')}**: {exam.get('exam_pattern', 'Information not available')}",
                            "status": "success"
                        }
                    elif "syllabus" in message_lower or "curriculum" in message_lower:
                        return {
                            "text": f"**Syllabus for {exam.get('name', '')}**: {exam.get('syllabus', 'Information not available')}",
                            "status": "success"
                        }
                    elif "application" in message_lower or "apply" in message_lower or "registration" in message_lower:
                        return {
                            "text": f"**Application Procedure for {exam.get('name', '')}**: {exam.get('application_procedure', 'Information not available')}",
                            "status": "success"
                        }
                    elif "date" in message_lower or "schedule" in message_lower or "when" in message_lower:
                        important_dates = exam.get("important_dates", {})
                        dates_info = "\n".join([f"- **{key.replace('_', ' ').title()}**: {value}" for key, value in important_dates.items()])
                        if not dates_info:
                            dates_info = "Information not available"
                        return {
                            "text": f"**Important Dates for {exam.get('name', '')}**:\n{dates_info}",
                            "status": "success"
                        }
                    elif "tip" in message_lower or "advice" in message_lower or "prepare" in message_lower or "suggestion" in message_lower:
                        preparation_tips = exam.get("preparation_tips", [])
                        tips = "\n".join([f"- {tip}" for tip in preparation_tips]) if preparation_tips else "No specific tips available for this exam."
                        return {
                            "text": f"**Preparation Tips for {exam.get('name', '')}**:\n{tips}",
                            "status": "success"
                        }
                    else:
                        # General overview
                        response = f"**{exam.get('full_name', '')} ({exam.get('name', '')})**\n\n"
                        response += f"{exam.get('description', '')}\n\n"
                        response += f"**Conducted by**: {exam.get('conducting_body', 'Information not available')}\n"
                        response += f"**Frequency**: {exam.get('frequency', 'Information not available')}\n\n"
                        response += "You can ask me more specific questions about eligibility, exam pattern, syllabus, application procedure, or important dates for this exam!"
                        return {
                            "text": response,
                            "status": "success"
                        }
                        
            # Check for preparation tips
            if "tip" in message_lower or "advice" in message_lower or "suggestion" in message_lower or "prepare" in message_lower:
                # Check for category-specific tips
                for category_key, category_name in [
                    ("engineering", ["engineering", "jee", "gate", "technical"]),
                    ("medical", ["medical", "neet", "doctor", "mbbs"]),
                    ("upsc", ["upsc", "civil service", "ias", "ips", "government service"]),
                    ("banking", ["bank", "sbi", "rbi", "finance"])
                ]:
                    if any(term in message_lower for term in category_name):
                        tips_list = self.exam_tips.get(category_key, [])
                        tips = "\n".join([f"- {tip}" for tip in tips_list]) if tips_list else "No specific tips available for this category."
                        return {
                            "text": f"**Preparation Tips for {category_key.title()} Exams**:\n{tips}",
                            "status": "success"
                        }
                
                # General tips if no specific category found
                tips_list = self.exam_tips.get("general", [])
                tips = "\n".join([f"- {tip}" for tip in tips_list]) if tips_list else "No general tips available."
                return {
                    "text": f"**General Exam Preparation Tips**:\n{tips}",
                    "status": "success"
                }
                
            # If no specific match is found, provide a general response
            return {
                "text": "I'm not sure I understand your question. You can ask me about:\n\n" +
                       "- Specific exams like JEE, NEET, UPSC, SBI PO, etc.\n" +
                       "- Exam categories like Engineering, Medical, Banking\n" +
                       "- Details like eligibility, exam pattern, syllabus\n" +
                       "- Application procedures and important dates\n" +
                       "- Preparation tips and advice\n\n" +
                       "Could you please rephrase your question?",
                "status": "success"
            }
            
        except Exception as e:
            logging.error(f"Error processing message: {e}")
            return {
                "text": "I'm sorry, but I encountered an error processing your request. Please try again with a different question.",
                "status": "error",
                "error": str(e)
            }

# Create a global instance of the chatbot
chatbot = ExamSeekChatbot()
