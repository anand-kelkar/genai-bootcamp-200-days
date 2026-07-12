from dataclasses import dataclass

@dataclass
class Incident:
    incident_number: str
    application: str
    error_message: str
    business_impact: str

