import sys
from openai import OpenAI

def initialize_client(use_ollama: bool= False)->OpenAI:
    """Initialize the OpenAI client for either OpenAi or OLLAMA"""