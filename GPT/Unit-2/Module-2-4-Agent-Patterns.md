# 🧩 **Submodule 2.4.1: ReAct Pattern**

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

# 🧩 Submodule 2.4.2: **Plan-and-Execute Pattern**

---

## 🟢 1. Mental Model (What it really is)

Plan-and-Execute is a **two-phase control strategy**:

> **First decide _what_ to do (plan),  
> then decide _how_ to do it (execute).**

Key separation:

- **Planning** reasons globally (future-oriented)
    
- **Execution** acts locally (step-by-step)
    

The plan is **not control**.  
The system still owns control.

---

## 🔵 2. Why This Exists (What broke before)

Pure ReAct fails when:

- tasks require multiple dependent steps
    
- success depends on order
    
- local reasoning misses global structure
    

Without a plan:

- the agent thrashes
    
- repeats work
    
- changes direction mid-way
    
- optimizes locally but fails globally
    

Plan-and-Execute exists to:

- introduce **temporal structure**
    
- reduce short-sighted decisions
    
- make progress measurable
    

---

## 🟣 3. Core Building Blocks (Parts of the machine)

### 1️⃣ Planner

- Produces a **high-level plan**
    
- Thinks in milestones, not actions
    
- Optimized for structure, not correctness
    

### 2️⃣ Plan Artifact

- Explicit representation of steps
    
- Treated as **data**, not authority
    
- Can be revised or discarded
    

### 3️⃣ Executor

- Executes steps one by one
    
- Often uses ReAct internally
    
- Reports progress and failures
    

### 4️⃣ Control Gate

- Decides whether to:
    
    - continue execution
        
    - replan
        
    - escalate
        
    - stop
        

---

## 🧠 4. How It Behaves in the Wild

### Normal case

- plan is roughly correct
    
- execution proceeds stepwise
    
- minor deviations handled locally
    

### Edge case

- environment changes
    
- a step becomes invalid
    
- partial replanning is needed
    

### Failure mode

- plan is treated as rigid truth
    
- executor follows a bad plan blindly
    
- errors compound instead of triggering replanning
    

This is the **classic Plan-and-Execute failure**.

---

## 🛠️ 5. Real-World Usage Patterns

Plan-and-Execute is used in:

- task automation
    
- multi-step workflows
    
- research pipelines
    
- code generation with dependencies
    

Professionals misuse it when:

- they trust the initial plan too much
    
- they never replan
    
- they store the plan as state authority
    

Experts exploit it by:

- treating plans as **hypotheses**
    
- allowing partial replans
    
- combining it with ReAct for execution
    

---

## 🔒 Critical Invariants (Non-negotiable)

- **Plans do not own control**
    
- **Plans can be wrong**
    
- **Execution must be interruptible**
    
- **Replanning is a feature, not a failure**
    

Break these and the agent becomes brittle

# 🧩 Submodule 2.4.3: **RAG (Retrieval-Augmented Generation) Pattern**

---

## 🟢 1. Mental Model (What it really is)

RAG is **not memory** and not “search glued to an LLM”.

RAG is:

> **A control strategy where an agent deliberately fetches external evidence  
> to inform a decision, without mutating long-term state.**

Key idea:

- Retrieval **informs** the current step
    
- It does **not** become persistent truth
    

RAG answers:

> “What do I need to look up _right now_ to decide correctly?”

---

## 🔵 2. Why This Exists (What broke before)

Without RAG:

- agents hallucinate confidently
    
- stale knowledge is treated as fact
    
- long contexts overflow
    
- memory is abused as knowledge
    

Pure prompting fails because:

- the model’s training data is static
    
- context windows are limited
    
- “remembering everything” causes drift
    

RAG exists to:

- externalize knowledge
    
- bound context
    
- make ignorance explicit
    
- separate **knowing** from **deciding**
    

---

## 🟣 3. Core Building Blocks (Parts of the machine)

### 1️⃣ Retriever

- Queries an external knowledge source
    
- Can be search, vector DB, API, docs
    
- Returns **candidates**, not answers
    

### 2️⃣ Retrieval Query

- Formulated deliberately
    
- A control decision, not a reflex
    
- Poor queries = poor outcomes
    

### 3️⃣ Retrieved Context

- Injected into the current reasoning step
    
- Ephemeral by default
    
- Scoped to the decision at hand
    

### 4️⃣ Control Policy

