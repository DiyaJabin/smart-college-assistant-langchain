from langchain_ollama import ChatOllama
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from tools import tool_list
from prompt import prompt

llm = ChatOllama(  # Creates the local model
    model="llama3.2",
    temperature=0, #Reduce creativity to make the model more predictable 
)

agent = create_tool_calling_agent(  # Connects the model, tools and prompt
    llm=llm,
    tools=tool_list,
    prompt=prompt
)

agent_executor = AgentExecutor(  # Actually runs the agent
    agent=agent,
    tools=tool_list,
    verbose=True  # Show the tool calling steps in the terminal
)


def run_college_assistant():
    print(f"{'-' * 50}SMART COLLEGE ASSISTANT{'-' * 50}")
    while True:
        user_input = input("Enter your query:")
        if user_input.lower() in ["exit","quit","bye"]:
            break
        if not user_input: #If query is blank
            print("Please enter a query.")
            continue
        response = agent_executor.invoke({
            "input": user_input,
        })
        print(response["output"])
        exit_var = input("Do you want to continue? (y/n): ")
        if exit_var.lower() == 'n':
            print("Thank you for using Smart College Assistant!")
            print("Exiting....")
            break

if __name__=="__main__":
    run_college_assistant()