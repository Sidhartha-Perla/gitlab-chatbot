---
layout: markdown_page
title: "Product Direction - Scalability-Practices"
description: "GitLab's Scalability-Practices team is responsible for providing scalable self-service pathways for onboarding and maintaining features and services across GitLab's infrastructure models"
---

- TOC
{:toc}

## Overview

The **Scalability-Practices team** is responsible for the democratising SRE capability across GitLab.
This includes creating infrastructure operating models and paved roads for those models.
These, along with tools and platforms, help GitLab team members to be more effective at building and operating features and services at production scale.
In addition, the Scalability-Practices team are stewards of the production GitLab Platform and ensure that the changes we rollout to customers are "Production Ready".

## Challenges
<!-- Optional section. What are our constraints? (team size, product maturity, lack of brand, GTM challenges, etc). What are our market/competitive challenges? -->

Our current operating models within infrastructure have served us well up until this point.
However, as the GitLab fleet grows and more independent services are stood up to meet the pace of customer demands, we recognise that our current models, like the stable counterpart model, will not be able to scale into the future.

Changing interfaces between teams and the implied contract formed from ways of working over many releases is difficult and contains a human element, which must be considered.
The pace of cultural change is typically not consistent with the pace of technological change and we will have to make a deliberate effort to encourage and enable teams to accelerate this collaboratively.

Additionally, changing operating models whilst delivering services to millions of customers is not unlike changing a wheels on a car when it is speeding down the highway.
We have to support GitLab team members through this change and iteratively adapt our team interfaces and contracts to ensure that GitLab remains reliable and available for customers during this transition.

## 1-Year Plus Plan

