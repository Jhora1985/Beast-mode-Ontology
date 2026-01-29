# Beast Mode Core Ontology

The core ontology for the Beast Mode ecosystem, defining how agents, capabilities, and tasks are explicitly modeled and validated using RDF and SHACL.

## Overview

Beast Mode is a declarative, ontology-first framework for modeling agents, what they are capable of, and the tasks those capabilities enable.

Rather than treating agents as opaque executors or relying on implicit inference, Beast Mode emphasizes explicit structure:

- Agents declare capabilities
- Capabilities enable tasks
- Tasks define clear inputs and outputs
- Relationships are validated, not assumed

This core ontology establishes the foundational vocabulary and constraints for the Beast Mode ecosystem. It is intentionally minimal, focusing on what exists and how it may relate, not on execution, orchestration, or runtime behavior.

The ontology is implemented in Turtle (TTL) with SHACL (Shapes Constraint Language) constraints, allowing systems to validate data correctness, completeness, and architectural intent before any execution layer is involved.

## Design Principles

- Declarative over inferred  
  All relationships are explicitly stated. Inference is a downstream concern.

- Validation before execution  
  SHACL constraints act as architectural guardrails.

- Separation of concerns  
  This ontology defines structure and meaning only.

- Composable, not monolithic  
  The core ontology is designed to be extended.

## What This Ontology Is and Is Not

This ontology is:
- A semantic model for agents, capabilities, and tasks
- A shared vocabulary for aligning humans and systems
- A validation layer for architectural correctness

This ontology is not:
- An agent runtime
- A workflow engine
- An orchestration system
- An execution framework

## Core Entities

### Agent

An autonomous or semi-autonomous actor in Beast Mode. Agents possess capabilities that enable them to perform various tasks.

Required properties:
- name (string)
- hasCapability (Capability), one or more

Optional properties:
- description
- id
- version
- status
- tags
- createdAt
- updatedAt

### Capability

A bounded skill that an agent can perform. Capabilities serve as the bridge between agents and tasks.

Required properties:
- name (string)
- enablesTask (Task), one or more

Optional properties:
- description
- id
- version
- status
- tags
- createdAt
- updatedAt

### Task

A unit of work with a clear input and output.

Required properties:
- name (string)
- hasInput (string)
- hasOutput (string)
- requiresCapability (Capability), exactly one

Optional properties:
- description
- id
- version
- status
- tags
- createdAt
- updatedAt

## Relationships

- Agent to Capability: hasCapability (one to many)
- Capability to Task: enablesTask (one to many)
- Task to Capability: requiresCapability (many to one)
- Agent to Task: derived through capabilities

Conceptual structure:

Agent
  hasCapability -> Capability
    enablesTask -> Task
      requiresCapability -> Capability

## Files

- beast_mode_ontology.ttl
- beast_mode_examples.ttl
- beast_mode_core.md
- README.md

## Usage

Loading the ontology with Apache Jena:

riot --validate beast_mode_ontology.ttl

Loading with rdflib in Python:

from rdflib import Graph  
g = Graph()  
g.parse("beast_mode_ontology.ttl", format="turtle")

## SHACL Validation

The ontology includes SHACL shapes for validating:

- Node shapes for Agent, Capability, and Task
- Property and cardinality constraints
- Datatype validation
- Enumerated status values

## Example Instances

See beast_mode_examples.ttl for examples demonstrating the Agent to Capability to Task pattern.

## Extending the Ontology

To extend this ontology:

1. Add new classes or subclasses in separate modules
2. Define additional properties
3. Extend SHACL shapes for new constraints
4. Keep execution logic out of the core

## Contributing

Contributions are welcome. Please keep extensions explicit and modular.

## License

Add license information here
