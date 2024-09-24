import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Obtener el secreto desde las variables de entorno
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3.1-8B"
headers = {"Authorization": f"Bearer {LLAMA_API_KEY}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})
