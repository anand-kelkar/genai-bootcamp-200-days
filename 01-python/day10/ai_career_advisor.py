# This app will take user input , call LLM model and provide career advise to the user
import prompt_builder 
import llm_client as lc

llm_client = lc.LLMClient()

user_experience = input("Enter your Experience in years : \n")
user_current_technology = input("Which technolgy you work on ,  e.g. BizTalk, MuleSoft and IBM MQ : \n")
user_target_role = input("Target role : \n")

pb =  prompt_builder.PromptBuilder()
pb.set_system_prompt("You are an Enterprise AI Career Coach.")
pb.set_user_prompt(f"""The user has {user_experience} years of enterprise integration experience in {user_current_technology}.
Recommend a 12-month learning roadmap to become an {user_target_role}. """)

prompt = pb.build_prompt()

print(prompt)

llm_response = llm_client.generate(prompt)
print(llm_response)

