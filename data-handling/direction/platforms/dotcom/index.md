---
layout: markdown_page
title: "Product Direction - GitLab.com"
description: "GitLab.com is GitLab's Multi-Tenant SaaS offering"
canonical_path: "/direction/saas-platforms/dotcom/"
---

- TOC
{:toc}

## Overview

Our multi-tenant SaaS platform, GitLab.com, provides the easiest and quickest way to adopt GitLab and the lowest overall total cost of ownership. GitLab.com should be the default for most customers.

Our SaaS offerings make up an [increasing percentage of revenue](https://ir.gitlab.com/financials/quarterly-results/default.aspx) and we see further growth opportunities because of the benefits of SaaS for our customers. 

## Vision

In the long term, GitLab.com will be the default choice for most customers when selecting a DevSecOps platform to power their business. 
GitLab.com's best in class availability, regional offerings and industry leading value will lead customers to choose .com over competitors and other deployment options like Self Managed GitLab. 
We will leverage vertical efficiencies driven by shared and consolidated tool-sets to bring the efficiencies of .com to all product lines (.com, Dedicated, Self Managed).

Customers with strict compliance and single tenant needs will continue to choose GitLab Dedicated for its unique value proposition.
GitLab.com will be the default option for customers that want a industry leading SaaS solution for a DevSecOps Platform that meets strict availability and disaster recovery targets.
As more of these needs are met by GitLab.com, we expect that both new and existing customers will choose GitLab.com for it's consistent performance and low total cost of operation.
Over time, this will mean that more customers choose GitLab.com over self-managed.

## Challenges
<!-- Optional section. What are our constraints? (team size, product maturity, lack of brand, GTM challenges, etc). What are our market/competitive challenges? -->

### High Operational Load

GitLab.com teams are responsible for the continued operations of the systems that are essential to deliver our multi tenant platform. 
Onboarding, operating, and maintaining these systems have a high cognitive and operational load. 
As a consequence, project work that could evolve our deployment capabilities and unlock new business opportunities can be deprioritised over “keep the lights on work” which prevents/mitigates user impact.

Additionally, GitLab.com is operating at the largest edge of what GitLab handles as a product.
This can reveal subtle, but significant issues that most customers operating GitLab will never experience, but create a large demand on the teams that support GitLab.com. The size of the customer base also comes with the varied ways GitLab.com is used, which not only shows up in subtle differences in how the product behaves, but also in how the users interact with the platform.

### Ownership of a Shared Platform

GitLab teams have a large amount of autonomy and are empowered to work on things that are the most important for their stage and user base. 
This can be great for the development of features, categories and stages, but can create a challenging environment for building and operating a platform at scale. 
Since stage teams are empowered to make the changes they need and GitLab operates with a bias for action, stage teams may decide that a shared implementation does not fit their requirements and end up building their own. 
This can lead to redundancy, the inability to share and re-use code and ultimately increases the tech debt of GitLab. It is therefore important to balance the overall velocity and scalability of GitLab with individual stage team's desire to ship value to our customers.

We are also working to match some parts of the platform that are currently unowned to relevant teams and groups.

### Staffing & Perception

Infrastructure teams are typically staffed very lean as a consequence of being understood as a "cost centre" for the business. 
Preventative cost avoidance is hard to account for and model and often leads to underinvestment in groups that prevent and manage negative business outcomes. 
We are already starting to change the perception of SaaS Platforms into a revenue generator or "profit centre" with Runway and there is a significant opportunity to build more compelling features which further drive our transformation into a principal revenue generator for GitLab.

## 3-5 Year Strategy

<!-- Where will the product be in 3 years? How will the customer's life/workflow be different in 3 years as a result of our product? -->

GitLab.com is our multi-tenant SaaS platform, and it should be the default for the widest set of customers because it offers the most value and lowest total cost of ownership (TCO).
Whether large enterprises with many thousands of users or small teams solving a specific problem, GitLab.com represents the solution with the lowest TCO with the most up to date functionality. 
This should make it the most attractive platform for most customers, with other platforms like GitLab Dedicated available for our customers with different (strict internal) compliance needs or a desire for Dedicated, single tenant GitLab.

### Increase Platform Availability & Reliability to Best in Class

GitLab currently has no publicly stated SLA. 
However, based on [3 years of historical data](https://handbook.gitlab.com/handbook/engineering/monitoring/#historical-service-level-availability) from August 2021 to August 2024, we achieve an average of three 9s (99.94%) in our availability SLI. 
Three 9s is the high end of availability targets set for complex SaaS applications across the industry. 
In order to win in the long term, we need to increase our availability to be best in class across the industry. 

Best in class means putting in place an SLO of four 9s as a clear differentiator. 
This will require a shared effort between many groups within SaaS platforms and some foundational investments and re-architecture of existing systems.

### Improve the Quality of our Product Development Practice through Stewardship

[Stewardship](https://www.merriam-webster.com/dictionary/stewardship) is defined as "the conducting, supervising, or managing of something" and in many contexts is extended to "the careful and responsible management of something entrusted to one's care".
In this context SaaS Platforms team members are stewards of GitLab.com. 
Delivery, Scalability & Production Engineering have a responsibility to ensure that GitLab.com remains operational and reliable every minute of every day. 

Globally improving our product and software development practice will result in a higher quality product, with fewer errors and incidents. 
That will enable teams to be more efficient with their time and bias work toward preventative measures rather than reactive measures post incident. 
In order to do this, we essentially have 2 levers:

- Manual engagement and approval with all teams building features for Gitlab
- Build tools and frameworks to make the right thing the easy thing to do

In FY25, much of our activity as stewards requires ICs to engage with teams and onboard onto a problem in order to drive towards an optimal outcome.
This has two major drawbacks, the first of which is that this process is slow and places a high burden on all team members involved to build context and understanding. 
The second is that, since this process is not scalable, many items that should have had review from our stewards slip through and eventually impact customers and in some cases impact customers the same way as previous incidents ([INC-18003](https://gitlab.com/gitlab-com/Product/-/issues/13406#note_1936034718), [INC-18548](https://gitlab.com/gitlab-com/gl-infra/production/-/issues/18548)).

To drive progress in this area, we will:
- Shift things left
- Invest in best practice tools and frameworks
- Create Education programs based on paved roads
- Drive cultural change & increase ownership on groups
- Raise the bar for features to hit GA

Many of theses domains, such as logging and rate limiting, require tight integration and collaboration with teams developing GitLab features. 
For example, rate limits are simpler to implement during feature development, but become exponentially harder to introduce as a feature gains adoption.

Improvements in this area will likely be driven by having [availability metrics better reflect the user experience](https://about.gitlab.com/direction/saas-platforms/scalability/#availability-metrics-better-reflect-the-user-experience), [enabling experimental deployments](https://about.gitlab.com/direction/saas-platforms/delivery/#enable-experimental-deployments) and [release channels](https://about.gitlab.com/direction/saas-platforms/delivery/#release-channels-on-com) as well as [increasing the number of paved roads](https://about.gitlab.com/direction/saas-platforms/scalability/#paved-roads-are-the-default-for-all-team-members) for team members to traverse.

### Unlock faster innovation by introducing different software delivery models

Runway introduced a new paradigm (to GitLab) for delivering software to customers. 
In FY25 Runway supported [multi region deployments](https://docs.runway.gitlab.com/guides/multi-region/), in many locations across the world for customers that wanted to use our hosted Duo AI powered services. 
In FY26, Runway will GA a new runtime, [aligned with our long term vision](https://docs.runway.gitlab.com/reference/blueprints/satellite-services-vision/), that will allow easy delivery of services built on Runway to Self Managed customers and expand to support more workloads across GitLab.

We expect this new paradigm to unlock new possibilites for stage teams and accelerate our time to value for new and innovative products like [GitLab Secrets Manager](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/secret_manager/). 
This will also drive opportunities to "Land" in categories that previously we looked to "Expand" into.

[Cells](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/cells/infrastructure/) also presents an opportunity to further innovate on our software delivery models and overall multi tenant product offering. 
Growth in this area will likely take the form of product offerings like per cell/customer Geo, exclusive customer cells, private connections and/or private runners. 
Cells will be the foundation on which these new product offerings are integrated into gitlab.com and SaaS Platforms teams must design future solutions with this in mind.

### In the direction of "Build it --> Run it" model

We know that this is something that will only scale linearly and with an increased number of services, the number of engineers we need to support those services will grow at an accelerated rate as will the organisational toil and management overhead to serve that increasing number of engineers.

![Runway Scale Model](./scale-model.png)

The best way to scale our organisation logarithmically, whilst supporting an increasing number of services, is by empowering teams to own and operate the services that they build.
Runway, our first self serve paved road for teams, is taking the first steps on this path as teams can make decisions on what infrastructure they need for their product/feature wihtout needing to speak to an SRE.
Eventually, we want teams building the features to design, build, own and operate their features end to end.
As we know from the [most popular book on the topic](https://sre.google/sre-book/introduction/), teams that own their services end to end and hold the pager are highly motivated to build reliable and performant features that don't page them at 2am.

This is a large scale cultural change and we will need to transform what operational support looks like at GitLab today.
We'll also need to partner with our people group and other functional leaders to understand what we can do and on what timeline.
Lastly, we'll need to level up our tools and education programs to make sure that teams can hit the ground running.

Early indicators of success here could look like:

- Teams deployed on Runway operate their own services
- More team members outside of SaaS Platforms hold pagers
- We have a documented, tiered support framework

### What we're not doing

Example of what we are not doing:

- We're not launching a separate GitLab EU service, this will be considered as part of our extended Cells work
- We're not offering user customisable versions for GitLab.com, GitLab.com will continue to recieve continuous deployments

## What's Next

For a Look at the work in progress and what's next, you can stay up to date with our in progress epic and our roadmap epics:

- Delivery
    - [Releases](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1276)
    - [Deployments](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1277)
- Production Engineering
    - [Runway](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/969)
    - [Observability](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1295)    
    - [Foundations](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1175)
    - [Ops](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1176)    
- [Cells](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1296)
