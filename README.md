# Beast Mode Core Ontology

A core ontology defining the fundamental entities and relationships in the Beast Mode system.

## Overview

Beast Mode is a system for modeling autonomous agents, their capabilities, and the tasks they can perform. This ontology provides the foundational structure for understanding how agents operate within the Beast Mode framework.

## Entities

### Agent
An autonomous or semi-autonomous actor in Beast Mode. Agents possess capabilities that enable them to perform various tasks.

**Properties:**
- `hasCapabilities`: Agents have one or more capabilities

### Capability
A bounded skill that an agent can perform. Capabilities serve as the bridge between agents and the tasks they can execute.

**Properties:**
- `enablesTasks`: Capabilities enable one or more tasks

### Task
A unit of work with a clear input and output. Tasks represent the atomic operations that agents can perform through their capabilities.

## Relationships

- **Agent → Capability** (`hasCapabilities`): One-to-many relationship
- **Capability → Task** (`enablesTasks`): One-to-many relationship
- **Agent → Task** (via Capability): Indirect relationship through capabilities

## Structure

```
Agent
  └── hasCapabilities → Capability
        └── enablesTasks → Task
```

## Files

- `beast_mode_core.md` - Core ontology definitions

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

[Add your license here]
