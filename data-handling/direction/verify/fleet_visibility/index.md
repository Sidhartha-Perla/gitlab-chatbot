---
layout: markdown_page
title: "Category Direction - Fleet Visibility"
description: "This is the Product Direction Page for the Runner:Fleet Visibility product category."
canonical_path: "/direction/verify/fleet_visibility/"
---

## Navigation & Settings

|                       |                               |
| -                     | -                             |
| Stage                 | [Verify](/direction/verify/)  |
| Maturity              | Complete |
| Content Last Reviewed | `2025-01-15`                  |

### Introduction and how you can help
<!-- Introduce yourself and the category. Use this as an opportunity to point users to the right places for contributing anzd collaborating with you as the PM -->
Thanks for visiting this direction page on the Fleet Visibility category at GitLab. This page belongs to the [Runner Group](https://handbook.gitlab.com/handbook/product/categories/#runner-group) within the Verify Stage and is maintained by [Darren Eastman](mailto:deastman@gitlab.com).

### Strategy and Themes

Our vision is that as customers more deeply integrate AI into their development processes, in one unified dashboard, they can manage a GitLab Runner Fleet at scale and have deep visibility into CI/CD pipeline metrics (`pipeline execution time,` `pipeline failure rate,` `CI job duration,` `CI job queue time,` and `CI job failure rate`), that easily correlate to the specific CI/CD build environment. 

Adequate Fleet Visibility starts with providing at-a-glance insights into all the statuses (online, offline, stale) of all runner-build servers in your organization. Fleet Visibility will allow you to determine the group or project a runner is associated with while also surfacing critical metrics such as runner build queue performance, failure rates, and the most heavily used runners.

This category also aims to provide platform administrators and developers with the metrics they need to identify CI pipeline performance or reliability issues and determine which component to focus on when using trial-and-error approaches to optimization. We aim to integrate key CI build fleet and pipeline metrics within the GitLab UI to eliminate developer pain points with automated CI/CD builds that negatively impact productivity. Those pain points include developers trying to determine if and how to optimize CI job duration or troubleshoot CI/CD job failures due to the build environment.

By correlating the insights provided to platform administrators at the admin or group levels exposed in the Fleet Dashboard with the CI/CD job and pipeline execution metrics (runner queue depth, job duration trends, job failure rates, pipeline reliability) at the project level exposed in CI Insights, organizations will spend less time building custom observability reporting dashboards for GitLab CI/CD pipelines. Developers and platform administrators will have a shared understanding of CI/CD performance trends across the platform.

For executives, as the AI-powered GitLab DevSecOps platform enables your development teams to deliver secure software faster, Fleet Visibility provides your operations team the visibility they need to operate a CI/CD build infrastructure at scale cost-effectively and efficiently on any public or private cloud infrastructure. We aim to provide your platform teams the capabilities to deliver a great developer experience, enable developer efficiency by reducing barriers to adopting CI/CD best practices, and optimize cloud computing costs for the CI/CD build infrastructure.

### 1 year plan
<!--
1 year plan for what we will be working on linked to up-to-date epics. This section will be most similar to a "road-map". Items in this section should be linked to issues or epics that are up to date. Indicate relative priority of initiatives in this section so that the audience understands the sequence in which you intend to work on them.
 -->
**Runner Fleet Dashboard**

The [Runner Fleet Dashboard - Admin View: Starter Metrics](https://gitlab.com/gitlab-org/gitlab/-/issues/424495) was released in 16.5.  The included metrics widgets for the initial release are as follows:

- Fleet Health (Postgres DB)
- Top Active Runners (Postgres DB)
- Wait Time to Pick up a Job (Clickhouse DB)

We followed this up by releasing the [Runner Fleet Dashboard for Groups](https://docs.gitlab.com/ee/ci/runners/runner_fleet_dashboard_groups.html) in the GitLab 17.1 release.  With this release, customers on GitLab.com and Self Managed can manage runner fleets at the group level. We have heard from many customers that they need this capability and related APIs to augment the current observability tooling and custom dashboards they rely on to monitor and operate GitLab CI/CD and Runners. Therefore, we will enable access to the data via GraphQL APIs for those customers who need to integrate the CI metrics with data from their internal systems to enable organization-specific analytics.

We plan to [gather and analyze customer feedback](https://gitlab.com/gitlab-org/gitlab/-/issues/421737) over the next few months based on the current features in the Fleet Dashboard. That feedback will guide the next evolution of the Fleet Dashboard strategy into calendar year 2025. While we have already identified additional metrics, such as runner failure trends, that could be valuable to include in the dashboard, it is also likely, based on recent customer feedback, that simply extending the metrics data model and enabling customers to create their reports and visualizations is the most valuable future iteration.

Regarding prediction, one prevalent theme in customer conversations is determining when there may be a slowdown in runner queue performance. Another critical problem and pain point often cited by customers is configuring the Runner Fleet to find the optimal balance between compute costs and developer efficiency as measured by reduced CI/CD job durations. These are classic prediction problems, so we aim to explore if we can reduce the cost of prediction and fleet operational costs for our customers by incorporating ML/AI into the Fleet Dashboard. With Clickhouse as the database layer and a new analytics database table structure for Runner Fleet, we believe the foundational elements are in place to make this next evolution a reality in FY26.

Also, based on many customer conversations, operating a CI/CD build fleet on Kubernetes can be complex. Platform engineering teams sometimes must spend months configuring and optimizing the Kubernetes environment to reliably run their organization's CI/CD jobs. For new users of GitLab, this configuration and optimization effort can be a critical blocker to CI adoption. 

In Runner Core, we have seen the immense value to platform teams of simply enabling the printing of Kubernetes events directly in the CI/CD job log. So, we are exploring the following questions:
- How can we expose the right metrics for the Kubernetes CI/CD build infrastructure in the Fleet Dashboard? 
- Will exposing the right Kubernetes stack infrastructure metrics and associating that data with the CI/CD job metrics reduce the operational burden for customers who use Kubernetes as the CI/CD build infrastructure? 

We aim to explore these questions in depth in planning the Fleet Dashboard's future roadmap. 

Our vision is that the next evolution of cloud-native CI/CD will automatically self-optimize across the entire workflow—from the GitLab CI pipeline configuration to the Runner Kubernetes CI/CD build infrastructure stack.

**CI/CD Insights**

The first phase in the unified Developer Efficiency strategy is solving the critical visibility problems developers and platform administrators have with using GitLab CI/CD. Those visibility problems include the fact that there is no built-in report in [GitLab CI/CD analytics](https://docs.gitlab.com/ee/user/analytics/ci_cd_analytics.html) for a developer to determine if a CI job is running as expected from a duration perspective or whether a CI job is unhealthy, as represented by an increase in job failures. As a result, customers have had to create custom reporting systems or implement third-party observability tools using data exposed in the GitLab jobs API.

Our goal for the second half of FY25 is to [improve the GitLab CI/CD analytics view](https://gitlab.com/gitlab-org/gitlab/-/issues/4444681) to incorporate the critical metrics our customers tell us they need to use, monitor, and optimize GitLab CI/CD efficiently. That includes providing insights into the pipeline and CI/CD job performance metrics with drill-down capabilities to individual jobs so developers can quickly identify CI/CD jobs with abnormal failure rates, leading to proactive CI/CD job optimization and improved reliability. Providing visibility into all aspects of CI/CD job performance is only the foundation. We intend to develop solutions using this data that seek to eliminate developer pain and frustration related to slow CI/CD job start times, less than optimal CI/CD job duration, and job failures that result in lost developer productivity as developers troubleshoot CI/CD failures, (not a result of code change), instead of working on value add sofware development tasks.

#### What is next for us
<!-- This is a 3 month look ahead for the next iteration that you have planned for the category. This section must provide links to issues or
or to [epics](https://handbook.gitlab.com/handbook/product/product-processes/#epics-for-a-single-iteration) that are scoped to a single iteration. Please do not link to epics encompass a vision that is a longer horizon and don't lay out an iteration plan. -->

In the next three months (Feburary to April) we are focused on the following:

**CI/CD Insights**

[Improve the GitLab CI/CD analytics view](https://gitlab.com/gitlab-org/gitlab/-/issues/444468)

#### What we are currently working on
<!-- Scoped to the current month. This section can contain the items that you choose to highlight on the kickoff call. Only link to issues, not Epics.  -->

- We are currently working on adding the foundational API's required to deliver the new [GitLab CI/CD analytics view](https://gitlab.com/gitlab-org/gitlab/-/issues/444468) currently targeted for delivery in 17.11.

<!-- 
#### What we recently completed

Lookback limited to 3 months. Link to the relevant issues or release post items. -->

#### What is Not Planned Right Now
<!--  Often it's just as important to talk about what you're not doing as it is to discuss what you are. This section should include items that people might hope or think
we are working on as part of the category, but aren't, and it should help them understand why that's the case.
Also, thinking through these items can often help you catch something that you should in fact do. We should limit this to a few items that are at a high enough level so someone with not a lot of detailed information about the product can understand -->

In the near term we are not focused on design or development efforts to improve Runners usability in [CI/CD settings](https://docs.gitlab.com/ee/administration/#cicd-settings) at the [project level](https://gitlab.com/groups/gitlab-org/-/epics/6867).

While improvements in this view could be valuable to the [software developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer) persona, feedback from customers indicates that providing meaningful CI insights that cover vital metrics such as CI job success and failure rates, job duration metrics, average job retries, average queue time for each job, are more valuable for customers and are critical enablers for broader CI adoption.

### Best in Class Landscape
<!-- Blanket description consistent across all pages that clarifies what GitLab means when we say "best in class" -->

BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

At GitLab, a critical challenge is simplifying the administration and management of a CI/CD build fleet at an enterprise scale and enabling developer efficiency. This effort is one foundational pillar to realizing the vision of GitLab Duo AI-optimized DevSecOps. Competitors are also investing in this general category. Earlier this year GitHub announced a new management experience that provides a summary view of GitHub-hosted runners. This is a signal that there will be a focus on reducing maintenance and configuration overhead for managing a CI/CD build environment at scale across the industry.

We also now see additional features on the GitLab public roadmap signaling an increased investment in the category we coined here at GitLab, 'Runner Fleet.' These features suggest that GitHub aims to provide a first-class experience for managing GitHub Actions runners and include features in the UI to simplify runner queue management and resolve performance bottlenecks. With this level of planned investment, it is clear that there is recognition in the market that simplifying the administrative maintenance and overhead of the CI build fleet is critical for large customers and will help enable deeper product adoption.

Indirect competitor Actutated is the first solution that we have seen whose product includes a [dashboard for Runners and build queue](https://docs.actuated.dev/dashboard/#runners) visibility. This is another strong signal that providing solutions that reduce the CI/CD build infrastructure's management overhead is valuable for organizations with mature DevOps practices.

In the CI Insights arena, a few startups, for example, [Trunk.io](https://trunk.io/ci-analytics), are providing CI visibility solutions for GitHub actions. The [Datadog CI Visbility product](https://www.datadoghq.com/product/ci-cd-monitoring/) is a mature, full-featured offering that provides CI/CD insights for GitLab CI/CD using the GitLab jobs API as the foundational layer.

To ensure that our GitLab customers can fully realize the value of GitLab's one DevSecOps platform vision, we must provide solutions that eliminate the complexities, manual tasks, and operational overhead and reduce the costs of delivering a CI build environment at scale. Our goal in FY25 is to introduce the basic building blocks for in-product developer efficiency visibility. These solutions will be good enough for customers who are not fully invested in third-party observability or custom tooling, allowing them to observe, analyze, optimize, or troubleshoot CI job failures natively in GitLab. However, the end state is that we will deliver GitLab native solutions that eliminate the impact on developer efficiency related to all aspects of reliable CI/CD job execution.

#### Key Capabilities
<!-- For this product area, these are the capabilities a best-in-class solution should provide -->

The key capabilities that we hear from customers describing fleet management and CI insights pain points are as follows:

- What is the root cause of a CI pipeline failure?
- CI/CD job failure rate trends
- CI/CD job duration trends
- CI/CD job retry rate trends
- Determine when test jobs started failing.
- Diagnose whether a test is Flaky versus failing consistently.
- Runner queue visibility (wait time)
- Frictionless upgrades
- Security
- Cost visibility for runners hosted on public cloud infrastructure
- Fleet autoscaling
- Fleet cost management while maintaining internal service level objectives (SLOs)
- Automatic fleet configuration optimization
- Managing runner sprawl
- Configuring and managing a heterogeneous runner fleet (container builds on Linux, container builds on Windows, shell builds on Windows, shell builds on macOS)
- Self-service runner creation for the developer persona
- Automating choosing the right cloud and compute to host a Runner based on CI/CD build performance

#### Top [1/2/3] Competitive Solutions

Runner Fleet is still a nascent category; competitors like GitHub are beginning to invest in this area. On their future roadmap, GitHub plans to introduce [seamless management of GitHub-hosted and self-hosted runners](https://github.com/github/roadmap/issues/504). This feature aims to deliver a "single management plane to manage all runners for a team using GitHub." GitHub also plans to offer [Actions Performance Metrics](https://github.com/github/roadmap/issues/561) to provide organizations with deep insights into critical CI/CD performance metrics. 

One example of how the cloud infrastructure market can evolve is [Active Assist for Google Cloud](https://cloud.google.com/solutions/active-assist) - a solution to optimize cloud operations cost reduction. Another is the recently [announced Komodor product - KlaudiaAI](https://komodor.com/blog/introducing-klaudiaai-redefining-kubernetes-troubleshooting/), which uses generative AI models to generate root cause analysis automatically and recommended fixes for issues on Kubernetes. Therefore we can imagine a future where Microsoft and GitHub bring to market AI-based solutions that use AI to more efficiently run GitHub Actions Runners on Azure infrastructure.

Our GitLab competitive position is solid in that we will continue to invest in features and capabilities to ensure that customers can use GitLab Runners efficiently on any cloud provider.

In the insights space DataDog has a [CI and Test Visibility](https://docs.datadoghq.com/continuous_integration/) offering and [CircleCI](https://circleci.com/docs/insights/) has had an insights offering for some time. While there is no main GitHub actions functionality there are several offerings in the marketplace for collecting test/run data and displaying it on a dashboard.

[Harness.io, Software Engineering Insights](https://developer.harness.io/docs/software-engineering-insights) includes several configurable [CI/CD job](https://developer.harness.io/docs/software-engineering-insights/sei-metrics-and-reports/velocity-metrics-reports/ci-cd-reports) and pipeline metric widgets.  The [CI/CD job count](https://developer.harness.io/docs/software-engineering-insights/sei-metrics-and-reports/velocity-metrics-reports/ci-cd-reports#job-count-reports) metric category aims to provide developers with insights into CI/CD job success and failure rates. We also see additional investment planned by [Harness.io](https://developer.harness.io/roadmap/#platform) with their Pipeline Analytics feature slated for Q3 2024 (August 2024+).

CloudBees has the [CI Workload Insights dashboard](https://docs.cloudbees.com/docs/cloudbees-cd/latest/dashboards-built-in/workload-insights) that includes `workload deviation`, `mean wait time`, `mean wait time deviation`, `job failure rate deviation`, and `job duration deviation` metrics.

In the Test Reduction area Sealights offers a [CutTests](https://www.sealights.io/solutions/cut-end-to-end-tests-cycle-time/) solution and [Redefine.dev](https://www.redefine.dev/product) is a new player in the space taking advantage of AI to reduce future test runs for faster pipelines.
