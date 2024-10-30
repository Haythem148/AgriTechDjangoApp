import os
from dotenv import load_dotenv

load_dotenv()

# Configuration HuggingFace
HF_TOKEN = os.getenv('HUGGINGFACE_TOKEN', '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')