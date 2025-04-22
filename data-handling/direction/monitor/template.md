---
layout: markdown_page
title: "Stage Direction - Monitor"
description: "Stay informed on GitLab’s monitoring tools that provide real-time insights into system performance and application health, ensuring smooth operations."
---

- TOC
{:toc}

# What we do

## Vision

Our vision is to continue to extend DevOps across its most painful gap - measuring user value. The Analytics Section closes the DevOps loop. It is not enough to deploy an app and hope for the best. It is critical to understand and explore the data and signals that GitLab provides to make the best, insight-based decisions. We will do this by providing a comprehensive solution to gather and interact with data for both our users and internal teams.

This will increase the value of GitLab as a platform since users will have a unified experience. They will know where to find definitive locations for the data they are interested in and have a single place to interact with it. It will also make our organization more efficient since teams can focus on building lovable features rather than re-building how we collect, store, and present data. We will create new product experiences where we can combine data from different features for user use cases that we uncover that would have previously been difficult to serve.

We heard a collection of common questions when talking with users that helped us create this vision.

Some of these were:
* How can I understand and connect all the different features that GitLab gives me?
* How are my teams using GitLab?
* How can I create reports and visualizations to answer business questions I have?
* What sort of data do you collect about usage and how can I view it as well?
* How do I interpret multiple GitLab reports together?
* Where should I focus my efforts on improving my product in future releases?

We previously were primarily focused on helping customers measure the usage and performance of their deployed apps. This was done with our Product Analytics and Observability offerings. What we learned is that many customers either did not prioritize this highly or had solutions in place. What they do not have, and where our opportunity lies, is understanding how their teams are using GitLab or how to combine all the different data signals we provide today. We will use the technology we built for those use cases and adapt it to focus on our GitLab platform use cases instead. We will continue to listen to customers and engage with those that are interested in measuring their deployed apps and consider if and when to re-focus on deployed apps.

## Composition
The Analytics Section is comprised of a single Stage: the Monitor stage. This stage has two groups:

