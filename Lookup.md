# 🧱 UNIT 1: Autonomy Foundations

*(Conceptual)*

## 📦 Module 1.1: Autonomy Spectrum

- Definition of autonomy in LLM systems  
- Freedom vs determinism  
- Human-driven vs agent-driven systems  

### Submodule 1.1.1: Code (Zero Autonomy)

- Deterministic rules  
- Explicit control flow  
- Rule explosion  
- Scalability limits  

### Submodule 1.1.2: Single LLM Call

- One-shot reasoning  
- Prompt-as-program  
- Prompt overload  
- No task decomposition  
- No recovery paths  

### Submodule 1.1.3: Chains

- Task decomposition  
- Sequential execution  
- Parallel chains  
- Fixed ordering  
- Specialist illusion  
- Rigid assembly-line behavior  

### Submodule 1.1.4: Routers

- LLM-based routing decisions  
- Conditional branching  
- Input classification  
- Tool / chain selection  
- No memory  
- No loops  

### Submodule 1.1.5: State Machines (Agents)

- Cycles and iteration  
- Refinement loops  
- LLM-influenced control flow  
- Human approval points  
- Multi-step decision making  

## 📦 Module 1.2: DAGs vs Cyclic Systems ✨

- One-directional execution vs looping execution  
- DAG constraints  
- Cyclic graph capabilities  

### Submodule 1.2.1: Directed Acyclic Graphs

- Chains as DAGs  
- Routers as DAGs  
- No backtracking  
- No revision paths  

### Submodule 1.2.2: Cyclic Graphs

- Loops  
- Backtracking  
- Time-travel semantics  
- Iterative improvement  
- Agent qualification criteria 🆕  

---

# 🧱 UNIT 2: Control

*(Conceptual)*

## 📦 Module 2.1: Control Loops

### Submodule 2.1.1: Ownership of Control

- Who owns repetition  
- Who decides next step  
- Why LLMs cannot self-govern  
- Proposal vs execution separation  

### Submodule 2.1.2: Exit Conditions

- Goal-satisfied exits  
- Budget-limited exits  
- Human escalation exits  
- Safety exits  
- Hard vs soft termination 🆕  

### Submodule 2.1.3: Human-in-the-Loop

- Authority vs input  
- Approval semantics  
- Rejection semantics  
- Resuming after intervention  
- Loop re-entry behavior 🆕  

## 📦 Module 2.2: State as a First-Class Citizen

### Submodule 2.2.1: What Is State

- State vs configuration  
- Mutable vs immutable data  
- Decision-relevant data only  
- State minimalism  

### Submodule 2.2.2: State Transitions & Invariants

- Allowed transitions  
- Forbidden transitions  
- Invariant enforcement  
- State corruption risks  
- Validation boundaries 🆕  

## 📦 Module 2.3: Tool Execution Boundaries

### Submodule 2.3.1: LLMs Suggest, Systems Execute

- Proposal vs execution  
- Tool invocation lifecycle  
- Side-effect ownership  
- Safety boundaries  
- Non-idempotent tool risks 🆕  

## 📦 Module 2.4: Agent Patterns as Control Strategies ✨

### Submodule 2.4.1: ReAct Pattern

- Think → Act → Observe loop  
- Tool-mediated reasoning  
- Observation feedback  
- Iterative reasoning cycles  

### Submodule 2.4.2: Reflexion Pattern

- Self-critique  
- Revision loops  
- Error-driven improvement  
- Separation of responder and reviser  

### Submodule 2.4.3: Multi-Agent Coordination

- Hierarchical agents  
- Head agent orchestration  
- Sub-agent delegation  
- Communication patterns  
- Coordination failure modes 🆕  

---

# 🧱 UNIT 3: State & Memory Patterns

*(Conceptual)*

## 📦 Module 3.1: Memory Is Not History

### Submodule 3.1.1: Ephemeral vs Persistent Memory

- Disposable context  
- Durable memory  
- Control relevance  
- Drift prevention  

### Submodule 3.1.2: Decision Memory vs Artifact Memory

- Commitments  
- Work products  
- Overwriting vs remembering  
- User intent preservation  

## 📦 Module 3.2: State Accumulation & Drift

### Submodule 3.2.1: Why Agents Go Off the Rails

- Accumulating failed attempts  
- Memory bias  
- Overconfidence loops  
- Stubborn behavior  

### Submodule 3.2.2: Memory Pruning & Checkpoints

