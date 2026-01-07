Below is a **fully precise, no-guesswork replacement** for **Section 2. Build Task only**.  
Everything else in the submodule remains unchanged.

---
## 🧩 Submodule 1.1.1 — Single-Node LLM Agent

**MODE:** BUILD MODE  
**DIFFICULTY TIER:** 1

---

### 🟢 0. Syntax & Semantics Inventory (MANDATORY — NO BUILD)

Scope: **minimum surface area to run a LangGraph graph whose single node is an LLM call**.

#### 1️⃣ `StateGraph`

- **What it is:** Graph constructor
    
- **Represents:** Executable system boundary
    
- **Why it exists:** Makes control flow explicit
    

**VALID**

```python
from langgraph.graph import StateGraph
g = StateGraph(dict)
```

```python
StateGraph(state_schema=dict)
```

```python
g = StateGraph(dict)
```

**INVALID / MISUSED**

```python
StateGraph()              # missing schema
```

```python
StateGraph([])            # invalid schema type
```

```python
StateGraph("state")       # meaningless schema
```

---

#### 2️⃣ LLM callable `(state) -> state`

- **What it is:** Node logic
    
- **Represents:** Reasoning / generation step
    
- **Why it exists:** Injects non-deterministic intelligence
    

**VALID**

```python
def llm_node(state):
    return {"output": "hello"}
```

```python
def llm_node(state: dict) -> dict:
    return state | {"result": "ok"}
```

```python
lambda state: {"text": "hi"}
```

**INVALID / MISUSED**

```python
def llm_node(): pass              # no state input
```

```python
def llm_node(state): print(state) # no return
```

```python
g.add_node("llm", llm_node())     # calling instead of passing
```

---

#### 3️⃣ `add_node(name, callable)`

- **What it is:** Node registration
    
- **Represents:** Executable LLM step
    
- **Why it exists:** Separates logic from topology
    

**VALID**

```python
g.add_node("llm", llm_node)
```

```python
g.add_node("agent", lambda s: s)
```

```python
g.add_node("step", llm_node)
```

**INVALID / MISUSED**

```python
g.add_node(llm_node)      # missing name
```

```python
g.add_node(1, llm_node)   # name must be string
```

```python
g.add_node("x", "llm")    # not callable
```

---

#### 4️⃣ `set_entry_point(name)`

- **What it is:** Execution start
    
- **Represents:** First reasoning step
    
- **Why it exists:** Prevents implicit flow
    

**VALID**

```python
g.set_entry_point("llm")
```

```python
g.set_entry_point("agent")
```

```python
g.set_entry_point("step")
```

**INVALID / MISUSED**

```python
g.set_entry_point()            # missing arg
```

```python
g.set_entry_point("missing")  # node not registered
```

```python
g.set_entry_point(llm_node)   # expects name
```

---

#### 5️⃣ `compile()`

- **What it is:** Graph finalization
    
- **Represents:** Runnable artifact
    
- **Why it exists:** Freezes structure
    

**VALID**

```python
app = g.compile()
```

```python
runner = g.compile()
```

```python
compiled = g.compile()
```

**INVALID / MISUSED**

```python
g()                 # graph not callable
```

```python
g.compile           # not invoked
```

```python
compile(g)          # wrong direction
```

---

#### 6️⃣ `invoke(state)`

- **What it is:** Execution trigger
    
- **Represents:** One full LLM run
    
- **Why it exists:** Deterministic entry
    

**VALID**

```python
app.invoke({})
```

```python
app.invoke({"input": "hi"})
```

```python
result = app.invoke(state)
```

**INVALID / MISUSED**

```python
app.invoke()        # missing state
```

```python
g.invoke({})        # must compile first
```

```python
invoke(app, {})     # wrong call style
```

---

### 🔑 1. Required Primitives to Act (OPERATIONAL)

- `StateGraph`
    
- One LLM-backed callable `(state) -> state`
    
- `add_node`
    
- `set_entry_point`
    
- `compile`
    
- `invoke`
    

---

### 🛠️ 2. Build Task (REGENERATED — PRECISE)

**Objective**  
Create a **single-node LangGraph agent** where the node:

- calls an LLM exactly once
    
- reads a user input from state
    
- writes the LLM response back into state
    

---

#### A. Required Behavior (EXACT)

Your graph **must** do all of the following:

1. Accept an **input state** with this shape:
    
    ```python
    {
      "user_input": "<string>"
    }
    ```
    
2. Contain **exactly one node** named:
    
    ```text
    "llm_node"
    ```
    
3. Inside `llm_node`:
    
    - Read `state["user_input"]`
        
    - Pass it as the **prompt** to an LLM
        
    - Receive the LLM’s text output
        
    - Return a **new state** with this shape:
        
        ```python
        {
          "user_input": "<original string>",
          "llm_output": "<model response string>"
        }
        ```
        
4. The graph must:
    
    - Set `"llm_node"` as the **entry point**
        
    - Compile successfully
        
    - Execute via `.invoke(...)`
        

---

#### B. Explicit Constraints (DO NOT VIOLATE)

- ❌ No additional nodes
    
- ❌ No branching / conditionals
    
- ❌ No tools
    
- ❌ No retries
    
- ❌ No memory abstractions
    
- ❌ No state mutation in-place (must return a new dict)
    

---

#### C. Success Criteria (CHECKLIST)

Your build is **correct** if and only if:

- `app.invoke({"user_input": "Hello"})` runs without error
    
- The returned value is a `dict`
    
- The returned dict contains **both** keys:
    
    - `"user_input"`
        
    - `"llm_output"`
        
- `"llm_output"` is a string generated by the LLM (not hardcoded)
    

---

#### D. Non-Goals (IGNORE COMPLETELY)

- Prompt engineering quality
    
- Response correctness
    
- Performance
    
- Cost optimization
    
- Safety / moderation
    
- Pretty formatting
    

If it runs and returns structured state, it is correct.

---

### 🔍 3. Where It Breaks (ARTIFACT-BOUND)

⛔ Do **not** fill this yet.  
Run your build first.

You will report:

- What failed
    
- Where you were unsure
    
- What behaved unexpectedly
    

---

### 🧠 4. Theory Injection (POST-BUILD ONLY)

⛔ Locked until failures are observed.

---

### 🔁 5. Apply Back to the Build

⛔ Locked until Section 4 is unlocked.

---

### ⚖️ 6. Trade-offs Introduced

⛔ Locked until build exists.

---

## 🔒 CRUCIAL CONCEPT GATE

- **CRUCIAL:** LLM-as-node (non-determinism introduced)
    
- **Mini-project:** ❌ Not required yet (contained scope)
    

---

### ⏭️ NEXT ACTION (REQUIRED)

👉 **Write and run the single-node LLM graph.**  
Then respond with:

- Your code
    
- Output
    
- Any errors or confusion points
    

Only then we proceed.

