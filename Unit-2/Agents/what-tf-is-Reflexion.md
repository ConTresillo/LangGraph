## 1️⃣ **Basic Reflexion Loop (Single Artifact)**

_Canonical Reflexion architecture_
![[Pasted image 20260105000204.png]]
**Explanation**

- One responder produces the artifact.
    
- A separate critic evaluates it.
    
- Revisions loop back to the **same responder**.
    
- Loop is bounded by a quality gate.
    

**Key invariant**

- Responder never judges itself.
    
- Critic never generates final output.
    

---

## 2️⃣ **Reflexion with Explicit Error Memory**

_Error-driven improvement_

**Explanation**
![[Pasted image 20260105000250.png]]
- Critic produces **structured errors**, not prose.
    
- Only error summaries are stored (not reasoning).
    
- Error memory influences future revisions.
    

**Used when**

- Repeated mistakes matter.
    
- You want learning across iterations without drift.
## 3️⃣ **Checklist-Based Reflexion**

_Deterministic self-critique_
![[Pasted image 20260105000343.png]]
**Explanation**

- Critic evaluates against a fixed checklist.
    
- Prevents vague feedback like “be clearer”.
    
- Makes Reflexion predictable and auditable.
    

**Professional pattern**

- Common in code review, compliance, safety checks.
## 4️⃣ **Reflexion + Budget / Attempt Limit**

_Prevents infinite self-critique_
![[Pasted image 20260105000400.png]]
**Explanation**

- System enforces revision limits.
    
- Reflexion cannot loop indefinitely.
    
- Escalation occurs when improvement stalls.
    

**Key point**

- Control stays outside the LLM.
## 5️⃣ **Reflexion + Human-in-the-Loop**

_Authority-aware improvement_
![[Pasted image 20260105000426.png]]
**Explanation**

- Human intervenes only after Reflexion fails.
    
- Human updates **constraints**, not the artifact directly.
    
- Reflexion resumes under new authority.
    

**Important**

- Human is not a “super critic”.
    
- Human resets context, not control logic.

## 6️⃣ **ANTI-PATTERN: Self-Judging Agent (Do NOT do this)**
![[Pasted image 20260105000445.png]]
```
flowchart TD
    Responder --> Responder
    Responder --> Responder
    Responder --> End
```
    
**Why this fails**

- Same role generates and evaluates.
    
- Leads to rationalization, verbosity, confidence inflation.
    
- Looks “smart” but does not improve.
    

**Smell**

- “The model will reflect on its own answer.”
    

---

## Core takeaway (lock this in)

> **Reflexion is not thinking harder.  
> It is separating generation from judgment under system control.**