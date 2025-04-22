---
layout: markdown_page
title: Product Direction - Analytics Instrumentation
description: "Analytics Instrumentation manages a variety of technologies that are important for GitLab's understanding of how our users use our products. Learn more here!"
---

## On this page
{:.no_toc}

- TOC
{:toc}

## Vision

GitLab's [3-year strategy](https://internal.gitlab.com/handbook/company/three-year-strategy/) centers on empowering our customers by driving [use case adoption](https://internal.gitlab.com/handbook/company/three-year-strategy/#pillar-2-drive-use-case-adoption). By offering intuitive and effective instrumentation tools that support the entire lifecycle, we empower teams to efficiently capture the data they need for informed, evidence-based decisions with minimal external support. This data-driven approach not only helps teams optimize their features but also provides both customers and internal teams with valuable insights into feature adoption, which is essential for driving broader use case adoption.

We will leverage our deep expertise and technical foundation to help users easily instrument their applications, analyze data, and optimize their experience. Through strong collaboration across GitLab—Product, Engineering, CSMs, Data and external customers—we are building a data-driven, product-led culture that fosters growth and success for both our customers and GitLab.

## Guiding principles
The key thesis of our group is that providing more visibility into how GitLab is used allows us to make better decisions which lead to better business outcomes for ourselves and our customers. In order to build the best DevOps product we can and provide the most value for our customers, we need to collect and analyze usage data across the entire platform to investigate trends, patterns, and opportunities. Insights generated from instrumentation enable GitLab to identify the best place to invest time and resources, which categories to push to maturity faster, where our UI experience can be improved, and how product changes effect the business.

