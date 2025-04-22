---
layout: markdown_page
title: "Category Direction - DORA Metrics"
description: "Track and improve software delivery performance with GitLab’s DORA metrics, helping teams monitor key DevOps metrics for success."
---

This direction page was last reviewed on:
`2025-01-25`

- TOC
{:toc}

## DORA Metrics

| Category | **DORA Metrics** |
| --- | --- |
| Stage | [Plan](https://handbook.gitlab.com/handbook/product/categories/#plan-stage) |
| Maturity | [Minimal](/direction/#maturity) |

### Introduction and how you can help

Thanks for visiting the DORA Metrics direction page. This page is actively maintained by the [Optimize group](https://handbook.gitlab.com/handbook/product/categories/#optimize-group). You can contribute or provide feedback by:

1. Posting questions and comments in the [public epic](https://gitlab.com/groups/gitlab-org/-/epics/9882).
1. Finding issues in this category that are labeled "Seeking community contributions".

### Strategy and Themes

[Using DORA metrics](https://about.gitlab.com/solutions/value-stream-management/dora/), Gitlab accelerates engineering work in the context of end-to-end value delivery.

DORA (DevOps Research and Assessment) metrics have become widely recognized and adopted as industry standards for measuring DevOps performance. Software leaders find DORA metrics very useful for measuring the outcome of DevOps because they provide valuable insights into the effectiveness and impact of their DevOps practices. DORA metrics are derived from extensive research conducted by the [DevOps Research and Assessment (DORA)](https://www.devops-research.com/research.html) team, which has identified a set of key metrics that correlate with high-performing software delivery and operational excellence.

The DORA team, has created a list of [four metrics that are straightforward, focused, and easy to implement](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance). They form an excellent foundation for data-driven initiatives, helping improve existing DevSecOps efficiency while also building a bridge to business stakeholders.

These four "DORA" metrics are:

- [Deployment Frequency](https://docs.gitlab.com/ee/user/analytics/dora_metrics.html#deployment-frequency)
- [Lead time for changes](https://docs.gitlab.com/ee/user/analytics/dora_metrics.html#lead-time-for-changes)
- [Time to restore service](https://docs.gitlab.com/ee/user/analytics/dora_metrics.html#time-to-restore-service)
- [Change Failure Rate](https://docs.gitlab.com/ee/user/analytics/dora_metrics.html#change-failure-rate).

#### DORA and Value Stream Management:

DORA metrics are available in GitLab [Value Streams Dashboard](https://docs.gitlab.com/ee/user/analytics/value_streams_dashboard.htm), [Insights reports](https://docs.gitlab.com/ee/user/project/insights/#dora-query-parameters) and in the [CI/CD analytics reports](https://docs.gitlab.com/ee/user/analytics/ci_cd_analytics.html#view-deployment-frequency-chart). [APIs](https://docs.gitlab.com/ee/api/dora/metrics.html) are also available for all four DORA metrics. In GitLab, DORA metrics are embedded as part of the [Value stream management end-to-end DevOps analytics framework](https://about.gitlab.com/direction/plan/value_stream_management/#value-stream-management-as-the-framework-for-end-to-end-devops-analytics). With DORA Metrics, Gitlab's VSM is visualized the work in the context of the value stream - measuring the velocity and stability of software delivery lifecycle through the [DORA4 metrics](https://docs.gitlab.com/ee/user/analytics/#devops-research-and-assessment-dora-key-metrics). 

The following video provides a brief overview of Gitlab's DORA metrics:



The DORA metrics are not intended to be a one-size-fits-all solution but rather provide a set of key metrics that organizations can use as a starting point to assess their DevOps performance. While there may be variations and adaptations of these metrics based on specific organizational contexts, the core principles and concepts outlined by DORA have had a significant impact on the DevOps community and are widely regarded as industry standards for measuring DevOps success.

To learn more check out the [DORA documentation](https://docs.gitlab.com/ee/user/analytics/#devops-research-and-assessment-dora-key-metrics).


### 1 year plan

1. Helps organizations [optimize their software development processes](https://handbook.gitlab.com/handbook/company/strategy/#1-customer-results) to deliver better software faster, by providing [analytics for enterprise management](https://about.gitlab.com/direction/#observability-analytics--feedback). To achieve this, we will focus on:
  - Releasing a new [Value Stream Dashboard.](https://gitlab.com/groups/gitlab-org/-/epics/9317) with [DORA metrics comparison](https://docs.gitlab.com/ee/user/analytics/value_streams_dashboard.html#devops-metrics-comparison) and [DORA Performers score](https://gitlab.com/gitlab-org/gitlab/-/issues/386843) widgets.
  - Extend [DORA Support multiple environment branches](https://gitlab.com/gitlab-org/gitlab/-/issues/358385).
  - Extend [DORA Integrations](https://gitlab.com/gitlab-org/gitlab/-/issues/369840)
2. Enhance usability: Deliver excellent "out-of-the-box" [experience](https://about.gitlab.com/direction/#world-class-devsecops-experience) for ~"Category:Value Stream Management" to visualize for everyone the unique power of measuring software delivery value in a single DevSecOps platform. To achieve this, we will focus on:
  - Uplift [VSA & DORA usability](https://gitlab.com/groups/gitlab-org/-/epics/5272) to enabling teams and managers understand all aspects of productivity, quality, security and delivery without any complex configurations or data scientists.
  - ~Dogfooding [DORA](https://gitlab.com/groups/gitlab-org/-/epics/3894).
  - Develop and publish best practices for [DORA](https://gitlab.com/groups/gitlab-org/-/epics/4788).
3. Demonstrate value of tier upgrades to drive progress on GitLab strategic pillar of [Customer Results](https://handbook.gitlab.com/handbook/company/strategy/#1-customer-results). To achieve this, we will focus on:
  - Adding [YML schema-driven customizable UI to Value Stream Dashboard.](https://gitlab.com/groups/gitlab-org/-/epics/8925). ~"GitLab Ultimate"
  - Add [business value metrics into Value Stream Dashboard](https://gitlab.com/gitlab-org/gitlab/-/issues/381730). ~"GitLab Ultimate"

#### What is next for us

- Moving DORA charts from the [CI/CD Analytics into the new dashboarding framework](https://gitlab.com/groups/gitlab-org/-/epics/16117)
- **Add a new [Dashboard for Executive](https://gitlab.com/groups/gitlab-org/-/epics/9317)** to enable decision-makers to identify trends, patterns, and opportunities for digital transformation improvements. In the next phases, we will focus on the following: 
  - Adding a [new DORA Metrics Overview page](https://gitlab.com/-/project/278964/uploads/9def9ff31b9812ad216043a40bdee5f9/DORA_metrics_-_Option_D.png) in the Value Stream Dashboard. This is related to https://gitlab.com/gitlab-org/gitlab/-/issues/453958. 
  - Adding a [new DORA Metrics Analytics page](https://gitlab.com/-/project/278964/uploads/11d6be804f65814c8ba9fe049338d4cc/DORA_metrics_-_Option_E.png) in the Value Stream Dashboard. This is related to https://gitlab.com/gitlab-org/gitlab/-/issues/453958. 
  - Adding [Custom Metrics Calculation Rules](https://gitlab.com/groups/gitlab-org/-/epics/11490) for DORA, to [support multiple environment branches](https://gitlab.com/gitlab-org/gitlab/-/issues/358385) (with GitLab flow), and [improve the metric calculation](https://gitlab.com/gitlab-org/gitlab/-/issues/444295) to effectively track incidents and deployments.
  - [Move DORA metrics to ClickHouse](https://gitlab.com/gitlab-org/gitlab/-/issues/451752) to provide best experience and robust indicators for measuring the metrics.
  - Adding the Fifth DORA Metric - [Reliability - Operational performance](https://gitlab.com/gitlab-org/gitlab/-/issues/393003)


#### What we recently completed

[Value Stream Management & DORA report generator tool](https://about.gitlab.com/releases/2024/06/20/gitlab-17-1-released/#new-value-stream-management-report-generator-tool) (17.1) – With the addition of the new Reports Generation Tool for Value Stream Management & DORA, we empower decision-makers to be more efficient and effective in the software development life cycle (SDLC) optimization. You can now schedule [DORA comparison metrics reports](https://gitlab.com/components/vsd-reports-generator#example-for-monthly-executive-value-streams-report) or the [AI Impact analytics report](https://about.gitlab.com/releases/2024/05/16/gitlab-17-0-released/#ai-impact-analytics-in-the-value-streams-dashboard) to be delivered automatically, proactively, and with relevant information in GitLab issues. With scheduled reports, managers can focus on analyzing insights and making informed decisions, rather than spending time manually searching for the right dashboard with the required data. You can access the scheduled reports tool using the [CI/CD Catalog](https://gitlab.com/explore/catalog).

### Why using GitLab for DORA Metrics tracking?

1. Out-of-the-box DORA Insight and Reporting.
2. DORA metrics coupled with GitLab Value Stream Analytics that helps draw insights to make data-driven decisions across the rntire DevOps Lifecycle.
2. The One DevOps Platform - collaborating from planning to production across one platform, with security built-in.
3. Open Source; Everyone Can Contribute.
4. Deploy Your Software Anywhere.

### Competitors in our landscape

#### Top three

Based on our analysis, we've identified Planview-Tasktop as the Best In Class (BIC) competitor over Digital.ai and Plutora.

- [Digital.ai](https://digital.ai/) AI-Powered DevOps platform.  Digital.ai has been on a multiyear, multiacquisition journey that includes Arxan, CollabNet
VersionOne, Experitest, Numerify, and XebiaLabs. Its plan to be a front-runner in AI-driven software delivery for Global 5000 enterprises.
- [XebiaLabs' analytics (acquired by Digital.ai)](https://docs.xebialabs.com/xl-release/concept/release-dashboard-tiles.html) are predominantly focused on the Release Manager and give useful overviews of deployments, issue throughput and stages. The company integrates with JIRA, Jenkins, etc and end users can see in which stage of the release process they are.
- [Plutora Analytics](https://www.plutora.com/platform/plutora-analytics) Plutora is a privately held global software (SaaS) company, providing Value Stream Management solutions for enterprise IT in the areas of Release Management and Orchestration, Test Environment Management, Deployment Management, and Analytics.. Plutora seem to target mainly the release managers with their [Time to Value Dashboard](https://www.plutora.com/platform/time-to-value-dashboard). The company also integrates with JIRA, Jenkins, GitLab, CollabNet VersionOne, etc but there is still a lot of configuration that seems to be left to the user.

#### More competitors in our landscape

- [CloudBees DevOptics](https://www.cloudbees.com/products/cloudbees-devoptics) is focused on giving visibility and insights to measure, manage and optimize the software delivery value stream. It allows comparisons across teams and integrates with Jenkins and Jira and SVM /VCS solutions.
- [Faros.ai](https://www.faros.ai/)
- [octopus.com](https://octopus.com/company/roadmap)
- [CollabNet VersionOne](https://www.collab.net) provides users with the ability to input a lot of information, which is a double edged sword as it can lead to duplication of effort and stale information when feeds are not automated. It does however, allow a company to visualize project streams from a top level with all their dependencies. End users can also create customizable reports and dashboards that can be shared with senior management.
- [Targetprocess](https://www.targetprocess.com) tries to provide a full overview of the delivery process and integrates with Jenkins, GitHub and JIRA. The company also provides customizable dashboards that can give an overview over the process from ideation to delivery.
- Although [GitPrime](https://www.gitprime.com) doesn't try to provide a value stream management solution, it focuses on productivity metrics and cycle time by looking at the productivity of a team. It uses only git data.
- Naturally, [Azure](https://docs.microsoft.com/en-us/azure/devops/report/dashboards/analytics-widgets?view=azure-devops) is working on adding analytics that can help engineering teams become more effective but it's still in very early stages. It has also recently acquired [PullPanda](https://pullpanda.com).
- Similarly to GitPrime, [Code Climate](https://codeclimate.com/velocity/understand-diagnose/) focuses on the team and uses git data only.
- Similarly to GitPrime, [Gitalytics](https://gitalytics.com) focuses on the team and uses git data only.
- [Gitential](https://gitential.com)
- [Gitclear](https://gitclear.com)
- [Gitlean](https://gitlean.com)
- [CA Agile Central](https://docs.ca.com/en-us/ca-agile-central/saas/iteration-burndown) combines data across the planning process in a single integrated page with custom applications available to CA Agile Central users. The applications can be installed in custom pages within CA Agile Central or on a dashboard.
- [Agile Craft](https://agilecraft.com)
- [Sleuth](https://www.sleuth.io)
- [jellyfish.co](https://jellyfish.co/blog/dora-metrics-101/)
- [jharness.io](https://harness.io/blog/dora-metrics/)
- [octopus.com](https://octopus.com/company/roadmap)
- [devlake.apache.org](https://devlake.apache.org/docs/UserManuals/DORA/)

### Maturity Plan

This category is currently at the Minimal maturity level, and our next maturity target is Viable (see our [definitions of maturity levels](https://about.gitlab.com/direction/#maturity).

- Link to the Optimize Group [maturity epic](https://gitlab.com/groups/gitlab-org/-/epics/9882).

### Target Audience

#### Who are we focusing on?

For DORA Metrics, we are targeting the following personas (in priority order):
1. [Dakota (Application Development Director)](https://handbook.gitlab.com/handbook/product/personas/#dakota-application-development-director)
2. [Erin (Application Development Executive)](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/roles-personas/buyer-persona/)
3. [Delaney (Development Team Lead)](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
4. [Parker (Product Manager)](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)


#### Jobs to be done:



### Analyst Landscape

In The Future of DevOps Toolchains Will Involve Maximizing Flow in IT Value Streams, Gartner recommended that "infrastructure and operations leaders responsible for selecting and deploying DevOps toolchains should: drive business ability by using DevOps value stream delivery platforms that reduce the overhead of managing complex toolchains." [1] By providing an entire DevOps platform as a single application, GitLab is uniquely suited to provide end-to-end visibility throughout the entire lifecycle without the “toolchain tax.” As the place where work happens, GitLab can also unite visualization with action, allowing users to jump from learning to doing at any time, without losing context.

[Gartner Market Guide for DevOps Value Stream Delivery Platforms](https://about.gitlab.com/analysts/gartner-vsdp21/)

Forrester's New Wave: Value Stream Management Tools, uncovered an emerging market. However, vendors from different niches of the development pipeline are converging to value stream management in response to customers seeking greater transparency into their processes.

Forrester’s vision for VSM includes:
- end-to-end visibility of the software development process, including the corresponding capture and storage of data, events, and artifacts
- definition and visualization of key performance indicators (KPIs)
- inclusive customer experience, which allows multiple roles (PMs, developers, QA, and release managers) to collaborate in one place
- governance, i.e. a framework to monitor compliance to organizational standards, automated audit capabilities, and traceability.

Other Analysts have highlighted that GitLab data gathering has much to offer and much more to mine and enable the insight generation. We have an immediate opportunity to extend the insight generation based on the data gathered in the delivery pipelines. Once this is achieved we will integrate additional data sources beyond the DevOps toolchains.

We have the ability to reach the decision makers that are consuming the insights generated from the GitLab platform, and one of the key elements here is getting beyond the DORA 4 metrics into those that are more specifically targeted: security, compliance, financial, product, but also enterprise architecture, AI/ML delivery teams and the like.
