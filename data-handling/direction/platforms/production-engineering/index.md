---
layout: markdown_page
title: "Product Direction - Production Engineering"
description: "GitLab's Production Engineering Stage is responsible for making sure that GitLab runs at scale across our SaaS platforms"
---

- TOC
{:toc}

## Vision

The Production Engineering Stage is focused on two core pillars that provide value for our customers

1. Building out paved roads that team members can follow to get software into production
2. Providing insight into & scaling the production operations that keep GitLab available and performant at scale.

This will position Production Engineering as a core engine or flywheel for growth at GitLab, enabling team members to get services to production quickly and reliabily.
Runway will serve all product lines and be the best example of a paved road for new services at GitLab, making it easy to get them in customers hands.
Other paved roads will emerge to make it easier for GitLab teams to create and work inside the monolith as well including paved roads for observability, rate limiting and our edge network that form part of our core services.
In addition, we will transform the operator experience by raising the bar on our SRE and incident management practices, providing new levels of insight and visibility to guide day 50 operations.
We will also take steps to re-architect parts of the application to improve resilience and usability, meaning that customers will be able to consume GitLab SaaS services with great user experience and availability.
Finally, comprehensive education programs delivered through GitLab's internal L&D platform will be available for all team members and required for certain roles, ensuring that everyone is able to create features that scale with our systems.

## Challenges
<!-- Optional section. What are our constraints? (team size, product maturity, lack of brand, GTM challenges, etc). What are our market/competitive challenges? -->

