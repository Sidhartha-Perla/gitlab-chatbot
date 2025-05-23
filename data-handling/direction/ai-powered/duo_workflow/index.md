---
layout: markdown_page
title: "Category Direction - GitLab Duo Workflow"
description: "Empower users with AI-assisted workflows to automate complex tasks and enhance productivity across the GitLab platform"
---

## On this page
{:.no_toc}

- TOC
{:toc}

| | |
| --- | --- |
| Stage | [AI-powered](/direction/ai-powered/) |
| Group | [Duo Workflow](/direction/ai-powered/duo_workflow/) |
| Maturity | [Planned](/direction/#maturity) |
| Content Last Reviewed | `2024-05-17` |

## Overview

Duo Workflow is the future of software development. It will be an autonomous AI agent aims to automate and streamline workflow execution across the entire SDLC, focusing on safe and efficient code execution, both locally and in CI pipelines. It will provide:

1. **Intelligent Task Execution**: Agents capable of understanding and executing complex tasks across GitLab projects.
2. **Adaptive Learning**: Continuous improvement based on user interactions and feedback.
3. **Seamless Integration**: Work harmoniously with existing GitLab features and third-party tools.

### Flexible Execution Environments
To cater to various user needs and security requirements, we plan to offer multiple execution modes:

1. **Local Executor**: For developers who prefer to run agents in their local environment.
2. **CI Executor**: For team-wide workflows triggered from the GitLab UI.
3. **Cloud Execution**: For users who prefer a fully managed solution.

### Intuitive UI

We're designing an intuitive interface that will allow users to:

1. Create and manage AI workflows easily.
2. Monitor agent activities in real-time.
3. Collaborate with AI agents on complex tasks.

### Robust Security

Security is paramount in AI agent interactions. We're implementing:

1. Sandboxed execution environments.
2. User confirmation for critical actions.
3. Comprehensive audit trails for all AI-generated activities.

## Roadmap

### Short-term Goals

- Implement core Duo Workflow Service and Executor components.
- Develop basic workflow creation and management UI.
- Establish secure communication channels between components.

### Medium-term Goals

- Expand the range of pre-built workflows and tools.
- Implement advanced features like workflow resumption and state management.
- Enhance integration with GitLab's existing features.

### Long-term Vision

- Develop advanced AI capabilities for complex problem-solving.
- Create an ecosystem for community-contributed workflows and tools.
- Seamlessly integrate AI agents into all aspects of the GitLab platform.

Stay tuned for updates as we progress on this exciting journey to bring advanced AI capabilities to GitLab!

### Iteration Plan

#### Phase 1: POC (Proof of Concept)

- **Goal:** Identify and address unknowns necessary for a production-grade product.
- **Focus:** Code-related use cases using multi-agent flows to address MR comments, create fixes based on issue links, resolve vulnerabilities, etc.
- **Definition of Done:** A working POC involving Duo chat that provides clear deliverables, such as auto-fixing MR comments.

#### Phase 2: MVP

- **Goal:** Ship an experiment to observe initial user reactions and engagement in a production setup.
- **Focus:** Introduce a use case for fixing failing tests or linting jobs as an experiment.
- **Definition of Done:** Deploy a workflow that executes code tasks such as- fix an MR, work base of an issue, fix failing tests or linting jobs, operable from GitLab web UI and IDE extensions, with sandboxed local execution, user command confirmation, documentation, and performance tracking.

#### Phase 3: SM Availability

- **Goal:** Ensure SM (Self-Managed) availability and establish CI (Continuous Integration) use cases.
- **Focus:** Collaborate with Cloud Connector for SM availability.
- **Definition of Done:** Complete Phase 2 objectives and ensure SM availability.

### Pricing and Packaging
We are currently not ready to share details about future pricing and packaging for GitLab Duo Chat.

*Last Reviewed: 2024-10-05  
Last Updated: 2024-10-05*
</p>