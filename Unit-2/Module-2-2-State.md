## 🧩 Submodule 2.2.1

# **What Is State (Really)?**

No jargon. No libraries.

---

## 🟢 Mental Model

**State** is simply:

> Everything the system needs to know  
> **to make the next correct decision**.

If something matters later, it is **state**.  
If it doesn’t, it should not exist.

State is **not memory for memory’s sake**.

---

## 🔵 Why this exists (real failure)

Most “agent bugs” are actually:

- missing state
    
- unclear state
    
- corrupted state
    

Symptoms:

- loops that don’t converge
    
- repeated mistakes
    
- “why did it do that?”
    

If you can’t explain behavior using state,  
the system is already broken.

---

## 🟣 What Counts as State (Concrete)

In **your system**, valid state includes:

- `draft` (current output)
    
- `cnt` (attempt counter)
    
- `max` (budget)
    
- `evaluation_result` (acceptable / not)
    
- `human_feedback` (if any)
    
- `status` (running / escalated / done)
    

These are **facts**, not opinions.

---

## 🚫 What is NOT state (important)

❌ “The agent is confused”  
❌ “The model feels uncertain”  
❌ “Quality seems low”

Those must be turned into:

- flags
    
- scores
    
- categories
    
- decisions
    

State must be **inspectable**.

---

## 🧪 Simple State Snapshot (paper)

At any moment, you should be able to write:
`STATE {`
  `cnt = 2`
  `max = 3`
  `draft = "..."`
  `evaluation = NOT_ACCEPTABLE`
  `human_feedback = null`
  `status = RUNNING`
`}`

If you cannot write this:

- debugging is impossible
    
- graphs feel magical
    
- LangGraph feels confusing

## 🔒 One Golden Rule of State

> **State is owned by the system, not the agent.**

The agent may:

- read state
    
- suggest changes
    

The system decides:

- what is written
    
- when it is written
    

---

## 🛠️ Common State Design Mistakes

### ❌ Overloading state

- dumping raw logs
    
- storing entire histories unnecessarily
    

### ❌ Implicit state

- “we know we’re in revision phase”
    
- but nothing says so explicitly
    

### ❌ Mutable-by-everyone

- agent modifies anything
    
- humans patch things manually
    

You are already avoiding these.

---

## 🚧 MINI PROJECT (PAPER ONLY)

Using your existing diagram:

1. List **every piece of state** you implicitly used
    
2. Write them as a clean list
    
3. Cross out anything that:
    
    - isn’t needed for the next decision
        
    - isn’t inspectable
        

If you end with **5–8 items**, you’re doing it right.

# 🧱 UNIT 2: CONTROL

## 📦 Module 2.2 — State as a First-Class Citizen

### 🧩 **Submodule 2.2.2: State Transitions & Invariants**

If you understand this, **agents stop feeling mysterious**.

---

## 🟢 Mental Model — what transitions really are

A **state transition** is simply:

> A **legal change** from one state snapshot to another.

Not every change is allowed.  
Not every change makes sense.

The system must answer two questions **explicitly**:

1. **Who is allowed to change what?**
    
2. **Which changes are illegal no matter what?**
    

Those “never break” rules are called **invariants**.

---

## 🔵 Why this exists (real failure)

Most agent failures are not “LLM mistakes”.

They are:

- illegal state mutations
    
- silent corruption
    
- impossible transitions
    

Symptoms look like:

- counters going backwards
    
- skipping required steps
    
- agents “teleporting” states
    

Without invariants, **loops drift**.

---

## 🟣 State Transitions (clean definition)

A transition is valid only if:

- It starts from a **known state**
    
- It ends in a **known state**
    
- The change is **intentional**
    
- The change is **authorized**
    

Example (from your system):

`Before: 
`cnt = 1` 
`status = RUNNING`

`After:` 
`cnt = 2` 
`status = RUNNING`

Valid, because:

- cnt increment is allowed
    
- status unchanged
    

---

### ❌ Illegal transition example

`Before: 
`cnt = 3` 
`status = RUNNING`  

`After:` 
`cnt = 0` 
`status = RUNNING`

Why illegal?

- Counter reset without policy
    
- Breaks loop guarantee
    
- Hides budget exhaustion
    

This is exactly the smell you caught earlier.

---

## 🔒 Invariants — the rules that must NEVER break

An **invariant** is:

> A property of the state that must always be true.

If it’s violated, the system is **wrong**, not “confused”.

---

### Typical invariants in your design

Let’s make them explicit.

1️⃣ **Counter monotonicity**

`cnt must only increase (unless system explicitly resets it)`

2️⃣ **Bounded execution**

`cnt ≤ max OR status ≠ RUNNING`

3️⃣ **Terminal states are final**

`If status = DONE or ESCALATED → no further transitions allowed`

4️⃣ **Human does not mutate control**

`human_feedback may change cnt may not`

These are **design laws**, not suggestions.

---

## 🧪 Why invariants are powerful

Once invariants exist:

- bugs are obvious
    
- graphs are safe
    
- agents are predictable
    

Without them:

- everything “sort of works”
    
- nothing is reliable
    

Invariants are what make:

> “state machines”  
> instead of  
> “LLMs flailing with memory”

---

## 🛠️ How professionals use this (no code)

They literally write:

**Allowed transitions**

- RUNNING → RUNNING
    
- RUNNING → ESCALATED
    
- RUNNING → DONE
    

**Forbidden transitions**

- DONE → RUNNING
    
- ESCALATED → RUNNING
    
- RUNNING → RUNNING with cnt reset
    

This is **before** any implementation.

---

## 🚧 MINI PROJECT (PAPER ONLY)

Using **your existing system**, write:

### A. Three allowed transitions

(example: RUNNING → DONE)

### B. Three forbidden transitions

(example: DONE → RUNNING)

### C. Two invariants you promise never to violate

If you can do this:

- you fully understand state
    
- graphs will feel natural
    
- LangGraph will stop being scary
    

---

## 🔑 One sentence to lock everything

> **State transitions are not what can happen —  
> they are what is allowed to happen.**

---

## Where we are now

You have learned:

- loops
    
- exits
    
- HITL
    
- state
    
- invariants
    

This is the **entire control layer**.