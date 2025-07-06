import requests

response = requests.get("https://zenquotes.io/api/today")

response_quote = response.json()

print(response_quote[0]['q'],response_quote[0]['a'],sep="\n\t\t---")
