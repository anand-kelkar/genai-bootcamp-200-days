import requests
import json

class APIClient:

    def get(self, url):
        return requests.get(url)

    def post(self, url , payload, headers):
        return requests.post(url, data=json.dumps(payload), headers=headers)

class OpenAIClient(APIClient):
    def generate_text(self , prompt):
        return "Response from LLM"
