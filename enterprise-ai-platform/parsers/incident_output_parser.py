# responsibility of this class is to parse LLM output and return JSON string
import json

class OutputParser:
    def parse(self):
        pass

class JSONOutputParser(OutputParser):
    def parse_to_json(self, raw_llm_response):
        response_dict = {}

        for line in raw_llm_response.strip().split("\n"):
            key, value = line.split(":", 1)  # Split only on the first ':'
            response_dict[key.strip()] = value.strip()
                    
        return response_dict


