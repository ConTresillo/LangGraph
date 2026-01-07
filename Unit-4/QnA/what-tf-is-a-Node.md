Your confusion is valid. The short answer is:

> **A node does not “do work.” It computes _what should happen next_, not _making it happen_.**

Below is the precise, systems-level explanation.

---

## 1. What a Node _Actually_ Does

A LangGraph node is a **pure decision function over state**.

Formally and operationally:

```
node(state_snapshot) → {proposed_state_changes}
```

That is all.

No execution.  
No effects.  
No memory.  
No time.

It **reads** state and **derives information**.

---

## 2. What “Doing Work” Means (and Why Nodes Don’t)

Let’s separate two very different things that people conflate.

### ❌ “Doing work” (NOT a node’s job)

- Calling an LLM
    
- Making HTTP requests
    
- Writing files / DBs
    
- Logging for behavior
    
- Sending messages
    
- Mutating shared objects
    

These are **side effects**.

Side effects:

- Are not replayable
    
- Depend on time, order, environment
    
- Cannot be safely retried
    
- Break crash recovery
    

So nodes are **forbidden** from doing them.

---

### ✅ What a Node _Does Instead_

A node answers questions like:

- _What tool should be called next?_
    
- _Is the current state valid?_
    
- _Should we continue, stop, or escalate?_
    
- _What input should the LLM receive?_
    
- _What constraints apply now?_
    

It encodes **intent**, not execution.

Example (conceptual):

```text
Given:
  user_goal = "summarize document"
  document_loaded = true
  summary_exists = false

Derive:
  next_action = "call_summarizer"
```

The node does **not** call the summarizer.

---

## 3. Where LLM Calls Actually Belong

There are **two valid architectures**.

### Pattern A — LLM Outside the Node (Strict Purity)

```
[Node decides prompt] → [System calls LLM] → [State updated] → [Next node]
```

Node output:

```json
{
  "llm_prompt": "...",
  "llm_role": "summarizer"
}
```

The **graph runner / tool executor**:

- Reads this intent
    
- Executes the LLM call
    
- Stores the result back into state
    

This is the **cleanest** model.

---

### Pattern B — LLM Inside a Node (Allowed but Dangerous)

LangGraph _allows_ this, but:

- You lose replay safety
    
- Checkpointing becomes partial
    
- Determinism is broken unless heavily controlled
    

This is why advanced users **avoid it** unless:

- Using cached responses
    
- Treating LLM output as stochastic but acceptable
    
- Explicitly marking nodes as non-replayable
    

Your course is teaching the **correct foundation**, not the convenience path.

---

## 4. Concrete Mental Reframe

Think in these terms:

|You might think|Correct model|
|---|---|
|“Node executes something”|“Node proposes what should happen”|
|“Node performs actions”|“Node encodes decisions as data”|
|“Node runs tools”|“Node selects tools”|
|“Node changes the world”|“Node changes the state description”|

A node is closer to:

- A compiler pass
    
- A planner step
    
- A policy function
    
- A reducer in Redux
    
- A pure function in functional programming
    

---

## 5. One Precise Sentence (Memorize This)

> **A LangGraph node computes the next _meaningful difference in state_, not the effect that causes it.**

If you internalize this, the entire framework becomes obvious.

---

## 6. Why This Matters (Non-Negotiable)

If nodes “do stuff”:

- You cannot rewind
    
- You cannot replay
    
- You cannot test
    
- You cannot resume after failure
    
- You cannot explain behavior
    

If nodes only **decide**:

- The system becomes inspectable
    
- Failures become debuggable
    
- Weeks-long runs become replayable
    
- Human-in-the-loop becomes safe
    

This is not stylistic.  
It is **systems engineering**.

---

## 7. Next Step (Don’t Skip This)

Now that this is clear, your **mini-project should be trivial**:

- One node that **decides** an action
    
- One node that **validates** state
    
- No execution anywhere
    

If anything is _still_ unclear, say **exactly which sentence or assumption is breaking in your head**, and we’ll fix that before proceeding.