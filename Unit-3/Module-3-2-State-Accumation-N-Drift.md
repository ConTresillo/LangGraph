### 🧩 **Submodule 3.2.1: Why Agents “Go Off the Rails”**

This is **the bug** behind 90% of bad agents.

---

## 🟢 Mental Model (plain English)

An agent **drifts** when:

> It keeps remembering things  
> that were never meant to matter again.

That’s it. No mystery.

---

## 🔵 What “state accumulation” actually means

State accumulation =  
**state growing over time without discipline**

Not in size only — in _meaning_.

The system starts carrying:

- old assumptions
    
- rejected ideas
    
- outdated interpretations
    
- failed attempts
    

Eventually, the agent is reasoning about a **fictional world**.

---

## 🧪 Concrete example (your exact scenario)

Let’s say the agent does this:

1. Draft v1 → rejected
    
2. Draft v2 → rejected
    
3. Draft v3 → user edits and clarifies intent
    

### ❌ Bad agent memory
```
- draft_v1: said X
- draft_v2: said Y
- user maybe wants X/Y?
```
Now the agent:

- hesitates
    
- contradicts itself
    
- argues with the user
    

This is **drift**.

### ✅ Correct memory discipline
```
- current_draft = draft_v3
- decision: previous attempts failed
- decision: user clarified intent
```
Old drafts are **dead**.  
They do not participate in future reasoning.

---

## 🔴 Where drift comes from (very specific)

Drift happens when you persist:

1. ❌ **Rejected artifacts**
    
2. ❌ **LLM reasoning**
    
3. ❌ **Tool paths**
    
4. ❌ **Intermediate interpretations**
    
5. ❌ **Unapproved inferences**
    

These _feel_ useful but are toxic long-term.

---

## 🟣 Why this breaks agents badly

Once drift starts:

- every new decision is biased
    
- the agent defends past mistakes
    
- “memory” feels like stubbornness
    

Users say:

> “Why do you keep going back to that?”

Because the system **never forgot**.

---

## 🔒 The invariant that prevents drift

Write this down. This is the rule.

> **State may only grow by decisions,  
> never by attempts.**

Attempts are disposable.  
Decisions are durable.

---

## 🛠️ How professionals prevent drift (no code)

They do **three things**:

1. **Overwrite artifacts**
    
    - Only one “current” draft exists
        
2. **Summarize failures**
    
    - “Attempt failed due to X” (one line)
        
3. **Freeze decisions**
    
    - Explicit user approvals are sacred
        

That’s it.

No fancy memory systems required.

---

## 🚧 MINI CHECK (answer mentally)

Which of these should survive **10 iterations**?

- ❓ “Draft #2 text”
    
- ❓ “User wants formal tone”
    
- ❓ “Tool call failed due to timeout”
    
- ❓ “Reasoning about why draft #1 was bad”

### ✅ The one that should survive 10 iterations

**“User wants formal tone”**

Why?

- It’s a **decision**
    
- It constrains future behavior
    
- Losing it breaks correctness
    
- Repeating it doesn’t cause drift
    

This is **decision memory**.

---

### ❌ The others should NOT survive

- **Draft #2 text** → rejected artifact
    
- **Tool call failed due to timeout** → transient event (maybe summarized once, then gone)
    
- **Reasoning about why draft #1 was bad** → ephemeral thinking
    

Keeping those causes:

- bias
    
- stubbornness
    
- “why are you bringing that up again?”
    

---

### One-line rule (final)

> **Persist user intent, not your attempts.**

### 🧩 **Submodule 3.2.2: Memory Pruning & Checkpoints**

This submodule exists because **perfect memory is a bug**.

---

## 🟢 Mental Model (very simple)

An agent must do **two opposite things well**:

1. **Remember what matters**
    
2. **Forget everything else**
    

Memory pruning and checkpoints are how you enforce that **on purpose**, not by accident.

---

## 🔵 Why this exists (real-world failure)

Agents fail when:

- memory only grows
    
