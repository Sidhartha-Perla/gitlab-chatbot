---
layout: markdown_page
title: "Category Direction - AI Agents"
description: "Empower non-technical users to create advanced AI-Powered chat agents customized to customer's data"
---

## On this page
{:.no_toc}

- TOC
{:toc}

| | |
| --- | --- |
| Stage | [AI-powered](/direction/ai-powered/) |
| Group | [AI Framework](/direction/ai-powered/ai_framework/) |
| Maturity | [Planned](/direction/#maturity) |
| Content Last Reviewed | `2024-01-30` |

## Overview
The AI Agents category is focused on enabling non-technical users to easily create AI-Powered chatbots that can be embedded into customer's applications built with GitLab. It leverages the AI Abstraction layer built by the AI Framework group and exposes those technologies via a simple workflow making it fast and easy for customers to start building AI chatbots. 

## Goals 
AI Agents allow all types of users to manage the lifecycle of their agents within GitLab itself, decoupling agent development from application development and transforming agents effectively into libraries to be consumed by the application.

### Problems to solve
* Agents are often coupled to the application code, impacting negatively on the iteration velocity
* Application developers don't know if a new version of a prompt is actually better than a previous deployed one
* Agents often need to rely on external tools to source information to complete a task

## Definitions
- **Language model**: A language model is the engine that the agent will be run against. Users don't create nor control the creation of the language model, but might have a list of and configure access to new language models. Users interact with language models by sending queries to them through an API. The same agent will provide different answers when sent to different language models. Examples: 'gpt-4', 'claude-2.1'
- **Tool**: A tool is an external procedure to be run to enhance the knowledge of the agent, adding information that is not part of the agent prompt nor part of the training corpus of the language model. Tools are defined as a piece of code that needs to be run. Examples: 'perform sql query', 'perform json operation'
- **Prompts**: a system level direction to steer and influence the language model 
- **Agent**: A definition of a task for the agent model to perform. The agent is defined as a prompt, which can be enhanced through the use of tools, that interacts with a specific mode. Changing the prompt, tools or model will create a different version of the agent. Examples: 'Summarize this MR', 'Complete the following code: {code}'

## AI Agents Management Capabilities

### Agent Management
- Create, update and delete agents
- Navigate across versions of agents
- Fetch agents to be consumed by the application
- Manage access of an agent to different tools
- Test the agent within the UI against different models
- Compare results of different versions of the agent with offline metrics (predefined test cases) 
- Compare results of different versions of the agent with online metrics (usage metrics)
- Manage user read access to agents
- Manage user write access to agents

### Tool management
- Create, update and delete tools according to a specific definition
- Deploy an entity that process requests to run said tools, and return the results to the agent
- Manage user read access to tools
- Manage user write access to tools

### Language model Management
- Select models (OSS, proprietary, custom)
- Configure different deployments (apis, keys, etc)
- Run queries against different language models

### Prompt Management
- Prompt registry to version and iterate on prompts
- Possibly some way to test/evaluate prompts (performance, quality, efficacy) 
- Create, update, delete prompts

### Agent deployment
- Ability to embed AI Agents into customer applications, similar to youtube embed codes
- Ability to control what domains embeds are allowed on

*Last Reviewed: 2024-01-30  
Last Updated: 2024-01-30*
</p>