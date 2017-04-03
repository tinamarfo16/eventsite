import eventbrite
import requests


endpoint = "https://www.eventbriteapi.com/v3/events/search/?token=C6HNAT657IPOB7635DXW"
payload = { "q": "<name>", "q": "London,UK"}

response =  requests.get(endpoint, params=payload)

print response
print response.json()