- nothing ever gets deleted
    
- every iteration adds “just one more thing”
    

Eventually:

- reasoning slows
    
- bias compounds
    
- wrong assumptions become permanent
    
- restarting becomes the only fix
    

That’s not intelligence failure.  
That’s **memory hygiene failure**.

---

## 🟣 Memory Pruning (what it really means)

**Memory pruning** is:

> Deliberately deleting or overwriting state  
> that is no longer allowed to influence decisions.

Key word: **allowed**.

This is not “garbage collection”.  
This is **policy**.

---

### What SHOULD be pruned (aggressively)

❌ Old drafts  
❌ Failed attempts  
❌ Intermediate tool outputs  
❌ LLM reasoning  
❌ Temporary interpretations

These must **not survive loops**.

If they do → drift.

---

### What should NEVER be pruned automatically

✅ User-approved decisions  
✅ Explicit constraints  
✅ Control state (`cnt`, `status`)  
✅ Final artifacts

These are **authoritative**.

---

## 🧪 Concrete example (your system)

Each loop iteration should conceptually do this:
```
Before next iteration:
- overwrite draft
- discard old reasoning
- keep only:
    - current draft
    - decision summary
    - control state
```
If you don’t do this explicitly, the agent will not “figure it out”.

---

## 🟣 Checkpoints (the second half)

A **checkpoint** is:

> A trusted snapshot of state  
> that you can safely resume from.

Think of it as:

- “this is a known-good point”
    
- “everything before this is settled”
    

---

### Why checkpoints matter

They allow:

- pause & resume
    
- crash recovery
    
- human intervention
    
- safe rollback
    

Without checkpoints:

- long-running agents are fragile
    
- restarts lose intent
    
- bugs force full resets
    

---

## 🧪 Checkpoint vs memory (clear distinction)

- **Memory** → what the agent _uses_
    
- **Checkpoint** → what the system _trusts_
    

You may prune memory **between** checkpoints.  
You may **never** violate a checkpoint silently.

---

## 🔒 Critical invariant (write this)

> **Only checkpointed state may survive interruption.**

Everything else is optional.

---

## 🛠️ Professional pattern (no code)

Systems often do:

- Checkpoint on:
    
    - user approval
        
    - successful completion
        
    - escalation boundary
        
- Prune aggressively between checkpoints
    
- Resume only from checkpoints, never from “half-thoughts”
    

This is how:

- CI systems work
    
- distributed jobs work
    
- databases work
    

Agents are no different.

---

## 🚧 MINI PROJECT (MENTAL, IMPORTANT)

For your system, answer:

1. When is it safe to create a checkpoint?
    
2. What exact state must be in that checkpoint?
    
3. What state must **never** be checkpointed?
    

If you can answer this, you fully understand memory discipline.

---

## 🔑 Sentence to lock this forever

> **Good agents forget constantly,  
> but remember deliberately.**

### 1️⃣ When is it safe to create a checkpoint?

**Correct answer:**

- After a **user-approved decision**
    
- After a **goal is explicitly satisfied**
    
- At a **clean escalation boundary**
    

In other words:

> When you are confident  
> the system may resume from here  
> without reinterpreting the past.

Not “when user says so” blindly —  
but when **authority is established**.

---

### 2️⃣ What must be in a checkpoint?

**Minimum checkpoint = control truth**

Example:
```
status
cnt
max
current_draft
explicit user constraints
```

Checkpoint does **not** store:

- reasoning
    
- tool traces
    
- alternatives
    

Just enough to **resume correctly**.

---

### 3️⃣ What must never be checkpointed?

Now this should be clear:

❌ Intermediate reasoning  
❌ Failed attempts  
❌ Old drafts  
❌ Temporary interpretations

These may exist in **archive**, but never in a checkpoint.

Checkpoint = trust boundary.

---

## One sentence that unifies everything (very important)

> **State decides.  
> Archive explains.  
> Checkpoints resume.**

If you keep those three separate, you will never get lost.