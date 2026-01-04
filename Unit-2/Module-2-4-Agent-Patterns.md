### 🧩 **Submodule 2.4.1: ReAct Pattern**

This is the **first named agent pattern** — and it’s foundational.

---

## 🟢 Mental Model (what ReAct really is)

ReAct is **not**:

- a clever prompt
    
- a reasoning trick
    
- an LLM behavior hack
    

ReAct is:

> **A control loop where reasoning is explicitly interleaved  
> with external actions and observations.**

Key idea:

> The agent does **not reason in isolation**.

It reasons **between actions**.

---

## 🔵 Why ReAct exists (what broke before)

Before ReAct, agents did this:

- Think everything upfront
    
- Decide a full plan
    
- Execute blindly
    

This failed because:

- the world changes
    
- tools fail
    
- assumptions are wrong
    
- plans become stale immediately
    

ReAct fixes this by:

> **Forcing the agent to look at reality after every action.**

---

## 🟣 Core Loop (structural, not prompt-level)

The canonical loop is:
```
THINK  →  ACT  →  OBSERVE 
↑                     │        │                     │
└─────────────────────┘
```

[reAct Examples](what-tf-is-reAct.md)

Important clarifications:

- **THINK**
    
    - internal reasoning
        
    - hypothesis formation
        
    - decision of next action
        
- **ACT**
    
    - proposal of a tool call
        
    - never direct execution
        
    - intent, not authority
        
- **OBSERVE**
    
    - system-provided result
        
    - external feedback
        
    - reality check
        

This loop repeats until an **exit condition** is met.

---

## 🧠 What makes ReAct a _control strategy_

ReAct enforces **three control properties**:

1. **Stepwise commitment**
    
    - no long unverified plans
        
2. **Observation gating**
    
    - reasoning must incorporate reality
        
3. **Bounded iteration**
    
    - loop count, budget, or success stops it
        

This directly connects to:

- Unit 2.1 (Control Loops)
    
- Unit 2.1.2 (Exit Conditions)
    
- Unit 2.3 (Tool Execution Boundaries)
    

---

## 🚫 Common misconceptions (important)

### ❌ “ReAct = reasoning + tools”

No.  
That’s superficial.

### ❌ “ReAct is autonomous”

No.  
The **system** still controls looping and execution.

### ❌ “ReAct removes the need for state”

Wrong.  
ReAct **depends** on state (observations accumulate).

---

## 🧪 How ReAct behaves in the wild

### Normal case

- tool works
    
- observation aligns with expectation
    
- reasoning converges
    

### Edge case

- tool returns unexpected output
    
- agent revises hypothesis
    
- different action proposed
    

### Failure mode

- agent loops on same failed action
    
- no learning from observation
    
- requires escalation or reflexion (next submodule)
    

This is why ReAct alone is **not sufficient**.

---

## 🛠️ Real-world usage patterns

ReAct is used in:

- search agents
    
- browsing agents
    
- RAG with tools
    
- diagnostic agents
    

Professionals misuse ReAct when:

- they let the LLM execute tools directly
    
- they don’t bound the loop
    
- they don’t validate observations
    

Experts exploit ReAct by:

- making observations structured
    
- enforcing budgets
    
- pairing it with Reflexion
    

---

## 🚧 MINI PROJECT (MANDATORY, PAPER ONLY)

### 🔨 Task: ReAct Control Sketch

On paper, design a ReAct agent for:

> “Find a reliable answer to a factual question using tools.”

You must include:

- a THINK step
    
- an ACT step
    
- an OBSERVE step
    
- **at least one explicit exit condition**
    

Do **not** write prompts.  
Draw boxes + arrows only.

### ✅ Proof of learning

You can explain:

- why observation changes reasoning
    
- who owns the loop
    
- when the agent must stop
    

⛔ Do **not** proceed until you reflect on this.


