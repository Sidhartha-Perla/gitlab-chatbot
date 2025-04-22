---
layout: markdown_page
title: "Category Direction - DevOps Reports"
description: "Discover how GitLab’s DevOps Reports provide actionable insights into your development and operations processes for continuous improvement."
canonical_path: "/direction/plan/devops-reports/"
---

- TOC
{:toc}

| Category | **DevOps Reports** |
| --- | --- |
| Stage | [Plan](https://handbook.gitlab.com/handbook/product/categories/#plan-stage) |
| Group | [Optimize](https://handbook.gitlab.com/handbook/product/categories/#optimize-group) |
| Maturity | [Minimal](/direction/#maturity) |
| Content Last Reviewed | `2023-12-30` |

### Introduction and how you can help
Thanks for visiting the direction page for DevOps Reports in GitLab. This page is being actively maintained by the Product Manager for the [Optimize group](https://handbook.gitlab.com/handbook/product/categories/#optimize-group). If you'd like to contribute or provide feedback on our category direction, you can:

1. Comment and ask questions regarding this category vision by commenting in the [roadmap epic for this category](https://gitlab.com/groups/gitlab-org/-/epics/5795).
1. Search for specific issues in this category using the `Category:Devops Reports` label.

### Overview

GitLab has [extraordinary breadth](https://about.gitlab.com/direction/) for a single application, providing an entire [DevOps platform](https://about.gitlab.com/stages-devops-lifecycle/) from portfolio planning all the way through to monitoring and service desk. As such, GitLab is uniquely positioned to provide a complete picture of your organization's DevOps journey and your return on investment in automation and DevOps practices.

GitLab shows [adoption of key GitLab features across an organization](https://docs.gitlab.com/ee/user/group/devops_adoption/), with a breakdown by sub groups. This provides insight into which groups are using each feature. The DevOps Reports category aims to extend the current functionality to answer questions such as:

- How many of my teams are doing security scans?
- How much progress has my organization made on our DevOps journey?
- How has the adoption of DevOps practices changed software delivery performance?
- Which teams have achieved the highest performance? What tooling did they use to accomplish this?
- Which teams need help with DevOps adoption? Which teams are best positioned to provide this help?

DevOps Adoption reports are also available in [Registration Features Program](https://docs.gitlab.com/ee/administration/settings/usage_statistics.html#registration-features-program) for GitLab customers with a self-managed instance running GitLab Enterprise Edition.

#### Themes

* **Adoption insights** 
  - Understand how teams are using GitLab
  - See which teams across your organization have adopted specific DevOps practices and learn from their experiences. 
  - Find teams that have not adopted specific practices and find out how you can help with adoption
  - View the percentage of key DevOps practices your organization has adopted to understand the status of your DevOps journey and the return of investment you are getting from GitLab
  - Measure progress on initiatives such as the adoption of security scanning to comply with industry regulations, or the addition of Codeowners to help identify who needs to review contributions to a repository
  - Track progress on migrating to GitLab from other tools that serve a single stage of the software development lifecycle. See which teams are yet to transition across. 
  

* **Adoption trends**
  - See how GitLab adoption is changing over time
  - See which GitLab features are being adopted most rapidly
  - Identify potential issues such as adoption of a feature followed by decline in usage of that feature. This could indicate a need for training on how to use the feature
  - Find where uptake has been slow. This may indicate a lack of awareness of the feature. 

* **Maturity of adoption** 
  - It's not always enough to know whether a feature or DevOps practice has been adopted. DevOps Reports aims to go a step further and show maturity of adoption such as **how often** security scans are being run. 

* **Correlation between adoption and performance** 
  - See how adoption of DevOps practices has improved the speed and reliability of code development by viewing DORA metrics alongside DevOps adoption data.
  - Identify highest performing teams based on DORA metrics and see what DevOps practices contributed to their success. Apply those learnings to other teams and track their progress on DORA metrics.
  - Find teams that are struggling with a specific DORA metric, such as Deployment Frequency. Put together a set of recommendations aimed at improving performance in that area.

* **Customized insights** 

  - Not all GitLab features are applicable for your application. We plan to support customizations to show only the data that is important to you. If you don't build web applications, hide features like Browser Performance Testing so they don't count towards your DevOps maturity score.
  - Pick the three GitLab features you wish your organization was using better and customize the dashboard to track progress of just those features.
  - Filter the dashboard to show only Ultimate features to more easily understand the value you are getting from the Ultimate tier.

* **Deep dive**

  - For each feature represented in DevOps Reports, link to key resources such as documentation so users can learn about the value of these features and how to use them
  - Link to corresponding areas in the GitLab UI so users can drill in and get more detailed information on feature usage

### Jobs to be done



### What's Next and Why
- Adding "AI Adoption view" by adding "AI features" to the [DevOps Adoption report](https://gitlab.com/gitlab-org/gitlab/-/issues/443699)
- Adding the [missing Sec features to DevOps Adoption Report](https://gitlab.com/gitlab-org/gitlab/-/issues/361000).
- Make [DevOps adoption report more granular](https://gitlab.com/gitlab-org/gitlab/-/issues/350389).
- Add a new [Dashboard for Executive](https://gitlab.com/groups/gitlab-org/-/epics/9317) to enable decision-makers to identify trends, patterns, and opportunities for digital transformation improvements. In the first phases, we will focus on the following:
   - [Executive-level summary](https://gitlab.com/groups/gitlab-org/-/epics/9558) of key metrics related to software performance and flow of value across the organization.
   - [Visualizing metrics comparisons](https://gitlab.com/groups/gitlab-org/-/epics/9559) to help decision-makers understand how different metrics are performing relative to each other or to identify trends and patterns in the data.
   - [Filtering and drill-down](https://gitlab.com/gitlab-org/gitlab/-/issues/383684) into the underline data to get a deeper understanding of specific metrics or trends to identify actionable insights.
   - [Customizable widgets](https://gitlab.com/groups/gitlab-org/-/epics/8925) to show data that is relevant to user's goals and needs.
Group Optimize is currently focused on [usability improvements](https://gitlab.com/groups/gitlab-org/-/epics/6050), aligned with the company goal to improve the [SUS](https://handbook.gitlab.com/handbook/product/ux/performance-indicators/system-usability-scale/) score.


### Maturity Plan

This category is currently **Minimal**. The next step in our maturity plan is achieving a **Viable** state of maturity. We are tracking progress to reach this next maturity state in [gitlab&1499](https://gitlab.com/groups/gitlab-org/-/epics/1499).
* You can read more about GitLab's [maturity framework here](https://about.gitlab.com/direction/#maturity, including an approximate timeline.
