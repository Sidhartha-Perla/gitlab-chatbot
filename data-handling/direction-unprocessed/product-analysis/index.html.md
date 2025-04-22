---
layout: markdown_page
title: Product Direction - Product Data Insights
description: "Explore GitLab’s product analysis roadmap, helping teams understand usage trends and product performance for continuous improvement."
canonical_path: "/direction/product-analysis/"
---

## On this page
{:.no_toc}

- TOC
{:toc}

## Product Data Insights overview
{:.no_toc}

The Product Data Insights team (formerly known as "Product Analysis") was created in October
2020 to provide dedicated, specialized analytics resources for the GitLab Product division
and to support product data-related analysis. In June 2024, the team expanded its scope to
support all of R&D (including Engineering). The team consists of product analysts, and reports
to the VP, Product Management. The team's primary customers are Product and Engineering Managers
across all sections, stages, and groups.

In addition to working with the Product and Engineering organizations, Product Data Insights
works closely with the [Customer Product Adoption (CPA) Pod](https://handbook.gitlab.com/handbook/enterprise-data/organization/#data-pod-assignments),
enabling collaboration between the product analysts and analytics engineers on the
[Enterprise Data team](https://handbook.gitlab.com/handbook/enterprise-data/). Product Data Insights is also a member
of the [Functional Analytics Center of Excellence (FACE)](https://handbook.gitlab.com/handbook/business-technology/data-team/functional-analytics-center-of-excellence/),
a group of functional analytics teams across GitLab.

## Vision

Simply put, the Product Data Insights team is charged with supporting product usage data-related
needs across GitLab. While the scope is quite broad, the team is organized to maximize support
of the Product and Engineering divisions, while protecting time for cross-functional initiatives.
The Product Data Insights team delivers actionable insights that help the Product division make
responsible, data-driven decisions in feature development, prioritization, and improving the
user experience. In addition, they help the Engineering division understand team productivity.
Part of Product Data Insights' role is also to enable greater self-service of product-related data and
follow GitLab's [handbook-first approach](/company/culture/all-remote/handbook-first-documentation/)
to build a strong remote culture.

## Working with us

You can read about the Product Data Insights team's issue intake, prioritization, and team
processes on their [handbook page](https://handbook.gitlab.com/handbook/product/groups/product-analysis/).

### R&D organization support

To maximize the team's ability to support a large R&D organization, Product Data Insights
is structured so that a single analyst supports a [section (or sections)](https://handbook.gitlab.com/handbook/product/categories/#devops-stages)
and/or the Engineering division. This gives analysts the opportunity to build subject matter
expertise in an area of the product and the data associated with it. In addition, it provides
both analysts and stakeholders (PMs or EMs) with a consistent counterpart for their data-related
needs. The analyst is intended to be an embedded member of the Product team to encourage closer
collaboration and increase the impact of analysis on the product.

### Data program collaboration

As a functional analytics team, Product Data Insights is reliant on other teams within the Data
Program to provide high-quality, easily-accessible data. As such, the team collaborates
closely with the [Enterprise Data team](https://handbook.gitlab.com/handbook/enterprise-data/) and
[Analytics Instrumentation group](https://handbook.gitlab.com/handbook/product/analytics-instrumentation-guide/).
Here is a quick summary of the responsibilities of each of these 3 teams:

| Team Name | DRI | Goal | Example Tasks |
| --- | --- | --- | --- |
| Product Data Insights | Carolyn Braza: Senior Manager, Product Data Insights | Perform analysis to unlock product insights and champion data-driven product decisions; Build and maintain meaningful Engineering Productivity metrics | Perform ad hoc product analysis; create and maintain standardized Product or Engineering metric dashboards; consult on data collection, instrumentation, and modeling |
| Analytics Instrumentation | Tanuja Jayarama Raju: Senior Product Manager | Define and improve capabilities of product data set | Build reliable and scalable tooling for product data instrumentation and collection; ensure our product data collection adheres to our [commitment to user privacy](https://handbook.gitlab.com/handbook/product/analytics-instrumentation-guide/service-usage-data-commitment/); empower team members to create new instrumentation, charts, and dashboards in a self-service fashion |
| Data Team | Israel Weeks: Director, Data and Analytics | Build and maintain product data models and infrastructure to support data analysis | Create repeatable and reliable product data sets, models, related data pipelines/processes; adhere to Trusted Data standards |

#### High level collaboration workflow between the three teams
{:.no_toc}

1. A data question needs to be answered with product data, the requester [opens a Product Data Insights
issue](https://gitlab.com/gitlab-data/product-analytics/-/issues/new?issuable_template=Ad%20Hoc%20Request)
1. Product analyst triages issue and determines if the required data is available and accessible
   1. If the required data is not currently collected (or there is an issue with the collection),
   work with Analytics Instrumentation and/or Product teams to start collecting it
   1. If the required data is collected but not exposed (ex: it is in the PREP database), work
   with the Enterprise Data team to surface and/or model the data
1. Product analyst performs the analysis, creates a dashboard, etc
1. Product analyst determines if the analysis needs to be repeatable or there is an opportunity
to improve data modeling
   1. If applicable, work with the Enterprise Data team to create a trusted data model to enable
   future analysis

## Helpful resources & links

1. [Product Data Insights handbook](https://handbook.gitlab.com/handbook/product/groups/product-analysis/)
1. [Product Data Insights project](https://gitlab.com/gitlab-data/product-analytics)
1. [Data Catalog](https://internal.gitlab.com/handbook/enterprise-data/data-catalog/)
1. [Data for Product Managers](https://handbook.gitlab.com/handbook/enterprise-data/programs/data-for-product-managers/)
1. [Enterprise Data team handbook](https://handbook.gitlab.com/handbook/enterprise-data/)
1. [Functional Analytics Center of Excellence (FACE)](https://handbook.gitlab.com/handbook/enterprise-data/functional-analytics-center-of-excellence/)