GitLab teams have a large amount of autonomy and are empowered to work on things that are the most important for their stage and user base.
This is great for the development of features, categories and stages, but can create a challenging environment for operating a platform at scale.
Since stage teams are empowered to make the changes they need and GitLab operates with a [bias for action](https://handbook.gitlab.com/handbook/values/#bias-for-action), stage teams may decide that a shared implementation does not fit their requirements and end up building their own.
This can lead to redundancy, the inability to share and re-use code and ultimately increases the tech debt of GitLab.
It is therefore important to balance the overall velocity and scalability of GitLab with individual stage team's desire to ship value to our customers.

Discoverability is also a significant challenge in the platform space.
It is vital that users of platform tools are able to quickly discover and implement shared tools and best practices.
If the tools are not flexible, easy to discover and easy to implement, they may hurt feature velocity rather than increase it.

Lastly, considering the image below, Scalability tends to operate on the right hand side of the graph, after changes are deployed to our SaaS platforms.
This can mean that our work is reactive in nature and we often treat symptoms of bad health in the platforms instead of root causes.
Shifting the scaling concerns left, earlier in the software development lifecycle, will help us to scale our SaaS platforms more efficiently.

Two examples where the Production engineering stage has already shifted left are [Error Budgets](https://handbook.gitlab.com/handbook/engineering/error-budgets/) and [Capacity Planning](https://handbook.gitlab.com/handbook/engineering/infrastructure/capacity-planning/).

![alt text](shift_left.png "Shift Left Model")

## 3-5 Year Strategy

### Observability across the Production Fleet is accessible for all.

The Observability team within the Scalability group is responsible for architecting, provisioning and operating the observability platforms that enable us to operate the SaaS platforms at GitLab.

#### Durable Observability at both the instance and fleet level

Observability and automation will become more critical as the number of instances of GitLab increases.
The growth in instances is being driven by the introduction of [GitLab Dedicated](https://about.gitlab.com/dedicated/) and the move toward a [cellular architecture](https://about.gitlab.com/direction/core_platform/tenant-scale/) for our multi-tenant SaaS solution.

We envision “Observability Units” rolled out alongside our GitLab instances, connecting into a Global observability stack that gives us insight into system health across all of GitLab and directs us to issues with actionable insights.
These “Observability Units” will be durable and capable of running independently without connection to the global stack.
The global stack will be eventually consistent with all of the units in the fleet, whilst preserving the data security and visibility requirements that we ensure today.

#### Single Pane of Glass that scales across GitLab use cases

As the complexity of GitLab's production systems grows, the observability of GitLab's platforms is critical.
In FY25, Dedicated and GitLab.com use different logging tools and have different operational solutions to their specific requirements.
This creates a lot of inefficiency in some of our most critical operations - error investigation, debugging and issue resolution.
Additionally, different product lines have different levels of isolation required and different access controls on operational data.
We will work to provide a single pane of glass that gives team members a low context entrypoint whilst handling the complex access and isolation requirements in the background.
This will make our observability platform easier to use and result in higher quality software that works well across product lines and not just for GitLab.com.

#### Leveraging cost effective managed service providers

As the number of GitLab instances grows, increasing the level of automation required to rollout and operate both units and the global observability stack will be paramount.
Additionally, to improve resiliency, it is likely that these units will become cloud agnostic over time.
In order to drive the level of automation up and the level of toil down, we leverage managed service providers where appropriate. That allows us to focus our efforts on the higher level functions of our observability platform instead of the mechanics of operating it.

We expect to continue to maintain some number of GitLab operated foundational services. We will assess this on a case by case basis considering the cost with associated benefit.

### Availability metrics better reflect the user experience

GitLab’s [availability metrics](https://handbook.gitlab.com/handbook/engineering/infrastructure/performance-indicators/#gitlabcom-availability) represent our experience of running and operating GitLab.com at million user scale.
This has been successful so far, but as the number of capabilities and use cases grow on our platform, we want to shift these to better reflect the user experience, rather than the operator experience.

#### Instrumentation of core user journeys

In the future we will instrument end to end user journeys on the platform, which represent core user experiences that must be performant to drive increase in customer satisfaction.
A side benefit of instrumenting user journeys will be the abilitiy to utilise these SLIs and SLOs for the purpose of evolving our testing strategy, shifting to observed metrics over fragile end to end tests and getting insight into performance only possible through observing production traffic.

#### Published availability metrics

As mentioned in other sections of this page, GitLab Dedicated and a cellular architecture increase the complexity of operating the SaaS solutions offered by GitLab.
Over time we will shift towards availability metrics that better represent the user experience on GitLab.com and GitLab Dedicated.
As our metrics become more representative of the user experience, we expect the Service Level Availability metric to change alongside.

#### Internal Error Budget metrics

Error budgets have allowed us to meaningfully address availability issues in the early stages of operating GitLab.com.
This has been great for product teams, who can proactively address performance and availability issues in their features.
Whilst they have been useful for improving the availability of GitLab.com over time, we understand that operating a GitLab instance the size of GitLab.com is not a common user experience.
To make our error budgets more effective guides for teams, we will implement error budgets across the production fleet, for all instances.
This will allow us to gain better insight on instances that look more like customer instances, improve the performance of GitLab at every size, and ensure that our Error Budgets can mature to reflect the user experience as well as system health.

#### Systematic reviews of data

While we have automation to cover as much as possible regarding the availability and performance of our platforms, our automation only covers what we know to look for.
We should conduct periodic human reviews to assess if there are missing pieces of our automation rather than waiting for incidents and customer reports.

### Paved roads are the default for all team members

One of our core focuses is providing paved roads for GitLab team members.
The way our infrastructure organization operates will likely evolve over the next few years and we aim to create paved roads for all the models that we operate in.
We aim to encourage cultural change over time by democratizing our capability and putting in the hands of GitLab team members.
Our paved roads will be as good for day-1 operations as they are for day-50 operations, supporting a number of different application architectures and generating more customer results through increased efficiency.

#### Onboarding

Feature owners and service owners will have a self-service onboarding experience that supports all stages of feature and service maturity.
Documentation and processes should be clear and easy to find and follow.

#### Operations

Feature owners and service owners should be empowered to operate their features and services as far as reasonably possible.
Self-serve will be a core part of this, with simple interfaces to allow SREs to collaborate on issues where deep expertise is required.

#### Foundations

Foundational components like DNS records, WAF and rate limiting should be easy to configure and set up for GitLab teams.
Self-serve should mean that teams are able to reduce their direct interation with SRE and move services to production faster.

### Solutions at GitLab Follow the Well Architected Services Framework

As part of the move to paved roads, we’ll create a Well Architected Services framework, which will tie in with our Service Maturity Model.
This will gives teams guidance on how to build services and solutions that are resilient and able to scale to serve our production load.
Having practical examples and guidelines, along with getting involved in the design and architecture process earlier will ensure that services get to production (and customers) sooner, safer and happier than they would with ad-hoc processes and reactive work.

Over time services will follow the paved road for the infrastructure model that best suits them and the engineering portal will provide the information needed for the owners to understand the needs of their services.

### Engineering Portal is the home for engineers at GitLab

Most of the information that we need to operate GitLab.com and maintain excellent levels of service for our customers is already present within GitLab.
We can improve this by providing a single pane of glass that empowers service owners, support engineers and members of the engineering organization to see all of this information in one place.

This should culminate in a Thinnest Viable Platform, where GitLab team members can discover vital information about their service(s)' health, key infrastructure performance indicators and other information that will contribute to the decision making process in feature development.
This will be composed of atomic tools and solutions, be customized to various GitLab roles and reduce cognitive load, increase discoverability & efficiency across GitLab.

### Incident management delivers best in class usuability & insights

We have observed significant gaps in the capability of the native functionality that make performing analysis and generating insight from our incidents is hard.
This makes it harder to prevent customer impacting incidents from re-occurring as well as to identify and address systemic issues
Our incident management practice meets a high bar currently, but over time we will evolve our capability to deliver reporting, insight and analysis into the causes and frequency of incidents.
This will drive an increased level of visibility into problem areas at the team and also the executive level, meaning that we can make tactical and strategic prioritisation decisions about the work that teams do to improve the quality of the platform.

At the same time we will invest in new incident management platforms that make it easy to create and manage incidents, complete thorough and timely incident reviews and raise the bar for quality across GitLab.
Through greater insight and ability to capture more detail about incidents and corrective actions, we will be able to integrate into other parts of the organisation and develop "risk assessments" based on the pieces of the system we are changing and the frequency/severity of incidents related to changing those parts of the system.
This should allow us to streamline controls in areas of the product that are low risk and increase the controls and governance of the platform in higher risk areas, leading to a lower change failure rate across the board.

## 1-Year Plus Plan

<!-- Describe key themes, projects, and/or features planned over the next year. Also highlight what we will not be doing in the next year -->
After the expansion of the Scalability Group and to stop this page becoming too long, we have broken out the one year plan into two new pages:

- [Observability Direction](/direction/saas-platforms/production-engineering/observability)
- [Practices Direction](/direction/saas-platforms/production-engineering/practices)

<!-- These pages ^^ still need to be created at the time of this MR, remove this comment when they are created -->

The list above can change and should not be taken as a hard commitment.
For the most up-to-date information about our work, please see our [top level epic](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/148).
