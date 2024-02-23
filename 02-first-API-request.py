# Import the OpenAI client
from openai import OpenAI

# Create the OpenAI client and set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Completions endpoint
response = client.completions.create(
  # Specify the correct model
  model="gpt-3.5-turbo-instruct",
  prompt="Who developed ChatGPT?"
)

print(response)