- Decides:
    
    - when to retrieve
        
    - how much to retrieve
        
    - whether to retry or proceed
        

---

## 🧠 4. How It Behaves in the Wild

### Normal case

- agent detects missing knowledge
    
- retrieves relevant context
    
- uses it once
    
- proceeds
    

### Edge case

- retrieved info is noisy or conflicting
    
- agent must weigh evidence
    
- may retrieve again or escalate
    

### Failure modes

- over-retrieval (context overload)
    
- stale retrieval treated as fact
    
- retrieval results silently persisted as memory
    

These failures cause **false confidence**.

---

## 🛠️ 5. Real-World Usage Patterns

RAG is used in:

- QA over documents
    
- enterprise copilots
    
- research assistants
    
- codebase navigation
    

Professionals misuse RAG when:

- they dump retrieval into long-term memory
    
- they retrieve on every step blindly
    
- they trust top-k results as truth
    

Experts exploit RAG by:

- retrieving only when uncertainty is detected
    
- keeping retrieval ephemeral
    
- separating **evidence** from **decisions**
    

---

## 🔒 Critical Invariants (Non-negotiable)

- **Retrieval is not memory**
    
- **Retrieved context is disposable**
    
- **User approval is required to persist facts**
    
- **Control decides when to retrieve, not the LLM**
    

Break these and the agent becomes hallucination-prone.

---

## 🚧 MINI PROJECT (MANDATORY — PAPER ONLY)

### 🔨 Task: RAG Control Sketch

Design an agent that:

> Answers questions using external documents.

Your sketch must include:

- a **decision point** for retrieval
    
- a **retrieval step**
    
- a **single-use context injection**
    
- an explicit **non-retrieval path**
    

No prompts.  
Only boxes, arrows, and labels.

---

## 🧠 Reflection Question (one sentence)

> Why must retrieved information not automatically become long-term memory?
# 🧩 Submodule 2.4.4: **Reflexion Pattern**

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

# 🧩 Submodule 2.4.5: **Self-Routing / Role-Switching Agent**

---

## 🟢 1. Mental Model (What it really is)

A Self-Routing agent is:

> **A single agent that dynamically switches roles  
> based on context, without spawning new agents.**

Key idea:

- There is **one identity**
    
- Multiple **modes of behavior**
    
- Control decides **which role is active**
    

This is **not multi-agent**.  
It is **role multiplexing inside one control loop**.

---

## 🔵 2. Why This Exists (What broke before)

Single-role agents fail when:

- tasks require different cognitive modes
    
- one behavior dominates incorrectly
    
- reasoning style does not fit the situation
    

Examples:

- creative writing vs factual answering
    
- planning vs execution
    
- critique vs generation
    

Without role-switching:

- agents become inconsistent
    
- prompts grow bloated
    
- logic becomes tangled
    

Self-Routing exists to:

- separate concerns
    
- keep roles clean
    
- avoid premature multi-agent complexity
    

---

## 🟣 3. Core Building Blocks (Parts of the machine)

### 1️⃣ Role Definitions

- Explicit behavioral modes
    
- Each role has a clear purpose
    
- Roles are **mutually exclusive at runtime**
    

### 2️⃣ Router / Dispatcher

- Decides which role to activate
    
- Uses state, signals, or context
    
- Owns the routing decision
    

### 3️⃣ Active Role Executor

- Executes behavior for the chosen role
    
- Does not question role selection
    
- Focused on doing one thing well
    

### 4️⃣ Role Transition Rules

- Define when switching is allowed
    
- Prevent oscillation or leakage
    
- Enforce clean boundaries
    

---

## 🧠 4. How It Behaves in the Wild

### Normal case

- agent identifies task context
    
- activates appropriate role
    
- performs action
    
- switches roles when needed
    

### Edge case

- ambiguous context
    
- multiple roles seem applicable
    
- routing decision becomes unstable
    

### Failure modes

- role confusion (two roles mixed)
    
- rapid oscillation between roles
    
- roles leaking assumptions into each other
    

These failures degrade clarity and control.

---

## 🛠️ 5. Real-World Usage Patterns

Self-Routing is used in:

- assistants with “modes”
    
- systems that alternate between planning and acting
    
- tools that switch between explanation and execution
    

Professionals misuse it when:

- roles are implicit, not defined
    
- routing logic is buried in prompts
    