# 🧩 Submodule 2.4.2: **Reflexion Pattern**

This is **not** “LLM thinking harder”.  
This is **control separation** applied to self-improvement.

---

## 🟢 1. Mental Model (what Reflexion really is)

Reflexion is:

> **A controlled feedback loop where an agent evaluates its own output  
> using a different role than the one that produced it.**

Key idea:

> **The agent is not trusted to judge itself while acting.**

So we split roles.

---

## 🔵 2. Why Reflexion Exists (what broke before)

In plain ReAct:

- the same reasoning process
    
- proposes
    
- acts
    
- and _implicitly_ judges success
    

This fails because:

- the agent defends its own reasoning
    
- errors repeat with more confidence
    
- failures are rationalized, not fixed
    

Humans don’t do this.  
We:

- act
    
- then step back
    
- then critique
    

Reflexion encodes that **structurally**.

---

## 🟣 3. Core Building Blocks (parts of the machine)

Reflexion **always** has these components:

### 1️⃣ **Responder**

- Produces the output (draft, answer, plan)
    
- Optimized for generation
    
- Allowed to be wrong
    

### 2️⃣ **Reviser / Critic**

- Evaluates the responder’s output
    
- Looks for errors, gaps, violations
    
- Does _not_ generate final output
    

### 3️⃣ **Revision Loop**

- Applies critique to produce a new version
    
- Bounded by attempts or quality threshold
    

### 4️⃣ **Memory of Failure (Optional but common)**

- Stores _why_ something failed
    
- Not the reasoning — the **lesson**
    

This is a **role separation**, not a prompt trick.

Start 
   |
Responder <------------------| 
   |   (produces draft)              | 
   v                                          | 
Critic / Reviser                        |   
   |   (finds errors, gaps)          |    
   v                                          |
Check Quality                         | 
   | yes            | no                   | 
   |                  |                        | 
 End      Apply Revisions -----|

---

## 🧠 Separation of Roles (this is the crux)

The critical rule:

> **The same role must never both defend and judge the same output.**

If you violate this:

- Reflexion collapses into self-justification
    
- You get verbosity, not improvement
    

That’s why:

- responder ≠ reviser
    
- even if both are the same LLM under the hood
    

---

## 🧪 4. How Reflexion Behaves in the Wild

### Normal case

- responder produces output
    
- reviser identifies concrete issues
    
- next iteration improves measurably
    

### Edge case

- reviser flags ambiguous or subjective issues
    
- requires human escalation or clearer criteria
    

### Failure mode

- reviser gives vague feedback (“be clearer”)
    
- no actionable revision
    
- loop stagnates
    

This is why **revision criteria must be explicit**.

---

## 🛠️ 5. Real-World Usage Patterns

Reflexion is used in:

- code generation
    
- long-form writing
    
- planning tasks
    
- evaluation-heavy domains
    

Professionals misuse Reflexion when:

- they let the reviser rewrite everything
    
- they don’t bound revision loops
    
- they store full critique history in state
    

Experts exploit Reflexion by:

- enforcing checklists
    
- separating _error detection_ from _repair_
    
- storing only **lessons learned**, not full critiques
    

---

## 🔒 Critical Control Invariants

Write these down mentally:

1. **Revision is optional, critique is mandatory**
    
2. **Critique must be structured, not free-form**
    
3. **Only the latest artifact survives**
    
4. **Reflection does not own control — the system does**
    

Reflexion without control becomes infinite navel-gazing.

---

## 🚧 MINI PROJECT (MANDATORY — PAPER ONLY)

### 🔨 Task: Reflexion Control Sketch

Design a Reflexion agent for:

> “Improve a technical explanation until it meets quality criteria.”

Your sketch must include:

- a **Responder node**
    
- a **Reviser/Critic node**
    
- a **Revision loop**
    
- **one explicit stop condition**
    

Do **not** write prompts.  
Only boxes, arrows, and labels.