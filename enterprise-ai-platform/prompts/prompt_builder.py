# this class build and return prompt based on prompt template stopred in /prompts/templates directory
# manadatory condition is , prompt template name passed should match with the template text file in /templates directpry
import models.incident as inc
from pathlib import Path


class PromptBuilder:

    def build_incident_prompt(self,template_name,incident:inc.Incident):
        template = self.load_template(template_name)
        prompt = template.format(incident_number = incident.incident_number,
                                 application = incident.application,
                                 error_message = incident.error_message,
                                 business_impact= incident.business_impact)
        return prompt

    def load_template(self,template_name):
        template_path  = (
            Path(__file__).parent
            / "templates"
            / f"{template_name}.txt"
        )
        with open(template_path,"r") as file:
                    template = file.read()
        return template





