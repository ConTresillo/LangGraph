
---

## The 3-Question Test (this decides fake vs real state)

For **any proposed state field** or **any proposed node**, ask these **in order**.

### **Q1. If the process crashes right now, must this be restored for correctness?**

- ❌ No → **fake state**
    
- ✅ Yes → go to Q2
    

> “Correctness” = the next step behaves wrongly if this is missing.

---

### **Q2. Does this enable alternative future path?**

- ❌ No → **fake state**
    
- ✅ Yes → go to Q3
    

Alternative future means:

- different node
    
- different stop
    
- different loop
    
- different authority
    

---

### **Q3. Is this value _decided_ rather than _mechanically produced_?**

- ❌ No → **fake state**
    
- ✅ Yes → **real state**
    

Mechanical = input reading, printing, copying, formatting, I/O.

---

## If it fails ANY question → it’s fake

That’s the rule. No intuition needed.

---

## Apply the test to your exact confusions

### ❓ `current_prompt`

**Q1:** If we crash, must it be restored?  
→ Yes (you need the query)

**Q2:** Does it enable an alternative future?  
→ ❌ No (there is only one next step)

**Result:** ❌ **Fake state**  
(It’s just an input parameter, not a decision)

---

### ❓ `llm_result`

**Q1:** Must it be restored after crash?  
→ Yes

**Q2:** Does it affect what happens next?  
→ In Project 1.1: ❌ No  
→ In Project 1.2+: ✅ Yes

**Result:**

- Project 1.1 → **borderline / training-only**
    
- Project 1.2+ → **real state**
    

This explains why Project 1.1 feels weird — it’s scaffolding.

---

### ❓ `attempts`

**Q1:** Must it be restored?  
→ Yes

**Q2:** Does it enable different futures?  
→ Yes (continue vs stop)

**Q3:** Is it a decision?  
→ Yes (system-controlled policy)

**Result:** ✅ **Real state**

---

### ❓ `printed_output`

**Q1:** Must it be restored?  
→ ❌ No

**Result:** ❌ **Fake state**

---

## The “alternative future” test (the most important one)

Here’s the concrete trick you can use **on paper**.

For every node or state field, complete this sentence:

> “If this value were different, the system would ______.”

If you can only say:

- “print differently”
    
- “log differently”
    
- “format differently”
    

→ ❌ fake

If you can say:

- “stop instead of continue”
    
- “retry instead of accept”
    
- “escalate to human”
    
- “choose a different path”
    

→ ✅ real

---

## Why you feel there are “too many ways”

Because **graphs are not pipelines**.

Most beginners think:

> “Every step should be a node”

That’s wrong.

**Production graphs are sparse.**

A 20-step pipeline often becomes:

- 3 nodes
    
- 2 edges
    
- 1 loop
    

Everything else is **inside nodes** or **outside the graph**.

---

## How professionals design state schemas (steal this)

They do **failure-first design**, not feature-first.

### Step 1: List all ways the system can stop

- success
    
- failure
    
- escalation
    
- budget exhausted
    

### Step 2: Ask: _what must I know to justify each stop?_

Those answers become state fields.

### Step 3: Add the minimum input and output artifacts

That’s it.

No creativity required.

---

## Example: your Project 1.1 (final form)

**Stops:**

- END (always)
    

**Justification needed:**

- none
    

**State schema:**

```python
State = {
  "query": str,
  "decision": str,
  "explanation": str
}
```

Anything more would be fake.

---

## One brutal rule (write this down)

> **If removing a node or state field does not change the set of possible futures, it was fake.**

This rule never lies.

---

## Why this is hard (and why you’re doing well)

This is **systems thinking**, not coding.  
Most people never learn this and build fragile agents forever.

Your struggle means you’re exactly at the right depth.

---

## Next step (recommended)

I suggest we do **one of these** next:

1. You propose a state schema → I ruthlessly prune fake state
    
2. We extend Project 1.1 → Project 1.2 and watch _real_ state appear
    
3. We take a random “agent tutorial” and dissect why it’s fake
    

Tell me which.