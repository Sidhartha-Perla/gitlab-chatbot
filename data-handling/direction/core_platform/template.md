---
layout: sec_direction
title: "Product Section Direction - Core Platform"
description: "GitLab's Core Platform section is responsible for the features and tools our customers use to operate GitLab at all scales. Learn more here!"
canonical_path: "/direction/core_platform/"
---

{:.no_toc}

- TOC
{:toc}

Last reviewed: 2022-11-01

## Core Platform section overview

The Core Platform section is responsible for the features and tools our customers use to explore and operate GitLab at all scales. Core Platform supports customers from initial deployment of GitLab to ongoing operation, as well as cross-stage end user features.

The Core Platform section is made up of one eponymous non-DevOps stage, Core Platform, and eight groups:

* [Distribution::Build](#distribution) - Packages, Containers, Dependencies
* [Distribution::Deploy](#distribution) - Installation, upgrades, maintenance
* [Geo](#geo) - Disaster recovery and worldwide performance
* [Global Search](#global-search) - Global search and ElasticSearch integration
* [Cloud Connector](#cloud-connector) - Make it easy to build a feature across multiple types of deployment
* [Database](#database) - Database architecture and best practices
* [Tenant Scale](#tenant-scale) - Ensuring GitLab self-managed and SaaS deployments can scale for years to come
* [Git](#git) - Build Git upstream and provide expertise on how to use Git effectively and efficiently
* [Gitaly](#gitaly) - Providing fast access to repository data

### Mission

> Provide **users** with a consistently great experience and achieve customer business requirements by making GitLab easy to deploy, operate, scale, and use.

GitLab delivers value by enabling organizations to build better software, faster. The most important success metric for the Core Platform group is therefore the broader success of the user base of GitLab, rather than its administrators. We need to provide the software necessary to make it easy for an administrator to provide a delightful and productive GitLab experience to their users.

Within the single platform, users as well as contributors need a common set of cross-stage features and frameworks. End users need a set of common cross-stage features to make the broad array of features and content easily consumable. Contributors need a set of frameworks and developer tools to efficiently and safely contribute to GitLab's growing code base and data sets.

### Impact on GitLab's addressable market

There is no traditional addressable market for Core Platform due to its foundational, GitLab-specific nature. Every GitLab user is directly impacted, however, by the work Core Platform delivers.

In light of this, we think of Core Platform's addressable market as that of GitLab's larger addressable market. By working to ensure we can meet the operational, compliance, and usability requirements of GitLab's enterprise customers, we can capture increasingly larger percentages of GitLab's total addressable market opportunity.

There are two primary segments within the broader "GitLab" market: organizations that would like to operate their own GitLab instances (self-managed) and those who prefer to utilize a SaaS service (such as GitLab.com). SaaS revenue within the DevOps space is predicted to [overtake self-managed in 2022](dotcom/#market-opportunity), with our key competitors already capitalizing on this shift. This is confirmed by [analysts reports (GitLab confidential)](https://docs.google.com/spreadsheets/d/1bwv2FpP34UHdCGDqZyvoeUzG7rahCc06/edit?usp=sharing&ouid=104246595813126297495&rtpof=true&sd=true) as well as [others in the DevOps space](https://www.forbes.com/sites/robertdefrancesco/2019/08/31/atlassian-turns-its-focus-to-the-rapidly-expanding-cloud-business/?sh=338eea558803).

#### Self-managed

Today, we are able to capture most of the self-managed segment with our mature [linux packages](https://docs.gitlab.com/omnibus/README.html) and more recently our [cloud-native deployment options](../distribution/cloud_native_installation/) for Kubernetes and OpenShift. A proof point is GitLab's [two-thirds market share](https://about.gitlab.com/blog/2017/06/29/whats-next-for-gitlab-ci/) in the self-managed Git market. While this speaks to the competitiveness of GitLab's overall product, a critical enabling factor is the high-quality, flexible, and scalable software and operational tools.

While we are able to meet the requirements of most organizations, there are some unmet needs:

* Unsupported deployment targets for the GitLab Server, such as [Linux on Z](https://gitlab.com/groups/gitlab-org/-/epics/2176) and Power9
* Difficulty in deploying a topology to meet the most demanding [service level objectives](https://en.wikipedia.org/wiki/Service-level_objective)
* Effort required to deploy and operate is higher than desired, typically resulting in the adoption of a SaaS service or lighter-weight solution

#### SaaS

Today, GitLab is underperforming compared to our peers in the SaaS segment. While GitLab's SaaS revenue is accelerating faster than self-managed, our revenue mix is heavily weighted towards self-managed. IDC predicts that the market for public cloud SaaS-based DevOps tools (currently 52% of the market in 2021) will continue to accelerate and account for **$20.0B in revenue** (or 61% of DevOps software tools market) by 2026.1(#footnotes) This represents both a significant growth opportunity if we can better serve this segment, or risk if we fail to execute.

There are a larger number of unmet needs on GitLab.com than self-managed, which primarily fall into two buckets:

* Service level indicators, primarily [performance](https://handbook.gitlab.com/handbook/engineering/infrastructure/performance-indicators/#gitlab-com-performance) and [availability](https://handbook.gitlab.com/handbook/engineering/infrastructure/performance-indicators/#gitlab-com-availability)
* Product [feature gaps compared to self-managed](https://about.gitlab.com/features/), most importantly in the realm of [authentication and compliance](https://about.gitlab.com/direction/core_platform/dotcom/#top-strategy-items)

For GitLab's FY23, [SaaS First](https://about.gitlab.com/direction/#1-year-plan) continues to be a key theme, driving the closure of these gaps. From an Core Platform perspective, much of our work is on improving the performance, reliability, scalability, and efficiency of our SaaS services. The GitLab.com  strategy is [available here](/direction/core_platform/dotcom/), and a high level overview of GitLab Dedicated is [available here](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/).

### Resourcing and investment

The existing team members and open vacancies for the Core Platform section can be found in the links below:

* [Development](https://about.gitlab.com/company/team/?department=enablement-section)
* [User Experience](https://about.gitlab.com/company/team/?department=enablement-ux-team)
* [Product Management](https://about.gitlab.com/company/team/?department=enablement-pm-team)

### Metrics

All Core Platform section metrics can be found on the [Core Platform Performance Indicator (internal only)](https://internal.gitlab.com/handbook/company/performance-indicators/product/core-platform-section/) page.

### Competitive space and position

As noted above, GitLab's competitive position is a tale of two cities. We are the leading self-managed Git solution but are third in SaaS. Our success in self-managed has driven the majority of the company's growth, however it is at risk of being disrupted by growing trends in the market. IDC forecasts that by 2026, 61% of the worldwide DevOps software tools market will be delivered as public cloud services.1(#footnotes) Our SaaS services represents both a large opportunity and risk depending on our execution.


We need to achieve what could be considered opposing goals: making GitLab efficient and easy to run at [small scales](https://docs.gitlab.com/omnibus/settings/rpi.html) and improving the scalability and reliability at internet-scale.

## Challenges

* Due to much of GitLab's code being written by other groups, Core Platform relies largely on influence by defining best practices, policies, and frameworks to achieve stability and performance goals
* Rapidly increasing feature surface area, driving increased demand for compute resources and operational complexity
* Breadth of deployment targets (bare metal, VM, container, Kubernetes, cloud-specific, etc.) and configuration matrixes
* Increasing scale of GitLab.com, we are pushing the limits of our software and dependencies

## 3-year strategy

In three years we expect:

* SaaS to be the strongly preferred delivery mechanism for IT services
* DevOps platforms to be business-critical applications with very high SLA's required
* Kubernetes adoption to continue to accelerate for IT services, including GitLab
* Continued improvement of open source Git projects like [gitea](https://gitea.io/en-us/) and [gogs](https://gogs.io)
* DevOps platforms like GitLab to become deeply interwoven into organizational workflows and processes
* Competition in the DevOps space to continue to consolidate and intensify, as more companies adopt modern tools
* Single platforms becoming the preferred DevOps toolchain
* The global regulatory framework for cloud to continue to fragment

As a result, in three years, GitLab will:

* Generate more ARR on SaaS (such as GitLab.com) than self-managed
* Demonstrate market-leading service availability for both GitLab.com and self-managed
* Set the bar for IT apps delivered on Kubernetes
* Enable users to get started with self-managed GitLab in under 10 minutes at both 5 and 50,000 user scales
* Automatically highlighting similar content within large organizations
* Make it quick and easy to find the desired content across the platform
* Refine SaaS services that meet the regulatory requirements of major markets throughout the world, like [Dedicated](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/) or [FedRAMP (internal only)](https://internal.gitlab.com/handbook/engineering/fedramp-compliance/)

## Themes

### SaaS First

Woven throughout all of the below themes is a focus on improving our competitiveness in the [SaaS](#saaS) segment. As this is critical outcome for the company, it is worth highlighting individually our efforts to contribute.

#### GitLab.com

We are improving the service levels and efficiency of GitLab.com, our multi-tenant SaaS service. A multi-tenant cloud service is the best solution for most customers, combining low cost of ownership and fast time to value. Core Platform is specifically focused on a few key outcomes:

* Improving the responsiveness of the platform, and providing data for other groups to further target their own performance efforts
* Increasing the availability of the platform, achieving our 99.95% goal
* Improving the cost efficiency of the platform, from a cloud spend perspective as well as reducing the human maintenance burden

#### GitLab Dedicated

To serve the large enterprise and highly regulated SaaS market, we have recently launched [GitLab Dedicated](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/), a single-tenant SaaS offering. Core Platform will be focusing on improving the efficiency of operating individual GitLab tenants, by improving underlying tools like the [GitLab Environment Toolkit](https://gitlab.com/gitlab-org/gitlab-environment-toolkit), and our [Operator](https://docs.gitlab.com/operator/). By building in automation and self-healing capabilities, we can reduce the maintenance overhead required per instance, improving the efficiency and reliability of not just Dedicated but also self-managed deployments who also use these tools.

### GitLab is easy to deploy and operate

Deploying and maintaining GitLab should be as frictionless as possible for organizations of all sizes. This is critical for GitLab at multiple points in the customer journey.

GitLab starts as a personal or side project at many organizations, representing an important driver of initial adoption and awareness. Delighting future champions by providing a thoughtfully designed out-of-the-box experience that runs well on hardware they have lying around pays dividends in future growth.

Once a company is ready to adopt GitLab enterprise wide, it is similarly important to ensure the GitLab instance is set up for success with minimal effort. Consider our [5,000-user reference architecture](https://docs.gitlab.com/ee/administration/reference_architectures/5k_users.html) which recommends setting up at minimum 27 different instances, and that our [GitLab configuration file is over 2,000 lines long](https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/files/gitlab-config-template/gitlab.rb.template). This is a significant upfront investment to ask a company to make, prior to seeing value returned. It can also be error prone given the complexity, with the only practical solution to ongoing management being [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code), which requires further investment.

[Day 2 operations](https://dzone.com/articles/defining-day-2-operations) like backups, scaling, and upgrades are equally important. GitLab is a [business critical application](#consistently-great-user-experience-regardless-of-location-or-scale), so events like upgrades need to be routine and [seamless](https://docs.gitlab.com/omnibus/update/README.html#zero-downtime-updates). The easier we make it for our customers to upgrade, the faster our users will be able to leverage our new features and provide feedback. Currently it takes [over 3 months](https://app.periscopedata.com/app/gitlab/406972/Version-Upgrade-Rate) after release for a majority of our users to feel the impact of our work.

By reducing the deployment/operating costs and packaging best practices, we will see the following benefits:

* Increased downloads and trials of GitLab
* Shortened sales cycles as a result of quicker [time to value](https://en.wikipedia.org/wiki/Time_to_value) and lower [total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership)
* Improved typical end-user experience across all GitLab instances, with services more likely to be deployed optimally and on a recent version
* Further penetrate the SaaS-leaning market segment with self-managed for those where GitLab.com does not currently meet their needs
* Improved customer deployment security, productivity, and satisfaction due to a higher population of users on recent versions

To support these goals, we are:

* Standardizing on a common automation framework for deploying and operating GitLab, the [GitLab Environment Toolkit](https://gitlab.com/gitlab-org/gitlab-environment-toolkit), which is available to customers and utilized by GitLab.
* Shifting more of our focus to the [GitLab Operator](https://docs.gitlab.com/operator/), which is able to continuously monitor a GitLab deployment and automatically take proactive and reactive action to optimally run a GitLab instance. Over the long term, we expect our Omnibus-based packages to be used only for single-node installs, with our Operator the primary installation path.
* Standardizing on a common orchestration framework to coordinate the provisioning and operations of all instances which GitLab operates, including GitLab.com. These tools will include the Operator, GitLab Environment Toolkit, and [Switchboard (internal only)](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team#cross-reference-to-gitlab-dedicated-projects).
* Improving our backup and restore functionality, through incremental and streaming backups, and the ability to [restore to a particular point in time across all stateful services](https://gitlab.com/groups/gitlab-org/-/epics/12043).

#### Cloud native is the future of GitLab deployments

We are moving towards a cloud-native deployment of GitLab. Cloud-native will become the strongly recommended architecture for all deployments beyond small single-node instances.

The outcomes we hope to achieve with this effort are:

* Majority of customers on recent, supported, versions of GitLab delivering improved security and customer value
* Significantly reduced operational burden and complexity (total cost of ownership)
* Ability to achieve shorter RPO and RTO times
* Declarative operations, for example: backup frequency, upgrade frequency, and more
* Proactive maintenance, for example: automatic provisioning of more repository space, self-healing a Gitaly Cluster deployment, and more

We plan to achieve this by delivering a few key projects:

* Deploying all GitLab-built components in Kubernetes. Kubernetes offers a standardized control plane to discover and operate the various aspects of a GitLab deployment. The GitLab operator provides a control plane which continuously analyzes the deployment and can take action when required. In order to achieve this:
  * [Gitaly will need to be able to run in Kubernetes](https://gitlab.com/groups/gitlab-org/-/epics/6127).
  * The GitLab Operator needs to [mature to recommend production use for Day 1 operations](https://gitlab.com/gitlab-org/cloud-native/gitlab-operator/-/issues/1033).
  * The GitLab Operator needs to be expanded to automate Day 2 operations
* Streaming backups of all stateful data.
  * [Gitaly Write-ahead Logging](https://gitlab.com/groups/gitlab-org/-/epics/8911)
  * Backup integration with hyperscaler managed services, like SQL and object storage (to configure backup policies and trigger restorations)
* Unified, point in time restoration of data
  * [Common backup interface](https://gitlab.com/groups/gitlab-org/-/epics/11635)
  * Ability to trigger stateful restores at a specific timestamp (SQL, Gitaly, object storage)
* Upgrades based on a target release channel (e.g. N-1)
  * Automated upgrade support within the Operator with zero downtime (as possible depending on managed services in use)
  * Automatic recovery of failed upgrade
  * Proactive notifications of deprecations and removals that affect instance

By automating and standardizing more of the operations of Gitlab, we can help our customers (both SaaS and self-managed) operate highly reliable, secure, and up-to-date deployments. This will allow end users and customers to maximize the value and potential of the GitLab platform.

### Consistently great user experience regardless of location or scale

As customers roll out and adopt additional stages of GitLab to realize the benefits of a [single application](https://about.gitlab.com/topics/single-application/), the service availability and performance requirements increase as well. Additional departments within the business utilize the service on a daily basis to accomplish their jobs, such as design, security, and operations teams. People around the world collaborate together. Work that may have been done manually is now automated using CI/CD, including delivering the latest update or bug fix to their customer facing application/website. For these reasons, GitLab is increasingly being identified as a business-critical application with attendant requirements. It is therefore important for GitLab to be a consistently reliable, performant service for all users to fulfill its potential.

By providing market-leading reliability and performance, we will see the following benefits:

* Establish the trust required for customers to adopt additional stages and consolidate on GitLab
* Further penetrate the large enterprise by displacing incumbents with unsatisfactory stability/performance
* Improve our market share of the [SaaS DevOps segment](#saas) by improving the [service level of GitLab.com](https://handbook.gitlab.com/handbook/engineering/infrastructure/performance-indicators/#gitlab-com-availability)
* Increase customer satisfaction by improving responsiveness and availability

### Achieve enterprise compliance needs

Organizations in regulated industries, the [public sector](https://en.wikipedia.org/wiki/Public_sector), and large enterprises often have a variety of standards and processes that they must adhere to.

In the public sector, there are standards like [NIST 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf) and [FedRAMP](https://www.fedramp.gov/). For companies handling credit card transactions, there is [PCI DSS](https://www.pcisecuritystandards.org/). These are just two examples. While some of these standards are not directly aimed at services like GitLab, they have a broad reach, and the requirements generally cannot be waived, as the penalties for non-compliance can be severe. Many enterprises have also developed their own internally driven processes and policies that can be important to support, rather than requiring changes prior to the adoption of GitLab.

For published standards, it is important that GitLab offers the required features and configuration to enable our customers to be in compliance. This includes changes to our code base; for example, fully encrypting all traffic between GitLab nodes, selection of specific cryptographic modules, availability via our [Reference Architectures](https://docs.gitlab.com/ee/administration/reference_architectures/), and [disaster recovery](https://docs.gitlab.com/ee/administration/geo/disaster_recovery/), among others. Additionally, some standards like [FedRAMP (internal only)](https://internal.gitlab.com/handbook/engineering/fedramp-compliance/) can also impact the operational and governance processes of GitLab.com, as well as where data can be stored and processed. The more that we can do to be compliant out of the box or provide documentation on recommended settings, the less work our customers will be required to do during evaluation and implementation.

By enabling our customers to meet their compliance requirements and reducing the required effort, we will see the following benefits:

* Increased penetration of these segments: large enterprise, regulated industries, and the public sector
* Shortened sales cycles by reducing the amount of evaluation and implementation work required to ensure they can remain compliant
* Increased adoption of GitLab by organization whom prefer SaaS but have compliance requirements we cannot meet today

### Reduce cycle time by providing tools to explore complexity

All parts of the software development process grow over time: the code base, its dependencies, data stores, the historical context, the organization, and more. This accretion leads to an increase in complexity, creating a drag on development velocity. At the outset of a project, changes can be quick to land as the code base and its impact is well understood. Fast forward 5 to 10 years and that same change will require significantly more effort, investigating where the change needs to happen across the code base, understanding why the code was written that way in the first place, determining the potential downstream impact, validating the performance, refreshing documentation, and more.  GitLab, at 10 years old, is experiencing these challenges as well.

As a single platform, GitLab is uniquely positioned to minimize these effects by providing tools to better explore and manage complexity. We plan to achieve this by:

* Providing a robust global search function across all content within GitLab, and allowing exploration of related content. From an identified code snippet, one could learn the merge request which landed the changes, the issue which discussed the problem, the CVE which is being resolved, the CI pipeline which validated the changes, and ultimately the deployment job to production.
* Testing all database changes on production data, prior to production. Changes which impact databases, whether it is a complex migration, a schema change, or a perceived simple query, can require an extensive period of review. GitLab aims to make this self-service, by executing all queries and database changes on a thin clone of the production database, and presenting the performance and impact directly to the developer in the merge request as they commit changes.
* Providing guidance on which data store to use for a given change.
* Exposing granular performance data for libraries and applications where this could be a challenge, like Ruby monoliths.

## One-year plan

Over the next 12 months, each group in the Core Platform section will play an integral part in this strategy.

Please see the [categories page](https://handbook.gitlab.com/handbook/product/categories/#core_platform-section) for a more detailed look at Core Platforms's plan by exploring `Direction page` links in areas of interest.

### Distribution

In FY23 (CY 2022), the Distribution team will focus on several main themes:
  * Improve the upgrade rate of instances, by polishing the upgrade experience
  * Reduce the time it takes to deploy and operate GitLab, especially for large-scale deployments
  * Achieve Loveable maturity of our Cloud Native installation
  * Complete maturity of the GitLab Operator according to the [Operator Framework capabilities](https://operatorframework.io/operator-capabilities/).

You can learn more about Distribution group plans on the [Distribution Direction page](/direction/distribution/).

#### Goals

1. Improve the upgrade rate of instances
  * For single-node instances, [automatically upgrade based on user preferences](https://gitlab.com/gitlab-org/gitlab/-/issues/15993)
  * For mult-node Omnibus instances, [make it easy to perform zero downtime upgrades](https://gitlab.com/gitlab-org/gitlab-environment-toolkit) with minimal risk
  * For cloud native, add support for [automated zero-downtime upgrades](https://gitlab.com/gitlab-org/gl-openshift/gitlab-operator/-/issues/59) in the Operator

2. [Reduce the time it takes to deploy and operate scaled GitLab](https://gitlab.com/gitlab-org/gitlab-environment-toolkit)
  * Automated deployments of reference architectures on AWS, GCP, and Azure
  * Automated zero downtime upgrades 
  * Automated Geo promotions and demotions

3. [Achieve Loveable maturity of our Cloud Native installation](https://gitlab.com/groups/gitlab-org/-/epics/5796)
  * Achieve feature parity between Omnibus and Chart based deployment options. New features are launched simultaneously on both Omnibus and Cloud Native
  * Clear and concise documentation for cloud-native installs so that configuration options are easily discoverable and users can more easily deploy in Kubernetes without relying on support from internal GitLab teams. 
  * Test the Helm chart and Operator install at different scales, develop reference architectures, and offer best in class solution for installing GitLab in a cloud environment. 

4. [Complete maturity of the GitLab Operator](https://gitlab.com/groups/gitlab-org/-/epics/6958)
  * Offer a Red Hat certified Operator
  * Make it easy for our existing Charts users to migrate to the Operator
  * Cloud Native users utilize Operator for more frequent upgrades


### Geo

You can read the Geo group plan on the [Geo Direction page](/direction/geo/).

In FY23, the Geo group is focused on delivering [Complete maturity for Disaster Recovery](https://gitlab.com/groups/gitlab-org/-/epics/3574). Disaster Recovery is a common, must-have, requirement for large enterprises, allowing them to feel comfortable that GitLab can remain available for their developers to be productive throughout a variety of disaster scenarios.

In FY23, Geo also plans to deliver [Complete maturity for Geo Replication](https://gitlab.com/groups/gitlab-org/-/epics/1508), another key feature for large enterprises with multiple offices, or the growing number of businesses embracing remote work. Geo-replication enables organizations to set up additional GitLab nodes throughout the world, enabling these users to work efficiently by reducing the latency and time it takes to perform common tasks like cloning or pulling container images.

In Q1 FY23, we will re-evaluate the priority of the backup and restore category and are going to assess [all currently open issues](https://gitlab.com/gitlab-org/gitlab/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=Category%3ABackup%2FRestore%20of%20GitLab%20instances) to define the priorities further.

#### Disaster Recovery

- [Verification of blob data types](https://gitlab.com/groups/gitlab-org/-/epics/5285).
- [Simplify promoting a secondary](https://gitlab.com/groups/gitlab-org/-/epics/3131)
- [Simplify demoting a secondary site](https://gitlab.com/groups/gitlab-org/-/epics/2153)
- [Working with Infrastructure to enable Geo on GitLab.com](https://about.gitlab.com/company/team/structure/working-groups/disaster-recovery/).

#### Geo Replication

- [Geo should be easy to setup](https://gitlab.com/groups/gitlab-org/-/epics/1465)
- [Publish the metrics to a preconfigured Grafana dashboard](https://gitlab.com/groups/gitlab-org/-/epics/1530).
- [Geo sites for CI/CD](https://gitlab.com/groups/gitlab-org/-/epics/1527)
- [Geo supports an advanced caching mode](https://gitlab.com/groups/gitlab-org/-/epics/2610) with the following properties:
- [Enable or disable replication by data type in the Geo Administrator UI](https://gitlab.com/groups/gitlab-org/-/epics/6388).


### Global Search

You can read the Global Search group plan on the [Global Search Direction page](/direction/global-search/).

For FY23 - Global Search provides a search experience across the entire GitLab Instance. 
The focus is on expanding the user’s needs to include new scopes as GitLab features. 
Vulnerabilities search will include multiple ways for sort and filter allowing users to quickly map find Vulnerabilities across groups and projects. 
Pipelines and Jobs Search will make it easier to find CI/CD components across multiple groups.
Snippets Search will make it easier for users to share snippets across their organization.  
Along with adding these additional scopes, we will be enhancing the Advanced Search experience to include additional ways to sort and filter results. 
Adding new content into its own search verticals puts pressure on the user to discover these sections and look at each one individually. To Improve this we will be adding an All results default view that will combine all scopes. 


##### Code Search

Code Search will focus on addressing the needs of Big Code, Which includes several key areas of focus.

* [Federated Search - Search that can include Self-managed and SaaS instances](https://gitlab.com/groups/gitlab-org/-/epics/6221). Better would be the ability to source content from Non-GitLab Repos
* [Elasticsearch Integration for Core/Free](https://gitlab.com/groups/gitlab-org/-/epics/6222) - This would provide faster results and have a much smaller footprint if not including code.
* [Local Editor Functionality](https://gitlab.com/groups/gitlab-org/-/epics/6223)
  * Exact Match
  * More than one line of results per file.
  * RegEx Syntax for Variable specified in code search
  * Case Sensitivity
* [Code Language Filtering](https://gitlab.com/groups/gitlab-org/-/epics/6236)
* [Relevancy Improvements 2](https://gitlab.com/gitlab-org/gitlab/-/issues/22553) - This would be also include Sorting options.
* [LSIF for Code Structure to be Specified in the Search.](https://gitlab.com/gitlab-org/gitlab/-/issues/223150)
* [Infrastructure investment](https://gitlab.com/groups/gitlab-org/-/epics/6248)- 400% over 2 years. Scaling needs to be flexible.
* [Platform change- (This might be required to solve these problems. ) Like zoekt](https://gitlab.com/gitlab-org/gitlab/-/issues/339121)

##### Code Navigation
Growing out of the early delivery of Code Intelligence, Code Navigation will bring more Local IDE style use cases to your Web IDE and across multiple Groups and Projects. 
Details specific to this delivery are in Discovery currently.


### Cloud Connector

GitLab Cloud Connector is a way to access services common to multiple GitLab deployments, instances, and cells. GitLab customers can choose between the following deployment options:
- GitLab.com’s multi-tenant SaaS offering.
- Deploying their own self-managed GitLab instance.
- Signing up for GitLab Dedicated, our managed single-tenant solution.
The goal of GitLab Cloud Connector is to ensure that GitLab features can work equally across all three. This aligns with Core Platform’s mission of accelerating other product groups by reducing the friction of developing for multiple deployments.

In FY25, we will work to formalize the technical boundaries for Cloud Connector by integrating at least two different services: AI gateway and TanuKey. This experience will help us iterate towards a framework-like solution where new feature teams can self-service their own Cloud Connector integration.

You can learn more about Cloud Connector group plans on the [Cloud Connector Direction page](/direction/cloud-connector/).


### Database

The Database group is focused on improving the scalability, performance, and resilience of GitLab's database layer as well as instituting best practices across the wider development organization.

You can learn more about Database group plans on the [Database Direction page](/direction/database/).

For FY23, the group is working on the following key themes:

* Ensuring that the database continues to scale
  * Update the [database tooling](https://gitlab.com/groups/gitlab-org/-/epics/6841) and our [framework for executing background migrations](https://gitlab.com/groups/gitlab-org/-/epics/6840) to support multiple databases
  * [Reduce tables sizes to < 100 GB per physical table](https://gitlab.com/groups/gitlab-org/-/epics/6211) ([analysis](https://docs.gitlab.com/ee/architecture/blueprints/database_scaling/size-limits.html))
* Improving the efficiency and reliability of making database changes
  * [Batched Background Migrations - General Availability](https://gitlab.com/groups/gitlab-org/-/epics/6751)
  * [Automated database testing using production clones: Advanced database testing features](https://gitlab.com/groups/gitlab-org/database-team/-/epics/10)
  * [Database Schema Validation](https://gitlab.com/groups/gitlab-org/-/epics/3928)


### Tenant Scale

You can read the Tenant Scale Group plan on the [Tenant Scale Direction page](/direction/enablement/tenant-scale/).

The Tenant Scale Group is concerned with delivering application changes that allow GitLab and GitLab.com to scale to millions of users and implement the strategies defined in the [Database Scalability Working Group](https://about.gitlab.com/company/team/structure/working-groups/database-scalability/).

In FY23, we expect GitLab.com will transition to run on multiple databases that are decomposed by feature. We expect that at least two independent databases exist: `main` and `ci`. This will provide significant headroom and will allow the Tenant Scale group to transition towards validating proposals for scaling GitLab even further.

Decomposition is only a first step to unlocking further scalability for GitLab. By the end of FY23, the Tenant Scale Group will have evaluated and implemented other scalability options for GitLab. There are several possible options that will have to be evaluated, including but not limited to sharding GitLab's database using existing PostgreSQL tooling, adopting [Vitess](https://vitess.io/), moving towards a Cell-like architecture and utilizing different datastores that fit specific use cases.


### Infrastructure

See the 1 year [GitLab.com infrastructure strategy](/direction/enablement/dotcom/)

### Project Horse

The one year Project Horse direction page can be found [in the internal handbook here](https://internal.gitlab.com/handbook/direction/platforms/horse).


### Git

You can read the Git group plan on the [Git Direction Page](/direction/git/).


### Gitaly

You can read the Gitaly group plan on the [Gitaly Direction Page](/direction/gitaly/).

In FY23, the Gitaly group is focused on improving the performance and availability of the Gitaly product. We have completed a [prioritization effort](https://gitlab.com/groups/gitlab-org/-/epics/7376) and have coordinated on our near term focus on improving data safety and improving stability for large repositories.

More detailed plans can be found by read the [Where we are headed](/direction/gitaly/#where-we-are-headed) section of our direction page, linked above.

## What we're not doing

Choosing to invest in these areas in 2021 means we will choose not to:

* Invest in marketplaces other than AWS.
  * To date we have not seen much customer traction via these deployment options, and providing a high quality experience can be a significant undertaking. If we learn how to make the AWS Marketplace successful, we can consider replicating the model elsewhere.
* [Federated GitLab](https://gitlab.com/gitlab-org/gitlab/issues/6468)
  * Connecting multiple GitLab instances together for a unified workflow is a frequent request, but is technically challenging and there are many different desired use cases.
* Invest further in improving our bespoke backup/recovery tools this year. Many of our larger customers already have established enterprise backup tools, or can use snapshots, and the current tool works for small instances. We are currently focused on improving our Disaster Recovery and Geo Replication features.

## Pricing

The Core Platform pricing strategy's aim is to ensure that the widest possible audience can benefit from GitLab through our free tier, and that we can meet the unique needs of large organizations through our paid tiers.

At the free tier, we want to provide an open-core product for everyone. To achieve this GitLab needs to be incredibly easy to try and adopt, for a wide variety of deployment methods. Today we support SaaS with GitLab.com, and self-managed on all major cloud providers as well as on-prem. This model helps keep our [open core flywheel](../../company/strategy/#dual-flywheels) spinning, and is a key factor in our organic growth by being a go-to DevOps application with a low time and effort investment required to see value.

As adoption across an organization grows, additional business and scale requirements may need to be met, these are particularly common for large enterprise and regulated industries. We aim to meet these more complex operational needs with features in our paid tiers, so that these organizations can adopt GitLab at scale.

### Free

From an operational standpoint, we believe GitLab should be easy to deploy and operate, and that all users should have a great user experience. To achieve this, we invest significantly in automating as much of the deployment and day 2 operations as we can, and embedding as many best practices into the product as possible. We want to set up administrators for success, so they can delight their users. We don't believe application performance, or ease of use, should be a paid-for feature. This helps to ensure that GitLab is easy to try, and that when deployed, provides a good user experience.

For the user-facing features that we build, we align with our overall [pricing strategy](https://handbook.gitlab.com/handbook/company/pricing/#four-tiers), focusing Free on individual developers. Presently this includes basic search, which provides a search experience across projects and groups.

### Premium

Operationally, this tier is where the majority of paid features are located, as Director-level buyers are typically more concerned about meeting wider business, compliance, and scale requirements. We focus features that relate to meeting these needs, typically found in larger enterprises or regulated industries, in this tier. Examples include meeting business continuity needs with [disaster recovery](https://docs.gitlab.com/ee/administration/geo/disaster_recovery/) and horizontally-scaled instances, as well as multi-region performance requirements with [geo-replication](https://docs.gitlab.com/ee/administration/geo/index.html). The [GitLab Environment Toolkit](https://gitlab.com/gitlab-org/gitlab-environment-toolkit) is also available at this tier, providing a great starting point for customers to develop their own deployment automation further.

For users, [Advanced Search](https://docs.gitlab.com/ee/user/search/advanced_search.html) provides cross-project code search as well as [advanced search syntax](https://docs.gitlab.com/ee/user/search/advanced_search.html) to help users more effectively locate content within larger organizations.

### Ultimate

Currently there are no Core Platform features in this tier. We would introduce new features in this tier that target highly specialized requirements typically seen at the executive level. For example companies who may operate multiple independent businesses, but still want to provide a unified experience across the organization through some type of [federation](https://gitlab.com/gitlab-org/gitlab/-/issues/6468).

## Group direction review

The Core Platform PM team reviews one of the groups direction every other week. Prior recordings and the upcoming schedule can be viewed [here](reviews/).

## Categories

### Systems



### Data Stores



## What's Next



#### Footnotes

1. IDC, Worldwide DevOps Software Tools Forecast, 2022–2026, Doc # US48599322, July 2022