We understand that usage tracking is a sensitive subject, and we respect and acknowledge our customers' concerns around what we track, how we track it, and what we use it for. We will always be transparent about what we track and how we track it. In line with our company's value of [transparency](https://handbook.gitlab.com/handbook/values/#transparency), and our [commitment to individual user privacy](https://handbook.gitlab.com/handbook/product/analytics-instrumentation-guide/service-usage-data-commitment/), our tracking source code and documentation will always be public.

As we build solutions for GitLab and our users to instrument their apps, aspects we will focus on are:

* Providing infrastructure and tools that enable teams to efficiently instrument with minimal support.
* Ensuring that the infrastructure we provide covers all relevant use cases across GitLab.
* Ensuring high instrumentation coverage across features to enable comprehensive insights.
* Ensuring the accuracy and reliability of the data we collect, so it can be trusted for decision-making.
* Adhering to legal and privacy policies to ensure compliance and protect user privacy.
* Ensuring that the data we collect can be transformed into actionable insights, enabling meaningful outcomes. This includes supporting data unification efforts, ensuring compatibility with downstream systems, and finding ways to directly report on the collected data.

## Roadmap (As of 2024-12-20)

- 🔴 **Not Started** – Work has not yet begun on this goal or initiative.
- 🟠 **In Progress** – Work is actively being done on this goal or initiative, but it's not yet complete.
- 🟡 **Under Review** – Work is complete or near completion, and is currently being evaluated for quality, impact, or alignment with goals.
- 🔵 **Implemented** – The solution or feature has been developed and deployed, but it may still need further improvements or refinements.
- 🟢 **Adopted** – The solution or approach has been implemented successfully and is now being used by the team or organization.
- ❤️ **Optimized** – The solution has been fully integrated, refined, and optimized for maximum efficiency and effectiveness.

| **Top Goals**                                                                                      | **Current Status**                                               | **1 Year Target**                                              | **Mid Term Target**                                           | **Reasoning**                                                                                                        |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Easy instrumentation:** _Providing infrastructure and tools that enable teams to efficiently instrument with minimal support_ | 🟢 Adopted                                         | 🟢 Adopted                                        | ❤️ Optimized                               | In the past few milestones, we've made significant improvements to simplify instrumentation. With [internal events](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/), teams no longer have to worry about the underlying complexity of different systems. With the [CLI generator](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/quick_start.html#defining-event-and-metrics), they no longer have to manually create event and metric definition files, and with the [metrics dictionary](https://youtu.be/NLquSWfWMII), they can more easily find the metrics they need. These and many other [improvements](https://gitlab.com/groups/gitlab-org/-/epics/10700) the team has worked on have made instrumentation much easier, and our ease of instrumentation scores have improved from 'hard' to 'very easy'. While we’ll focus on low-hanging fruits to improve ease of instrumentation this year, major improvements will be taken on the long term so we can prioritize moving to the green category for our other areas. You can track our work in this area [here](https://gitlab.com/groups/gitlab-org/-/epics/10700)|
| **Cover all use cases**                             | 🔵 Implemented                                         | 🟢 Adopted                                          | ❤️ Optimized                                | We now support instrumenattion outside of the GitLab domain in applications such as the [AI gateway](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/7198)and [Switchboard](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/8400). Our goal is to ensure teams can instrument features consistently and easily, regardless of their specific use case or platform. You can track our work [here](https://gitlab.com/groups/gitlab-org/architecture/gitlab-data-analytics/-/epics/13) |
| **Instrumentation coverage:** Ensure all our categories have instrumentation| 🟠 **In Progress**                     | 🟡 **Under Review**                                      | 🟢 **Adopted** | Ensuring complete instrumentation across all features is critical for maximizing data quality and enabling comprehensive insights. We'll continue to work on ensuring [instrumentation coverage on our lighthouse metrics](https://gitlab.com/groups/gitlab-org/-/epics/14859) and then move to ensuring all our [categories have instrumentation](https://gitlab.com/gitlab-org/gitlab/-/issues/458421) |
| **Data quality:** Ensure the accuracy and reliability of the data we collect for trusted decision-making. Adhering to legal and privacy policies to ensure compliance and protect user privacy      | 🟠 In Progress        | 🔵 Implemented                                     | 🟢 Adopted     | Ensuring data accuracy and reliability is critical for effective decision-making. While [we've made progress](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/3529), ongoing improvements are needed to ensure data integrity at scale. You can track our work [here](https://gitlab.com/groups/gitlab-org/-/epics/12643) |
| **Data to Insights:** Ensure the data we collect can be effectively transformed into actionable insights by our internal teams and customers| 🔵 Implemented                                         | 🟢 Adopted                                          | ❤️ Optimized                                | The data we collect is compatible with our downstream systems, maintained by the data team, and can be accessed through Tableau and Snowflake. Self-managed customers can more easily access aggregated metrics via the [REST API](https://about.gitlab.com/direction/monitor/analytics-instrumentation/#:~:text=for%20manual%20downloads.-,More%20here,-Complete). We aim to enable both customers and internal teams to access usage data more effectively and easily, ensuring they can derive value from it. We will actively [support product data unification effort](https://gitlab.com/groups/gitlab-org/architecture/gitlab-data-analytics/-/epics/38)s to ensure internal teams and customers can more easily derive insights from the data we collect.|


## Evolution of analytics instrumentation
<iframe width="560" height="315" src="https://www.youtube.com/embed/_D-C8B5vPS0" frameborder="0" allowfullscreen>
</iframe>

*In this [GitLab Unfiltered video](https://youtu.be/_D-C8B5vPS0) Niko is talking about the groups's approach to Analytics Instrumentation tools improvements and evolution*


## Personas that we work with

A key aspect of aligning on our direction is understanding who we are building for. This allows us to best understand the problems they may have and the context that they will be approaching our offerings with.

### Product groups within GitLab
Product [groups](https://handbook.gitlab.com/handbook/product/categories/) within GitLab consist of a Product Manager, Engineering Manager, engineers, and other stable counterparts. These groups implement new features in GitLab and want to understand how users interact with those features.
These teams have understanding of how the GitLab code base works as it relates to their features, but not necessarily how the instrumentation APIs and architecture work. They are not necessarily aware of the end-to-end story about how information flows from when a user clicks a button to a result being shown in Sisense or a report.

These product groups are our primary customer that we are serving and developing solutions for.

#### Product Manager personas

Consider reading more about [Parker](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager), our Product Manager persona.

Product Managers within these groups will have an understanding of how their group's features work from a user perspective, the problem those features solve, and what sorts of actions result in a user "succeeding" at the [job to be done](https://handbook.gitlab.com/handbook/product/ux/jobs-to-be-done/), and have growth and usage goals for that feature. They will be able to describe a user journey and key points that should be instrumented along that journey to measure success or need for improvement. They will not necessarily understand what the underlying code for the feature looks like or how all the technology pieces fit together. They need to be able to easily understand which kinds of tracking are available and how they are differentiated to be able to understand the resulting data.
If they find it difficult to add the instrumentation they want, they will instead rely solely on qualitiative analysis, such as direct user conversations, rather than a blend of both qualititative and quantitative analysis.

#### Engineer personas

Consider reading more about [Sasha](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer), our Software Developer persona.

Engineers within these groups will have an understanding of how GitLab is built and run but likely are not familiar with the product instrumentation architecture nor APIs. They heavily rely on documentation, examples, and previous MRs to add instrumentation that their PM requests. When they are unable to self-serve, they will ask the Analytics Instrumentation group for help or give up.

This persona relies on what we provide to them, which means it is critical for us to keep examples up to date and have clear guidance around deprecated APIs so that engineers use our newer, preferred APIs instead of older ones.

### GitLab Data program

The GitLab [data program](https://handbook.gitlab.com/handbook/business-technology/data-team/#data-program-teams) is responsible for surfacing data and data-driven insights to the business. They have expertise in building data pipelines, models, and managing data once collected.
They are not necessarily familiar with the GitLab code base and rely on product groups to add instrumentation for new metrics or update existing ones.
They rely on Analytics Instrumentation to effectively collect and send data to Snowflake, which is their main interface with the data.

### Customer success

Customer Success team members play a crucial role in partnering with clients to ensure they realize the full value of GitLab's offerings. Although they are experts in customer engagement and optimizing the GitLab experience, they may not have deep knowledge of the product’s instrumentation details. They rely on the Analytics Instrumentation group to help them easily find the relevant metrics and data for features and capabilities and to provide guidance and support on implementing missing instrumentation where needed. Effective support hinges on our ability to assist them in accessing the metrics they need and offering clear, actionable guidance for incorporating necessary instrumentation.

### External GitLab users

External GitLab users are a broad category of individuals with different needs and who have different skill sets. These users may be interested in reading about what data we collect and how to interact with it. In the future, external users will use the application instrumentation SDKs our group provides to be able to instrument their own apps.

External users rely on our handbook pages and sites like [metrics.gitlab.com](https://metrics.gitlab.com/) to understand what data is collected from their GitLab use, how to view it, and how to interact with it. If they are unable to get clear answers to their questions, they become frustrated. In that case, they may reach out to their account manager to help them, post on a forum, or stop using GitLab.

External users will use the application instrumentation SDKs we provide to instrument their apps. These teams will be similar to our own product groups within GitLab. That is, PMs will understand user journeys about their features, developers will understand how their own app is built, but neither will be familiar with our instrumentation SDKs. They will rely heavily on our documentation and examples or else they will give up and do something else.

## Challenges we face in Analytics Instrumentation

- GitLab's [single application approach to DevOps](https://handbook.gitlab.com/handbook/product/categories/gitlab-the-product/single-application/) creates a product that is both wide and deep, encompassing a large collection of features used by many teams within an organization, which are composed of different types of users.
- That depth/breadth makes it exceedingly complex to properly map out and understand how our diverse customer set is using the product and gaining value.
- We currently are unable to provide GitLab the required data to identify opportunities and make the right decisions against them.
- GitLab's MVC approach to product development introduces frequent changes to the product stages and what data is available, making historical trend analysis difficult.
- There are more and more supplementary applications outside of the GitLab instance, such as the [AI gateway](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist), that need their own instrumentation setup to get a full picture of product usage.

## Our opinion on automated tracking

It is a valid question to ask why analytics instrumentation can not be automated to a high extent by automatically tracking API hits based on the URL or button clicks in the UI.
While this would be the most usable solution, as it does not require any manual instrumentation, it is neither scalable nor manageable or adaptable:

* It would multiply the amount of events we receive, which would affect the effort needed for event processing. Querying the useful events will become slower and/or more costly due to the high amount of unneeded events. This can impact the reliability of the system as well.
* It increases the likelihood of personal data unintentionally leaking into event collection as API request parameters or button texts are collected.
* It is not clear which events are useful and which are not since there is no intent behind tracking a specific event. The same user interaction could be tracked through multiple automated events, like a UI click or an API hit.
* It does not obviate the need for instrumentation, since not all events can be automatically tracked, such as the results of an asynchronous computation.
* It creates a dependency between feature code and analytics code since automatic tracking by definition depends on implementation details such as the URI of an API call or the CSS selector of a button. This can lead to a resistance to feature changes since they could break tracking. Analytics instrumentation aims to benefit future feature development not hinder it.

Instrumentation should be easy as possible while still clearly documenting the intent to track a specific behavior and getting out of the way of feature changes.


## How We Work

For more information on Analytics Instrumentation, you can checkout our [Analytics Instrumentation Guide](https://handbook.gitlab.com/handbook/product/analytics-instrumentation-guide/) which details a [high-level overview of how we make data usable](https://handbook.gitlab.com/handbook/product/analytics-instrumentation-guide/#analytics-instrumentation-overview), the [Collection Frameworks](https://handbook.gitlab.com/handbook/product/analytics-instrumentation-guide/#collection-framework) we leverage, our [Metrics Dictionary](https://handbook.gitlab.com/handbook/product/analytics-instrumentation-guide/#metrics-dictionary), and much more!


## Working Groups and Cross-Functional Initiatives

Analytics Instrumentation provides the necessary frameworks, tooling, and expertise to help us build a better GitLab. Naturally we sit in the middle of many projects, initiatives and OKRs at GitLab. In order to provide clarity and realistic expectations to our stakeholders and customers we practice relentless prioritization ([per Product Principle #6](https://handbook.gitlab.com/handbook/product/product-principles/)), identifying what is above the line, what is below, and what is unfunded and not possible for us to action on in a given timeline.

This table lists recurring activities that are part of [working groups and cross-functional initiatives](https://about.gitlab.com/company/team/structure/working-groups/).

| Activity                                                                                                                           | Cadence       | Type | Teams Involved                                                              |
|------------------------------------------------------------------------------------------------------------------------------------|---------------|------|-----------------------------------------------------------------------------|
| [GTM Product Usage Data Working Group](https://docs.google.com/document/d/1riUXq1GdavnSWJklrebBeZnzcAl6XATyLod9tR6-AlQ/edit)       | Weekly        | Sync | Fulfillment PMs, Analytics Instrumentation, Data, Customer Success, Sales        |
| [Data & Analytics Program for R&D Teams](https://docs.google.com/document/d/1CRIGdNATvRAuBsYnhpEfOJ6C64B7j8hPAI0g5C8EdlU/edit)     | Every 2 Weeks | Sync | Fulfillment PMs, Analytics Instrumentation, Growth, Data                         |
| [Product ARR Drivers Sync](https://docs.google.com/document/d/1TxcJqOPWo4pP1S48OSMBnb4rysky8dRrRWJFflQkmlM/edit)                   | Monthly       | Sync | Customer Success, Sales, Product Leadership
| [ClickHouse Datastore](https://about.gitlab.com/company/team/structure/working-groups/clickhouse-datastore/) | Weekly | Sync | Multiple |

## Quick Links

| Resource                                                                                                                          | Description                                               |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [Internal Analytics Docs](https://docs.gitlab.com/ee/development/internal_analytics/)                                              | An implementation guide for Usage Ping                    |
| [Metrics Dictionary](https://handbook.gitlab.com/handbook/product/analytics-instrumentation-guide#metrics-dictionary)                                        | A SSoT for all collected metrics from Usage Ping               |
| [Privacy Policy](/privacy/)                                                                                                       | Our privacy policy outlining what data we collect and how we handle it     |
| [Implementing Product Performance Indicators](https://handbook.gitlab.com/handbook/product/analytics-instrumentation-guide#implementing-product-performance-indicators)                                   | The workflow for putting product performance indicators in place   |
| [Analytics Instrumentation Development Process](https://handbook.gitlab.com/handbook/engineering/development/analytics/analytics-instrumentation/) | The development process for the Analytics Instrumentation groups         |
| [Project resposibilities](https://handbook.gitlab.com/handbook/engineering/development/analytics/analytics-instrumentation/#responsibilities) | List of several projects that our group is the DRI for |
| [Incident Reporting](https://handbook.gitlab.com/handbook/engineering/development/analytics/analytics-instrumentation/#incidents) | Analytics instrumentation specific incident reporting process  |
| [Technical Roadmap FY25/FY26](https://gitlab.com/groups/gitlab-org/-/epics/15674) | The [technical roadmap](https://handbook.gitlab.com/handbook/engineering/#technical-roadmaps) for Analytics instrumentation. |
