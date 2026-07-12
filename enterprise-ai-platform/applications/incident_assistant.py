from models.incident import Incident
from workflows.incident_analysis_workflow import IncidentWorkflow
import json
import prompts.prompt_builder as pb
import llm.llm_client as llmc
import parsers.incident_output_parser as inc_op_parser

def run_incident_assistant(workflow:IncidentWorkflow) -> None:
    """Collect incident information and execute the analysis workflow."""

    print("\nIncident Analysis Assistant")
    print("-" * 50)

    incident_number = input("Enter incident number: ").strip()
    application = input("Enter application name: ").strip()
    error_message = input("Enter error message: ").strip()
    business_impact = input("Enter business impact: ").strip()
    incident = Incident(
        incident_number=incident_number,
        application=application,
        error_message=error_message,
        business_impact=business_impact,
    )
    formatted_llm_response = workflow.trigger(incident)
    display_report(incident,formatted_llm_response)
    # incident Report

def display_report(incident, formatted_llm_response):
    print("=" * 50)
    print("\nAI Incident Report")
    print("=" * 50)
    print("\nIncident Number : ")
    print(f"\n{incident.incident_number}")

    print("\nApplication : ")
    print(f"\n{incident.application}\n")
    print("-" * 50)
    print("\nRoot Cause : \n")
    print(formatted_llm_response["Root Cause"])
    print("-" * 50)
    print("\nImmediate Action : \n")
    print(formatted_llm_response["Immediate Action"])
    print("-" * 50)
    print("\nLong-term Prevention : \n")
    print(formatted_llm_response["Long-term Prevention"])
    print("-" * 50)
    print("\nConfidence : \n")
    print(formatted_llm_response["Confidence"])
    print("-" * 50)

