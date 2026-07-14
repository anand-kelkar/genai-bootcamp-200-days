from llm.llm_client import LLMClient
from utils.logger import logger
class OpenAILLMClient(LLMClient):
    raw_llm_response = """
    Root Cause:MQ Listener Down
    Immediate Action:Restart Listener  
    Long-term Prevention:Enable Monitoring
    Confidence:90% """
    def generate(self,prompt):
        logger.info(f"Generating response by calling OpenAI")
        return self.raw_llm_response

