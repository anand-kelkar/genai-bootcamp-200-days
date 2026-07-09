class PromptBuilder:
    def set_system_prompt(self,system_prompt):
        self.__system_prompt = system_prompt

    def set_user_prompt(self,user_prompt):
        self.__user_prompt = user_prompt

    def build_prompt(self):
        prompt = f"""
System:
{self.__system_prompt}

User:
{self.__user_prompt}
"""
        return prompt

    def build_career_prompt(self, user_experience,user_current_technology,user_target_role):
        system_prompt = "You are an Enterprise AI Career Coach."
        user_prompt = f"""The user has {user_experience} years of enterprise integration experience in {user_current_technology}.
Recommend a 12-month learning roadmap to become an {user_target_role}. """
        return self.build_prompt()
    
    def build_summary_prompt(self, document_text, summary_Length_in_words):
        system_prompt = "You are an expert document reviewer and expert in sumarizing the content of the document."
        user_prompt = f"""Sumarize the document mentioned after this line in {summary_Length_in_words} words. \n Input Document : {document_text} .  """
        return self.build_prompt()

    def build_translation_prompt(self, text_to_translate , language_from , language_to):
        system_prompt = "You are an expert in translating text from one language to another"
        user_prompt = f"""Translate the text mentioned after '{language_from}:' to {language_to} 
Example:
English: Hello
French: Bonjour

Example:
English: Good Morning
Hindi: Suprabhat

Now translate :
{language_from}:{text_to_translate}

"""
        return self.build_prompt()


