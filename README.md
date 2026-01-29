# Beast Mode Core Ontology

The core ontology for the Beast Mode ecosystem, defining how agents, capabilities, and tasks are explicitly modeled and validated using RDF and SHACL.

## Overview

Beast Mode is a declarative, ontology-first framework for modeling agents, what they are capable of, and the tasks those capabilities enable.

Rather than treating agents as opaque executors or relying on implicit inference, Beast Mode emphasizes **explicit structure**:

- Agents declare capabilities  
- Capabilities enable tasks  
- Tasks define clear inputs and outputs  
- Relationships are validated, not assumed  

This core ontology establishes the foundational vocabulary and constraints for the Beast Mode ecosystem. It is intentionally minimal, focusing on *what exists* and *how it may relate*, not on execution, orchestration, or runtime behavior.

The ontology is implemented in **Turtle (TTL)** with **SHACL (Shapes Constraint Language)** constraints, allowing systems to validate data correctness, completeness, and architectural intent before any execution layer is involved.

---

## Design Principles

The Beast Mode Core Ontology is guided by a small set of design principles:

- **Declarative over inferred**  
  All relationships are explicitly stated. Inference is a downstream concern.

- **Validation before execution**  
  SHACL constraints act as architectural guardrails, ensuring data correctness and intent alignment.

- **Separation of concerns**  
  This ontology defines structure and meaning only. Messaging, networking, and execution live elsewhere.

- **Composable, not monolithic**  
  The core ontology is designed to be extended by additional vocabularies and implementation layers.

---

## What This Ontology Is (and Is Not)

**This ontology is:**
- A semantic model for agents, capabilities, and tasks
- A shared vocabulary for aligning humans and systems
- A validation layer for architectural correctness

**This ontology is not:**
- An agent runtime
- A workflow engine
- An orchestration or scheduling system
- An execution framework

---

## Core Entities

### Agent
An autonomous or semi-autonomous actor in Beast Mode. Agents possess capabilities that enable them to perform various tasks.

**Required Properties:**
- `name` (string): Human-readable name
- `hasCapability` (Capability): At least one capability (one-to-many)

**Optional Properties:**
- `description` (string): Detailed description
- `id` (string): Unique identifier
- `version` (string): Version identifier
- `status` (string): Status (active, deprecated, draft, archived)
- `tags` (string): Tags or keywords
- `createdAt` (dateTime): Creation timestamp
- `updatedAt` (dateTime): Last update timestamp

---

### Capability
A bounded skill that an agent can perform. Capabilities serve as the bridge between agents and the tasks they can execute.

**Required Properties:**
- `name` (string): Human-readable name
- `enablesTask` (Task): At least one enabled task (one-to-many)

**Optional Properties:**
- `description` (string): Detailed description
- `id` (string): Unique identifier
- `version` (string): Version identifier
- `status` (string): Status (active, deprecated, draft, archived)
- `tags` (string): Tags or keywords
- `createdAt` (dateTime): Creation timestamp
- `updatedAt` (dateTime): Last update timestamp

---

### Task
A unit of work with a clear input and output. Tasks represent the atomic operations that agents can perform through their capabilities.

**Required Properties:**
- `name` (string): Human-readable name
- `hasInput` (string): Description of required input
- `hasOutput` (string): Description of produced output
- `requiresCapability` (Capability): Exactly one required capability

**Optional Properties:**
- `description` (string): Detailed description
- `id` (string): Unique identifier
- `version` (string): Version identifier
- `status` (string): Status (active, deprecated, draft, archived)
- `tags` (string): Tags or keywords
- `createdAt` (dateTime): Creation timestamp
- `updatedAt` (dateTime): Last update timestamp

---

## Relationships

- **Agent → Capability** (`hasCapability`): One-to-many  
- **Capability → Task** (`enablesTask`): One-to-many  
- **Task → Capability** (`requiresCapability`): Many-to-one (inverse of enablesTask)  
- **Agent → Task** (`performsTask`): Derived relationship through capabilities  

### Conceptual Structure
