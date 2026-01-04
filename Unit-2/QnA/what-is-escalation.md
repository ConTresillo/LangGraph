## Short, exact definition

> **Escalation is a controlled transfer of authority  
> from autonomous execution to an external decision-maker.**

That’s it.

Not error.  
Not failure.  
Not panic.

**Authority transfer.**

---

## What escalation is NOT ❌

- ❌ “Something went wrong”
    
- ❌ “The agent is confused”
    
- ❌ “Ask a human just in case”
    
- ❌ “Retry with more power”
    

Those are symptoms, not escalation.

---

## What escalation actually means

When a system escalates, it is saying:

> “Under current rules, I am **no longer allowed**  
> to continue autonomously.”

Key word: **allowed**, not **able**.

The system might _still be capable_ —  
but policy forbids it from proceeding.

---

## Why escalation exists (real reason)

Autonomous systems are bounded by:

- safety limits
    
- cost limits
    
- confidence limits
    
- ethical limits
    
- authority limits
    

Escalation exists to **respect those bounds**.

Without escalation:

- systems lie and continue
    
- or silently fail
    

With escalation:

- failure is visible
    
- responsibility is clear
    

---

## Escalation in your system (concrete)

In your design, escalation happens when:

- `cnt > max`
    
- repeated refinement failed
    
- budget is exhausted
    

At that point:
`state.status = ESCALATED`

Meaning:

- loop is frozen

- no further autonomous transitions allowed

- waiting for external input

That is escalation.

## What happens AFTER escalation (important)

Escalation **does not mean the task ends forever**.

It means:

1. Autonomous execution stops
    
2. External authority intervenes
    
3. New constraints or framing are introduced
    
4. System may resume under updated policy
    

This is why:

`ESCALATED → RUNNING`

is valid **only through human + policy checkpoint**.

---

## Types of escalation (mental taxonomy)

### 1️⃣ **Human escalation**

- Needs judgment
    
- Needs approval
    
- Needs re-framing
    

### 2️⃣ **System escalation**

- Hard stop
    
- Partial output
    
- Degraded mode
    

### 3️⃣ **Operational escalation**

- Kill switch
    
- Alert operator
    
- Abort job
    

All are escalation — different authorities.

---

## The invariant (write this down)

> **Escalation suspends autonomy until new authority is granted.**

That sentence alone prevents 80% of agent bugs.

---

## Final intuition check

If you ever ask:

> “Why didn’t the agent just continue?”

The answer should be:

> “Because escalation removed its authority.”

Not:

> “Because it couldn’t think.”