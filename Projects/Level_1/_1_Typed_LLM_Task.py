from typing import TypedDict

class State(TypedDict):
    query: str
    decision: str
    explanation: str

from Projects.llm import get_llm

from dotenv import load_dotenv
load_dotenv()

llm = get_llm()

def llm_node(state: State) -> dict:
    prompt = f"""
Answer the user query.

Return JSON with:
- decision: short answer
- explanation: brief explanation

User query:
{state["query"]}
"""

    result = llm.invoke(prompt)
    #d: Why we hardcoded the prompt
    #d: Why we didn't use Unions or some stuff which i learnt in langgraph tutorials
    #d: Human message, Ai message, System message no segregation happened here?

    # IMPORTANT: extract content, not whole message
    text = result.content

    # simple parsing (good enough for Project 1.1)
    # assume model follows instructions
    import json
    data = json.loads(text)

    #d: How can we assume AI returns json properly and we can parse it lol
    # Hows this even working?? json.loads is already made library to parse json like stuff using regex or something?

    return {
        "decision": data["decision"],
        "explanation": data["explanation"],
    }
    #d: Why returning partial state matters, why not full state and if we return partial state does langgraph merge it under the hood?

from langgraph.graph import StateGraph, START, END

graph = StateGraph(State)

graph.add_node("llm", llm_node)

graph.add_edge(START, "llm")
graph.add_edge("llm", END)

app = graph.compile()

if __name__ == "__main__":
    user_input = input("Enter your question: ")

    final_state = app.invoke({
        "query": user_input
    })
    #d: Here the state is assumed to be null or something? cus only the query thingy we filled in wat about others?

    print("Query:", final_state["query"])
    print("Decision:", final_state["decision"])
    print("Explanation:", final_state["explanation"])
