from gradio_client import Client
from huggingface_hub import InferenceClient

import os

LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")

client = Client("Hilbrakaku/google-gemma-2-2b-it")
result = client.predict(
		param_0="¿Cual es la diferencia entre URL y URN? explicame un poco mas",
		api_name="/predict"
)
print(result)

client = InferenceClient(
    "google/gemma-2-2b-it",
    token=LLAMA_API_KEY,
)

for message in client.chat_completion(
	messages=[{"role": "user", "content": "What is the capital of France?"}],
	max_tokens=500,
	stream=True,
):

print(message.choices[0].delta.content, end="")
