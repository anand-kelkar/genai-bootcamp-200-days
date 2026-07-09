import prompt_builder_v1 as pb

incident_number = input("Enter incident number : \n")
application = input("Enter Application Name: \n")
error_message = input("Enter Error Message : \n")
business_impact = input("Enter Business Impact : \n")


prompt_builder = pb.PromptBuilder()
inc_assit_prompt = prompt_builder.build_incident_assistant_prompt(application,error_message,business_impact)
print(inc_assit_prompt)

