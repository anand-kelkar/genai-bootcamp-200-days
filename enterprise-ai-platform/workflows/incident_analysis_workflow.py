from models.incident import Incident
from prompts.prompt_builder import PromptBuilder
from llm.llm_client import LLMClient
from parsers.incident_output_parser import OutputParser
from utils.logger import logger
import config.settings as config_setting
from dataclasses import asdict

class IncidentWorkflow:
    # Receive incident as part of initialization of incident workflow
    def __init__(self, prompt_builder:PromptBuilder, 
                 llm_client:LLMClient, parser:OutputParser):
        self.prompt_builder = prompt_builder
        self.llm_client = llm_client
        self.parser = parser

    def execute(self, incident:Incident):
        try:
            # build prompt start
            variables = asdict(incident)
            prompt = self.prompt_builder.build_prompt(config_setting.DEFAULT_TEMPLATE,variables)
            # build prompt End

            # call LLM started
            logger.info("Calling LLM")
            raw_llm_response = self.llm_client.generate(prompt)
            logger.info("Response received")
            # call LLM ended

            # parse LLM output and convert to json start
            logger.info("Parsing LLM Response")
            parsed_llm_response = self.parser.parse(raw_llm_response)
            logger.info("Parsing completed")
            # parse LLM output and convert to json end
            logger.info("Workflow completed")
            return parsed_llm_response
        except Exception as ex:
            print(f"Workflow failed: {ex}")
            logger.exception(ex)
            raise
        



