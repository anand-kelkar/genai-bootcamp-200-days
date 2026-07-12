from applications.incident_assistant import run_incident_assistant
import prompts.prompt_builder as pb
import llm.llm_client as llmc
import parsers.incident_output_parser as inc_op_parser
from workflows.incident_analysis_workflow import IncidentWorkflow

def main() -> None:
    """Start the Enterprise AI Platform."""
    print("=" * 50)
    print("Enterprise AI Platform")
    print("=" * 50)
    prompt_builder = pb.PromptBuilder()
    llm_client = llmc.OpenAILLMClient()
    parser = inc_op_parser.JSONOutputParser()

    workflow = IncidentWorkflow(prompt_builder,llm_client,parser)
    run_incident_assistant(workflow)


if __name__ == "__main__":
    main()