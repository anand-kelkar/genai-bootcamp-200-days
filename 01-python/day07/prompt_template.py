class PromptTemplate:
    def __init__(self,template_name,prompt):
        self.template_name = template_name
        self.prompt = prompt

    def display(self):
            print(self.prompt)

    def fill_prompt(self, name):
        return str(self.prompt).format(name)

prompt_template = PromptTemplate("Greetings","Hello {}, welcome to Enterprise AI.")
print(prompt_template.fill_prompt("Anand"))