import prompt_template as pt
class PromptBuilder():
    def build_career_prompt(self, user_experience,user_current_technology,user_target_role):
        career_coach_template = pt.PromptTemplate.get_prompt_template("career_coach")
        career_coach_prompt = career_coach_template.format(user_experience=user_experience,
                            user_current_technology=user_current_technology,
                            user_target_role=user_target_role)
        return career_coach_prompt
    
    def build_summary_prompt(self, document_text, summary_Length_in_words):
        doc_summary_template = pt.PromptTemplate.get_prompt_template("document_summarizer")
        doc_summary_prompt = doc_summary_template.format(summary_Length_in_words=summary_Length_in_words,
                            document_text=document_text)
        return doc_summary_prompt

    def build_translation_prompt(self, text_to_translate , language_from , language_to):
        doc_translation_template = pt.PromptTemplate.get_prompt_template("translator")
        translator_prompt = doc_translation_template.format(text_to_translate = text_to_translate,
                            language_from=language_from,
                            language_to=language_to)
        return translator_prompt
    
    def build_code_Reviewer_prompt(self, document_text):
            code_review_template = pt.PromptTemplate.get_prompt_template("code_reviewer")
            code_review_prompt = code_review_template.format(document_text=document_text)
            return code_review_prompt

    def build_incident_assistant_prompt(self, application,error_message,business_impact):
                incident_assistant_template = pt.PromptTemplate.get_prompt_template("incident_assistant")
                incident_assistant_prompt = incident_assistant_template.format(application=application,error_message=error_message,business_impact= business_impact)
                return incident_assistant_prompt