- Forgetting vs archiving  
- Trusted checkpoints  
- Reset strategies  
- Resume safety  

## 📦 Module 3.3: Long-Running Processes

### Submodule 3.3.1: Resumability

- Pause and resume  
- Crash recovery  
- State completeness  
- Partial progress recovery  

### Submodule 3.3.2: Idempotence & Replay

- Safe retries  
- Replay without side effects  
- Deterministic recovery  
- Tool idempotence constraints 🆕  

## 📦 Module 3.4: Structured Outputs & Grounding ✨

### Submodule 3.4.1: Why Free-Text Is Unsafe

- Ambiguity  
- Downstream brittleness  
- Parsing failure modes  

### Submodule 3.4.2: Schema-Bound Outputs

- Output contracts  
- Typed responses  
- Schema enforcement  

### Submodule 3.4.3: Parsers as Enforcement

- Validation layers  
- Rejecting malformed outputs  
- Fail-fast behavior  

---

# 🧱 UNIT 4: LangGraph Foundations

*(Minimal implementation abstractions)*

## 📦 Module 4.0: Why LangGraph Exists ✨

- Limits of LangChain  
- Linear control flow bias  
- Hidden execution paths  
- Need for explicit graphs  

## 📦 Module 4.1: Graph Basics

### Submodule 4.1.1: Nodes as Pure Functions

- Input → output discipline  
- No side effects  
- Deterministic behavior  

### Submodule 4.1.2: Edges & Conditional Routing

- Static edges  
- Conditional edges  
- Control-driven branching  

### Submodule 4.1.3: Cycles & Loops

- Iterative graphs  
- Termination conditions  
- Infinite loop prevention  

## 📦 Module 4.2: State in LangGraph

### Submodule 4.2.1: State Schema Definition

- Typed state  
- Fixed schema  
- Minimal state design  

### Submodule 4.2.2: State Updates

- Write permissions  
- Partial updates  
- Invariant preservation  

### Submodule 4.2.3: Entry & Exit Points

- Start nodes  
- End nodes  
- Terminal states  

---

# 🧱 UNIT 5: Memory & Persistence

*(Practical)*

## 📦 Module 5.1: Checkpointing in Practice

- Checkpoint triggers  
- User approval boundaries  
- Safe resume points  

### Submodule 5.1.2: Resume & Recovery

- Restarting graphs  
- Crash recovery  
- Deterministic replay  

## 📦 Module 5.2: External Memory

### Submodule 5.2.1: Artifact Storage

- Draft storage  
- File handling  
- Version replacement  

### Submodule 5.2.2: Archived Context

- Cold storage  
- Retrieval on demand  
- Preventing drift  

## 📦 Module 5.3: Retrieval-Augmented Control ✨

### Submodule 5.3.1: Adaptive RAG

- Query reformulation  
- Feedback-driven retrieval  

### Submodule 5.3.2: Corrective RAG

- Error detection  
- Retrieval repair  

### Submodule 5.3.3: Self-RAG

- Self-evaluation  
- Retrieval gating  

---

# 🧱 UNIT 6: Human-in-the-Loop Systems

*(Production patterns)*

## 📦 Module 6.1: Human Interaction Nodes

- Waiting states  
- External input  
- Resume semantics  

### Submodule 6.1.2: Approval & Rejection

- Explicit approval  
- Explicit rejection  
- Authority boundaries  

## 📦 Module 6.2: Failure & Escalation Handling

### Submodule 6.2.1: Escalation Policies

- When to escalate  
- What to expose  
- What not to expose  

### Submodule 6.2.2: Recovery After Escalation

- Reframing tasks  
- Resetting budgets  
- Safe continuation  

---

# 🧱 UNIT 7: Capstone Agent

*(System integration)*

## 📦 Module 7.1: End-to-End Agent

- Problem framing  
- Constraints definition  
- Success criteria  

### Submodule 7.1.2: System Design

- Control flow design  
- State schema design  
- Failure paths  

### Submodule 7.1.3: Implementation

- Graph assembly  
- Tool integration  
- Human-in-the-loop wiring  

### Submodule 7.1.4: Evaluation & Hardening

- Failure testing  
- Drift testing  
- Recovery testing  

## 📦 Module 7.2: Observability & Tooling ✨

- Execution tracing  
- Debugging loops  
- Graph visualization  
- Studio tooling  
- Production inspection  
