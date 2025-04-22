---
layout: markdown_page
title: "Category Direction - AI Gateway"
description: "Empower users to access to AI features regardless of their instance type"
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


## AI Gateway

The AI Gateway is a standalone service that provides access to AI features for all GitLab users, regardless of their instance type (self-managed, dedicated, or GitLab.com). It acts as an API Gateway, handling traffic from cloud.gitlab.com/ai/* and directing it to AI providers and their models.

### Key Features

- Centralized access point for AI features
- Scalable and stateless service
- Enables self-managed installations to access AI features without hosting their own models
- Written in Python for ease of use by data and ML engineers

### Future Plans

- Multi-region deployment (currently under consideration)
- Direct connections from clients (tracked in an epic)
- Support for the last 2 major GitLab versions

### API and Protocol

- JSON-based API with single-purpose endpoints
- Version-agnostic design for cross-version compatibility
- Uses a simple JSON envelope for transporting feature-specific information

### Authentication & Authorization

- GitLab provides the first layer of authorization
- AI Gateway accessed through Cloud Connector for instance authentication
- Plans for end-user authentication support

### Deployment

- Currently deployed from the project repository in gitlab-org/modelops/applied-ml/code-suggestions/ai-assist
- Future plans to deploy using Runway with production and staging environments

## Future Work

1. Centralized Access Through AI Gateway
2. Unit Primitives
   - Initial support for Code Suggestions and Chat
   - Future decomposition of Chat into multiple primitives
3. Self Managed AI Gateway
   - Option for self-managed instances to use GitLab-hosted AI Gateway or deploy their own

## Related Components

- AI Agents: For creating and managing agents and prompts
- Model Registry: For managing and deploying machine learning models

*Last Reviewed: 2024-06-28  
Last Updated: 2024-06-28*
</p>