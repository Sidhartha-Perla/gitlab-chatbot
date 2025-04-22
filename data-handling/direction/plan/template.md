---
layout: markdown_page
title: Product Stage Direction - Plan
description: "The Plan stage enables teams to effectively plan features and projects in a single application"
canonical_path: "/direction/plan/"
---

Content last reviewed on 2024-10-23

- TOC
{:toc}

**Enable teams to effectively plan and execute work in a single application**
    

As GitLab pursues its vision of replacing disparate DevSecOps toolchains with a single application, the Plan stage aspires to build robust planning tools that tie directly into the broader DevSecOps lifecycle. Our goal is to empower teams to continuously deliver customer and business value with the shortest possible cycle times.



## Stage Overview

The Plan Stage provides tools for teams to manage and optimize their work, track operational health and measure outcomes. As an end-to-end DevSecOps platform, GitLab is uniquely positioned to deliver a planning suite that enables business leaders to drive their vision and DevSecOps teams to deliver value while improving how they work. The unification of the DevSecOps process allows GitLab to interlink data across every stage of development, from ideation to value delivered to customers.

### Group and Categories

The Plan Stage is made up of four groups supporting all major categories needed to plan work for DevOps organizations, including:

- The Project Management group focuses on the needs of individual engineering teams to plan their work. Core features include Issues, Work Items and Iterations to help teams plan, track, triage, and complete their work.
- The Product Planning group focuses on connecting the work that engineering teams perform to higher level strategy, across multiple teams and in longer time horizons (quarters or years). Core features include Epics and Roadmaps.
- The Knowledge group focuses on enabling users to create, share, use and manage the knowledge and information of an organization. Core features include the Content Editor, Pages and Wiki.
- The Optimize group focuses on enabling organizations to uncover opportunities to continuously improve upon their software development lifecycle. Core features include Value Stream Management and DORA metrics.

