import sys
from typing import Dict, List
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def initialize_client(use_ollama: bool= False)->OpenAI:
    """Initialize the OpenAI client for either OpenAi or OLLAMA"""
    if use_ollama:
        return OpenAI(base_url="http://localhost:11434/v1",api_key="ollama")
    return OpenAI()

def create_initial_messages() -> List[Dict[str,str]]:
     """Create the initial messages for the context memory."""
     return [
         {"role":"system", "content": "Hi, how can i help you today?"}
     ]