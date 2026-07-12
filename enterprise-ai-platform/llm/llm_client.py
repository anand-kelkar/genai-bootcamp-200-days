# This is parent class to call the LLM and return response
class LLMClient:
    row_llm_response = """
    Root Cause:MQ Listener Down
    Immediate Action:Restart Listener  
    Long-term Prevention:Enable Monitoring
    Confidence:90% """

    def generate(self,promt):

        return self.row_llm_response

class OpenAILLMClient(LLMClient):
    def generate(self,promt):
        return super().generate(promt)

