---
layout: markdown_page
title: "Cross Stage Vision for Analytics Data"
description: "This page describes the vision for cross-stage collaboration around analytics."
---

- TOC
{:toc}

This page describes the vision for cross-stage collaboration around GitLab usage analytics. Data collection, storage, and consumption methods will be provided within the GitLab product, so that users and internal team members can take advantage of it. The goal is to ensure that we have systems in place to collect relevant data to a single location and to empower different consumers of that data and help them collaborate with each other.

# The Challenge

There are many reasons to look at usage data from GitLab. Customers want to understand which features they are using from their license, product teams want to understand how features they built are being used, operations teams want to understand usage patterns for predicting load, and more. There's also a need to build reports in GitLab that look at historical data to help users understand their DevOps health and team performance. GitLab Inc wishes to understand how our product is used by both our GitLab.com and self-managed users. This means we have systems in place for GitLab.com that are different from self-managed.

Today there are multiple ways to both submit and consume this usage data to and from GitLab. This ranges from using [Service Ping](https://handbook.gitlab.com/handbook/customer-success/csm/service-ping-faq/) to collect counts to using [Snowplow](https://handbook.gitlab.com/handbook/business-technology/data-team/platform/snowplow/) to log full events to directly logging query results from Postgres. Teams that expose data within Gitlab have even more different solutions to collect data. Consuming that data could be done from in GitLab directly, using [Sisense](https://handbook.gitlab.com/handbook/business-technology/data-team/platform/sisensecdt/), [Gainsight](https://handbook.gitlab.com/handbook/sales/gainsight/), or others tools all of which have different sets of data available to view and often do not scale for large data sets.

Because of these different approaches, it is difficult to know how to properly add instrumentation and gather data, easily find answers to data-related questions, and incredibly difficult to collaborate with different functional groups, who all likely have a different set of data to work with. It is also likely individuals reach different conclusions to the same question because they have access to different data.

We have documented many of the [personas](https://about.gitlab.com/direction/monitor/analytics-instrumentation/#personas-that-we-work-with) that interact with this problem space and that we need to address. In addition to the problems above, many of these personas are unaware of each other and what their needs are. This leads to some personas, such as Product Managers, changing a metric without understanding how it affects other personas, such as Customer Success. When multiple groups are unaware of each other, they could each be solving the same problems and they could be doing it in ways that don't help or even negatively impact other groups.

# The Opportunity

We will work towards having a unified way of both collecting data and providing that data for consumption by providing a single source of truth for users, customers, product teams, customer success, and others to use. We will ensure that everyone can see the same information and reach the same conclusions.

Our vision is that the Analytics section will provide a single way for usage data to be recorded and consumed, with the [Analytics Instrumentation](https://about.gitlab.com/direction/monitor/analytics-instrumentation/) group and [Platform Insights](https://about.gitlab.com/direction/monitor/platform-insights//) group, respectively. Usage data, such as how many times a button has been clicked, when a feature is used, or when an activity like a deployment happens, can be recorded in a single way, stored in a single repository, and consumed later. We intend this to be used by our external users and customers as well as by GitLab to [dogfood](https://handbook.gitlab.com/handbook/product/product-processes/#dogfood-everything) what we build.

Once all data has been stored in a centralised data repository, this opens up many opportunities to build persona-specific reporting on top of it. We envision this data would be served:
- Directly back to end users for their review as part of the product
    - This could be in marquee features, such as [value stream analytics](https://about.gitlab.com/solutions/value-stream-management/), through text logs, or some combination.
- To Product teams to gauge feature success or need for improvement
    - Understanding if feature use is increasing or decreasing and how users engage with a feature is critical to determining next steps.
- Customer success and account teams to understand how their customers are doing with GitLab
    - Seeing what parts of GitLab are and are not being used is a way to ensure customers are getting the value they expect.

We will also support the larger vision for [customizable dashboards](/direction/customizable-dashboards/).

## Breaking it down

It is important to break the large picture described above down into more tangible pieces so they can each be discussed and described in more detail.

### Data recording

This will be provided as a single SDK that is then integrated into GitLab and user applications. The code in those apps will then call APIs in the SDK to log relevant information when it occurs. This SDK will provide ways to collect data from both the front-end and back-end of an application. This SDK will allow recording of individual raw events as they happen, computed aggregate events, or a combination of the two. Wherever possible, this SDK will speak to use cases that can be done with it, rather than technologies used to implement it (for example, an API might be about "counting unique users" rather than "create a RedisHLL counter" like we have today).

This SDK will also allow (and will highly encourage) metadata to be provided for all information provided. Today we have the GitLab [Metrics Dictionary](https://handbook.gitlab.com/handbook/product/analytics-instrumentation-guide/#metrics-dictionary) to display metadata about every action that we instrument and it is very valuable since it lets people understand more about the data, what it is, and how they might use it without needing to directly view the code base of the application. The SDK will make it easy to do something similar so that it is easy to understand the data being collected and not needing to do a technical deep dive to figure out what is going on.

### Data storage

We will provide a single solution for all collected data, regardless of type, to be sent to and stored. Our current vision is this will be an instance of ClickHouse, which is what Platform Insights and several other teams at GitLab are [already building on top of](https://handbook.gitlab.com/handbook/engineering/development/ops/monitor/observability/#clickhouse-datastore). By providing a centralised repository for data to be stored, it makes it easier to reason about how data collection and retrieval should be done.

This will be our long term focus given [the challenges](https://docs.gitlab.com/ee/architecture/blueprints/clickhouse_usage/#non-goals) of using ClickHouse on self-managed instances.

### Data consumption

Since all data will be stored in a [single location](#data-storage), it will be possible to provide multiple persona-specific ways to access that data and ensure that they are all built off of the same source of truth. This means each persona can be confident that they are viewing the data most interesting to them but also that it is correct and not in conflict with the data set another team is using.

We envision that whenever we collect a metric or piece of data, it will be possible to view that data directly within the GitLab product. This may be in the form of a marquee feature or it may be in a screen that allows downloading data in a CSV file. We will decide how to best display this data in the product based on the data type, the personas it informs, and how useful it is. This will enable all personas to see the information within GitLab and not require another tool to view it. If desired, they may then take the data and reformat & re-process it for their own needs (possibly using another tool). If we find users doing this often, that is a good signal for us that we should build their approach as a feature.

Providing a single place to access data makes it easier for different personas to talk to each other about data since they both have the full context available. As an example, an account team could notice that a customer has not been using a new feature that they expressed interest in. They could point the customer to the usage data so that the customer could also see that they have not been using the new feature. This would then let them have a conversation, backed by data, about how to start using the feature more or if there is an issue.

Because multiple groups benefit from this, we expect contributions from and collaborations with many of these other groups. This is discussed in more detail [below](#who-s-involved).

## What's next and why

In FY23 Q3, [we interviewed](https://gitlab.com/gitlab-org/analytics-section/analytics-instrumentation/internal/-/issues/671) different personas that interact with Gitlab usage data to understand their needs around it. Understanding these use cases helped us define and execute a roadmap that works for everyone.

In the coming quarters we will focus on the following work items:
- The old way of using multiple collection systems to record data is now deprecated in favor of a single interface called [internal events](https://docs.gitlab.com/ee/development/internal_analytics/).We will continue to cover a [wide range of use cases](https://gitlab.com/groups/gitlab-org/-/epics/11903) with internal events so that users don't have to look for other ways to track usage data.
- [Simplifying instrumentation](https://gitlab.com/groups/gitlab-org/-/epics/11904) using internal events after exploring different solutions so teams can more efficiently instrument their features.
- [Ensuring metadata on events and metrics that are recorded is more easily and always collected](https://gitlab.com/gitlab-org/gitlab/-/issues/428014) on [Metrics Dictionary](https://handbook.gitlab.com/handbook/product/analytics-instrumentation-guide/#metrics-dictionary). This is so that teams understand more about the data, what it is, and how they might use it without needing to directly view the code base of the application.
- Exploring ways of reducing the gaps in the granularity of the data collected between self-managed and SAAS so that this data can be more easily combined and compared when aggregated upon from a single storage.
- [Continuing to improve on internal events](https://gitlab.com/groups/gitlab-org/-/epics/10700) based on feedback from teams
- Ensuring our external customers have access to the data we are recording and can service insights more easily from it. Here, we will [focus on self-managed](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/4594) customers in the short-term and SAAS customers in the long term
- Continuing to dogfood Platform Insights features for Gitlab usage analytics

On the long term, we will focus on the problem of GitLab usage data stored in multiple places which can cause incomplete or incorrect data to be presented to users. Our vision is to have a single data store for GitLab usage data to ensure consistency for the personas who want to access the data.

## Decisions and tradeoffs

Part of the reason for the multiple different approaches to data collection and consumption is because users have a myriad of different needs when it comes to data. Several of these tradeoffs are listed below:

### Event granularity

There is a tradeoff between exposing raw data and measures that are computed from raw data. Raw data is definitive and comprehensive at the cost of being an incredibly large data set. Aggregate measures computed from raw data (e.g. number of users per month using a given feature) are more compact at the cost of being a lossy transformation.

We have found that most people we have talked to are most interested in aggregate measures more than raw data. Understanding Monthly Active Users (MAU), how many users are using a given feature, if a capability is being used or not are the most common workflows we hear about, compared to understanding the individual click events that feed into those aggregate measures. There are usually privacy concerns when individual events are discussed. Users don't mind us understanding overall pictures that aggregate measures provide, but are uncomfortable when individual actions are measured. Individual events are also very high volume which it makes it more difficult to manage them effectively.

As a result, we plan to primarily focus our efforts on providing aggregate measures. Aggregate measures make the scale of the problem more manageable and can surface insights more effectively than raw data. Aggregate measures are also more privacy friendly for end users. We intend to collect certain usage data from our customers and they will be more amenable to sharing aggregate data with us than raw events. Raw data can be useful for low-level analysis but won't be our primary focus.

Notably, the raw data will be available to look at if so desired by directly viewing the databases storing the data. This means that for GitLab.com, it will be possible for internal teams to examine raw data if that is useful to them.

# Who's Involved

This vision is large and will encompass multiple groups and teams within GitLab to make it a reality. This section highlights several groups that are involved and their responsibilities. This is by no means exhaustive and this section can be expanded as needed.

All involved parties are encouraged and expected to provide feedback and input so that we can gauge what is working well and what needs improvements.

`group::analytics instrumentation` - The Analytics Instrumentation group is responsible for providing a single way to record data and submit this data to GitLab for storage. They are also responsible for maintaining these systems so that they are robust and efficient under load. This group is not responsible for implementing tracking for every feature within GitLab. More details about this group is on their [direction page](https://about.gitlab.com/direction/monitor/analytics-instrumentation/).

`group::platform insights` - The Platform Insights group is responsible for providing the place for data to be stored and ways for users to consume it with APIs. This group will provide a minimal way to consume all data, so we can meet the goal of exposing all collected data within the product. This group will provide tooling to be able to create visualizations for collected data.

The group will also build on top of the APIs to provide ways to consume certain data visually. The group will provide several visualizations but will not be responsible for implementing every desired visualization. More details about this group is on their [direction page](https://about.gitlab.com/direction/monitor/product-analytics/).

`All product groups` - Each individual product group best understands the features it works on and the relevant metrics for it. Each of those groups is responsible for using the provided SDK and APIs to add instrumentation to their own features to submit data.

Product groups can also leverage the stored data and build features on top of this. An example of this is how we would envision the [Value Stream Management](https://about.gitlab.com/direction/plan/#value-stream-management) dashboards being built on top of the stored data we collect.

`Data team` - The data team is responsible for analyzing the data to uncover insights from it. These insights could then be surfaced in custom reports or built back into the product.

`Customer success` - Customer success is responsible for using the collected data to understand how well customers are able to use GitLab or if they need assistance. They can use the collected data to build reports, such as [customer health scorecards](https://handbook.gitlab.com/handbook/customer-success/customer-health-scoring/), to achieve this. They can also work directly with customers to discuss what they are seeing and show the customers the exact same data set in the product.

`End users` - End users will look at the data visualizations we provide as well as the raw data that is stored to understand their own usage. They may then either build custom reporting that they need or request GitLab to provide additional features on top of it.

