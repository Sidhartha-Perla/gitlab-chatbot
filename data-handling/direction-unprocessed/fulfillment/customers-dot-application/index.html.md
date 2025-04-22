---
layout: markdown_page
title: "Category Direction - CustomersDot and Quote to Cash integrations"
description: "The CustomersDot Application and underlying Quote to cash integrations strategy page belongs to the Fulfillment Platform group of the Fulfillment section."
---

## On this page
{:.no_toc .hidden-md .hidden-lg}

- TOC
{:toc}

<link rel="stylesheet" type="text/css" href="/stylesheets/biztech.css" />

 **Last updated**: 2024-05-10

## Mission

> Within the category of the CustomersDot and quote to cash (QTC) integrations the mission is to provide robust billing infrastructure and ensure it is scalable as our business evolves. This initiative centers on building a foundation and optimizing the QTC orchestration with the customersDot application. By strengthening these critical components, contributors will gain the confidence and efficiency needed to deliver enhancements to the CustomersDot application swiftly and reliably. This strategic effort will also enable data integrity and governance, compliance, and reliability while also promoting seamless collaboration and innovation within the Fulfillment section at GitLab.

## Overview

Within [CustomersDot](https://gitlab.com/gitlab-org/customers-gitlab-com/) our customers and all relevant stakeholders are able to manage billing accounts, subscriptions, add-ons and licenses.

[CustomersDot](https://gitlab.com/gitlab-org/customers-gitlab-com/) is the central application to contribute for the Fulfillment Platform group.

The Fulfillment Platform group is responsible for the following areas of CustomersDot:

- Authentication system 
- Integration with Zuora, Salesforce ,and Channel partner eMarketplace solutions
- CustomersDot admin view and functionality
- Quote-to-Cash (QTC) data architecture and orchestration within CustomersDot
- Audit and compliance initiatives

The Fulfillment Platform group owns, maintains and evolves the underlying architecture and orchestration for GitLab’s Quote-to-cash flow (QTC).

## Target audience

The target audience of the CustomersDot and quote to cash integrations spans all stakeholder groups, as it enables them to create and manage subscriptions with corresponding payments or quotes, customers, billing accounts, and licenses.

Therefore, we see the following parties interacting with CustomersDot
1. **Customers:** SSO with gitlab.com 
2. **Fulfillment groups and team members:** Plan and SKU management improvements and Cdot and billing rearchitecture 
3. **Internal stakeholders (Customer Success, Support, Sales, Billing operations):** Multiple active orders, Enabling Admin functions for subscription modifications, and Data integrity initiatives 


We are enhancing the overall customer experience for all our clients, whether they are self-service users, sales-assisted customers, or resellers, by optimizing infrastructure to create cohesive Quote to Cash flows.

## What's up now (up to 12 months)

Within the next 12 months we want to strengthen the foundation of the fulfillment platform which includes the following focus areas:

- Improve the billing infrastructure to align with existing and future QTC integrations
- Establish the application foundations for Fulfillment teams
- Make our billing infrastructure and underlying systems compliant 
- Introduce the partner eMarketplace integration to automate sales processes for public and private offers via AWS/GCP and other potential partners

The focus will help us to support the scale within Fulfillment and adjacent areas as GitLab continues to grow.

**Current key projects for category:**

- [Zuora offline mode](https://gitlab.com/groups/gitlab-org/-/epics/11840)
- [Improve Plan / SKU management](https://gitlab.com/groups/gitlab-org/-/epics/6579)
- [Channel partner eMarketplace integration](https://gitlab.com/groups/gitlab-org/-/epics/12188)

**Roadmap:**

For a full list of our upcoming and ongoing projects for the category CustomersDot Application, check out our [Roadmap](https://gitlab.com/groups/gitlab-org/-/roadmap?state=opened&sort=end_date_asc&layout=QUARTERS&timeframe_range_type=THREE_YEARS&label_name[]=Fulfillment+Roadmap&label_name[]=group::fulfillment+platform&label_name[]=Category:CustomersDot+Application&progress=COUNT&show_progress=true&show_milestones=false&milestones_type=GROUP&show_labels=false).

### Future opportunities

As we progress with our current key projects to build the underlying foundation of CustomersDot, we will identify new areas of opportunity. Future opportunities will continue to focus on Fulfillment process efficiency and internal team efficiency in relation to the CustomersDot application.

**List of opportunities we will tackle in the future:**

| Type | Example Projects/Intiatives |
| ------ | ------ |
| Expanding QTC capabilities |    [Support and enable Organizations/Cells from Fulfillment perspective and align models within data architecture](https://gitlab.com/groups/gitlab-org/-/epics/9885)    |
| Scalability |  [Improve Plan / SKU management](https://gitlab.com/groups/gitlab-org/-/epics/6579)      |
| Scalability | [Align Customers Dot Orders to Zuora Subscriptions](https://gitlab.com/groups/gitlab-org/-/epics/9748) to further strengthen Zuora as Single Source of Truth (SSoT) | 
| Scalability | [Zuora offline mode](https://gitlab.com/groups/gitlab-org/-/epics/11840)
| Compliance risk management | Sox Compliance initiatives, Data governance/data integrity improvements for CustomersDot and corresponding integrations |

We also strive to make improvements in the below areas as we identify the need for it
- Further refinement of our [Quote-2-Cash Systems Data Architecture](https://about.gitlab.com/company/quote-to-cash/#q2c-system-architecture)
- Enabling other Fulfillment groups for specific projects
- CustomersDot admin view enhancements for newly launched features

## Key Links

For more details into future oportunities of other categories within the Fulfillment Platform group, please refer to the sections in the dedicated category pages:
- [Fulfillment Infradev](/direction/fulfillment/fulfillment-infrastructure/)
- [Fulfillment Internal Admin Tooling](/direction/fulfillment/fulfillment-admin-tooling/)
- [Performance indicators](https://internal.gitlab.com/handbook/company/performance-indicators/product/fulfillment-section/#fulfillment-platform---general-availability-through-slis-and-error-budgets)
- [Fulfillment Platform group roadmap](https://gitlab.com/groups/gitlab-org/-/roadmap?state=opened&sort=start_date_asc&layout=QUARTERS&timeframe_range_type=THREE_YEARS&label_name[]=Fulfillment+Roadmap&label_name[]=group::fulfillment+platform&progress=COUNT&show_progress=true&show_milestones=false&milestones_type=GROUP&show_labels=false)
