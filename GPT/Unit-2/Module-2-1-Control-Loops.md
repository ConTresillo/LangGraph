## **🧩 Submodule 2.1.1 Who Owns the Loop?**

### 🟢 Mental Model (core idea)

A **loop** is simply:

> “Do something → check → repeat”

The _only_ question that matters is:

> **Who is allowed to decide whether the loop continues?**

There are only **two possible answers**.

---

### ❌ Case 1: The AI owns the loop (BAD)

Example in plain English:

> “Keep improving the answer until you think it’s good.”

Problems:

- “Good” is undefined
    
- Confidence ≠ correctness
    
- No upper bound
    
- No accountability
    

This is how agents:

- loop forever
    
- hallucinate confidence
    
- burn time/money
    

---

### ✅ Case 2: The SYSTEM owns the loop (GOOD)

Example:

> “Improve the answer **at most 3 times**.  
> If still unsatisfactory, stop and escalate.”

Here:

- The AI participates **inside** the loop
    
- The system controls **existence of the loop**
    

This single shift is the difference between:

- a demo
    
- a production system
    

---

## 🔵 Why this concept exists (real failure reason)

Early “agent” systems failed not because:

- LLMs were weak ❌
    
- prompts were bad ❌
    

They failed because:

> **No one was in charge of repetition.**

Humans assume:

- iteration magically converges  
    Engineering reality:
    
- iteration often oscillates or diverges
    

---

## 🟣 The 3 Non-Negotiable Parts of a Controlled Loop

Every safe loop must have **all three**:

### 1️⃣ A **Counter**

- Max attempts
    
- Max revisions
    
- Max tool calls
    

Written as:

> “No more than N times”

---

### 2️⃣ A **Progress Check**

Not “feels better”.

But something like:

- shorter than before
    
- fewer errors than before
    
- passed a checklist
    
- human approved
    

If you cannot define progress:  
👉 **you do not have a loop, you have hope**

---

### 3️⃣ A **Hard Stop**

A state where:

- the system **must exit**
    
- even if the task is unfinished
    

Examples:

- escalate to human
    
- return partial result
    
- fail safely
    

The AI is **never allowed** to override this.

---

## 🧪 Simple Paper Example (no tech)

Imagine designing this on paper:

`[Start]    ↓ [Draft]    ↓ [Evaluate]    ├─ acceptable → [Finish]    └─ not acceptable → [Revise]                         ↓                  (increment counter)                         ↓                  counter < 3 ?                    ├ yes → back to [Draft]                    └ no  → [Escalate to Human]`

That diagram alone already contains:

- control
    
- safety
    
- autonomy (bounded)
    

No code needed.

---

## 🛠️ Common Mistakes (important)

❌ “Until it’s good enough”  
❌ “Until the AI is confident”  
❌ “Let the agent decide”

All of these are **control failures**, not intelligence problems.

---

## 🚧 MINI PROJECT (MANDATORY, PAPER ONLY)

### 🔨 Task: **Design a Controlled Loop**

Pick **any one task**:

- writing
    
- researching
    
- reviewing
    
- planning
    

On paper, define **explicitly**:

1. What step repeats?
    
2. What never changes?
    
3. What is counted?
    
4. What proves progress?
    
5. What happens when the limit is hit?
    

You don’t need to show me the drawing.  
You just need to **be able to explain it**.

### 🧩 **Submodule 2.1.2: Exit Conditions**

> **Unit 2.1.1 answered:** _Who owns repetition?_  
> **Unit 2.1.2 answers:** _Why and when must the system stop?_

This is where most agent systems quietly fail.

---

## 🟢 Mental Model — _What an exit condition really is_

An **exit condition** is **not**:

- “Looks good”
    
- “The model is confident”
    
- “No more ideas”
    

An exit condition is:

> **An externally verifiable fact that ends the process.**

If a system cannot point to a _fact_ and say

> “Because this is true, we must stop”  
> then it doesn’t have an exit condition.

It has a _feeling_.

---

## 🔵 Why this exists (real failure)

Most runaway agents fail **even with counters** because:

- They stop for the **wrong reason**
    
- Or they never stop because the reason is subjective
    

Examples of bad exits:

- “Answer seems complete”
    
- “Quality improved”
    
- “No obvious errors”
    

These cannot be enforced by code or policy.

---

## 🟣 The Three Legitimate Exit Types

Every correct exit condition belongs to **one of these three**.

---

### 1️⃣ **Goal-Satisfied Exit**

> The original goal is demonstrably met.

Examples:

- All checklist items are satisfied
    
- Output passes validation rules
    
- Human explicitly approves
    

Key property:

- Binary (yes/no)
    
- Independent of model opinion
    

---

### 2️⃣ **Budget-Exhausted Exit**

> The system is no longer allowed to continue.

Examples:

- `cnt >= max`
    
- time limit reached
    
- cost limit reached
    

Key property:

- Mechanical
    
- Non-negotiable
    

This is the most important safety exit.

---

### 3️⃣ **Escalation Exit**

> The system admits it cannot proceed autonomously.

Examples:

- Human review required
    
- Partial result returned
    
