import requests

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2-large"
headers = {"Authorization": f"Bearer {LLAMA_API_KEY}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "What is reactJS? ",
})

print(output)
