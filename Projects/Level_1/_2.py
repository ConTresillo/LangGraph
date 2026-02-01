from typing import TypedDict, List
from datetime import datetime
import json

from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from Projects.llm import get_llm

load_dotenv()

# --------------------
# Types
# --------------------

class Snapshot(TypedDict):
    timestamp: str
    query: str
    response: str
    explanation: str


class State(TypedDict):
    query: str
    history: List[Snapshot]
    continue_chat: bool


# --------------------
# LLM
# --------------------

llm = get_llm()


# --------------------
# Helpers
# --------------------

def build_history_text(history: List[Snapshot]) -> str:
    if not history:
        return "None"

    lines = []
    for i, h in enumerate(history, 1):
        lines.append(
            f"{i}. User: {h['query']}\n"
            f"   Assistant: {h['response']}\n"
            f"   Explanation: {h['explanation']}"
        )
    return "\n".join(lines)


def safe_json_parse(text: str):
    try:
        return json.loads(text)
    except Exception:
        return None


# --------------------
# Nodes
# --------------------

def llm_node(state: State) -> dict:
    state["query"] = input("Enter your Query: ")
    history_text = build_history_text(state["history"])

    prompt = f"""
You are a conversational assistant with memory.

Conversation so far:
{history_text}

Current user query:
{state["query"]}

Return STRICT JSON (no ```json ``` fencing) with:
- response
- explanation

Just the 2 alone no multiple params watever it might be 
if u solving 2 qns even then response , explanation thats it
"""

    result = llm.invoke(prompt)
    raw = result.content

    data = safe_json_parse(raw)

    if data and "response" in data and "explanation" in data:
        response = data["response"]
        explanation = data["explanation"]
    else:
        # fallback if model ignores JSON
        response = raw.strip()
        explanation = "Model did not return valid JSON."

    snapshot: Snapshot = {
        "timestamp": datetime.utcnow().isoformat(),
        "query": state["query"],
        "response": response,
        "explanation": explanation,
    }

    print(f"[ai][response]: {response}")
    print(f"[ai][explanation]: {explanation}")

    return {
        "history": state["history"] + [snapshot]
    }


def continue_node(state: State) -> dict:
    answer = input("Do you want to continue? (y/n): ").strip().lower()
    return {
        "continue_chat": answer == "y"
    }


# --------------------
# Routing
# --------------------

def route(state: State):
    return "loop" if state["continue_chat"] else "stop"


# --------------------
# Graph
# --------------------

graph = StateGraph(State)

graph.add_node("llm", llm_node)
graph.add_node("continue", continue_node)

graph.add_edge(START, "llm")
graph.add_edge("llm", "continue")

graph.add_conditional_edges(
    "continue",
    route,
    {
        "loop": "llm",
        "stop": END,
    }
)

app = graph.compile()


# --------------------
# Entry point
# --------------------

if __name__ == "__main__":
    state: State = {
        "query": "",
        "history": [],
        "continue_chat": True,
    }

    final_state = app.invoke(state)

    print("\n=== FINAL HISTORY ===")
    for i, h in enumerate(final_state["history"], 1):
        print(f"\n[{i}] {h['timestamp']}")
        print(f"User: {h['query']}")
        print(f"Assistant: {h['response']}")
        print(f"Explanation: {h['explanation']}")
