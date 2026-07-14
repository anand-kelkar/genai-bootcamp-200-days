# this class build and return prompt based on prompt template stopred in /prompts/templates directory
# manadatory condition is , prompt template name passed should match with the template text file in /templates directpry
from pathlib import Path
from utils.logger import logger 
class PromptBuilder:

    def build_prompt(self, template_name: str, variables:dict):
        """
        Build a prompt by loading the template and replacing placeholders.

        Args:
            template_name: Name of the template file (without .txt)
            variables: Dictionary containing placeholder values

        Returns:
            Fully formatted prompt string
        """
        template = self.load_template(template_name)
        logger.info(f"Template {template_name} loaded")
        try:
            logger.info(f"forming {template_name} prompt by supplyig variables to template")
            return template.format(**variables)

        except KeyError as ex:
            raise ValueError(
                f"Missing placeholder '{ex.args[0]}' in template '{template_name}'."
            ) from ex   
        

    def load_template(self,template_name):
        template_path  = (
            Path(__file__).parent
            / "templates"
            / f"{template_name}.txt"
        )
        try:              
            with open(template_path,"r") as file:
                    template = file.read()
                    return template
        except FileNotFoundError as ex:
            raise FileNotFoundError(
                f"Prompt template '{template_name}.txt' was not found at '{template_path}'."
            ) from ex
        except PermissionError as ex:
            raise PermissionError(
                f"Permission denied while reading '{template_path}'."
            ) from ex
        except OSError as ex:
            raise OSError(
                f"Unable to read prompt template '{template_path}'."
            ) from ex
        





