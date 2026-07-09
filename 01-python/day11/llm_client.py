class LLMClient:
    def generate(self,system_prompt,user_prompt):
        prompt = f"""
        system : {system_prompt},
        user : {user_prompt}
        """
        return prompt