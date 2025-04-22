---
layout: markdown_page
title: "Category Direction - API"
description: "This GitLab product category is focused on GitLab's APIs and related tooling. Find more information here!"
canonical_path: "/direction/foundations/import_and_integrate/api/"
---

- TOC
{:toc}

## API

| | |
| --- | --- |
| Stage | [Foundations](/direction/foundations/) |
| Maturity | [Viable](/direction/#maturity) |
| Content Last Reviewed | `2023-07-27` |

### Introduction and how you can help

Thanks for visiting this category direction page on API in GitLab. This page belongs to the [Import and Integrate](https://handbook.gitlab.com/handbook/product/categories/#import-and-integrate-group) group of the Foundations stage and is maintained by the group's Product Manager, [Magdalena Frankiewicz](https://gitlab.com/m_frankiewicz) ([E-mail](mailto:mfrankiewicz@gitlab.com), [Calendly](https://calendly.com/gitlab-magdalenafrankiewicz/45mins)).

API category is a special one within GitLab product. The GitLab API enables other applications and services the ability to integrate with the GitLab application. Import and Integrate group supports cross-cutting needs while each Product area is responsible for their API features/functionality. Below we share list of issues and epics that belong to API category and Import and Integrate group.

This direction page is a work in progress, and everyone can contribute:
 
- Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=Category%3AAPI&label_name%5B%5D=group%3A%3Aimport%20and%20integrate&first_page_size=20) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=Category:API&label_name[]=group::import+and+integrate) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
 - Please share feedback directly via email, Twitter, or on a video call. If you're a GitLab user and want to discuss how GitLab can improve Importers, we'd especially love to hear from you.

### Strategy and Themes

<!-- Describe your category. Capture the main problems to be solved in market (themes). Describe how you intend to solve these with GitLab (strategy). Provide enough context that someone unfamiliar with the details of the category can understand what is being discussed. -->

GitLab offers a REST and GraphQL API to give customers options on how to best integrate with GitLab. Until now, we have not developed a cohesive strategy that optimizes for parity between them and efficiency in maintaining both implementations.

Import and Integrate group facilitates the discussion around our APIs with a key objective of improving usability, reliability, and performance for customers and partners in our ecosystem.

To identify the key areas of focus and foster cross-functional support, we've established a working group to drive these topics forward.

The [Import and Integrate group](https://handbook.gitlab.com/handbook/product/categories/#import-and-integrate-group) will focus on creating a joint REST and GraphQL API strategy and other possible improvements like:

* Testing our [POC for a REST wrapper over our GraphQL API](https://gitlab.com/gitlab-org/gitlab/-/issues/363795), dubbed `Raisin`.
* Exploring mechanisms for [Automated Documentation](https://gitlab.com/groups/gitlab-org/-/epics/5792), ideally generating OpenAPI specs based on our REST APIs.

### Vision

We will guide and enable GitLab to adopt and reinforce an API First and GraphQL First approach to development. Through a combination of best practices, policies, API standards, and tooling, we'll enable developers to build features in a way that increases velocity, transparency, accessibility/usability of data by developers across the many personas of API users that not only use, but depend, on our APIs - our internal GitLab users, our customers, Technology Partners, and 3rd party maintainers.

### 1 year plan
<!--
1 year plan for what we will be working on linked to up-to-date epics. This section will be most similar to a "road-map". Items in this section should be linked to issues or epics that are up to date. Indicate relative priority of initiatives in this section so that the audience understands the sequence in which you intend to work on them. 
 -->

Please be aware that we are putting API category in maintenance mode from FY24Q2 (May 2023) due to lack of resources. There will be no dedicated investment in this category until further notice. We will revisit this in planning for FY25.

We will only support the most critical and severe bug fixes with significant business impact while we shift our attention to improve high-priority importers, GitLab to GitLab importer, GitHub importer and BitBucket Server importer.

