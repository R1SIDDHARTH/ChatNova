#!/usr/bin/env python3
"""
Terminal-based Chatbot using Google's Gemini API

This script creates a simple command-line chatbot that leverages 
the Gemini API for generating responses to user inputs.
"""
# Prepare the request payload
"""
TYPE THIS IN CMD:

"C:\ALL folder in dexstop\PycharmProjects\gemni-Ai.py" --api-key="Your_Gemini_API_Key"

"""

import os
import sys
import time
import argparse
import json
import traceback
from typing import List, Dict, Any, Optional
import requests

# ANSI color codes for terminal output
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class GeminiChatbot:
    def __init__(self, api_key: str, model: str = "gemini-1.5-flash"):
        """
        Initialize the Gemini chatbot.
        
        Args:
            api_key: Your Gemini API key
            model: The Gemini model to use (default: gemini-1.5-flash)
        """
        self.api_key = api_key
        self.model = model
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"
        self.conversation_history: List[Dict[str, str]] = []
        
    def generate_response(self, user_input: str) -> str:
        """
        Generate a response using the Gemini API.
        
        Args:
            user_input: The user's input message
            
        Returns:
            The generated response from Gemini
        """
        # Add user message to conversation history
        self.conversation_history.append({"role": "user", "parts": [{"text": user_input}]})
        
        # Prepare the request URL and headers
        url = f"{self.base_url}/{self.model}:generateContent?key={self.api_key}"
        headers = {
            "Content-Type": "application/json"
        }
        
        # Prepare the request payload
        payload = {
            "contents": self.conversation_history
        }
        
        try:
            # Make the API request
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response_data = response.json()
            
            # Parse the response
            if response.status_code == 200 and "candidates" in response_data:
                text_response = response_data["candidates"][0]["content"]["parts"][0]["text"]
                
                # Add model response to conversation history
                self.conversation_history.append({"role": "model", "parts": [{"text": text_response}]})
                
                return text_response
            else:
                error_message = response_data.get("error", {}).get("message", "Unknown error")
                return f"Error: {error_message}"
                
        except Exception as e:
            return f"Error: {str(e)}"
            
    def clear_history(self) -> None:
        """Clear the conversation history."""
        self.conversation_history = []
        
    def show_welcome_message(self) -> None:
        """Display a welcome message when starting the chatbot."""
        print(f"\n{Colors.BOLD}{Colors.BLUE}====================================={Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.BLUE}   Welcome to the Gemini Chatbot    {Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.BLUE}====================================={Colors.ENDC}")
        print(f"{Colors.YELLOW}Type a message to start chatting!{Colors.ENDC}")
        print(f"{Colors.YELLOW}Type 'exit', 'quit', or 'bye' to end the conversation.{Colors.ENDC}")
        print(f"{Colors.YELLOW}Type 'clear' to clear conversation history.{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.BLUE}====================================={Colors.ENDC}\n")

    def run(self) -> None:
        """Run the chatbot in an interactive loop."""
        self.show_welcome_message()
        
        try:
            while True:
                # Get user input
                user_input = input(f"{Colors.GREEN}You: {Colors.ENDC}")
                
                # Check for exit commands
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print(f"\n{Colors.YELLOW}Thank you for chatting. Goodbye!{Colors.ENDC}")
                    break
                
                # Check for clear command
                if user_input.lower() == 'clear':
                    self.clear_history()
                    print(f"{Colors.YELLOW}Conversation history cleared.{Colors.ENDC}")
                    continue
                
                # Skip empty inputs
                if not user_input.strip():
                    continue
                
                # Show "thinking" animation
                print(f"{Colors.BLUE}Gemini is thinking", end="")
                for _ in range(3):
                    time.sleep(0.3)
                    print(".", end="", flush=True)
                print(f"{Colors.ENDC}")
                
                # Get and display the response
                response = self.generate_response(user_input)
                print(f"{Colors.BOLD}Gemini: {Colors.ENDC}{response}\n")
                
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Chat interrupted. Goodbye!{Colors.ENDC}")
        except Exception as e:
            print(f"\n{Colors.RED}An error occurred: {str(e)}{Colors.ENDC}")


def main():
    """Main function to run the chatbot."""
    try:
        parser = argparse.ArgumentParser(description="Terminal-based Gemini Chatbot")
        parser.add_argument("--api-key", help="Your Gemini API key")
        parser.add_argument("--model", default="gemini-1.5-flash", help="Gemini model to use (default: gemini-1.5-flash)")
        args = parser.parse_args()
        
        # Get API key from arguments or environment variable
        api_key = args.api_key or os.environ.get("GEMINI_API_KEY")
        
        if not api_key:
            print(f"{Colors.RED}Error: Please provide a Gemini API key using --api-key or set the GEMINI_API_KEY environment variable.{Colors.ENDC}")
            sys.exit(1)
        
        print(f"API Key received: {api_key[:5]}...{api_key[-5:] if len(api_key) > 10 else ''}")  # Debug: Show first and last 5 chars of API key
        
        # Create and run the chatbot
        chatbot = GeminiChatbot(api_key=api_key, model=args.model)
        chatbot.run()
    except Exception as e:
        print(f"ERROR: {str(e)}")
        print("Traceback:")
        traceback.print_exc()
        input("Press Enter to exit...")  # This keeps the window open


if __name__ == "__main__":
    main()