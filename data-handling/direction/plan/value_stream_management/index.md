---
layout: markdown_page
title: "Category Direction - Value Stream Management"
description: "Value stream management helps software organizations understand and measure how quickly and reliably they can deliver value to end users."
---

This direction page was last reviewed on:
`2025-02-23`


- TOC
{:toc}

### Introduction and how you can help

Thanks for visiting the Value Stream Management direction page. This page is actively maintained by the [Optimize group](https://handbook.gitlab.com/handbook/product/categories/#optimize-group).  

You can contribute or provide feedback by **sharing your feedback about your Value Stream Management experience in this [survey](https://gitlab.fra1.qualtrics.com/jfe/form/SV_50guMGNU2HhLeT4)**, or posting questions and comments in the [public epic](https://gitlab.com/groups/gitlab-org/-/epics/9882).

### Overview

Built as a single application with a unified data store GitLab Value Stream Management (VSM) allows all stakeholders from Executives to individual contributors to have visibility to the [entire software delivery lifecycle](https://about.gitlab.com/blog/2023/06/01/value-stream-total-time-chart/) - enabling teams and managers to understand all aspects of productivity, quality and delivery without the [“toolchain tax”](https://about.gitlab.com/solutions/value-stream-management/). 

Value Stream Management helps organizations understand and [optimize](https://about.gitlab.com/direction/plan/#use-devsecops-data-to-optimize-planning) the impact of their activities across the DevOps lifecycle by:
- Understanding how [quickly and reliably](https://about.gitlab.com/blog/2023/06/26/three-steps-to-optimize-software-value-streams/) value is being delivered to end users. 
- [Identifying and removing bottlenecks](https://about.gitlab.com/blog/2025/02/20/how-we-reduced-mr-review-time-with-value-stream-management/) to improve time to value. 
- Measuring the velocity and stability of software delivery lifecycle through [DORA metrics](https://docs.gitlab.com/ee/user/analytics/#devops-research-and-assessment-dora-key-metrics). 
- [Optimize planning](https://about.gitlab.com/direction/plan/#use-devsecops-data-to-optimize-planning) with data from across the SDLC.
- Connecting developer activities to business value delivery.

To achieve this, users can map Value Streams and finds bottlenecks in their process. Value Stream Analytics provide a [high-level overview of end-to-end cycle and stage times](https://about.gitlab.com/blog/2023/06/26/three-steps-to-optimize-software-value-streams/) and is the starting point for drilling down into each stage of a value stream to identify opportunities for improvements.

#### Why value streams are important for optimizing DevSecOps workflows:

Value streams in the context of DevSecOps workflows refer to the series of actions that take place to add value to a customer, starting from the initial request through to the realization of that value by the customer.
Organizations typically have several value streams, catering to both external and internal customers. 

By defining [DevSecOps workflows as value streams](https://docs.gitlab.com/ee/user/group/value_stream_analytics/#value-stream-stage-events), you can bridge the gap between business and technical teams. The [starting point for this optimization](https://about.gitlab.com/blog/2023/06/26/three-steps-to-optimize-software-value-streams/) is to focus on business outcomes and the creation of customer value, ensuring that each step in the workflow contributes to delivering meaningful results to the customer.

See it in action with this [live VSA example](https://gitlab.com/gitlab-org/gitlab/-/value_stream_analytics?label_name[]=type%3A%3Afeature)—test it out yourself!

#### How Value Stream Management (VSM) solves the challenge of measuring AI Impact

[Value Stream Management (VSM) shifts the focus from individual developer metrics to end-to-end software delivery performance and business impact](https://about.gitlab.com/blog/2024/02/20/measuring-ai-effectiveness-beyond-developer-productivity-metrics/). It tracks AI’s effect on the entire SDLC, ensuring AI-driven efficiencies align with business goals. Ultimately, VSM connects AI impact to business value, measuring whether AI accelerates feature delivery, improves customer outcomes, and optimizes workflows. Implementing AI Impact in VSM enables organizations to move beyond simplistic metrics and make data-driven improvements.

Check out this [FAQ](https://gitlab.com/gitlab-org/gitlab/-/issues/512931) to learn more about GitLab 'AI Impact' analytics. 

#### Value stream management as the framework for end-to-end DevOps analytics

In order to accelerate customer value, it is not enough to streamline the work in a single area. We need to optimize delivery across multiple stages to improve enterprise lead times. Therefore in addition to the [Value Streams Dashboard](https://docs.gitlab.com/ee/user/analytics/value_streams_dashboard.html) and [Analytics](https://docs.gitlab.com/ee/user/group/value_stream_analytics/) as part of Gitlab's [Value Stream Management (VSM) solution](https://about.gitlab.com/solutions/value-stream-management/) the [Optimize group](https://handbook.gitlab.com/handbook/product/categories/#optimize-group) maintains a variety of actionable reports with different levels of insight into Gitlab's DevOps stages. Here is a summary of what’s available today:



</figure> 

As the place where work happens, GitLab Value stream management also [unite flow visualization with actions](https://about.gitlab.com/blog/2023/06/01/value-stream-total-time-chart/), allowing users to jump from learning to doing at any time, without losing context.

#### DORA metrics for optimizing engineering work in Value Stream Management

[DORA metrics are in a separate category](https://about.gitlab.com/direction/plan/dora_metrics/), however in the context of Value Stream Management, measuring DORA provides valuable insights into the speed, quality, and reliability of software delivery. 

The DORA metrics will continue to be the core measurements for engineering work in the value stream, and remain embedded in the VSM optimization flow.


### Vision

GitLab will be the tool of choice for the data-driven DevOps organization — enabling teams and managers to understand all aspects of productivity, quality, security and delivery without any complex configurations or data scientists.


### 1 year Strategic Themes 

1. Establish market leadership by delivering a unique AI Impact measurement framework through Value Stream Management (VSM).
2. Providing Unified Analytics and Robust Reporting Capabilities for Enterprise Management - across the entire organization.
3. "Customer zero" - Enhance VSM dogfooding capabilities.
4. Extend VSM Integrations to source data from third-parties.

#### Current focus

* Improved ["AI Impact" analytics to the Value Stream Dashboard](https://gitlab.com/groups/gitlab-org/-/epics/12978#roadmap), to provide more holistic view of the ROI from the investments in AI features. We're currently focusing on adding [per-user metrics](https://gitlab.com/groups/gitlab-org/-/epics/15026), making [basic AI Impact Analytics available for Duo Pro customers via the GraphQL API](https://gitlab.com/gitlab-org/gitlab/-/issues/498497), and making [iterative improvements to the data visualization and user experience on the AI Impact Analytics dashboard](https://gitlab.com/groups/gitlab-org/-/epics/15030).
* **[Enhanced configuration for custom value stream analytics reports](https://gitlab.com/groups/gitlab-org/-/epics/9129)** - With this change, custom VSA report stage configuration moves from a modal to a standalone page and adds support for persistent filters that apply to all items included in the custom VSA report.


#### What's next and why

- **Surface additional AI Impact Analytics metrics to help customers better understand the impact and ROI for using GitLab Duo Pro and Duo Enterpise** -- In addition to metrics for code suggestions and chat, we will provide insight into productivity gains from:
  - Adoption of [pipeline root cause analysis](https://gitlab.com/groups/gitlab-org/-/epics/15025).
  - Adoption of [vulnerability explanation/resolution](https://gitlab.com/groups/gitlab-org/-/epics/15024).
  - Adding [AI vs. Non-AI Cohort Analysis](https://gitlab.com/groups/gitlab-org/-/epics/15906).
  - Adding insight into ["language usage" of Code Suggestions](https://gitlab.com/gitlab-org/gitlab/-/issues/454809). 
  - Working on an update [UX vision for AI adoption dashboard](https://gitlab.com/gitlab-org/gitlab/-/issues/505532). 
- Mature [Value Streams Dashboard for Executives](https://gitlab.com/groups/gitlab-org/-/epics/9317) to enable decision-makers to identify trends, patterns, and opportunities for digital transformation improvements.In the next 1-3 milestones, we will focus on the following: 
  - [Consolidate Group::Optimize dashboards](https://gitlab.com/groups/gitlab-org/-/epics/13801) into the [Cross-stage Dashboards framework](https://gitlab.com/groups/gitlab-org/-/epics/13801). With the new framework, customers can visualize their DevSecOps data using built-in dashboards provided by GitLab or by creating custom dashboards with custom visualizations.
  - [Customizable widgets](https://gitlab.com/groups/gitlab-org/-/epics/8925) to show data that is relevant to user's goals and needs. Adding the ["Platform Insights" customizable UI capabilities](https://gitlab.com/groups/gitlab-org/-/epics/8925). Integrate the Value streams dashboard page into the [Platform Insights schema driven UI](https://docs.gitlab.com/ee/user/analytics/analytics_dashboards.html).
- Adding [VSA settings](https://gitlab.com/groups/gitlab-org/-/epics/9129) with label filters configuration. In a similar way to boards, teams want to use saved filtered labels with value streams.



#### Recent accomplishments

- New event into Value Stream Analytics (VSA) was added - "Merge request last approved at" to improve development workflow tracking. This enhancing workflow visibility with [new insights into merge request review time](https://about.gitlab.com/releases/2025/02/20/gitlab-17-9-released/#enhancing-workflow-visibility-new-insights-into-merge-request-review-time).
- New [API with code suggestion usage events (17.5)](https://about.gitlab.com/releases/2024/10/17/gitlab-17-5-released/#export-code-suggestion-usage-events). Thjis API provide the raw event data and designed for customers without ClickHouse to gain insights into AI usage.
- **[Value Stream Management report generator tool (17.1)](https://about.gitlab.com/releases/2024/06/20/gitlab-17-1-released/#new-value-stream-management-report-generator-tool)** -- With the addition of the new Reports Generation Tool for Value Stream Management, we empower decision-makers to be more efficient and effective in the software development life cycle (SDLC) optimization. You can now schedule [DevSecOps comparison metrics reports](https://gitlab.com/components/vsd-reports-generator#example-for-monthly-executive-value-streams-report) or the [AI Impact analytics report](https://about.gitlab.com/releases/2024/05/16/gitlab-17-0-released/#ai-impact-analytics-in-the-value-streams-dashboard) to be delivered automatically, proactively, and with relevant information in GitLab issues. With scheduled reports, managers can focus on analyzing insights and making informed decisions, rather than spending time manually searching for the right dashboard with the required data. You can access the scheduled reports tool using the [CI/CD Catalog](https://gitlab.com/explore/catalog).
- **[Adding a new event "MR first reviewer assigned" (17.2)](https://gitlab.com/gitlab-org/gitlab/-/issues/466383)** -- To improve the tracking of development workflows in GitLab, we added the Value Stream Analytics has been extended with a new stage event: "MR first reviewer assigned".
- **[AI Impact analytics: Code Suggestions acceptance rate and GitLab Duo seats usage (17.3)](https://about.gitlab.com/releases/2024/08/15/gitlab-17-3-released/#ai-impact-analytics-code-suggestions-acceptance-rate-and-gitlab-duo-seats-usage) -- These two new metrics highlight the effectiveness and utilization of GitLab Duo, and are now included in the AI Impact analytics in the Value Streams Dashboard, which helps organizations understand the impact of GitLab Duo on delivering business value.
- **[AI Impact analytics with enhanced sparklines trend visualization (17.3)](https://about.gitlab.com/releases/2024/08/15/gitlab-17-3-released/#ai-impact-analytics-with-enhanced-sparklines-trend-visualization)** -- We are excited to announce a significant improvement to our AI Impact analytics with the introduction of sparklines. These small, simple graphs embedded in data tables enhance the readability and accessibility of AI Impact data. By transforming numerical values into visual representations, the new sparklines make it easier to identify trends over time, so you can spot upward or downward movements. This new visual approach also streamlines the process of comparing trends across multiple metrics, reducing the time and effort required when relying solely on numbers.
- **[New Value Stream Analytics stage events for Cycle Time Reduction (17.3)](https://about.gitlab.com/releases/2024/08/15/gitlab-17-3-released/#new-value-stream-analytics-stage-events-for-cycle-time-reduction)** -- To improve the tracking of merge request (MR) review time in GitLab, we added a new stage event to Value Stream Analytics: MR first reviewer assigned. With this new event teams can identify where delays occur in the review process, find opportunities to improve collaboration, and encourage a culture of responsiveness and accountability among team members. Reducing the review time directly impacts the overall cycle time of development, leading to faster software delivery. For example, you can now add a new custom Review Time to Merge (RTTM) stage that starts with MR first reviewer assigned and ends with MR merged.
- **[Export code suggestions usage events (17.5)](https://about.gitlab.com/releases/2024/10/17/gitlab-17-5-released/#export-code-suggestion-usage-events)** -- Previously, AI impact analytics were available only on GitLab.com to GitLab Duo Enterprise customers, and on GitLab self-managed with a ClickHouse integration. Additionally, the default metrics were aggregated. Now, you can export raw code suggestion events from the GraphQL API. This way you can import the data into your data analysis tool to get deeper insights into acceptance rates across more dimensions, such as suggestion size, language, and user. The raw events are not stored in ClickHouse, so some AI Impact Analytics metrics become available to all GitLab deployments, including GitLab Dedicated and self-managed.


#### Top Vision Item(s)

- Adding VSM "Duo Chat Analytics" - [adding analytics tool to GitLab Duo Chat](https://gitlab.com/gitlab-org/gitlab/-/issues/426861).
- Software delivery [optimization AI recommendation](https://gitlab.com/groups/gitlab-org/-/epics/10329) 
- Enhance VSM for agile planning - [tracking the new Workflow Status](https://gitlab.com/gitlab-org/gitlab/-/issues/466409)
- [AI Descriptive Analytics with quick insights](https://gitlab.com/gitlab-org/gitlab/-/issues/389233)
- Adding [business value metrics](https://gitlab.com/gitlab-org/gitlab/-/issues/381730) widget into the Value Streams Dashboard.
- Measuring [SPACE framework metrics in GitLab](https://gitlab.com/gitlab-org/gitlab/-/issues/372054)
- Introduce [Value Streams forecasting to VSD comparison panel](https://gitlab.com/gitlab-org/gitlab/-/issues/407798).
- Value-stream Autonomous mapping tool

### Top cross-stage items

- Value Stream Dashboard - extend to "Product Analytics" [schema-driven customizable UI](https://gitlab.com/groups/gitlab-org/-/epics/8925).
- DORA integration with GitLab [Incident Tag.](https://gitlab.com/gitlab-org/gitlab/-/issues/336026)
- Adding [Organization-level / Instance-level analytics for VSM & DORA](https://gitlab.com/gitlab-org/gitlab/-/issues/413202)

## Competitive Analysis

### Why using GitLab for Value Stream Management?

1. Out-of-the-box [Value Stream Insight, Reporting and dashboards](https://gitlab.com/gitlab-org/gitlab/-/value_stream_analytics?created_after=2022-12-31&created_before=2023-01-29&stage_id=issue&sort=end_event&direction=desc&page=1).
2. Collects and shows data across the entire software lifecycle with no integrations to be managed.
3. [DORA metrics](https://about.gitlab.com/direction/plan/dora_metrics/) coupled with the Value Stream Analytics that helps draw insights about the velocity and stability of software delivery lifecycle.
4. A common data model representing people, processes, work items, and time to remove silos.
5. Multiple [custom value streams](https://docs.gitlab.com/ee/user/group/value_stream_analytics/#create-a-value-stream-with-custom-stages) for end-to-end view of value delivery and application health
6. The One DevOps Platform - Single Application for Entire DevOps Lifecycle
7. Open Source; Everyone Can Contribute. 
8. Deploy Your Software Anywhere.

### Competitive Landscape

Top 3 Competitors: 

1. [Tasktop](https://www.tasktop.com/) (acquired by Planview) - Best In Class (BIC) competitor.
2. [Digital.ai](https://digital.ai/)
3. [Plutora Analytics](https://www.plutora.com/platform/plutora-analytics) 

Based on our analysis,  we've identified Planview-Tasktop as the Best In Class (BIC) competitor over Digital.ai and Plutora.

#### Tasktop - Best In Class (BIC) competitor
[Tasktop ](https://www.tasktop.com/integration-hub) is exclusively focused on Value Stream Management and allows users to connect more than 50 tools together, including Atlassian's JIRA, GitLab, GitHub, JamaSoftware, CollabNet VersionOne, Xebia Labs, and TargetProcess to name a few. Tasktop serves as an integration layer on top of all the software development tools that a team uses and allows for mapping of processes and people in order to achieve a common data model across the toolchain. End users can visualize the flows between the different tools and the data can be exported to a database for visualization through BI tools.

Based on our analysis, we've identified these gaps against Tasktop:

| Gap | Roadmap to close this gap|
|-----|---------|
| Limited Analytics & Visualization capabilities | [Adding Value Stream Dashboard - Comparison page](https://gitlab.com/groups/gitlab-org/-/epics/9559),  [Overview page](https://gitlab.com/groups/gitlab-org/-/epics/9558),  [Schema-driven customizable UI](https://gitlab.com/groups/gitlab-org/-/epics/8925) |
| limited flow analysis | [Add VSA Overview cumulative flow diagram](https://gitlab.com/gitlab-org/gitlab/-/issues/366780),  [Add Stage time - scatterplot](https://gitlab.com/groups/gitlab-org/-/epics/8374),  [Add SAFe Flow Metrcis](https://gitlab.com/groups/gitlab-org/-/epics/6795),  [Usability improvements to "tasks by type" chart](https://gitlab.com/groups/gitlab-org/-/epics/7412) |
| limited number of integrations | [VSA API](https://gitlab.com/groups/gitlab-org/-/epics/8369) |
| Missing value delivery metrics | [Adding business value metrics](https://gitlab.com/gitlab-org/gitlab/-/issues/381730),  [Adding OKR Health status](https://gitlab.com/gitlab-org/gitlab/-/issues/384923) |

#### Digital.ai 

[Digital.ai](https://digital.ai/) AI-Powered DevOps platform.  Digital.ai has been on a multiyear, multiacquisition journey that includes Arxan, CollabNet
VersionOne, Experitest, Numerify, and XebiaLabs. Its plan to be a front-runner in AI-driven software delivery for Global 5000 enterprises.

[XebiaLabs' analytics (acquired by Digital.ai)](https://docs.xebialabs.com/xl-release/concept/release-dashboard-tiles.html) are predominantly focused on the Release Manager and give useful overviews of deployments, issue throughput and stages. The company integrates with JIRA, Jenkins, etc and end users can see in which stage of the release process they are.

#### Plutora
[Plutora Analytics](https://www.plutora.com/platform/plutora-analytics) Plutora is a privately held global software (SaaS) company, providing Value Stream Management solutions for enterprise IT in the areas of Release Management and Orchestration, Test Environment Management, Deployment Management, and Analytics.. Plutora seem to target mainly the release managers with their [Time to Value Dashboard](https://www.plutora.com/platform/time-to-value-dashboard). The company also integrates with JIRA, Jenkins, GitLab, CollabNet VersionOne, etc but there is still a lot of configuration that seems to be left to the user.

Key Features for Comparison:

1. Data Analytics - Visualize the data into valuable insights and actionable information to support decision-making and strategic planning. The ability to analyze the stream performance, team productivity, and work distribution. This includes custom dashboards and detailed reports with the underline data.   
2. Data Collection - Capturing and aggregating DORA, Flow, DevOps, Ops and Security metrics.
3. Common Data Model - Set of value stream objects representing the DevOps lifecycle to enable customers to map the end-to-end processes. The ability to create and manage single or multiple value streams as a single source of insight for the organization.This include - users, processes (workflow labels), work items (issues, MRs and epics) and time tracking. 
4. Integrations - Inbound and outbound integrations with 3rd party tools.
5. Value Measurement - Connect software investments to business results. Capture, calculate, and track product usage, OKRs, cost metrics, and business KPIs (Revenue, Renewals).
6. Governance and Compliance - The ability to monitor compliance to organizational standards.
7. AI/ML - Leverages AI/ML for better decision-making. The ability to predict trends, detects blind spots, bobble-up insights, and automate processes to reduce manual tasks.

GitLab vs the Top 3 Competitors - Planview-Tasktop/Digital.ai/Plutora:

1. GitLab versus [Planview-Tasktop](https://www.tasktop.com/): 

| Feature | GitLab | Planview-Tasktop |
| ------ | ------ | ------ |
|   Data Analytics   | 🟨  |  🟩 |
|   Capturing Data, Metrics and KPIs    | 🟨 | 🟩 |
|   Common Data Model    | 🟩 | 🟩 |
|   Integrations     | ⬜️  | 🟩 |
|   Value Measurement    | ⬜️  | 🟩 |
|   Governance and Compliance    | 🟩 | 🟩 |
|   AI/ML     | ⬜️ | 🟨 |

2. GitLab versus [Digital.ai](https://digital.ai/): 

| Feature | GitLab | Digital.ai |
| ------ | ------ | ------ |
|   Data Analytics   | 🟨  |  🟩 |
|   Capturing Data, Metrics and KPIs    | 🟨| 🟩 |
|   Common Data Model    | 🟩 | 🟩 |
|   Integrations     | ⬜️  | 🟩 |
|   Value Measurement    | ⬜️  | 🟩 |
|   Governance and Compliance    | 🟩 | 🟨 |
|   AI/ML     | ⬜️ | 🟩 |

3. GitLab versus [Plutora](https://www.plutora.com): 

| Feature | GitLab | Plutora |
| ------ | ------ | ------ |
|   Data Analytics   | 🟨  |  🟩 |
|   Capturing Data, Metrics and KPIs    | 🟨| 🟩 |
|   Common Data Model    | 🟩 | 🟩 |
|   Integrations     | ⬜️  | 🟩 |
|   Value Measurement    | ⬜️  | 🟨 |
|   Governance and Compliance   | 🟩 | 🟨 |
|   AI/ML     | ⬜️ | ⬜️ |

More competitors in our Landscape:

#### TargetProcess
[Targetprocess](https://www.targetprocess.com) tries to provide a full overview of the delivery process and integrates with Jenkins, GitHub and JIRA. The company also provides customizable dashboards that can give an overview over the process from ideation to delivery.

#### GitPrime
Although [GitPrime](https://www.gitprime.com) doesn't try to provide a value stream management solution, it focuses on productivity metrics and cycle time by looking at the productivity of a team. It exclusively uses only git data.

#### Azure DevOps
Naturally, [Azure](https://docs.microsoft.com/en-us/azure/devops/report/dashboards/analytics-widgets?view=azure-devops) is working on adding analytics that can help engineering teams become more effective but it's still in very early stages. It has also recently acquired [PullPanda](https://pullpanda.com).

#### Velocity by Code Climate
Similarly to GitPrime, [Code Climate](https://codeclimate.com/velocity/understand-diagnose/) focuses on the team and uses git data only.

#### Gitalytics
Similarly to GitPrime, [Gitalytics](https://gitalytics.com) focuses on the team and uses git data only.

#### Gitential
[Gitential](https://gitential.com)

#### Gitclear
[Gitclear](https://gitclear.com)

#### Gitlean
[Gitlean](https://gitlean.com)

#### CollabNet VersionOne
[CollabNet VersionOne](https://www.collab.net) provides users with the ability to input a lot of information, which is a double edged sword as it can lead to duplication of effort and stale information when feeds are not automated. It does however, allow a company to visualize project streams from a top level with all their dependencies. End users can also create customizable reports and dashboards that can be shared with senior management.

#### CA Technologies
[CA Agile Central](https://docs.ca.com/en-us/ca-agile-central/saas/iteration-burndown) combines data across the planning process in a single integrated page with custom applications available to CA Agile Central users. The applications can be installed in custom pages within CA Agile Central or on a dashboard.

#### Atlassian's JIRA Align
[Agile Craft](https://agilecraft.com)

#### Sleuth
[Sleuth](https://www.sleuth.io)

#### Allstacks

[allstacks.com](https://www.allstacks.com/product/value-stream-intelligence)

#### Blueoptima

[blueoptima.com](https://www.blueoptima.com/about/)

### Analyst Landscape

[Gartner Market Guide for DevOps Value Stream Delivery Platforms](https://about.gitlab.com/analysts/gartner-vsdp21/). It is also possible to utilize GitLab's Value Stream Management as a [Software Engineering Intelligence Platform](https://www.gartner.com/en/documents/4214399).

Forrester's New Wave: Value Stream Management Tools, Q3 2018 uncovered an emerging market with no leaders. However, vendors from different niches of the development pipeline are converging to value stream management in response to customers seeking greater transparency into their processes.

Forrester’s vision for VSM includes:
- end-to-end visibility of the software development process, including the corresponding capture and storage of data, events, and artifacts
- definition and visualization of key performance indicators (KPIs)
- inclusive customer experience, which allows multiple roles (PMs, developers, QA, and release managers) to collaborate in one place
- governance, i.e. a framework to monitor compliance to organizational standards, automated audit capabilities and traceability.

Other Analysts have highlighted that Gitlab data gathering has much to offer and much more to mine and enable the insight generation. We have an immediate opportunity i to extend the insight generation based on the data gathered in the delivery pipelines. Once this is achieved we will integrate additional data sources beyond the DevOps toolchains.

We have the ability to reach the decision makers that are onsuming the insights generated from the Gitlab platform, and one of the key elements here is getting beyond the DORA 4 metrics into those that are more specifically targeted: security, compliance, financial, product, but also enterprise architecture, AI/ML delivery teams and the like.

Additional functionality, requested by clients includes:
- integration with other tools, including the ability to double-click into each tool to directly observe status or take action
- business value custom definitions in terms of financials, time, effort or similar
- mapping of business value, people, processes, data
- visualization dashboards, which users can customize to support different role-based views.

### Jobs to be done



### Maturity plan

This category is currently **Viable**. Our next step is **Complete** ([see epic](https://gitlab.com/groups/gitlab-org/-/epics/9882#maturity-plan)). You can read more about GitLab's [maturity framework here](https://about.gitlab.com/direction/#maturity.