- the agent decides roles ad hoc
    

Experts exploit it by:

- defining roles explicitly
    
- centralizing routing logic
    
- keeping role behaviors minimal and pure
    

---

## 🔒 Critical Invariants (Non-negotiable)

- **Only one role is active at a time**
    
- **Routing is a control decision**
    
- **Roles must not self-select**
    
- **Role switching must be explicit**
    

Break these and the agent becomes incoherent.

---

## 🚧 MINI PROJECT (MANDATORY — PAPER ONLY)

### 🔨 Task: Self-Routing Control Sketch

Design an agent that:

> Switches between planning, execution, and critique roles.

Your sketch must include:

- at least **three roles**
    
- an explicit **routing decision**
    
- at least **one role transition rule**
    
- a clear **exit condition**
    

No prompts.  
Only boxes, arrows, and labels.

---

## 🧠 Reflection Question (one sentence)

> Why is self-routing safer than prompt-based role mixing?

# 🧩 Submodule 2.4.6: **Multi-Agent Coordination**

---

## 🟢 1. Mental Model (What it really is)

Multi-Agent Coordination is:

> **A control strategy where multiple agents operate under explicit  
> authority and communication rules to achieve a shared goal.**

Key idea:

- Intelligence is **distributed**
    
- Control must be **explicit**
    
- Coordination is a **systems problem**, not a reasoning problem
    

This is not “many agents chatting”.  
It is **orchestrated autonomy**.

---

## 🔵 2. Why This Exists (What broke before)

Single-agent systems fail when:

- tasks exceed one cognitive mode
    
- parallel work is required
    
- responsibilities conflict
    
- context becomes too large
    

Without coordination:

- agents duplicate work
    
- contradict each other
    
- deadlock or race
    
- amplify errors instead of correcting them
    

Multi-Agent systems exist to:

- decompose responsibility
    
- enable parallelism
    
- isolate failures
    
- scale complexity safely
    

---

## 🟣 3. Core Building Blocks (Parts of the machine)

### 1️⃣ Head / Orchestrator Agent

- Owns global goal
    
- Assigns tasks
    
- Collects results
    
- Makes final decisions
    

### 2️⃣ Sub-Agents

- Specialized roles or capabilities
    
- Operate within bounded scopes
    
- Do **not** own global control
    

### 3️⃣ Communication Channel

- Structured message passing
    
- Explicit inputs and outputs
    
- No shared hidden state
    

### 4️⃣ Coordination Policy

- Defines:
    
    - who can talk to whom
        
    - when delegation occurs
        
    - how conflicts are resolved
        

---

## 🧠 4. How It Behaves in the Wild

### Normal case

- head agent decomposes task
    
- sub-agents work independently
    
- results are aggregated
    
- head agent decides next step
    

### Edge case

- sub-agents disagree
    
- partial results conflict
    
- orchestrator must arbitrate
    

### Failure modes

- unclear authority (agents override each other)
    
- uncontrolled communication (message explosion)
    
- circular delegation
    
- hidden shared state causing inconsistency
    

These failures are **coordination failures**, not model failures.

---

## 🛠️ 5. Real-World Usage Patterns

Multi-Agent Coordination is used in:

- research assistants
    
- code analysis systems
    
- planning + execution separation
    
- large task decomposition
    

Professionals misuse it when:

- they add agents instead of fixing control
    
- agents communicate freely without structure
    
- the head agent abdicates authority
    

Experts exploit it by:

- keeping the head agent simple
    
- strictly bounding sub-agent scope
    
- treating communication as data contracts
    

---

## 🔒 Critical Invariants (Non-negotiable)

- **There must be a single authority for final decisions**
    
- **Sub-agents must not coordinate implicitly**
    
- **All communication must be explicit**
    
- **More agents ≠ better performance**
    

Violating these leads to chaos, not intelligence.

---

## 🚧 MINI PROJECT (MANDATORY — PAPER ONLY)

### 🔨 Task: Multi-Agent Control Sketch

Design a system where:

> A head agent delegates research, evaluation, and synthesis to sub-agents.

Your sketch must include:

- one **head agent**
    
- at least **two sub-agents**
    
- explicit **communication paths**
    
- one **coordination failure case**
    

No prompts.  
Only boxes, arrows, and labels.

---

## 🧠 Reflection Question (one sentence)

> Why is authority more important than intelligence in multi-agent systems?