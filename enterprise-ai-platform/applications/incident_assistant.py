from models.incident import Incident
from workflows.incident_analysis_workflow import IncidentWorkflow
from utils.logger import logger

def run_incident_assistant(workflow:IncidentWorkflow) -> None:
    """Collect incident information and execute the analysis workflow."""

    print("\nIncident Analysis Assistant")
    print("-" * 50)
    logger.info(f"Collecting incident details from user")

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
    logger.info(f"incident number : {incident_number}, application :{application}, error :{error_message}, business implact : {business_impact}")
    logger.info(f"Executing workflow")
    formatted_llm_response = workflow.execute(incident)
    logger.info(f"Displaying report")

    display_report(incident,formatted_llm_response)
    # incident Report

def format_report(incident:Incident, formatted_llm_response) -> str:
    report = {
        "Incident Number": incident.incident_number,
        "Application": incident.application,
        "Root Cause": formatted_llm_response["Root Cause"],
        "Immediate Action": formatted_llm_response["Immediate Action"],
        "Long-term Prevention": formatted_llm_response["Long-term Prevention"],
        "Confidence": formatted_llm_response["Confidence"],
    }

    lines = [
        "Incident Analysis Report",
        "-" * 50,

    ]

    lines.extend(
        f"{label:<25}: {value}"
        for label, value in report.items()
    )

    return "\n".join(lines)

def display_report(incident:Incident, formatted_llm_response) -> None:
    print(format_report(incident,formatted_llm_response))
