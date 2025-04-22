---
layout: markdown_page
title: "Category Direction - Developer Portal"
description: "Explore GitLab's vision for its developer platform, providing powerful tools and features to enhance developer productivity and collaboration."
---

- TOC
{:toc}

## Developer Portal

| | |
| --- | --- |
| Stage | Cross Section CI, CD, Core Platforms |
| Maturity | [Planned](/direction/#maturity) |
| Content Last Reviewed | `2024-09-02` |

### Introduction and how you can help

Thanks for visiting this category direction page on Developer Portal in GitLab. This page is [Cross-section catgeory](https://handbook.gitlab.com/handbook/product/cross-stage-features/#cross-stage-feature-collaboration), and is owned by Jackie Porter and Viktor Nagy. 

This direction page is a work in progress, and everyone can contribute:

 - Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=developer+portal) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?label_name[]=developer+portal) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
 - Please share feedback directly via email, Twitter, or on a video call. If you're a GitLab user and have direct knowledge of your need for the Developer Portal, we'd especially love to hear from you.


### Overview

The Developer Portal category aims to provide a comprehensive set of tools and services that empower developers to self-serve and easily find the DevSecOps resources they need as offered by GitLab or 3rd party integrators. 
On the market today, Internal developer platforms (IdPs), aim to make developers faster by removing manual tasks and providing consolidation of resources into a centralized pane. 
With the Developer Portal category, we aim to create a SSoT for the developer to easily contextualize the GitLab resources relevant for their Application, services and processes. 

### Strategy and Themes

Key focus areas for the Developer Portal include:

1. Self-service automation including deployment and database tasks
1. Improved metadata across software, services, catalog resources, and more
1. Centralized view and documentation for APIs within the company
1. Secure way to connect to a backend
1. Pre-built plugins for popular tooling

By addressing these areas, we aim to provide a unified platform that covers the entire software development lifecycle, from coding to deployment and beyond.

### 1 year plan

IdPs and service catalogs are becoming more and more urgent in terms of meeting customer expectations in the DevSecOps landscape although, these efforts are not planned or funded in the next year. 

#### What is next for us

We are conducting longer term research, proof of concepts, and integrations with ecosystems tools to provide a better experience for our customers. Related to self-service automation we are defining the Eventing strategy that will be foundational for how users would conduct automation in a Developer Portal. 

#### What we are currently working on

This category is currently not funded. 

#### What we recently completed

1. We support using GitLab APIs (including with the GitLab Terraform provider) to [enable self-service automations using GitLab pipelines](https://gitlab.com/gitlab-org/terraform-provider-gitlab/-/issues/1303)
1. We completed strategic research outlining what DevOps Portals and GitLab could offer to the market to inform our approach [Internal Report](https://docs.google.com/presentation/d/1VtdotLh0p1sEGawadO98DqWwkNPsiHgY-WnJZvg49qM/edit?usp=sharing)
2. We completed research on what are our [users core expectations from a service catalog](https://gitlab.com/gitlab-org/ux-research/-/issues/2577)
1. We outlined an integration approach with the Service Catalog with the [Pipeline Authoring Category](https://about.gitlab.com/direction/verify/component_catalog/#service-catalog). 

#### What is Not Planned Right Now

Implementation of features or epics. 

<!-- ### Best in Class Landscape
<!-- Blanket description consistent across all pages that clarifies what GitLab means when we say "best in class" 

BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

#### Key Capabilities 
<!-- For this product area, these are the capabilities a best-in-class solution should provide -->

#### Roadmap

Beyond 2025, we do have plans to invest in Developer Portal. The roadmap for Developer Portal include: 

1. 

#### Top [1/2/3] Competitive Solutions

There are currently two main competitive solutions in market: Backstage.io and Port. 

#### Backstage.io 

There are some real values and strengths of Backstage from the market and user POV: 

- Easy to customize and to create plug-ins 
- Allows quick creation of a UI experience for different applications and services 
- Has a scheduling mechanism for common tasks
- Helps to mitigate competing needs across microservices 
- Descriptions of APIs and metadata for services helps users to identify what services are for and how to build broader services with them 
- Being able to test workflows and to see what an example response to API calls gives users  starting point for designing applications
- Seeing upstream and downstream dependencies for different services helps users understand how to use services, to mitigate any impact of changes, and to triage issues
- Being able to filter services / entities by teams allows users to quickly understand the services that they provide, and who to contact with issues
- Search functionality works well
Deployments are easier and quicker, and users have transparency into who has approved deployments / their status
- Onboarding is quick

The drawbacks we have heard is that the the intial configuration and maintenance overhead is high. Additionally, the navigation is painful to use. 

#### Port 

Port is the second most commonly used IdP offering and has some strong advantages to Backstage, these include: 

- Ease of use and configurability with pre-built integrations - meaning people spend less time setting up commonly used integrations 
- Out of the box paved roads that meet most use cases - people can get started faster using Port because connecting your CI, CD, SCM and other ecosystem tools is much easier then havin to script a ton of API integrations 
- Navigation - Port UX is nicer and easier to use than Backstage.io

The drawbacks of Port from customers are the breadth of customizable metrics in the scorcards and benchmarks are not as flexible. 

### Target Audience

For Developer Portal, we are targeting the following personas, as ranked by priority for support: 

1. [Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
1. [Priyanka - Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)


<!-- ### Pricing and Packaging


### Analyst Landscape 

### Best in Class Landscape
<!-- Blanket description consistent across all pages that clarifies what GitLab means when we say "best in class"  -->

BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

#### Key Capabilities 
<!-- For this product area, these are the capabilities a best-in-class solution should provide -->

- A single pane of glass to know everything about a software component, service or resource
- Self-serving on new service creation or deployment is more efficient than waiting on others
- No context switching, single entry-point to find everything
- Users need to find documentation about how to consume a service, use a component or get support within their company/team.
- Different users require different information to do their day to day job

#### Roadmap

We are discussing the potential approach internally. As we expect this to be a cross-section initiative, we created a [gap analysis](https://docs.google.com/document/d/148J32ch2ySu80ckSeMU0UXLtrBxVp1kgstP8AgcEisQ/edit) (internal only) to highlight the various domains involved.

#### Top [1/2/3] Competitive Solutions

There are currently two main competitive solutions in market: Backstage.io and Port. 

#### Backstage

Backstage is an open source, plugin-based, component registry framework. Backstage ships to some extent all the mentioned key capabilities. It's primary strengths are

- Framework design allows for extensive customization through plug-ins
- Slick, easy to use UI
- Open source

Its primary weaknesses are:

- initial configuration and maintenance overhead is high

#### Port 

Port is a closed source IdP offering and has some strong advantages over Backstage. Port ships to some extent all the mentioned key capabilities. It's primary strengths are

- Ease of use and configurability with pre-built integrations - meaning people spend less time setting up commonly used integrations 
- Out of the box paved roads that meet most use cases - people can get started faster using Port because connecting your CI, CD, SCM and other ecosystem tools is much easier then havin to script a ton of API integrations 
- Navigation - Port UX is nicer and easier to use than Backstage.io

Its primary weaknesses are:

- the breadth of customizable metrics in the scorecards and benchmarks are not as flexible

### Target Audience

For Developer Portal, we are targeting the following personas, as ranked by priority for support: 

1. [Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
1. [Priyanka - Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)


### Pricing and Packaging

TBD

### Analyst Landscape 

- [Gartner (Market Guide for Internal Developer Portals)](https://drive.google.com/file/d/1CyvRaaf68wOEPRVA9yGKFWwuQOTZDLnf/view?ts=661404e5) (GitLab internal only)
