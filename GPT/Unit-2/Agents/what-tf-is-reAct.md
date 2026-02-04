
## 1️⃣ **Basic ReAct Loop (Single Tool)**

_Canonical architecture_
### ![[Pasted image 20260104232426.png]]
### Structure

- LLM reasons
    
- Proposes one tool
    
- System executes
    
- Observation feeds back
    
- Loop is bounded

### **Control facts**

- Loop owned by system
    
- Tool execution is external
    
- Observation is structured input
    
- Exit condition is explicit

## 2️⃣ **ReAct with Multiple Tools (Tool Selection)**

_Realistic production pattern_

### Structure

- LLM chooses _which_ tool
    
- Same Think → Act → Observe loop
    
- Tools are interchangeable
![[Pasted image 20260104233354.png]]
### **Control facts**

- Tool choice is a _proposal_
    
- Execution is centralized
    
- Observation normalizes tool outputs
    
- Prevents tool-specific reasoning leakage
    

---

## 3️⃣ **ReAct + Budget / Attempt Counter**

_Safety-aware loop_

### Structure

- Same ReAct loop
    
- Budget enforced outside the LLM
    
- Prevents infinite reasoning
![[Pasted image 20260104233547.png]]
### **Control facts**

- LLM does not know exact limits
    
- Counter is system-owned
    
- Escalation is deterministic
## 4️⃣ **ReAct + Human-in-the-Loop Escalation**

_Production-grade autonomy_

### Structure

- ReAct runs normally
    
- Failures trigger human node
    
- Human modifies state, not flow
![[Pasted image 20260104233642.png]]
### **Control facts**

- Human does **not** execute tools
    
- Human updates constraints/artifacts
    
- Control returns to system
    

---

## 5️⃣ **ReAct + Checkpointing (Resumable Agent)**

_Long-running agent design_

### Structure

- Checkpoints after observations
    
- Safe resume after crashes
![[Pasted image 20260104234723.png]]
### **Control facts**

- Only checkpointed state survives crashes
    
- No reasoning is checkpointed
    
- Replay is safe
    

---

## 6️⃣ **Anti-Pattern (What NOT to Do)**

_For clarity_
![[Pasted image 20260104234800.png]]flowchart TD
    Think --> Think
    Think --> Think
    Think --> ToolExec
    ToolExec --> End

### **Why this is bad**

- No observation feedback
    
- Tool result doesn’t influence reasoning
    
- Not ReAct — just delayed execution

## Key takeaway (lock this in)

> **ReAct is not a prompt pattern.  
> It is a control loop where reality interrupts reasoning.**