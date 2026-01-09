## 🧩 Submodule 1.1.2 — Structured LLM Output

**MODE:** BUILD MODE  
**DIFFICULTY TIER:** 1 → 2 (small increase)

---

### 🟢 0. Syntax & Semantics Inventory (MANDATORY — NO BUILD)

Scope: **forcing the LLM to return a structured object and validating it**.

#### 1️⃣ `TypedDict` (or equivalent schema)

- **What it is:** Static schema for state / outputs
    
- **Represents:** Contract between LLM output and system
    
- **Why it exists:** Prevents ambiguous free-form text from leaking into control flow
    

**VALID**

```python
class State(TypedDict):
    user_input: str
    llm_output: str
```

```python
class Output(TypedDict):
    answer: str
```

```python
result: Output = {"answer": "hello"}
```

**INVALID / MISUSED**

```python
class Output: pass              # not a schema
```

```python
result = "hello"                # unstructured
```

```python
{"ans": "hi"}                   # key mismatch
```

---

#### 2️⃣ Prompt-enforced structure (LLM-side)

- **What it is:** Instruction to emit JSON-like output
    
- **Represents:** Soft contract with the model
    
- **Why it exists:** LLMs default to prose
    

**VALID**

```text
Respond ONLY as JSON with keys: answer
```

```text
Output format:
{"answer": "<string>"}
```

```text
Return a JSON object. No extra text.
```

**INVALID / MISUSED**

```text
Explain your answer
```

```text
Be conversational
```

```text
Return a paragraph
```

---

#### 3️⃣ Parsing structured output

- **What it is:** Converting model text → Python object
    
- **Represents:** Boundary between reasoning and system
    
- **Why it exists:** Text is not executable state
    

**VALID**

```python
import json
data = json.loads(text)
```

```python
answer = data["answer"]
```

```python
return {"llm_output": answer}
```

**INVALID / MISUSED**

```python
return {"llm_output": text}     # raw text assumed structured
```

```python
eval(text)                      # unsafe
```

```python
data.answer                     # dict misuse
```

---

### 🔑 1. Required Primitives to Act (OPERATIONAL)

- `TypedDict` schema
    
- LLM prompt that enforces structure
    
- JSON parsing
    
- Partial state return
    

---

### 🛠️ 2. Build Task (PRECISE)

**Objective**  
Modify your existing single-node LLM agent so that the LLM **must return structured JSON**, and the graph **stores only the parsed field**.

---

#### A. Input State (EXACT)

```python
{
  "user_input": "<string>",
  "llm_output": ""
}
```

---

#### B. LLM Behavior (MANDATORY)

The LLM **must be instructed** to return **only**:

```json
{
  "answer": "<string>"
}
```

No prose. No markdown. No extra keys.

---

#### C. Node Responsibilities

Inside the single node:

1. Read `state["user_input"]`
    
2. Send a prompt that **forces JSON output**
    
3. Receive the raw LLM text
    
4. Parse it using `json.loads`
    
5. Extract `"answer"`
    
6. Return **partial state only**:
    
    ```python
    {"llm_output": "<answer string>"}
    ```
    

---

#### D. Constraints (STRICT)

- ❌ Do NOT return raw LLM text
    
- ❌ Do NOT mutate state in-place
    
- ❌ Do NOT add nodes
    
- ❌ Do NOT add retries or fallbacks
    
- ❌ Do NOT handle errors yet
    

---

#### E. Success Criteria

Your build is correct if:

- `invoke()` runs without error
    
- The LLM output is valid JSON
    
- `llm_output` contains only the parsed string
    
- No prose leaks into state
    

---

### 🔍 3. Where It Breaks (ARTIFACT-BOUND)

Run it **as-is**, then report:

- JSON parsing failures (if any)
    
- Model disobedience
    
- Ambiguous outputs
    

Do **not** pre-fix.

---

### 🧠 4. Theory Injection (LOCKED)

⛔ Only unlocked after failures are observed.

---

### 🔁 5. Apply Back to the Build

⛔ Locked until Section 4.

---

### ⚖️ 6. Trade-offs Introduced

⛔ Locked until build exists.

---

## 🔒 CRUCIAL CONCEPT GATE

- **CRUCIAL:** Structured output as a system boundary
    
- **Mini-project:** ❌ Not required (single-node scope)
    

---

### ⏭️ NEXT ACTION

👉 **Implement the changes exactly.**  
Then reply with:

- updated node code
    
- one successful output
    
- one failure case (if it happened)
    

Only then we continue.