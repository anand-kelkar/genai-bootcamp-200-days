import prompt_template as pt
import prompt_builder_v1 as pb

# career_coach_template = pt.PromptTemplate.get_prompt_template("career_coach")

# career_coach_prompt = career_coach_template.format(user_experience=14,
#     user_current_technology="production support and enterprise integration",
#     user_target_role="Enterprise GenAI Architect")

# print(career_coach_prompt)

prompt_builder = pb.PromptBuilder()
career_prompt = prompt_builder.build_career_prompt(12,"BizTalk","AI Forward System Engineer")
print(career_prompt)

code_review_prompt = prompt_builder.build_code_Reviewer_prompt("AAAAAAAAAAAAA")
print(code_review_prompt)