For more details about groups scope of work and team members that support it, visit our [categories page](https://handbook.gitlab.com/handbook/product/categories/#plan-stage). 


## 3 Year Stage Themes

### Enterprise planning frameworks support

As examples, GitLab will provide:
* Out of the box functionality that allows DevSecOps teams to follow Scrum, Kanban, and Requirements-based development processes.
   * Work Items that represent discrete units of work and are typically used by single teams. Today we use Issues to represent work but we plan to [standardize on an underlying common model](https://docs.gitlab.com/ee/development/work_items.html) and introduce more work item types. Examples of team work items types are Stories, Bugs, and Requirements.
   * Views to facilitate Plan workflows for personas that work in a single team, like Engineers, UX, Product, and Engineering Managers. Example workflows are iteration planning, status views for a single team, and retrospectives.
* Out of the box functionality that aligns to industry-standard program and portfolio management, including frameworks like [SAFe](https://www.scaledagileframework.com), [LeSS](https://less.works), and [Disciplined Agile](https://www.pmi.org/disciplined-agile).
   * Work Items that represent collections of units of work and are typically used by multiple teams. Today we use Epics to represent collections of units of work but we plan to [standardize on an underlying common model](https://docs.gitlab.com/ee/development/work_items.html) and introduce additional portfolio level work item types. Examples of portfolio level work item types are Features, Epics, Themes, and OKRs.
   * Views to facilitate Plan workflows for personas that work across teams, like Program Managers, Managers of Managers, and Executives. The ability to relate and roll up work items across projects and groups will be critical for these personas. Example workflows are quarterly or program increment planning, status reporting across multiple teams, and retrospectives across multiple teams.
* Options to customize the data captured about work items and their status. We currently rely on labels for this information, but our customers have expressed the need for a more structured approach. A lightweight custom data solution in GitLab has the ability to enable a wide range of use cases such as prioritization models and CapEx reporting.

#### Our approach to configuration

Our vision is to build a Plan experience that aligns with our [configuration principles](https://handbook.gitlab.com/handbook/product/product-principles/#configuration-principles). When you look across the Enterprise Agile Planning tool landscape, you'll find solutions with large customer bases that cover many methodologies and personas. Our competitors have built highly flexible solutions with many customization options to accommodate the large array of use cases. Unfortunately, this makes these tools non-performant and challenging to administer, leading to customer dissatisfaction.

We have strong signals from our customers that they want a planning tool that supports their processes but is not overbearing. Recent conversations include:
* An industry leading telecommunications company that wants to consolidate multiple planning tools into GitLab. Their current setup has complicated enforced workflows and data integrations that make their tools difficult to use.
* A bank that is migrating their teams to GitLab, leaving behind their current highly customized planning tool. Our plan capabilities are lighter weight, increase developer productivity, and encourage collaboration.
* A manufacturing company that values team automony and collaboration. They are moving to GitLab to reduce context switching with separate development and planning tools and to improve cross-team planning workflows.

There are now countless solutions that aim to make planning tools that teams love. For example, tools like Notion, Monday.com, and Asana simplify configuration and focus on user experience. Embracing a comparable philosophy, our approach will distinguish itself through a tailored experience driven by our platform strategy. Our focus is empowering DevSecOps organizations to enhance their [agile fluency](https://martinfowler.com/articles/agileFluency.html) by seamlessly integrating workflows throughout the DevSecOps lifecycle.

We have heard the feedback that, while we should stay true to our principle of convention over configuration, GitLab should enable configuration options that allow organizations to accurately represent their way of working. Introducing additional configuration options will also allow us to create an experience that works by default, instead of heavily relying on label configuration. To address this feedback, we plan to introduce the features below:
- [Custom fields](https://gitlab.com/groups/gitlab-org/-/epics/235) - Labels are not flexible enough to efficiently or accurately represent all the different data types that organizations need to track within GitLab. Custom fields will offer a structured way to capture and report on business critical metadata that is specific to an organization or team. 
- [Configurable statuses](https://gitlab.com/groups/gitlab-org/-/epics/5099) - Today, work items can be open or closed which is not granular enough to communicate or produce reports based on where work is in the lifecycle. 
- [Work Item Types](https://gitlab.com/groups/gitlab-org/-/epics/7897) - Instead of relying solely on labels to classify work items, you will be able to define the types of work items. Using work item types will enable more robust analytics into the health of your value stream. 
- [Automation rules](https://gitlab.com/groups/gitlab-org/-/epics/364) - Relying on automation streamlines processes and reduces human error more effectively than configuring complex status workflows in agile planning tools, enhancing efficiency and ensuring consistent performance. We will prioritize automation over intricate status workflows to satisfy requirements for work items to follow a specific workflow path.

GitLab will continue to put the user at the forefront, while further enabling organizations to satisfy their planning requirements through:

1. Streamlined configuration: We will prioritize simplicity by minimizing configuration options while always providing sensible defaults. This approach avoids the confusion and inconsistency often associated with overly customizable tools, ensuring a smoother experience for end users. Examples of overly complex configuration are defining a field as mandatory once a work item reaches a certains status or only allowing certain fields to be only edited by specific users. 
2. Uninterrupted workflows: Embracing Agile principles, we will steer clear of imposing rigid toll gates or checkpoints that hinder progress. By fostering flexibility and continuous delivery, we empower teams to respond swiftly to changes and deliver value incrementally, without unnecessary bureaucracy.
3. Empowering autonomy: Balancing governance and autonomy, we will offer organization and team-level management options. Our cascading configuration model will allow for flexibility, enabling groups to define and refine processes while ensuring compliance where needed. Administrators can choose to empower sub-groups and projects with additional configuration options to suit their unique needs without risking disorganized sprawl.

#### Duo Pro and Enterprise usage metrics

The Optimize team is focusing on iterating on [AI Impact Analytics](https://gitlab.com/groups/gitlab-org/-/epics/12978) to surface usage and value metrics for customers adopting Duo Pro and Duo Enterprise. While there are several avenues we could explore for AI Impact Analytics, it's important to distinguish what we are incorporating into our scope and what we are not. Items in scope represent those things for which Optimize is the DRI. Items not in scope fall outside of the domain and ownership of Optimize. 

In scope:

- Metrics that help a single customer gain insights into the value and ROI for using Duo.
- This focus is primarily on quantifying productivity gains, business outcomes, and Duo adoption for individual customers. 
- AI Impact Analytics dashboards built in alignment with the vision of a [platform-level dashboarding framework](https://gitlab.com/groups/gitlab-org/-/epics/13801).
- Tiering strategy for AI Impact Analytics for Duo Pro and Duo Enterprise.
- Per-user adoption of Duo Enterprise features within the context of a single customer. 

Not in scope:

- Utilization metrics that span across the fleet of instances and customers communicating with the AI Gateway.
- Utilization metrics intended for internal audiences such as those captured via product telemetry and visualized in Tableau. 
- Functionality and maintenance of existing and future Duo unit primitives outside of those where Optimize is the DRI. 
- Duo license provisioning and management, including field support where customers encounter challenges with license management.
- Adding support for ClickHouse to GitLab Dedicated.
- Instrumenting Duo metrics for other teams. The DRI for a Duo unit primitive is responsible for instrumenting their own metrics.
- Duo usage data specifically related to fulfillment use cases.     

### Use DevSecOps data to optimize planning

As an end-to-end DevSecOps platform, GitLab is uniquely positioned to deliver a planning suite that enables business leaders to drive their vision and empower their development teams to work efficiently. Our unification of the DevSecOps process allows us to interlink data across every stage of development, from initial analysis to planning, implementation, deployment, and monitoring. Today, few teams can answer how long their software projects take, and even fewer can answer how long each stage in the process takes. Without this information, most teams are flying blind on their estimates, using past experiences and best guesses to best calculate the time or level of effort that it will take to get from an idea to production.
Engineering and product managers need to parse through information in multiple systems to know if problems will keep their teams from meeting their plans. The data is often hard to understand, so engineers' days are interrupted with requests for status updates. Executives rely on status reports that are created manually and often inaccurate. To fully solve this problem, DevSecOps data should be displayed so that it's easy to understand for users that are not developers.

As examples, GitLab will:

* Roll-up reports and dashboarding that provide visibility into where to focus next on improving performance and reliability includes:
   - Value stream dashboard to allow all stakeholders, from executives to individual contributors, to have visibility in the process and value delivery metrics associated with the software development life cycle. The Value stream dashboard enables teams to continuously improve workflows by benchmarking key DevSecOps metrics and comparing these metrics over time to identify and fix engineering inefficiencies and bottlenecks.
   - Everyday analytics for teams: Increasing the effectiveness and efficiency of everyday software development teams — surfacing actionable insights, identifying bottlenecks, and highlighting waste.
* Leverage data from other DevSecOps stages to provide context to non-technical users in work items; enabling them to derive the current status of work.
* Flag work items that are at risk during an iteration based on [DORA key metrics](https://docs.gitlab.com/ee/user/analytics/ci_cd_analytics.html#DevSecOps-research-and-assessment-dora-key-metrics) and [Value Stream Analytics](https://docs.gitlab.com/ee/user/group/value_stream_analytics/).
* Incorporate data from [DORA key metrics](https://docs.gitlab.com/ee/user/analytics/ci_cd_analytics.html#DevSecOps-research-and-assessment-dora-key-metrics) and [Value Stream Analytics](https://docs.gitlab.com/ee/user/group/value_stream_analytics/) into retrospective workflows.

### Automation, Artificial Intelligence and Machine Learning to improve quality of life

Managing issues across an organization can be a time-consuming and tedious endeavor. It's normal for organizations to have a large number of stale issues that require manual clean-up. Our focus will be to let automation do the lower value work like managing status changes and automating the movement of work items among workstations (queues) so the people doing the work can focus more on creating value and less on remembering the process. At GitLab, we dogfood our issue tracker and have implemented a considerable amount of [automation](https://gitlab.com/gitlab-org/gitlab-triage) to start down this direction. We will double down on this strategy, incorporate automation into our product and reduce the manual setup required to enable it. GitLab can also provide suggestions and nudges that reduce the number of actions required to complete common tasks.

GitLab has recently created [AI-powered stage](https://about.gitlab.com/direction/ai-powered/) and the Plan Stage has been collabrating with that stage to bring new AI-powered Planning capabilities.

As examples, GitLab will provide:
* Assistance in generating text for work items like issues and epics.
* Auto-assign issues based on previous assignments.
* Auto-close or suggest closing issues if downstream activity implies it.
* Apply labels automatically based on historical issue data.
* Change issue health if downstream DevSecOps activity implies it.
* Surface, categorize and rank work items that may need a user's attention.
* Optimize everyday manual actions like work item data entry or updates by providing real-time suggestions.

 
## 3 Year Strategy

In three years, the Plan Stage market will:
* Continue to shift from project to product and focus on outcomes instead of output.
* Continue to move away from command and control mentality and instead empower teams to determine how they can contribute toward business objectives.
* Make operational efficiency and continual improvement a top priority.  
* Embrace AI within the Plan stage of the DevSecOps toolchain and lifecycle.
* Shift toward consolidation into a single platform for all stages of the DevSecOps lifecycle.

As a result, in three years, Gitlab will:
* Provide support for individual DevSecOps teams and entire organizations, keeping Agile frameworks in mind.
* Allow GitLab to capture and tie metrics to [Work Items](https://docs.gitlab.com/ee/development/work_items.html) to reflect business outcomes. 
* Surface metrics like DORA, Flow and Value Stream in key parts of a teams workflow to help drive improvements. 
* Support frameworks like OKRs that encourage bottom-up contributions. 
* Use downstream DevSecOps data for automation and AI to help teams improve their plans.
* Make it easy for non-Developer Personas to contribute in GitLab. 


## 1 Year Plan

### What We Recently Completed

- **[Adds type attribute to issues webhook payloads (17.1)](https://gitlab.com/gitlab-org/gitlab/-/issues/467415)** -- Issues, tasks, incidents, requirements, objectives, and key results all trigger payloads under the Issues Events webhook category. Until now, there has been no way to quickly determine the type of object that triggered the webhook within the event payload. This release introduces an object_attributes.type attribute available on payloads within the Issues events, Comments, Confidential issues events, and Emoji events triggers.
- **[Resolve threads in tasks, objectives, and key results (17.3)](https://about.gitlab.com/releases/2024/08/15/gitlab-17-3-released/#resolve-threads-in-tasks-objectives-and-key-results)** -- You can now resolve threads in tasks, objectives, and key results, making it easier to manage and track important conversations. Resolved threads are collapsed by default, helping you focus on active discussions and streamline your collaboration workflows.
- **[Add Merge Requests to Tasks (17.3)](https://gitlab.com/gitlab-org/gitlab/-/issues/440851)** -- When referencing a task from within an MR description using the [closing pattern](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically), Merge Requests will now be linked to the task, providing better visibility and traceability between tasks and related code changes. This feature enhances project management by allowing teams to easily track which merge requests are associated with specific tasks, improving workflow and collaboration.
- **[Summarize Issue discussions GA (17.4)](https://gitlab.com/groups/gitlab-org/-/epics/10760)** -- View an AI generated summary of all threads and comments within an issue or epic to quickly get up to spead on the discussion. 



* Improvements to the rich text editor - Following the initial rollout in GitLab 16.2, we continue to make improvements to the rich text editor. In 17.1, we introduced [draggable media in the rich text editor](https://gitlab.com/gitlab-org/gitlab/-/issues/452233) and [downscaling pasted images](https://gitlab.com/gitlab-org/gitlab/-/issues/419913).
* [Real-time boards (17.1)](https://gitlab.com/gitlab-org/gitlab/-/issues/468187) - Changes you make in the sidebar will instantly appear on the board itself, no more refreshing required. This reactive boards experience streamlines your workflow, allowing you to quickly make updates while seeing them reflected in real-time.
- **[Adds type attribute to issues webhook payloads (17.1)](https://gitlab.com/gitlab-org/gitlab/-/issues/467415)** -- Issues, tasks, incidents, requirements, objectives, and key results all trigger payloads under the Issues Events webhook category. Until now, there has been no way to quickly determine the type of object that triggered the webhook within the event payload. This release introduces an object_attributes.type attribute available on payloads within the Issues events, Comments, Confidential issues events, and Emoji events triggers.
- **[Resolve threads in tasks, objectives, and key results (17.3)](https://about.gitlab.com/releases/2024/08/15/gitlab-17-3-released/#resolve-threads-in-tasks-objectives-and-key-results)** -- You can now resolve threads in tasks, objectives, and key results, making it easier to manage and track important conversations. Resolved threads are collapsed by default, helping you focus on active discussions and streamline your collaboration workflows.
- **[Add Merge Requests to Tasks (17.3)](https://gitlab.com/gitlab-org/gitlab/-/issues/440851)** -- When referencing a task from within an MR description using the [closing pattern](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically), Merge Requests will now be linked to the task, providing better visibility and traceability between tasks and related code changes. This feature enhances project management by allowing teams to easily track which merge requests are associated with specific tasks, improving workflow and collaboration.
- **[Summarize Issue discussions GA (17.4)](https://gitlab.com/groups/gitlab-org/-/epics/10760)** -- View an AI generated summary of all threads and comments within an issue or epic to quickly get up to spead on the discussion. 


- New event into Value Stream Analytics (VSA) was added - "Merge request last approved at" to improve development workflow tracking. This enhancing workflow visibility with [new insights into merge request review time](https://about.gitlab.com/releases/2025/02/20/gitlab-17-9-released/#enhancing-workflow-visibility-new-insights-into-merge-request-review-time).
- New [API with code suggestion usage events (17.5)](https://about.gitlab.com/releases/2024/10/17/gitlab-17-5-released/#export-code-suggestion-usage-events). Thjis API provide the raw event data and designed for customers without ClickHouse to gain insights into AI usage.
- **[Value Stream Management report generator tool (17.1)](https://about.gitlab.com/releases/2024/06/20/gitlab-17-1-released/#new-value-stream-management-report-generator-tool)** -- With the addition of the new Reports Generation Tool for Value Stream Management, we empower decision-makers to be more efficient and effective in the software development life cycle (SDLC) optimization. You can now schedule [DevSecOps comparison metrics reports](https://gitlab.com/components/vsd-reports-generator#example-for-monthly-executive-value-streams-report) or the [AI Impact analytics report](https://about.gitlab.com/releases/2024/05/16/gitlab-17-0-released/#ai-impact-analytics-in-the-value-streams-dashboard) to be delivered automatically, proactively, and with relevant information in GitLab issues. With scheduled reports, managers can focus on analyzing insights and making informed decisions, rather than spending time manually searching for the right dashboard with the required data. You can access the scheduled reports tool using the [CI/CD Catalog](https://gitlab.com/explore/catalog).
- **[Adding a new event "MR first reviewer assigned" (17.2)](https://gitlab.com/gitlab-org/gitlab/-/issues/466383)** -- To improve the tracking of development workflows in GitLab, we added the Value Stream Analytics has been extended with a new stage event: "MR first reviewer assigned".
- **[AI Impact analytics: Code Suggestions acceptance rate and GitLab Duo seats usage (17.3)](https://about.gitlab.com/releases/2024/08/15/gitlab-17-3-released/#ai-impact-analytics-code-suggestions-acceptance-rate-and-gitlab-duo-seats-usage) -- These two new metrics highlight the effectiveness and utilization of GitLab Duo, and are now included in the AI Impact analytics in the Value Streams Dashboard, which helps organizations understand the impact of GitLab Duo on delivering business value.
- **[AI Impact analytics with enhanced sparklines trend visualization (17.3)](https://about.gitlab.com/releases/2024/08/15/gitlab-17-3-released/#ai-impact-analytics-with-enhanced-sparklines-trend-visualization)** -- We are excited to announce a significant improvement to our AI Impact analytics with the introduction of sparklines. These small, simple graphs embedded in data tables enhance the readability and accessibility of AI Impact data. By transforming numerical values into visual representations, the new sparklines make it easier to identify trends over time, so you can spot upward or downward movements. This new visual approach also streamlines the process of comparing trends across multiple metrics, reducing the time and effort required when relying solely on numbers.
- **[New Value Stream Analytics stage events for Cycle Time Reduction (17.3)](https://about.gitlab.com/releases/2024/08/15/gitlab-17-3-released/#new-value-stream-analytics-stage-events-for-cycle-time-reduction)** -- To improve the tracking of merge request (MR) review time in GitLab, we added a new stage event to Value Stream Analytics: MR first reviewer assigned. With this new event teams can identify where delays occur in the review process, find opportunities to improve collaboration, and encourage a culture of responsiveness and accountability among team members. Reducing the review time directly impacts the overall cycle time of development, leading to faster software delivery. For example, you can now add a new custom Review Time to Merge (RTTM) stage that starts with MR first reviewer assigned and ends with MR merged.
- **[Export code suggestions usage events (17.5)](https://about.gitlab.com/releases/2024/10/17/gitlab-17-5-released/#export-code-suggestion-usage-events)** -- Previously, AI impact analytics were available only on GitLab.com to GitLab Duo Enterprise customers, and on GitLab self-managed with a ClickHouse integration. Additionally, the default metrics were aggregated. Now, you can export raw code suggestion events from the GraphQL API. This way you can import the data into your data analysis tool to get deeper insights into acceptance rates across more dimensions, such as suggestion size, language, and user. The raw events are not stored in ClickHouse, so some AI Impact Analytics metrics become available to all GitLab deployments, including GitLab Dedicated and self-managed.

[Value Stream Management & DORA report generator tool](https://about.gitlab.com/releases/2024/06/20/gitlab-17-1-released/#new-value-stream-management-report-generator-tool) (17.1) – With the addition of the new Reports Generation Tool for Value Stream Management & DORA, we empower decision-makers to be more efficient and effective in the software development life cycle (SDLC) optimization. You can now schedule [DORA comparison metrics reports](https://gitlab.com/components/vsd-reports-generator#example-for-monthly-executive-value-streams-report) or the [AI Impact analytics report](https://about.gitlab.com/releases/2024/05/16/gitlab-17-0-released/#ai-impact-analytics-in-the-value-streams-dashboard) to be delivered automatically, proactively, and with relevant information in GitLab issues. With scheduled reports, managers can focus on analyzing insights and making informed decisions, rather than spending time manually searching for the right dashboard with the required data. You can access the scheduled reports tool using the [CI/CD Catalog](https://gitlab.com/explore/catalog).


### What We Are Currently Working On

* Migrating [epics to the work items](https://gitlab.com/groups/gitlab-org/-/epics/9290) framework will allow us to eventually bring more consistency with issues and address long-standing requests, like [assignees on epics](https://gitlab.com/groups/gitlab-org/-/epics/4231).
* [Wiki Connectivity](https://gitlab.com/groups/gitlab-org/-/epics/12835) - Allow users to connect their Wiki knowledge base with the rest of the DevSecOps lifecycle. 
* [Pages Multi-Version Support](https://gitlab.com/groups/gitlab-org/-/epics/10914) - Currently a project can have only a single version of a GitLab Pages site. This make it hard for customers to try new ideas on their sites without changing the only version of the site. Customers need a way to preview changes or have multiple environments for their GitLab Pages sites to make it possible to validate changes before deploying their site.
- **[Work Item Enhancements](https://gitlab.com/groups/gitlab-org/-/epics/6033)** -- [Standardize the workflow for creating planning objects](https://gitlab.com/groups/gitlab-org/-/epics/11012) and [associate DevSecOps artifacts to supported work item types](https://gitlab.com/groups/gitlab-org/-/epics/7105).
- **[Add support for custom fields to work items](https://gitlab.com/groups/gitlab-org/-/epics/235)**. Provide teams with a more robust solution for associating business-specific meta-data to work items. We're starting with adding support for [basic custom fields](https://gitlab.com/groups/gitlab-org/-/epics/14904), which will be configurable within root groups. 
- **[Enable work items (Tasks) to be visible on Boards](https://gitlab.com/gitlab-org/gitlab/-/issues/368816)**. Teams can manage their tasks (and other work items) from within Boards. 
- **[Complete the migration of issues to work items](https://gitlab.com/groups/gitlab-org/-/epics/9584)**. Replace the legacy issue detail view with the new and improved real-time work item detail view. 

* Improved ["AI Impact" analytics to the Value Stream Dashboard](https://gitlab.com/groups/gitlab-org/-/epics/12978#roadmap), to provide more holistic view of the ROI from the investments in AI features. We're currently focusing on adding [per-user metrics](https://gitlab.com/groups/gitlab-org/-/epics/15026), making [basic AI Impact Analytics available for Duo Pro customers via the GraphQL API](https://gitlab.com/gitlab-org/gitlab/-/issues/498497), and making [iterative improvements to the data visualization and user experience on the AI Impact Analytics dashboard](https://gitlab.com/groups/gitlab-org/-/epics/15030).
* **[Enhanced configuration for custom value stream analytics reports](https://gitlab.com/groups/gitlab-org/-/epics/9129)** - With this change, custom VSA report stage configuration moves from a modal to a standalone page and adds support for persistent filters that apply to all items included in the custom VSA report.

- **[DORA Performers project comparison](https://gitlab.com/gitlab-org/gitlab/-/issues/408516)** — In a previous release, we added a visualization to show the number of projects performing on a low/medium/high scale for the primary DORA metrics. In this release, we will expand the performers table to include a project-level breakdown of DORA metrics to quickly understand which projects are performing compared to those not.


### What's Next For Us

Over the next year, we are focused on the following:

- **[Group issues](https://gitlab.com/groups/gitlab-org/-/epics/12320)**. Issues can be created within groups without depending on a project within the group. This will optionally allow teams to consolidate their planning workflows within a single location instead of spreading them across a group and a project.  
- **[Work items open in a drawer within boards and lists](https://gitlab.com/gitlab-org/gitlab/-/issues/387224)**. Reduce the context switching and tab fatique when drilling down into a work item detail view. 
- **[Customizable work item statuses](https://gitlab.com/gitlab-org/gitlab/-/issues/368290)**. Provide a foundation for building a more robust work item lifecycle management solution, and enable teams to mark work items as done or cancelled. 
- **[Report on iteration velocity and volatility](https://gitlab.com/groups/gitlab-org/-/epics/435)** -- Helps teams have meaningful discussions about trade-offs and estimations when planning upcoming iterations. Issues and tasks can be assigned to iterations, so our next step is [showing parent/child relationships in the iteration report](https://gitlab.com/gitlab-org/gitlab/-/issues/457538), followed by [displaying velocity and volatility](https://gitlab.com/gitlab-org/gitlab/-/issues/457094). 
- **[Work items are natively supported within Groups](https://gitlab.com/groups/gitlab-org/-/epics/8308)** -- Eliminate the need to maintain projects under groups solely for agile planning purposes, allow teams to consolidate their planning activities at the group level, and enable issues and epics to be migrated to work items. We're currently working on [the remaining blockers](https://gitlab.com/gitlab-org/gitlab/-/issues/458986) to feature parity between legacy issues and work item issues. Once issues are migrated to work items, we will be able to turn on native Group Issues. 

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


- Moving DORA charts from the [CI/CD Analytics into the new dashboarding framework](https://gitlab.com/groups/gitlab-org/-/epics/16117)
- **Add a new [Dashboard for Executive](https://gitlab.com/groups/gitlab-org/-/epics/9317)** to enable decision-makers to identify trends, patterns, and opportunities for digital transformation improvements. In the next phases, we will focus on the following: 
  - Adding a [new DORA Metrics Overview page](https://gitlab.com/-/project/278964/uploads/9def9ff31b9812ad216043a40bdee5f9/DORA_metrics_-_Option_D.png) in the Value Stream Dashboard. This is related to https://gitlab.com/gitlab-org/gitlab/-/issues/453958. 
  - Adding a [new DORA Metrics Analytics page](https://gitlab.com/-/project/278964/uploads/11d6be804f65814c8ba9fe049338d4cc/DORA_metrics_-_Option_E.png) in the Value Stream Dashboard. This is related to https://gitlab.com/gitlab-org/gitlab/-/issues/453958. 
  - Adding [Custom Metrics Calculation Rules](https://gitlab.com/groups/gitlab-org/-/epics/11490) for DORA, to [support multiple environment branches](https://gitlab.com/gitlab-org/gitlab/-/issues/358385) (with GitLab flow), and [improve the metric calculation](https://gitlab.com/gitlab-org/gitlab/-/issues/444295) to effectively track incidents and deployments.
  - [Move DORA metrics to ClickHouse](https://gitlab.com/gitlab-org/gitlab/-/issues/451752) to provide best experience and robust indicators for measuring the metrics.
  - Adding the Fifth DORA Metric - [Reliability - Operational performance](https://gitlab.com/gitlab-org/gitlab/-/issues/393003)

- Enhancing our ability to [visualize data](https://gitlab.com/groups/gitlab-org/-/epics/5516) by providing a singular hub for accessing and presenting information, adaptable to different visualization preferences.
- Maturing our Wiki to satisfy more [jobs to be done](https://gitlab.com/groups/gitlab-org/-/epics/12826).

### What We're Not Doing

* GitLab will not provide extensive configuration options that complicate collaboration and increase the maintenance burden. Examples are:
   * Blocking users from editing work items due to field-level configuration.
   * Creation of state workflows with transition rules. 
   * Configuring screen field layouts.
* Plan functionality will be generic enough to allow its use by many personas and use cases. However, we will focus on optimizing for use cases for DevSecOps workflows in the immediate future. Our long-term vision is to become the system of record for planning across any function, but we are starting with DevSecOps teams as our target.  Example use cases that we are not focused on include:
   * Marketing
   * HR
   * Legal
   * Service Desk
* In order to meet the vision described in this page, we will decrease investment in our Requirements Management, Test Management, DevOps Reports, Design Management and Time Tracking categories. We will continue to address defects and support community contributions but we are not planning to make significant improvements. 


### Cross-Stage Initiatives

Plan offers functionality that ties into workflows in other stages.  We are actively collaborating with other stages that are building upon Plan functionality to meet their users needs.

* The Manage:Import and Integrate group has built a Jira integration that displays Jira Issue data within GitLab. We will collaborate with that team to tie Jira Issues into more workflows like reporting and tying Jira Issues to higher level work items.
* The Manage:Import and Integrate owns the [Jira importer](https://docs.gitlab.com/ee/user/project/import/jira.html) to allow Jira issues to be migrated to GitLab. We will continue to work with that team to extend GitLab work items to accomodate more critical data elements from Jira to ensure a seamless import process.
* The Plan stage and the [Service Desk Single Engineer Group](https://handbook.gitlab.com/handbook/engineering/development/incubation/service-desk/) are collaborating on [accelerating Service Desk](https://gitlab.com/groups/gitlab-org/-/epics/8769), which will extend work items to support adjacent use cases to portfolio and team planning.
* Plan:Optimize is collaborating with Manage:organization to Consolidate [Value Stream Analytics Group & Project into a single object - Workspace](https://gitlab.com/groups/gitlab-org/-/epics/9295).
* Plan:Optimize is collaborating with Analytics:Product Analytics to consolidate standalone analytics pages and reports to a [platform-level dashboarding framework](https://gitlab.com/groups/gitlab-org/-/epics/13801).
* Plan:Optimize is collaborating with Govern:Threat Insights to add [Vulnerabilities metrics to the Value Streams Dashboard](https://gitlab.com/gitlab-org/gitlab/-/issues/383697).
* Plan:Optimize is collaborating with AI:Framework team to create an [AI Impact Dashboard](https://gitlab.com/groups/gitlab-org/-/epics/12978) to better quantify the effect of using AI on productivity.
* Plan:Knowledge collaborates with Groups across all areas of GitLab to develop and improve upon the rich text editor. The rich text editor is a what you see is what you get editing experience, and is an alternative to the plain text editor which requires knowledge of markdown to leverage.
* Plan:Project Management is collaborating with Deploy:Environments on a [platform-level automation framework](https://gitlab.com/groups/gitlab-org/-/epics/13171).


### Target audience

GitLab identifies who our DevSecOps application is built for utilizing the following categorization. We list our view of who we will support when in priority order.
* 🟩 - Targeted with strong support
* 🟨 - Targeted but incomplete support
* ⬜️ - Not targeted but might find value

### Today

1. 🟩 [Software Developers](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
1. 🟨 [Development Team Leads](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
1. 🟨 [Application Development Director](https://handbook.gitlab.com/handbook/product/personas/#dakota-application-development-director)
1. 🟨 [Product Managers](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)
1. 🟨 [Software Engineer in Test](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
1. 🟨 [Product Designers](https://handbook.gitlab.com/handbook/product/personas/#presley-product-designer)
1. 🟨 [DevOps Engineers](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
1. 🟨 [Security Operations Engineers](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer)
1. 🟨 [Release Manager](https://handbook.gitlab.com/handbook/product/personas/#rachel-release-manager)
1. 🟨 [Security Analysts](https://handbook.gitlab.com/handbook/product/personas/#sam-security-analyst)
1. ⬜️ [Application Ops](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops)
1. ⬜️ [Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
1. ⬜️ [Compliance Managers](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)
1. ⬜️ [Systems Administrator](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)

### Medium Term (1-2 years)

1. 🟩 [Software Developers](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
1. 🟩 [Development Team Leads](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
1. 🟩 [Application Development Director](https://handbook.gitlab.com/handbook/product/personas/#dakota-application-development-director)
1. 🟩 [Product Managers](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)
1. 🟨 [Software Engineer in Test](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
1. 🟨 [Product Designers](https://handbook.gitlab.com/handbook/product/personas/#presley-product-designer)
1. 🟨 [DevOps Engineers](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
1. 🟨 [Security Operations Engineers](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer)
1. 🟨 [Release Manager](https://handbook.gitlab.com/handbook/product/personas/#rachel-release-manager)
1. 🟩 [Security Analysts](https://handbook.gitlab.com/handbook/product/personas/#sam-security-analyst)
1. ⬜️ [Application Ops](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops)
1. ⬜️ [Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
1. 🟨 [Compliance Managers](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)
1. ⬜️ [Systems Administrator](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)


### Pricing

Our pricing strategy is derived from GitLab's [buyer based pricing model](https://handbook.gitlab.com/handbook/company/pricing/#three-tiers), with Free aligning to individuals, Premium to teams and Ultimate to organizations.

##### Free

As a general rule of thumb, features will fall in the Core/Free tier when they meet one or more of the following criteria:
* The feature is primarily for an individual planning their work. 
* The feature enables planning for time periods that span up to a month.
* The feature does not require cross-linking or rolling up data across multiple groups. 

Some examples include:
* Issues, Stories and Bugs
* Project and Group Issue Boards
* Labels

##### Premium

As a general rule of thumb, features will fall in the Premium tier when they meet one or more of the following criteria:
* The feature is primarily for a team planning their work rather than an individual. 
* The feature enables collaboration for multiple individuals to plan work together. 
* The feature enables multi-month or quarterly planning.
* The feature cross-links or aggregates data across multiple groups.

Some examples include:
* Epics and Features
* Epic Boards
* Multiple Group Issue Boards
* Scoped Labels

##### Ultimate

As a general rule of thumb, features will fall in the Ultimate tier when they meet one or more of the following criteria:
* The feature focuses on enabling an organization or enterprise to operate at scale rather than individuals or single teams.
* The feature enables yearly and multi-year planning.
* The feature enables collaboration for multiple teams to plan work. Functionality aligns to capabilities found in [Portfolio SAFe](https://www.scaledagileframework.com/portfolio-safe/).

Some examples include:
* Multi-level epics, Themes and OKRs
* Configurable terminology to match an organization naming convention
* Portfolio-level Roadmaps
* Issue and Epic Health Reporting


An example of what the end result data model and pricing could look like based on these pricing principles:

![Work Items Hierarchy](/images/direction/plan/workitemhierarchy.png)
