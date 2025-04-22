---
layout: markdown_page
title: "Category Direction - Continuous Integration"
description: "Continuous Integration is an important part of any software development pipeline. It must be easy to use, reliable, and accurate. Learn more here!"
canonical_path: "/direction/verify/continuous_integration/"
---

- TOC
{:toc}

## Continuous Integration

| | |
| --- | --- |
| Stage | [Verify](/direction/verify/) |
| Maturity | Competitive|
| Content Last Reviewed | `2024-10-22` |


### Introduction and how you can help

Thanks for visiting this category direction page on Continuous Integration (CI) in GitLab. This page belongs to the [Verify Stage](https://handbook.gitlab.com/handbook/product/categories/#verify-stage) and is maintained by Rutvik Shah ([E-Mail](mailto:<rutshah@gitlab.com>)).

This direction page is a work in progress, and everyone can contribute:

- Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues/?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=Category%3AContinuous%20Integration) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=Category:Continuous+Integration) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
- Please share feedback directly via email or on a video call. If you're a GitLab user and want to discuss how GitLab can improve Continuous Integration, we'd especially love to hear from you.

### Overview

Continuous Integration is an important part of any software development cycle. We recognize a key advantage of GitLab CI is that we can define pipelines as code, while making CI easy to use, reliable, and accurate in terms of its results. We are very proud that we are recognized as [a leader in DevOps Platforms](https://about.gitlab.com/gartner-magic-quadrant) in the Gartner Magic Quadrant, as well as a leader in Forrester's most recent and final 2019 Q3 [Cloud Native CI Wave](https://about.gitlab.com/press/releases/2019-09-20-gitlab-named-cloud-native-continuous-integration-tools-leader/), and it's important for us that we continue to innovate in this area and provide not just a "good enough" solution, but a speedy and reliable one.

Making it easy to run a pipeline is our first focus and this applies to both running a pipeline manually as well as triggering one automatically when submitting a code commit or a merge request. In addition, we want to provide data for examining your pipeline's performance, so that you can optimize CI configurations to make your pipelines run more efficiently.

For specific information and features related to authoring and pipelines, check out [Pipeline Authoring](/direction/verify/pipeline_composition/). For work related to Pipeline Abuse Prevention, see the [Category page](https://about.gitlab.com/direction/software_supply_chain_security/anti-abuse/instance_resiliency/).

You may also be looking for one of the following related product direction pages: [Overall Vision of the Verify stage](/direction/ops/#verify) and [GitLab Runner](/direction/verify/runner_core/).


### Strategy and Themes

Our strategy to regain a category maturity of "Complete" is by delivering features that help our customers realize the orchestration power of GitLab CI by integrating other systems and continue to work on features that power the core CI experience.

### 1 year plan
In FY25-26, our plan is to help users to deliver software faster and efficiently. This includes:

1. Abilty to identify and fix pipeline failures quickly with our AI powered [Root Cause Analysis feature](https://gitlab.com/groups/gitlab-org/-/epics/14457)
2. Integrate seamlessly with other systems and unblocking access to security and compliance features offered by GitLab Platform

     a. [Ability to call and asynchronously wait for an external system](https://gitlab.com/groups/gitlab-org/-/epics/10866) from the pipelines with the focus on FluxCD and Jenkins as primary use cases.
     
     b. Ability to [integrate seamlessly with GitHub SCM](https://gitlab.com/groups/gitlab-org/-/epics/13806)
3. Provide a great user experience to locate pipelines and jobs.

     a. [Additional ways to filter a job](https://gitlab.com/groups/gitlab-org/-/epics/6690)

     b. [Optimize the pipeline details page](https://gitlab.com/groups/gitlab-org/-/epics/14919)
     

#### What is next for us

<!-- This is a 3 month look ahead for the next iteration that you have planned for the category. This section must provide links to issues or
or to [epics](https://handbook.gitlab.com/handbook/product/product-processes/#epics-for-a-single-iteration) that are scoped to a single iteration. Please do not link to epics encompass a vision that is a longer horizon and don't lay out an iteration plan. -->
We are excited to continue improving the core capabilities of GitLab CI/CD to make it the best-in-class solution for our users. Some key areas we are focusing on in the near-term include:

1. [First party integration with GitHub SCM](https://gitlab.com/groups/gitlab-org/-/epics/13806)
2. [Improve usability and response quality for Root Cause Analysis](https://gitlab.com/groups/gitlab-org/-/epics/14815)

#### What we are currently working on
<!-- Scoped to the current month. This section can contain the items that you choose to highlight on the kickoff call. Only link to issues, not Epics.  -->

We are currently focusing on 
1. Determine the technical approach that we want to choose for [integrating with GitHub](https://gitlab.com/gitlab-org/gitlab/-/issues/460503)

#### What we recently completed
<!-- Lookback limited to 3 months. Link to the relevant issues or release post items. -->

The top deliverables from the Pipeline Execution group over the last quarter are:
1. [User can debug pipeline failures with our AI powered Troubleshoot feature](https://docs.gitlab.com/ee/user/gitlab_duo_chat/examples.md#troubleshoot-failed-cicd-jobs-with-root-cause-analysis)
2. [Added a filter for job name on job list view](https://gitlab.com/gitlab-org/gitlab/-/issues/387547)
3. [Improved readability of RCA response](https://gitlab.com/gitlab-org/gitlab/-/issues/473333)

#### What is Not Planned Right Now

- CI related [notifications](https://gitlab.com/groups/gitlab-org/-/issues?label_name%5B%5D=notifications&label_name[]=group%3A%3Apipeline%20execution) (by email or via integration with other tools)
- CI related [API endpoints](https://gitlab.com/gitlab-org/gitlab/-/issues?label_name%5B%5D=api&label_name%5B%5D=group%3A%3Apipeline+execution&state=opened) (unless related to features on the roadmap)
- CI related [permissions](https://gitlab.com/gitlab-org/gitlab/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=CI%20permissions&label_name[]=group%3A%3Apipeline%20execution&not[label_name][]=bug) (non-bug issues)
- [Configure CI/CD Quotas by project](https://gitlab.com/gitlab-org/gitlab/-/issues/357760) going forward we will work with the community to review and merge contributions but are not planning active development on new features.


### Best in Class Landscape

BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

#### Key Capabilities

* [Pipelines as code](https://about.gitlab.com/solutions/continuous-integration/)
* [Scheduled triggering of pipelines](https://docs.gitlab.com/ee/ci/pipelines/schedules.html)
* [Trigger pipeline on any event in code repository](https://docs.gitlab.com/ee/ci/triggers/)
* [CI/CD Horizontal Autoscaling](https://docs.gitlab.com/runner/configuration/autoscale.html#overview)
* [Live streaming of logs from running pipeline](https://docs.gitlab.com/ee/ci/jobs/#expand-and-collapse-job-log-sections)
* [CI/CD for external repo](https://docs.gitlab.com/ee/ci/ci_cd_for_external_repos/)

#### Roadmap
<!-- Key deliverables we're focusing on to build a BIC solution. List the epics by title and link to the epic in GitLab. Minimize additional description here so that the epics can remain the SSOT. This may be duplicative to the 1 year section however for some categories the key deliverables required to become the BIC solution will extend beyond one year and we want to capture all of the gaps. Moreover, the 1 year section may contain work that is not directly related to closing gaps if we are already the BIC or if we are differentiating ourselves.-->


#### Top Competitive Solutions

The majority of CI market conversation is between us, Jenkins, and GitHub Actions at this point. An example of this placement is from [Jet Brain's 5th annual Developer Ecosystem Survey](https://www.jetbrains.com/lp/devecosystem-2021/) which has placed GitLab as #2 CI solution for enterprises. Atlassian has built BitBucket Pipelines, a more modernized version of Bamboo, which is still in the early stages. Microsoft is maintaining (at least for now) Azure DevOps at the same time as GitHub Actions but for personal usage GitHub Actions is gaining traction among developers. CodeFresh and CircleCI have both released [container-based plugin model](https://steps.codefresh.io/), similar to GitHub Actions. CircleCI in particular is known for very fast startup times and we're looking to ensure we [keep up or get even faster](https://gitlab.com/groups/gitlab-org/-/epics/7290). Jenkins is largely seen as a legacy tool, and most people we speak with are interested in moving off to something more modern. We are addressing this with our [External CI jobs](https://gitlab.com/groups/gitlab-org/-/epics/10866) vision to support a broader CI ecosystem beyond GitLab CI workloads. 

From [GitHub's 2023 Roadmap](https://github.com/orgs/github/projects/4247), we are seeing GitLab-reminiscent features which include [Pull Request Merge Queue](https://github.com/github/roadmap/issues/370), akin to [Merge Trains](https://docs.gitlab.com/ee/ci/pipelines/merge_trains.html) with a fit-finish that we aim to make easier in [gitlab#294169](https://gitlab.com/gitlab-org/gitlab/-/issues/294169). Also to note is an emphasis on governance and controls with [Audit Log streaming](https://github.com/github/roadmap/issues/344), bringing parity to the capabilities GitLab has created with the [Compliance group's Audit Event streaming](https://docs.gitlab.com/ee/administration/audit_event_streaming.html).


### Target Audience

For Continuous Integration, our "What's Next & Why" are targeting the following personas, as ranked by priority for support:

1. [Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
1. [Priyanka - Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
1. [Delaney - Development Team Lead](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)

### Maturity Plan

Our current maturity is at "Competitive" and the next maturity target is "Complete". We will continue to focus on quality and stability as we move forward while providing a way for our users to adopt GitLab CI within their existing ecosystem and differentiate ourselves with a solution that helps debugging pipelines efficient. 

### Pricing and Packaging
<!--
-->

### Analyst Landscape

There are a few key findings from the Forrester Research analysts on our CI solution. GitLab is seen as capable as the solutions provided by the hyperclouds themselves, and well ahead of other neutral solutions. This can give our users flexibility when it comes to which cloud provider(s) they want to use. We are also seen as the best end to end leader, with other products  not keeping up and not providing as comprehensive solutions. What this tells us is that it is important for us to continue to innovate and make it hard or even impossible for competitors to maintain pace. As such, our path to improving our analyst performance matches our solutions above in terms of staying ahead of our competitors.
