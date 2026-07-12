import models.incident as inc
import prompts.prompt_builder as pb
import llm.llm_client as llmc
import parsers.incident_output_parser as inc_op_parser


class IncidentWorkflow:
    # Receive incident as part of initialization of incident workflow
    def __init__(self, prompt_builder:pb.PromptBuilder, 
                 llm_client:llmc.OpenAILLMClient, parser:inc_op_parser.JSONOutputParser):
        self.prompt_builder = prompt_builder
        self.llm_client = llm_client
        self.parser = parser

    def trigger(self, incident:inc.Incident):
        # build prompt start
        prompt = self.prompt_builder.build_incident_prompt("incident_analysis",incident)
        # build prompt End

        # call LLM started
        row_llm_response = self.llm_client.generate(prompt)
        # call LLM ended

        # parse LLM output and convert to json start
        parsed_llm_response = self.parser.parse_to_json(row_llm_response)
        # parse LLM output and convert to json end

        return parsed_llm_response



