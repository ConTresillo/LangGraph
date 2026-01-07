from dotenv import load_dotenv
from Projects.llm import get_llm
from typing import TypedDict
from langgraph.graph import START, END, StateGraph

load_dotenv()
llm = get_llm()


class State(TypedDict):
    user_prompt: str
    llm_response: str

def act(state: State) -> dict:
    llm_response = llm.invoke(state["user_prompt"]).content
    print(f"LLM Response: {llm_response}")
    return {"llm_response": llm_response}

def main():
    graph = StateGraph(State)
    graph.add_node("LLM", act)
    #Philosophy: Add all Nodes then u can connect them with edges
    graph.add_edge(START, "LLM")
    graph.add_edge("LLM", END)
    agent = graph.compile()

    #No do while loop in Python, so we use this approach
    user_prompt = input("Enter your prompt (or type 'exit' to quit): ")
    while not user_prompt.strip().lower() == "exit":
        initial_state: State = {"user_prompt": user_prompt, "llm_response": ""}
        agent.invoke(initial_state)
        user_prompt = input("Enter your prompt (or type 'exit' to quit): ")
   



if __name__ == "__main__":
    main()
