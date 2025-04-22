---
layout: markdown_page
title: "Custom Dashboards Foundation Category Direction"
description: "GitLab Platform Insights Custom Dashboards Foundation Category Direction Page"
---

- TOC
{:toc}

We would appreciate your feedback on this direction page. Please create an issue to collaborate with us or propose a MR to this page!

## Overview

Data is everywhere. Whether explicitly calculated and collected, or generated automatically, users need a way to interface with their GitLab data in order to meaningfully understand and turn the data into valuable actions to improve their workflows. With the Custom Dashboards Foundation effort, backed by a new unified event collection platform, users will be able to query, visualize, and analyze their GitLab data. 

## Mission & Vision

### Mission

Remove data boundaries across all stages of GitLab and empower customers to explore their data and build custom dashboards tailored to their specific use cases. All the data, both native to GitLab, and outside of GitLab, can be queried, visualized, collaborated upon, and operationalized without the need for GitLab development team intervention.  

### Vision

[Dashboards](https://gitlab.com/groups/gitlab-org/-/epics/13801) are a core piece of any analytics workflow. Customers use them to track a variety of things from customer behavior to service health to team productivity/output. GitLab is striving to allow customers a single place to ask questions of their data, source agnostic, so that they can truly connect their code, delivery, team productivity, security results, and customer outcomes in a single, unified visualization. We have heard the need for customers to be able to customize their reporting and build views that align with their team/project specific needs. 

The Platform Insights team developed a dashboard framework to serve as the single source of truth for the way GitLab internal teams should develop and deliver their prescriptive dashboard views. Our goal is that we catalog all the current analytics dashboards available in GitLab and iteratively migrate them to the standard dashboard framework in order to provide customers with a consistent user experience.

As we pave the way for consolidated data exploration with efforts of [data unification](https://gitlab.com/groups/gitlab-org/architecture/gitlab-data-analytics/-/epics/3) and unified query language, GLQL, we get closer to the grander vision of unlocking the ability for our customers to build their own dashboards from all GitLab data sources.  Starting with the Optimize stage, we will iteratively unlock new GitLab data sources and produce experiences in the dashboard Data Explorer that allow customers to query their data and build custom dashboards that combine visualizations for any supported source.  In the next few quaters (FY25 Q4 into FY26), we will get closer to providing a single Dashboard experience that is available at group and project levels. Empowering customers to build their own reporting views means that individual GitLab internal teams will be able to spend less time building prescriptive experiences and more time enriching the GitLab features that produce that data. It also means that our customers can immediately see the value of their ingested data without waiting for reporting feature requests to be prioritized. This will ultimately lead to more customer satisfaction with the overall GitLab reporting experience, and improved time to value for depth on GitLab features. 

#### [Q4 FY25 Goals](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/9520)

* [Decouple Product analytics from the dashboard framework and customizable dashboard concepts and improve the onboarding experience for new data source](https://gitlab.com/groups/gitlab-org/-/epics/15691)
* [Migrate all basic panel structured dashboards under the Analyze left navigation to the framework](https://gitlab.com/gitlab-org/gitlab/-/issues/506650).  This migration can be completed by the Platform Insights team and will not require prioritization or resources from the individual dashboard owners.  Completing this work unlocks the ability for those teams to move more quickly on future modifications and utilitize the standard design system workflows for introducing new requirements.
* Complete an end-to-end migration into both the dashboard framework and early exploration into the customizable framework for the Optimize dashboards and datasource.  [By end of Q4, both the Value Stream Analytics and AI Impact (GitLab Duo Adoption) dashboards should be fully implemented in the framework.](https://gitlab.com/gitlab-org/gitlab/-/issues/500216)
* Deliver updated onboarding documentation, demos, and developer content to kick-start the adoption of future team dashboards. 
* [Begin exploring the use of GLQL](https://gitlab.com/gitlab-org/gitlab/-/issues/497578) as the single method for data querying across all supported data sources. By providing customers with a consistent method for querying data, users can more easily ramp up on building dashboards tailored to their needs.  Without this single query language, the query experience will feel disjointed and customers will have to understand what's possible for each data source (aggregations, filter options, time constraints) and may lead to dashboards that have visualizations that are not easily meshed together.  We will make our best efforts in Q4 to work through options to inform users via tooltips and error messaging when issues arise in individual charts due to incompatibility with applied filters or time ranges.  Note that this is also common practice in competitive solutions and even a unified query language can still need chart level messaging to highlight data constraints behind the scenes.

#### Q1 FY26 Goals

* Work directly with PM/UX in Security Insights stage to develop new Vulnerability Management reports on the dashboard framework
* Collaborate with Compliance team to understand their requirements for their new dashboard and guide them towards adoption of the framework
* Begin migration of more "advanced" dashboard views - continue iterating on design system additions and GitLab UI implementation
* Unlock additional data source on dashboard data explorer thus empowering customers to build custom dashboards with multiple data sources, tailored to their use cases.  Likely, the first candidates will included Optimize and Security use cases.
* [Implement GLQL for building visualizations from the Data Explorer for all supported data sources](https://gitlab.com/groups/gitlab-org/-/epics/15815)