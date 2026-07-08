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

# prompt_builder = PromptBuilder()

# prompt_builder.set_system_prompt("You are an AI Career Coach.")
# prompt_builder.set_user_prompt("How do I become an Enterprise GenAI Architect?")
# print(prompt_builder.build_prompt())
