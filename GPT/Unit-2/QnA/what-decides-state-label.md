This is the **right frustration** to have — and the fix is _not_ to add more state.  
It’s to **collapse state to the minimum surface area**.

Right now you’re labeling **state on every node**, which makes it feel like “too many params”.  
Let’s clean this **surgically**.

---

## The core mistake (very common, very fixable)

You’re treating **state labels as decorations on steps**.

That creates this feeling:

> “Everything is state → too many state params”

But the rule is:

> 🔑 **State is not per-node.  
> State is global and minimal.**

---

## The minimal state you actually need (for your entire diagram)

You only need **ONE state variable** for mode:

`state.status ∈ { RUNNING, ESCALATED, DONE }`

That’s it.

Not:

- running on init
    
- running on evaluate
    
- running on apply refinements
    

Those are **actions**, not states.

---

## The correct interpretation of your diagram

### All these nodes are the SAME state

- init
    
- make draft
    
- evaluate draft
    
- check cnt/max
    
- apply refinements
    
- save
    

All of them happen while:

`state.status = RUNNING`

You **do not annotate each one**.  
They inherit it implicitly.

---

### This single node is escalation

- Human gives suggestion
    

That node means:

`state.status = ESCALATED`

Nothing else runs while here.

---

### This single node is terminal

- End
    

That means:

`state.status = DONE`

No outgoing transitions.

---

## Why labeling “running” everywhere feels wrong

Because it **is** wrong 😄 — not conceptually, but visually.

Think of it like this:

- You don’t label every line of code with “program is running”
    
- You don’t label every instruction with “CPU is executing”
    

Same idea.

State is **context**, not annotation.

---

## The correct way to _think_ about state (this will calm everything)

### Layer 1 — State (very small)

`status cnt max draft human_feedback`

### Layer 2 — Process graph (what you drew)

Boxes and arrows.

The graph **reads and writes state**,  
but does **not redefine it per box**.

---

## Rewrite your diagram mentally like this

Instead of:

> “make draft — running”  
> “evaluate — running”  
> “apply refinements — running”

Think:

> “While RUNNING, the system executes these steps.”

That’s the whole shift.

---

## One sentence that fixes the overload

> **State is a condition the system is in,  
> not a label you attach to every action.**

If you remember that, the explosion disappears.

---

## Final reassurance (important)

- ❌ You are NOT overcomplicating
    
- ❌ You do NOT need more states
    
- ❌ You do NOT need more params
    
- ✅ You just crossed the line where people confuse _process_ with _state_
    

That’s a **good sign**, not a bad one.

---

## What to do next (simple instruction)

1. **Remove all “running” labels from individual nodes**
    
2. Keep only:
    
    - implicit RUNNING (default)
        
    - explicit ESCALATED (human)
        
    - explicit DONE (end)
        

Your diagram then becomes **clean and correct**.