# Extract the model from response
print(response.model)

# Extract the total_tokens from response
print(response.usage.total_tokens)

# Extract the text from response
print(response.choices[0].text)
