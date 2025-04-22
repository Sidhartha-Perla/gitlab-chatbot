---
layout: markdown_page
title: "Product Direction - Observability (Internal)"
description: "The Observability team at GitLab is responsible for observability and related critical business processes like Capacity Planning across our SaaS platforms"
---

- TOC
{:toc}

## Overview

The Observability team is responsible for the observability of GitLab at scale.
This includes architecting, rolling out and operating our global observability platform that powers our SaaS Platforms.
In addition, the Observability team runs our related business critical process like capacity planning and error budgets reporting.

## Challenges
<!-- Optional section. What are our constraints? (team size, product maturity, lack of brand, GTM challenges, etc). What are our market/competitive challenges? -->

Observability of a distributed monolith is complex.
There are many teams that own code inside one project in the GitLab codebase and working out who is responsible for performance issues requires mapping pieces of code to teams across the company.
To combat this, we have created feature categories within our error budgets so that we can attribute any performance or availabiltiy issues directly to the teams that can take action on them.

Observability is only going to become more challenging as our fleet grows.
Both Cells and our Dedicated instances need observability that is durable and capable of operating independently of a global service, without losing data.
At the same time, we need to provide observability for the entire fleet and drive attention to actionable notifications when issues occur.
There is a limit to how far humans can scale and so we have to ensure that our observability and processes can scale atomically at the instance level and globally to our fleet.

## 1-Year Plus Plan

<!-- Describe key themes, projects, and/or features planned over the next year. Also highlight what we will not be doing in the next year -->
For FY 26, we’re prioritizing investment in the following capabilities, which are linked to our [group 3-5 year strategy](/direction/saas-platforms/production-engineering#3-5-year-strategy):


### Building on the Foundation of Scalable Observability

#### Re-Architecting the Logging Stack

The team will re-architect GitLab’s logging infrastructure by optimizing the ingest pipeline and migrating our logging systems to a unified, standardized solution that ensures better scalability and improved observability across the platform. We will build the system to support the best logging tools that suit our requirements, including creating a Single Pane of Glass (SPOG) to view logging and metrics data side by side, enhancing granular access controls, and standardizing logging fields, while also improving observability through SLIs, SLOs, and availability metrics.

The existing log ingestion pipeline and tooling needs significant optimization to handle GitLab's present and future scale. If we don’t invest here, we risk being overwhelmed by complexity, leading to slower issue detection, growing costs, and greater operational overhead. By focusing on optimizing these systems, we ensure that we can support GitLab's growth and maintain our commitment to operational excellence. This project will not only enhance the reliability of our observability platform but also help streamline the entire log management process, reducing noise and improving the signal-to-noise ratio for more effective decision-making.

#### Next Generation Service and Metrics Catalog

With the growing complexity of our services, it’s becoming increasingly difficult to maintain a consistent, comprehensive and easy to manage view of all the metrics across GitLab’s diverse infrastructure. The Next Generation Service and Metrics Catalog is an initiative that will provide a centralized, organized registry of all metrics, services, and their interdependencies. This catalog will be a critical tool for engineers and product teams to efficiently collaborate in order to interpret metrics, identify bottlenecks, and prioritize improvements.

By shifting-left and making it easier for engineers and teams to contribute directly to the observability stack, the Service and Metrics Catalog will empower users to take more ownership of system operability. This initiative will provide a streamlined way for teams to integrate and monitor their services, enabling them to quickly identify performance bottlenecks and proactively address issues. By democratizing access to observability tools and data, we will ensure that all teams can act quickly and efficiently, enhancing overall platform stability and reducing dependency on central observability teams.

### Enhancing User-Centric Observability

#### Covered Experience SLIs

Understanding how users interact with GitLab and how different features affect the user experience is a critical piece of observability. In FY26, we will continue to build on our initial work with (First iteration of a User Journey SLI)[https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1393] and focus on expanding this framework across other areas of GitLab. By linking observability to [Covered Experiences using SLIs](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1510), we will create a more user-centric view of performance and reliability, and we'll be able to relate those to User Journeys. This enables  teams to prioritize work that directly impacts users on the critical Journeys through the application.

[Covered Experiences](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1524#are-these-related-to-covered-experiences-fka-user-journey-slis) provide a more holistic view of the user experience, which is essential for aligning technical goals with business objectives. While observability has traditionally focused on system performance and resource usage, Covered Experiences shift the focus to actual user experiences, making it easier to prioritize improvements that have the most significant impact on customer satisfaction. Because covered experiences map directly to User Journeys, we can use these measurements to inform decisions the product team needs to make. By investing in this area, we’ll be able to better track the health of our features from the perspective of the user, allowing us to address pain points more effectively and improve our overall service delivery.

### Observability Units: Local and Global Observability

### Supporting the Rollout of Cells

As the Cells architecture progresses, we need to prepare for both local and global observability. Cells 1.0 is expected to roll out in mid 2025, and a supporting observability stack is required to ensure this is successful. This includes developing observability tools that can function independently at the local cell level, while still being able to roll up into a global view across GitLab’s fleet.

The introduction of Cells will add a new layer of complexity to GitLab’s infrastructure, but by aligning our observability efforts with the Observability Units initiative, we can ensure scalability across all GitLab tenants. By designing observability tools that operate independently at the local cell level but can also roll up into a global view, we will create a modular framework that makes it easier to scale observability as we expand. This approach will not only improve our ability to monitor and troubleshoot performance at both the cell and global levels, but it will also streamline the process of extending observability across the entire GitLab fleet.

### A note on 'keeping the lights on'

As part of the Scalability Group’s responsibility to scale GitLab.com, there is a significant amount of operational load on the team.
We regularly swarm around issues and production incidents, helping teams to quickly identify, root cause and solve GitLab.com problems.
This work will typically be prioritized ahead of any project work to ensure that gitlab.com customers are not disrupted.
### What we're not doing

Based on the above priorities it is unlikely we will make significant progress on some of our other Categories without reprioritization. This includes: Metrics, Distributed Tracing, Error Tracking, Error Budgets, and Capacity Planning.

## Categories
<!-- Provide brief descriptions of stage + category direction, along with links to supporting direction pages -->

- [Category Board](https://gitlab.com/groups/gitlab-com/gl-infra/-/epic_boards/1060230)
- [Error Budgets](https://handbook.gitlab.com/handbook/engineering/error-budgets/)
- [Infrastructure Cost Data](/direction/saas-platforms/cost-data)
- [Capacity Planning](https://handbook.gitlab.com/handbook/engineering/infrastructure/capacity-planning/)
- Observability Stack

## What's Next

For the most up-to-date information about our work, please see our [Roadmap](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1295).
