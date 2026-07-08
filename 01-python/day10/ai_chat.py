# This is simple AP chatbot client
import llm_client as lc

llm_client = lc.LLMClient()
continue_session = True
while continue_session:
    user_question = input("Ask AI :\n")
    response = llm_client.generate(user_question)
    print(f"AI: \n {response} \n")
    user_continue_chat = input("Do you want to continue session Y/N:\n")
    if (user_continue_chat == "N"):
        continue_session = False


     