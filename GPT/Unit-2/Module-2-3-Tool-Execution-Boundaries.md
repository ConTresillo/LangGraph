## 📦 Module 2.3 — **Tool Execution Boundaries**

> This module answers one question:  
> **Who is allowed to act on the world?**

Most agent bugs live here.

## 🧩 Submodule 2.3.1

# **LLMs Suggest. Systems Execute.**

This is a **hard boundary**, not a guideline.

---

## 🟢 Mental Model

An LLM is **not an actor**.  
It is a **proposer**.

It can:

- reason
    
- plan
    
- suggest
    
- describe actions
    

It must **never**:

- execute actions
    
- mutate control state
    
- call tools directly
    
- decide side effects
    

All real-world effects happen **outside** the LLM.

---

## 🔵 Why this boundary exists (real failures)

When LLMs are allowed to:

- execute tools directly
    
- write files freely
    
- call APIs autonomously
    

You get:

- repeated destructive actions
    
- infinite tool loops
    
- irreversible side effects
    
- security disasters
    

This is why ReAct was designed the way it was.

---

## 🟣 The Correct Execution Pattern (conceptual)

Every tool interaction must follow this shape:

```
LLM → proposes action + arguments
SYSTEM → validates proposal
SYSTEM → executes tool
SYSTEM → observes result
SYSTEM → updates state
```
The LLM is **never in the middle** of this chain.

---

## 🚫 What the LLM must NEVER do

❌ “I will now save the file”  
❌ “Calling the API…”  
❌ “Executing search…”

These are **lies** unless the system confirms them.

The LLM should only say:

> “I propose calling X with Y.”

---

## 🧪 Example (plain English)

### ❌ Bad

> “I saved the file successfully.”

No it didn’t.

---

### ✅ Good

> “The next step would be to save the file at location X.”

Then the **system** decides whether that happens.

---

## 🔒 One critical invariant

> **The LLM may describe intent.  
> Only the system may cause effects.**

If you violate this:

- control collapses
    
- safety collapses
    
- debugging becomes impossible
    

---

## 🛠️ How this fits YOUR design

In your diagram:

- `make draft` → LLM work (pure computation)
    
- `evaluate` → LLM or rule-based judgment
    
- `apply refinements` → LLM proposes edits
    
- `save` → **SYSTEM action**
    
- `reset cntr` → **SYSTEM action**
    
- `check cntr/max` → **SYSTEM action**
    

Notice:

- LLM never touches `cnt`
    
- LLM never decides save
    
- LLM never decides escalation
    

You already did this correctly — intuitively.

---

## 🧪 Subtle but important distinction

There are **two kinds of “tools”**:

### 1️⃣ **Pure tools** (safe)

- text transform
    
- summarization
    
- rewriting
    
- classification
    

These can be LLM-internal.

---

### 2️⃣ **Effectful tools** (dangerous)

- file I/O
    
- APIs
    
- network
    
- databases
    
- payments
    
- emails
    

These must always be:

- proposed by LLM
    
- executed by system
    

Never merged.

---

## 🚧 MINI PROJECT (MENTAL ONLY)

Take your system and answer:

1. Which steps are **pure computation**?
    
2. Which steps cause **external effects**?
    
3. Which steps must be **system-owned** no matter what?
    
4. What would break if the LLM executed tools directly?
    

If you can answer this, you fully understand Module 2.3.

---

## 🔑 One-sentence lock-in

> **Autonomy is allowed in reasoning,  
> never in execution.**

Write that down. It’s non-negotiable.


