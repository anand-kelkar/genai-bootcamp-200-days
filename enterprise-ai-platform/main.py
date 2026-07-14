from applications.incident_assistant import run_incident_assistant
from prompts.prompt_builder import PromptBuilder
from  llm.openai_llm_client import OpenAILLMClient
from parsers.incident_output_parser import JSONOutputParser
from workflows.incident_analysis_workflow import IncidentWorkflow

def main() -> None:
    """Start the Enterprise AI Platform."""
    print("=" * 50)
    print("Enterprise AI Platform")
    print("=" * 50)
    prompt_builder = PromptBuilder()
    llm_client = OpenAILLMClient()
    parser = JSONOutputParser()

    workflow = IncidentWorkflow(prompt_builder,llm_client,parser)
    run_incident_assistant(workflow)


if __name__ == "__main__":
    main()