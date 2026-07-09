class PromptTemplate:

    __template_collection = {
        "career_coach": """
                        System:
                        You are an Enterprise AI Career Coach.        
                        User:
                        The user has {user_experience} years of enterprise integration experience in {user_current_technology}.
                        Recommend a 12-month learning roadmap to become an {user_target_role}. 
                        """,
        "document_summarizer": """
                        System:
                        You are an expert document reviewer and expert in sumarizing the content of the document.        
                        User:
                        Sumarize the document mentioned after this line in {summary_Length_in_words} words. \n Input Document : {document_text} . 
                        """,
        "translator": """
                        System:
                        You are an expert in translating text from one language to another.        
                        User:
                        Translate the text mentioned after '{language_from}:' to {language_to} 
                        Example:
                        English: Hello
                        French: Bonjour

                        Example:
                        English: Good Morning
                        Hindi: Suprabhat

                        Now translate :
                        {language_from}:{text_to_translate}
                        """,
        "code_reviewer": """
                        System:
                        You are an expert python sr. developer specialized in reviewing pear's code.        
                        User:
                        Review the code given after this line. 
                         Input Document : {document_text} . 
                        """,
        "incident_assistant": """
                                System:
                                You are a Senior Enterprise Production Support Architect.        
                                User:
                                Analyze the following incident. 
                                Application:
                                {application}
                                Error:
                                {error_message}
                                Business Impact:
                                {business_impact}
                                Suggest:
                                1. Possible root causes
                                2. Immediate actions
                                3. Long-term preventive actions 
                                """
    }

    @classmethod
    def get_prompt_template(cls, key):
        return cls.__template_collection.get(key)