- Task handed off
    

This is not failure.  
This is **designed humility**.

---

## 🚫 What is NOT an exit condition (critical)

❌ “The agent feels done”  
❌ “No more tools to try”  
❌ “The response is good enough”

These are **internal states**, not exits.

---

## 🧪 Paper Example (tight and clean)

`[Evaluate]`
   `↓`
`Is output valid?`
   `├─ yes → [SAVE & END]`
   `└─ no`
        `↓`
`Is cnt >= max?`
   `├─ yes → [ESCALATE]`
   `└─ no  → [REFINE]`

Notice:
- Evaluation does **not** decide looping
    
- Control logic does

## 🛠️ Common Exit Bugs (watch for these)

### ❌ Exit-by-Confidence

- Agent says “this is final”
    
- System believes it
    

### ❌ Exit-by-Exhaustion Only

- System always runs until max
    
- Never recognizes success early
    

### ❌ Exit-by-Silence

- Nothing explicitly ends
    
- Loop falls out accidentally
    

---

## 🚧 MINI PROJECT (PAPER ONLY)

### 🔨 Task: **Define Real Exit Conditions**

Using **your existing diagram**, do this:

1. Circle **every place** where the system can stop
    
2. Label each stop as:
    
    - Goal-satisfied
        
    - Budget-exhausted
        
    - Escalation
        
3. Remove any stop that depends on _judgment words_  
    (good, better, enough, confident)
    

If you can’t label a stop cleanly → it’s invalid.

---

## 🔒 One invariant to remember

> **Exit conditions must be enforceable by the system, not argued by the agent.**

Write that in your notebook. It’s foundational.

## 🧩 **Submodule 2.1.3: Human-in-the-Loop (Done Right)**

> Up to now, you learned **how systems loop and stop**.  
> Now we answer: **when (and how) humans are allowed to intervene**.

Most systems get this wrong.

---

## 🟢 Mental Model — what HITL really is

**Human-in-the-Loop is NOT:**

- “Ask a human whenever confused”
    
- “Let the human fix things”
    
- “Pause and wait for approval everywhere”
    

**Human-in-the-Loop IS:**

> A **controlled escalation mechanism** triggered by the system  
> when autonomy is no longer justified.

Humans are **not part of the loop**.  
They are **above the loop**.

---

## 🔵 Why this concept exists (real failures)

Systems without HITL:

- hallucinate confidently
    
- fail silently
    
- cause damage at scale
    

Systems with _bad_ HITL:

- stop too often
    
- depend on humans for trivial decisions
    
- lose all automation value
    

The goal is **precision**, not safety theater.

---

## 🟣 The Three Legitimate Reasons to Involve a Human

A human may be invoked **only** for one of these reasons.

---

### 1️⃣ **Authority Transfer**

> The system is not allowed to decide this.

Examples:

- Publishing content
    
- Approving irreversible actions
    
- Legal / ethical boundaries
    

Here:

- Human is the **final authority**
    
- The system must stop and wait
    

---

### 2️⃣ **Ambiguity Resolution**

> Multiple valid paths exist, and preference matters.

Examples:

- Tone choices
    
- Trade-offs
    
- Subjective judgments
    

Here:

- Human provides _direction_
    
- System continues execution afterward
    

---

### 3️⃣ **Failure Escalation**

> The system has exhausted safe autonomy.

Examples:

- Budget exhausted
    
- Repeated failure
    
- Conflicting signals
    

Here:

- Human helps **re-frame**
    
- System decides whether to continue
    

This is the case you designed — correctly.

---

## 🚫 What humans must NEVER do

This is critical.

Humans must NOT:

- Reset counters directly
    
- Override stop conditions
    
- Secretly “just allow one more loop”
    
- Modify control state ad-hoc
    

If they do, the system becomes:

- non-deterministic
    
- un-auditable
    
- impossible to debug
    

Humans advise.  
Systems decide.

---

## 🧪 Clean HITL Pattern (paper form)

Here is the **canonical structure**:

`[System detects boundary]`
        `↓`
`[Escalate to Human]`
        `↓`
`[Human provides input]`
        `↓`
`[System applies policy]`
        `↓`
`[Continue OR Terminate]`

Notice:
- Human never jumps back into the loop
    
- Control always returns to the system
    

---

## 🛠️ Common HITL Anti-Patterns (watch out)

### ❌ “Approval Everywhere”

- Humans approve every step
    
- No scalability
    

### ❌ “Human as Fix-It Button”

- System offloads responsibility
    
- No learning, no structure
    

### ❌ “Silent Override”

- Human secretly edits state
    
- Violates invariants
    

You avoided these — that’s good.

---

## 🔒 One non-negotiable invariant

> **Human input is data, not control.**

If you remember only one line from this submodule, make it this.

---

## 🚧 MINI PROJECT (MENTAL ONLY)

Using **your existing diagram**, answer:

1. Why is the human invoked _here_ and not earlier?
    
2. What exact question is the system asking the human?
    
3. What would happen if the human didn’t respond?
    
4. Could this HITL be removed safely in the future?
    

If you can answer these, your HITL design is correct.