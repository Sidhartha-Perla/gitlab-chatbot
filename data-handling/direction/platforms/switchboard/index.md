---
layout: markdown_page
title: "Category Direction - Switchboard"
description: "Learn about GitLab's Switchboard, a centralized management platform that simplifies SaaS administration and enhances user control and scalability."
---

- TOC
{:toc}

## Switchboard

<!--
| | |
| --- | --- |
| Stage | [<STAGE-NAME>](/direction/<STAGE-NAME>/) |
| Maturity | [<MATURITY-LEVEL>](/direction/#maturity) |
| Content Last Reviewed | `yyyy-mm-dd` |
-->

### Introduction and how you can help

This page outlines the Direction for the GitLab Switchboard category which belongs to the [GitLab Dedicated group](https://handbook.gitlab.com/handbook/product/categories/#gitlab-dedicated-group). To provide feedback or ask questions about this product category, reach out to the [Product Manager](mailto:lbortins@gitlab.com).

You can contribute to this category by:

- Commenting on a relevant epic or issue in [our project](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team) (GitLab internal), or opening a new issue in the [GitLab Dedicated issue tracker](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues/new?issue%5Bmilestone_id%5D=)
- Joining the discussion in the [#f_gitlab_dedicated](https://gitlab.slack.com/archives/C01S0QNSYJ2) Slack channel

To learn more about concepts and terminology discussed in this direction page, please refer to the [Switchboard Glossary](./glossary).

## Overview

### Solution

Switchboard is the customer console for the [GitLab Dedicated](/direction/saas-platforms/dedicated/) single-tenant SaaS offering. Switchboard is used both by GitLab Dedicated customers and internal GitLab teams who support and maintain GitLab Dedicated instances.

Switchboard also automates much of the ongoing maintenance work needed to maintain GitLab Dedicated instances, reducing the amount of time internal teams need to spend on operational tasks and freeing up bandwidth to focus on [maturing and adding features to GitLab Dedicated](/direction/saas-platforms/dedicated/#roadmap).

Our north star for Switchboard is to reduce time to value (TTV) for new GitLab Dedicated customers and create internal efficiencies by minimizing the assistance tenant operators need from GitLab to manage their instances.

### Background

Maturing Switchboard is critical to the success of GitLab Dedicated at scale.

During the Beta and Limited Availability (LA) phases of GitLab Dedicated, all management of tenant instances was performed by the same internal SRE teams who are responsible for developing the architecture and automation needed to fully scale GitLab Dedicated as a product offering. 

While regular tenant maintenance operations continue to be handled by these teams, customer tenant admins can use Switchboard to quickly make configuration changes to their organization's GitLab Dedicated tenant instance on their own. Switchboard also serves as the "front door" to GitLab Dedicated by providing a welcoming and efficient onboarding experience.

From an operational and architectural perspective, Switchboard serves as the primary connection between internal tenant operators and GitLab Dedicated tenant instances, enabling them to operate at scale. GitLab tenant operators do not have direct access to customer tenant environments. For more information, see [Access controls](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/#access-controls) and the [GitLab Dedicated architecture](https://docs.gitlab.com/ee/administration/dedicated/#architecture).

### Target Audience

Switchboard shares its target customer with [GitLab Dedicated](/direction/saas-platforms/dedicated/#target-customer).

The primary user persona for Switchboard is [Sidney (systems administrator)](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator), with some overlap with [Priyanka (platform engineer)](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer).

Within GitLab, Switchboard is used by the tenant operators (SREs), support, and professional services teams.

### Comparative Analysis

Similar portals or consoles have been built for other products used by Switchboard's target audience including [Managed Elasticsearch](https://www.elastic.co/elasticsearch/service), [MongoDB cloud](https://www.mongodb.com/products/tools/cloud-manager), [AWS](https://aws.amazon.com/console/features/) and [IBM power](https://www.ibm.com/products/cloud-management-console). See [Figma page](https://www.figma.com/file/YaJQT4WARRk9u0YQveioPJ/%F0%9F%AA%A6-DEPRECATED---Switchboard-onboarding?type=design&node-id=3-12118&mode=design) for more details (internal only).

We will look to common patterns shared by these portals as we continue to build out the capabilities of Switchboard.

### Success Criteria

We have begun using the [Performance Indicator framework](https://internal.gitlab.com/handbook/company/performance-indicators/product/) to measure Switchboard's contributions to engineering efficiency.

GitLab team members can review the [Saas Platforms PI page](https://internal.gitlab.com/handbook/company/performance-indicators/product/saas-platforms-section/#gitlab-dedicatedswitchboard---self-service-actions-per-dedicated-tenant-sapt) for the latest updates. 

Read more about how we arrived at our metric through the [SaaS Platforms North Star workshop](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1097) in FY24.

## Current state

Switchboard has been generally available since 2023-09-29.

Most of the internal operators' responsibilities (maintenance windows, incident response/remediation) are now completed with the Switchboard application. Monitoring tools remain separate and are housed within the tenant instances themselves. Many formerly manual tasks have been automated or removed.

Over the past year, we have matured Switchboard as an application by adding several foundational "table stakes" capabilities including email notifications and a configuration change log visible to Dedicated customers.

See our [documentation](https://docs.gitlab.com/ee/administration/dedicated/configure_instance.html) for the most up to date list of customer-facing configurations and features available in Switchboard.

## Where are we headed

Moving forward, the Switchboard team's focus will continue to remain balanced between delivering new customer-facing features and internal-facing work to continue to streamline internal operations.

New customer-facing work will be either tied to supporting significant new GitLab Dedicated features (e.g. [Hosted Runners for Dedicated](https://docs.gitlab.com/ee/administration/dedicated/hosted_runners.html)) or to further enable self-serve capabilities for GitLab Dedicated tenant admins.

Internal-facing Switchboard work will focus not only on continuing to automate operational tasks and reduce engineering toil within the Dedicated group but also on investigating where foundational Switchboard components might be relevant to other teams and initiatives within SaaS Platforms.

### What is next for us

In FY25 Q4 we will further expand Switchboard's foundational capabilities by completing foundational work to allow Dedicated customers to integrate Switchboard with their own IDPs and enable SSO.

These two capabilties are examples of requests we have received from enterprises with complex access and compliance requirements which is expected given GitLab Dedicated's [target customer base](/direction/saas-platforms/dedicated/#target-customer). As  Switchboard continues to mature, we expect we will add more compliance-focused features like these.

We will also begin building out an instance of Switchboard to meet the needs of GitLab Dedicated for Government based on the investigation underway in [FY25 Q3](#fy25-q3).

### What we are currently working on

In FY25 Q3 our two primary focuses for customers are the tenant overview page and enabling self-serve configuration of Outbound Private Link and Private Hosted Zones.

For internal-only features we are focused on making improvements to emergency maintenance automation, reducing toil required for Hosted Runner onboarding to support GA, and implementing a review app to minimize Quality concerns.

For more details see our Q3 OKRs:

- [Enable SREs to use Switchboard as the SSOT for supporting and maintaining Dedicated Tenant instances](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/8778)
- [Expand self-serve capabilities](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/8773)

### What is not planned right now

* Switchboard will not directly interact with customer tenant environments. Read more about that in the [GitLab Dedicated documentation](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/#access-controls).

* Switchboard will not replace or reproduce functionality of logging or monitoring tools for Dedicated instances (e.g. Grafana dashboards for infrastructure health).

## What we have recently completed

In the first half of FY25, the Switchboard team has been equally focused on closing critical gaps in customer-facing functionality and further automating internal operations work to increase efficiency of the Environment Automation team.

NOTE:
Internal demo videos of all features completed by the Switchboard team in FY25 are available in our [demo library](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/switchboard/-/blob/main/docs/walkthrough-library.md) as well as on each completed epic linked below.

### FY25 Q1

- [MVC: customer-facing configuration change logs](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/337)
- [MVC: email notifications](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/338)
- [Fully automate creation of Geo-enabled Dedicated Tenant Instances (internal feature)](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues/3688)
- [Add import of geo-based migration secrets to Switchboard flows (internal feature)](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/328)
- [Support for BYOD configuration (internal feature)](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/403)
- [Support for Pages configuration (internal feature)](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues/4110)

### FY25 Q2

- [MVC: Configure Hosted Runners for Dedicated](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/416)
- [Emergency maintenance form and automation (internal feature)](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/444)
- [Ability to schedule Amp jobs (internal feature)](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/443)
- [Support for SMTP configuration (internal feature)](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues/4741)
- [Automated tenant configuration delta reporting (internal feature)](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues/3070)

## Roadmap

Below are the key capabilities we plan to add to Switchboard in the second half of FY25 and first half of FY26.

The Switchboard roadmap remains closely tied to the [GitLab Dedicated roadmap](/direction/saas-platforms/dedicated/#roadmap) - we often have dependencies on the Environment Automation team or vice versa when developing new features or feature enhancements. 

It is common for new Switchboard features to be driven by the growing set of [features available for GitLab Dedicated](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/#available-features)

We are also continuing to gather internal feedback and feature requests via this [feedback issue](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues/2078) (internal).

### FY25 Q3

- [Release Reverse Private Link Config UI](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/284)
- [Release Private Hosted Zones Config UI](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/275)
- [MVC: tenant overview page](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/153)
- [Discovery: Switchboard for Dedicated for Government (FedRAMP)](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/517)

### FY25 Q4

- [POC: Integrate with customer IDPs to provide SSO for Switchboard](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues/6341)
- [Support for Multiple Login providers](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/523)
- MVC: Switchboard for Dedicated for Government (FedRAMP)

### FY26 Q1

- User management enhancements
- Realtime tenant data in Switchboard (internal feature)
- GA: Switchboard for Dedicated for Government (FedRAMP) tenant onboarding

### FY26 Q2

- Switchboard tenant onboarding re-design
- Switchboard tenant configuration page re-design