<!-- Describe key themes, projects, and/or features planned over the next year. Also highlight what we will not be doing in the next year -->
For FY25, we’re investing in the following capabilities, which are linked to our [group 3-5 year strategy](/direction/saas-platforms/scalability#3-5-year-strategy):

### Continue to build out paved roads for GitLab team members

We are working to make our infrastructure models into paved roads with greater definition and predictability for team-members.
Paved roads will include production readiness, a Well Architected Framework, Service Maturity Models and interaction models with the infrastructure team.
One of the ways we are doing this is by increasing the capability of Runway to encourage adoption and move more services to the platform.
Using Runway, team members get SRE capability out of the box. You can read more on Runway [in these internal only slides](https://docs.google.com/presentation/d/1RxCP1GYMdV1wYL-orDppDMmV34kf9rsLMc6dcC1zENM/edit#slide=id.g2a8be5106db_0_0).

#### Support more business critical initiatives through expanding Runway

Now that we've proved the model works and Runway is able to support multiple business critical services like Model Gateway and our GCP integration, we're working on expanding Runway's capability to support more business critical services.
Stateless, containerised workloads are fully supported on Runway today and we're working towards supporting more stateful capability.
We're starting by adding support for multiple regions, some stateful workloads, internal only services and high compliance requirement solutions.
Further down the line we will add support for running more complex workloads like Kubernetes deployments with the goal of covering 70% of the independent services running at GitLab.
This will allow us to deliver results to customers sooner, safer and happier.

#### Refactor Runway so that everyone can contribute

Making Runway easy to contribute to will ensure it is successful in the future. Runway was first built, with a very specific purpose in mind - to launch our AI services and iterate on them quickly and safely.
Almost a year later we have multiple services on Runway and the requirements for additional services to be onboarded on Runway are increasing.
In order to support a growing number of workloads and use cases, we will revisit the architecture of Runway to make sure it fits with our [guiding principles](https://gitlab.com/gitlab-com/gl-infra/platform/runway#guiding-priciples) and is able support the pace of iteration required.

The Mission of GitLab is 'Make it so that everyone can contribute'.
We want Runway to embody this mission and this means that Runway will iterate towards a composable and modular platform, where you don't need to be a core contributor in order to add value and merge code.

### Bring our capability together into a single pane of glass

Over time we have built a lot of separate tools & components that help us to operate and manage gitlab.com efficiently.
As we are working on expanding these tools & components to support the GitLab fleet, we're realising the discoverability of these tools & components is not optimal and a high level of context is required to be efficient.
Over time we want to move all of this capability into a single pane of glass, that provides actionable notifications and allows team members at GitLab to see everything they need to in one place.

#### Enhance the discoverability of our tools

Over time we have built a lot of the capability we may wish to include inside of a single pane of glass.
However, it is fragmented, non-discoverable and requires a high level of context to be able to operate efficiently.
A key component that is missing is a single place where the capability is documented and can be consumed.
For that, we need a UI Layer, which should take the form of a [Thinnest Viable Platform](https://teamtopologies.com/key-concepts-content/what-is-a-thinnest-viable-platform-tvp) in it's first iteration.

### Democratise SRE Capability at GitLab

SREs at GitLab are responsible for running a highly available, distributed monolith and a number of additional services as part of their day to day.
This operating model has served us well so far but, as the number and complexity of services grows, this will not be sustainable.
Human SREs have a hard limit of scale.
We will work towards democratising SRE capability with tools, frameworks, and documentation that enable GitLab team members to benefit from 'junior SRE' capability on demand.
As one of multiple groups who provide SRE support for GitLab, we expect to work on this in collaboration across infrastructure.

#### Enable teams to 'build it, run it'

The most boring solution for democratising SRE capability is giving teams the tools to manage and operate their own services.
This is something we have started with Runway and the teams currently on Runway are interested in iterating on this further.
However, managing, troubleshooting and operating a service is not a set of skills that are built overnight.
We plan to migrate slowly away from our stable counterpart model and push teams to relevant infrastructure models and paved roads like Runway.
We understand that this kind of cultural change will take time and effort from all parties involved and we predict that it is worth it to enable GitLab teams to move at their own pace.
Complex problems will require deep SRE experience. With less overall pressure on SREs from low and medium severity issues, we can focus our efforts onto solving the challenges that come with our scale.

#### Introduce the Well Architected Framework

As well as by introducing platforms like Runway, we can democratise SRE capability by providing frameworks on how to design and build applications that scale to meet the demand of our users.
We'll do this by reinvigorating the Service Maturity Model and integrating it into a 'Well Architected Framework', which will act as a guide and a set of templates and models that shifts production readiness left, making it a core part of early iterations, delivering more value, sooner.

#### Launch an SRE Knowledgebase

SREs at GitLab provide support across the organisation and not just to engineers. As the stewards and experts of GitLab.com, SREs are often called upon to diagnose and resolve customer issues and work regularly with our Support and Account teams. We can increase the efficiency of this support and ensure our SREs are directed to the most valuable work by democratising SRE knowledge across the company.

This will start by creating an indexed, centralised knowledge repository that can act as a troubleshooting guide for support engineers working on customer queries.
Discoverability, search and regular contribution to this documentation should totally eliminate the waiting time for and need to engage an SRE for common, easy to resolve issues, which represent around 60% of the requests for SRE support in the latter half of FY24.
This will shorten the cycle time for customer support tickets driving organisational efficiency and customer results

### A note on 'keeping the lights on'

As part of the Scalability Group’s responsibility to scale GitLab.com, there is a significant amount of operational load on the team.
We regularly swarm around issues and production incidents, helping teams to quickly identify, root cause and solve GitLab.com problems.
This work will typically be prioritized ahead of any project work to ensure that gitlab.com customers are not disrupted.

### What we're not doing

We are not working on the Service Maturity Model directly, as this will be absorbed by the Well Architected Framework.
We’re not working on deploying the monolith or any of our core services on Runway.
We are not focused on how to include Runway deployed services into the GitLab package.

## Categories
<!-- Provide brief descriptions of stage + category direction, along with links to supporting direction pages -->

- [Infrastructure Cost Data](/direction/saas-platforms/cost-data)
- [Runway](https://gitlab.com/gitlab-com/gl-infra/platform/runway#guiding-priciples)
- Redis
- Well Architected Framework

## What's Next

- Runway GA
- Keep the lights on
- Automatic Dependency Update / remediation - TBC

The list above can change and should not be taken as a hard commitment.
For the most up-to-date information about our work, please see our [top level epic](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/148).