- [Platform Insights](https://about.gitlab.com/direction/monitor/platform-insights)
  - Custom Dashboards Foundation category
  - Observability category
  - Product Analytics category

  The Platform Insights group focuses on allowing users to analyze product data to uncover insights about how their teams are using GitLab and their apps are being used. This is done through preconfigured dashboard and reports as well as enabling users to build their own dashboards and reports.

- [Analytics Instrumentation](https://about.gitlab.com/direction/monitor/analytics-instrumentation)
  - Service Ping category
  - Application Instrumentation category

  The Analytics Instrumentation group focuses on empowering both internal and external users to send usage data to GitLab by providing SDKs and a stable reporting platform. Internally, this means tools like Service Ping and Snowplow as well as providing support to the groups that use them. External users will use the SDK that this group publishes to instrument their own apps. This group focuses on data unification efforts across the platform as part of the [product usage data](https://gitlab.com/groups/gitlab-org/architecture/gitlab-data-analytics/-/epics/3) efforts.

### The Analytics section DOES NOT INCLUDE all analytics in GitLab
Despite the name, the Analytics section doesn't encompass all analytics capabilities in GitLab. Categories like [Value Stream Analytics](https://handbook.gitlab.com/handbook/product/categories/features/#manageoptimize-group) and capabilities like [Issue Analytics](https://docs.gitlab.com/ee/user/group/#issues-analytics), [Release Metrics](https://docs.gitlab.com/ee/user/project/releases/#release-metrics), or [CI/CD analytics](https://docs.gitlab.com/ee/user/analytics/ci_cd_analytics.html) analytics those are not within the scope of the Analytics section.

## Cross-stage vision for GitLab usage analytics

We know that many groups and teams within GitLab as well as users rely on data to understand how they are using GitLab. There are multiple approaches to produce and consume data currently, which introduces confusion and friction. Our long-term vision is to unify these so that there is a Single Source of Truth for both how to record data about how GitLab is being used as well as how to consume it. There are additional details on this vision at our [cross-stage directional vision](./cross-stage-vision.html) page.

## How we do it

### Personas

The primary personas we address, in priority order, are:

1. [Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
1. [Parker - Product Manager](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)

Some nuance can be added to our personas and how we approach them. Nearly all analytics questions, workflows, funnels, or any metrics gathering will require technical work to add instrumentation, test, and deploy it. This is the reason we are focusing on Sasha as our primary persona before Parker. We are addressing Sasha in the context that they are supporting Analytics efforts for their team. This means they are interested in how to do tasks related to adding instrumentation code, deploying it, and debugging it in support of analytics-related questions and projects. This is a more focused version of the Sasha overall persona.

Both of these personas exist on our users' teams and they also exist on our own GitLab team. Our internal members share many of the same use cases and pain points as our external users. We keep this in mind when developing features and capabilities and try to dogfood as much as possible. We also need to remain mindful that while we share many use cases, we will not have _all_ use cases our external users have, so we should not build only for ourselves and not validate with external users. This aligns with our [you're not the customer](https://handbook.gitlab.com/handbook/product/product-principles/#:~:text=You%E2%80%99re%20not%20the%20customer.) product principle.

## Right to Win
We have the right to win in this Section because:
- **The value stream delivery process is integrating** - Gartner’s market definition of Value Stream Delivery Platforms ends at Deployment today. We expect it to extend to Monitor and then the outer-loop. If we don’t capture this market as part of our platform - someone else will.
- **Developer experience is key** - The current market is broken by poor developer experience. Capturing User Engagement insights in digital products requires developers. We already capture developer workflow, and we know how to delight developers.
- **Our distribution models are disruptive** - Our bottom’s up distribution model allows for adoption without displacement. Developers in larger organizations can instrument and utilize GitLab’s outer-loop categories alongside existing tools. In smaller organizations, they can utilize outer-loop tools as an alternative to using no tool.
- **We are trusted** - User data, like code - is sensitive data. The focus against third-party ownership of user data, and our availability as a SaaS and self-managed platform allow us to leverage the trust we’ve built as an open-source and transparent company. We are able to develop open-standards for data-storage, and enable contribution to how we handle data to ensure our users can trust it is safe.
- **The single DevOps Platform unlocks unique technical possibilities** - GitLab stores our users source code, issues, vulnerability records, and other project info. This gives us the opportunity to do associations and correlations that will not be possible to do (or at least not easily) on a standalone analytics product.

## Product Principles
We will pursue this opportunity with the following principles:
- [Focus on Developers](https://handbook.gitlab.com/handbook/product/product-principles/#developer-first) - We have established relationships with them, and they are key to building an onramp to the product and a [dual flywheel](https://handbook.gitlab.com/handbook/company/strategy/#dual-flywheels) to our strategy.
- [Works by Default](https://handbook.gitlab.com/handbook/product/product-principles/#configuration-principles) - The way we can establish bottom-up disruption is by making outer-loop categories available, on-by-default in every GitLab instance.
- [Focus on Next Generation Adopters](https://handbook.gitlab.com/handbook/product/product-principles/#prioritize-current-adopters) - Every company is becoming a software company, there are many more software experiences to be written than our written today. The market of tools spanning the outer-loop is segmenting and consolidating, there are many organizations who will be new to it. Focusing on them will allow us to concentrate our R&D effort on future platform growth rather than integration with existing vendors.
- [Integrate Open Source Standards](https://handbook.gitlab.com/handbook/product/product-principles/#avoid-not-invented-here-syndrome) - We will stand on the shoulders of giants and use open-source standards, particularly when considering product analytics instrumentation.
- [Dogfood](https://handbook.gitlab.com/handbook/product/product-processes/#dogfood-everything) - We should be our own first customer, utilizing our outer-loop capabilities to drive GitLab’s Product Led Growth amongst developers in order to accelerate our learning cycles.
- [Start with the problem, not the solution.](https://handbook.gitlab.com/handbook/product/product-principles/#our-product-principles) - We will focus on what is impactful for our users and solves real problems for them. There will be temptations to record more data or create more views but we will not do so unless we can first identify who would want to use that and what they would use it for.

## Where we're going

Thematically, our direction centers around:

- **Data Completeness** - Adding the data that users need but are missing from the GitLab platform so that they can get the whole picture.
- **Experience Completeness** - Adding experiences to allow customers to find what they need and consume data from GitLab in they ways they want so they don't need to leverage other tools.
- **Experience Usability** - Providing a consistent experience across GitLab as it relates to consuming and creating data visualizations, and reporting so that users can easily complete their tasks and other GitLab teams have a solid foundation to build on top of.

### 1 Year Plan

Our 1 year plan is to:
- **Build the platform which internal teams use for visualizing and reporting data within the GitLab product.** - We will focus on providing a single method for creating visualizations, dashboards, and reporting within GitLab so teams can spend more time on addressing use cases and less time on rebuilding visualizations and so that customers will have consistent experiences across the product. We will allow teams to leverage data that they already have, not just from Product Analytics or Observability, to do this.
- **Unify the architecture used for product usage data** - Right now there are multiple approaches within the product with respect to how data is stored and managed for different features. We will work to support the work being done in the [product usage data](https://internal.gitlab.com/handbook/product-usage-data-architecture/) steering committe to provide a single way that product usage data is stored and managed.
- **Enhance our unified instrumentation approach** - We recently introduced a unified instrumentation method for Product Analytics, called [internal event tracking](https://docs.gitlab.com/ee/development/internal_analytics/), which allows seamless data tracking within GitLab, eliminating the need to delve into the intricacies of Snowplow, Redis, or Redis HLL. Our ongoing commitment is to iterate and improve on this, with the ultimate objective of encouraging more internal teams to effortlessly and promptly instrument their features.
- **Provide customer access to usage data** - In pursuit of our overarching goal to achieve the [cross-stage data vision](./cross-stage-vision.html), we will work towards enhancing accessibility of usage data for our SAAS and self-managed customers
- **Dogfood everything we build** - Dogfooding allows us to experience what our users experience - for better or worse. By using our own product, we can identify what needs to be fixed and better understand our users. Dogfooding Product Analytics in the [Internal Handbook](https://handbook.gitlab.com) and starting to use our [new instrumentation approaches](https://gitlab.com/groups/gitlab-org/-/epics/9610) will give us valuable feedback to iterate on.
- **Support the ongoing needs of GitLab in understanding our own users** - GitLab relies on our existing instrumentation and metrics frameworks, such as Service Ping, Redis, and Snowplow, to make data-driven decisions. We will remain focused on ensuring these are robust, scalable, and address any issues that arise.

## Deployment approaches

There is a discussion on the different deployment options related to our Product Analytics and Observability technology on our [deployments page](./deployments). This was particularly important for when we were asking customers to deploy ClickHouse and related services but since we will now focus on internal teams, it will be less work that we ask external users to do. It will also be updated over time as the [data unification efforts](https://gitlab.com/groups/gitlab-org/architecture/gitlab-data-analytics/-/epics/3) make progress and decisions on how to best bundle these services with GitLab.

## Handbook Pages
- [Analytics Instrumentation Group Engineering](https://handbook.gitlab.com/handbook/engineering/development/analytics/analytics-instrumentation/)
- [Observability Group Engineering](https://handbook.gitlab.com/handbook/engineering/development/ops/monitor/observability/)
