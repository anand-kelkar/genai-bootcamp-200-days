from parsers.output_parser import OutputParser
class JSONOutputParser(OutputParser):
    def parse(self, raw_llm_response):
        response_dict = {}

        for line in raw_llm_response.strip().split("\n"):
            key, value = line.split(":", 1)  # Split only on the first ':'
            response_dict[key.strip()] = value.strip()
                    
        return response_dict


