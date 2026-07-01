name = input("Enter your name:")
years_of_experience = input("Years of Experience::")
python_knowledge = input("Do you know Python?:")
cloud_knowledge = input("Do you know Cloud?:")

skills_recommonded = ["Python","Azure AI","LLM Engineering","RAG","Agents"]

estimated_readiness_percent  = 45
target = "Enterprise GenAI Architect"

#Start Preparing the career report

print("============================")
print("Career Report")
print("============================")

print(f"Name       : {name}")
print(f"Experience : {years_of_experience}")
print(f"Python     : {python_knowledge}")
print(f"Cloud      : {cloud_knowledge}")

print(f"Recommendation")
print("You should learn:")

for skill in skills_recommonded:
    print(f"✓ {skill}")

print("Estimated Readiness")
print(f"{estimated_readiness_percent}%")
print("Target")
print("Enterprise GenAI Architect")

