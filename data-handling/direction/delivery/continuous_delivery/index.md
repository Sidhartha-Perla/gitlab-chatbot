---
layout: markdown_page
title: "Category Direction - Continuous Delivery"
description: We follow the well-known definitions from Martin Fowler on the difference between continuous delivery and continuous deployment. Learn more here!
---

- TOC
{:toc}

## Continuous Delivery

Many teams are reporting that development velocity is stuck; they've
reached a plateau in moving to more and more releases per month, and now need help on how to improve. According to analyst research, 40% of software development
team's top priorities relate to speed/automation, so our overriding vision
for Continuous Delivery is to help these teams renew their ability to
accelerate delivery.

Additionally, Continuous Delivery serves as the "Gateway to Operations"
for GitLab, unlocking the downstream features such as the [Configure](/direction/ops/#configure)
and [Monitor](/direction/ops/#configure) stages.

- [Maturity Plan](#maturity-plan)
- [Issue List](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=Category%3AContinuous%20Delivery)
- [Overall Vision](/direction/ops/#release)
- [UX Research](https://gitlab.com/gitlab-org/ux-research/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=group%3A%3Aprogressive%20delivery&label_name[]=Category%3AContinuous%20Delivery)
- [Research insights](https://gitlab.com/gitlab-org/uxr_insights/-/issues?scope=all&utf8=%E2%9C%93&state=all&label_name[]=Category%3AContinuous%20Delivery)
- [Documentation](https://docs.gitlab.com/ee/ci/)

### Vision

GitLab Continuous Delivery enables organizations to have the latest changes to their software ready for production at any time. Even beyond that, organizations are also able to deploy to production automatically using the Continuous Deployment model.

GitLab provides a complete toolset for organizations to use to improve their deployment frequency and evolve their DevOps capabilities. Teams are able to use org-level standards for delivery and deployment while also ensuring teams are able to move quickly and make updates to their software continuously as desired.

GitLab Continuous Delivery also leverages other GitLab platform capabilities to streamline setup, deploy to different environments, monitor or even simulate the impact of changes to production, and help improve organization performance.

### Continuous Delivery vs. Deployment

We follow the well-known definitions from Martin Fowler on the
difference between continuous delivery and continuous deployment:

- **Continuous Delivery** is a software development discipline
 where you build software in such a way that the software can
 be released to production at any time.
- **Continuous Deployment** means that every change goes through the
 pipeline and automatically gets put into production, resulting in many
 production deployments every day.
In order to do Continuous Deployment, you must be doing Continuous Delivery.

_Source: [https://martinfowler.com/bliki/ContinuousDelivery.html](https://martinfowler.com/bliki/ContinuousDelivery.html)_

### Infrastructure Provisioning

Infrastructure Provisioning and Infrastructure as Code, using solutions like Terraform or other provider-specific methods, is an interesting topic that relates to deployments but is not part of the Continuous Delivery category here at GitLab. For details on solutions GitLab provides in this space, take a look at the [category page](/direction/delivery/infrastructure_as_code/) for our Infrastructure as Code team.

### Deployment with Auto DevOps

For deployment to Kubernetes clusters, GitLab has a focused category called Auto DevOps which is oriented around providing solutions for deploying to Kubernetes. Check out their [category page](/direction/delivery/auto_devops/) for details on what they have planned.

We are working on a similar experience for non Kubernetes users, starting with [Streamline AWS Deployments](https://gitlab.com/groups/gitlab-org/-/epics/2351) that will automatically detect when users are deploying to AWS and will connect the dots for them.

The [Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/#auto-deploy) [jobs](https://gitlab.com/gitlab-org/gitlab/-/tree/master/lib%2Fgitlab%2Fci%2Ftemplates%2FJobs) within [Auto DevOps](https://docs.gitlab.com/ee/topics/autodevops/) are maintained by the Continuous Delivery category.

## What's Next & Why

The continuous delivery product category is currently in maintenance mode. We do not have any new features on our roadmap.
We are still encouraging community contributions, especially around [connecting releases and environments](https://gitlab.com/groups/gitlab-org/-/epics/15715), [improving resource group management](https://gitlab.com/groups/gitlab-org/-/epics/13766) or improving environment access controls [here](https://gitlab.com/gitlab-org/gitlab/-/issues/437133) and [here](https://gitlab.com/gitlab-org/gitlab/-/issues/437132).

## Maturity Plan.

This category is currently at the "Complete" maturity level, and our next maturity target is Lovable (see our [definitions of maturity levels](/direction/#maturity)).
Key deliverables to achieve this are:

 **CI.yaml features**
- [Group deploy tokens](https://gitlab.com/gitlab-org/gitlab/issues/21765) (Complete)
- [Allow only forward deployments](https://gitlab.com/gitlab-org/gitlab/issues/25276)  (Complete)
- [Allow Deploy keys to push to protected branches](https://gitlab.com/gitlab-org/gitlab/-/issues/30769) (Complete)
- [Group Deploy Keys](https://gitlab.com/gitlab-org/gitlab/issues/14729) (Complete)
- [Support Resource Group for cross-project (parent/child) pipelines](https://gitlab.com/gitlab-org/gitlab/-/issues/39057) (Complete)
- [Allow fork pipelines to run in parent project](https://gitlab.com/groups/gitlab-org/-/epics/3278) (Partial)
- [Possibility to enforce the execution order of jobs using resource_group](https://gitlab.com/gitlab-org/gitlab/-/issues/202186)
- [Group-level resource group](https://gitlab.com/gitlab-org/gitlab/-/issues/122010)

**Cloud Deployments**
- [Streamline AWS Deployments](https://gitlab.com/groups/gitlab-org/-/epics/2351)

**Observability**
- [Post-deployment monitoring MVC](https://gitlab.com/groups/gitlab-org/-/epics/3088)
  * We recently recorded a [Think Big](https://youtu.be/zMmmAhrOIDs) session describing the vision for this.
  * [Automatic rollback in case of failure](https://gitlab.com/gitlab-org/gitlab/-/issues/35404) (Complete)
- [Measure DORA 4 Metrics in GitLab](https://gitlab.com/groups/gitlab-org/-/epics/4358)
  * [API support for Deployment Frequency](https://gitlab.com/gitlab-org/gitlab/-/issues/279039) (Complete)
  * [Add charts Deployment Frequency in CI/CD dashboard](https://gitlab.com/gitlab-org/gitlab/-/issues/275991) (Complete)
  * [Group Level API support for Deployment Frequency](https://gitlab.com/gitlab-org/gitlab/-/issues/291747) (Complete)
  * [API support for Lead time for MRs to be merged](https://gitlab.com/gitlab-org/gitlab/-/issues/291746) (Complete)
  * [Present Lead time for MRs in CI/CD dashboard](https://gitlab.com/gitlab-org/gitlab/-/issues/250329) (Complete)
  * [Group Level charts for Deployment Frequency]- Group Level Deployment Frequency CI/CD chart
  * [API support for Time to restore service](https://gitlab.com/gitlab-org/gitlab/-/issues/299096)
  * [API support for Change Failure Rate](https://gitlab.com/gitlab-org/gitlab/-/issues/299407)

**Auto Deploy (AutoDevOps Flow)**
- [Customize readinessProbe and livenessProbe for Auto DevOps](https://gitlab.com/gitlab-org/gitlab/-/issues/22327)
- [Expand AutoDevops for AWS targets](https://gitlab.com/groups/gitlab-org/-/epics/3897)

## Competitive Landscape

Because CI and CD are closely related, the [competitive analysis for Continuous Integration](/direction/verify/continuous_integration/#competitive-landscape)
is also relevant here. For how CD compares to other products in the market,
especially as it relates to pipelines themselves, also take a look there.

## Analyst Landscape

In our conversations with industry analysts, there are a number of key trends
we're seeing happening in the CD space:

### Support a breadth of platforms, both legacy and cloud-native.

Cloud adoption of CI/CD is growing, extending capabilities for deploying to cloud environments, including Kubernetes and other modern container
architectures are a key metric. While cloud migration is accelerating and more teams are adopting it, on-premises and
legacy hardware environments remain.

We invite you to follow our plans to [natively support hypercloud deployments](https://gitlab.com/groups/gitlab-org/-/epics/1804) and  Serverless to offer feedback or ask questions.

### Inject insight and analytics into pipelines.

Users are looking for the ability to not just measure platform stability and other
performance KPIs post-deployment, but also provide functionality such as automated release-readiness scoring
based on analysis of data from across the digital pipelines.
Tracking and measuring customer behavior, experience, and financial impact, after deployment via [gitlab#37139](https://gitlab.com/gitlab-org/gitlab/issues/37139) solves an important
pain point.

### Metrics to Drive Agile, DevOps and Continuous Delivery

Metrics are a primary source of quantifiable feedback, which is a key objective of agile and DevOps methodologies. Development teams that collect and analyze metrics understand successes, failures and opportunities for improvement better than their peers. Mature development teams actively monitor metrics data and compare results against baselines, which can be industry benchmarks or constant improvements against past results of the individual team. We are actively working on supporting [DORA4](https://gitlab.com/groups/gitlab-org/-/epics/4358) metrics as an integral part of GitLab which will allow you to gain efficincy and stability insights into you softwarre development lifecycle. 

### Progressive Delivery

Progressive Delivery allows you to deploy code incrementally and target the audience that will receive the new code based on user segments and environments. By doing so, it enables experimentation with reduced risk. Progressive Delivery builds on the foundations laid by Continuous Integration and Continuous Delivery. Related categories to this theme are [Feature Flags](https://about.gitlab.com/direction/delivery/) and [Advanced Deployments](https://about.gitlab.com/direction/delivery/).
To read more about this see [RedMonk's post](https://redmonk.com/jgovernor/2019/07/10/progressive-delivery-at-gitlab/).

## Top Customer Success/Sales Issue(s)

The ability to monitor deployments and automatically halt/rollback deployment in case of exceeding a specific error rate is frequently mentioned by CS and in the sales cycle as a feature teams are looking for. This will be
implemented via [gitlab&3088](https://gitlab.com/groups/gitlab-org/-/epics/3088). We have recently added the ability to rollback automatically in case a critical alert is raised via [gitlab#35404](https://gitlab.com/gitlab-org/gitlab/-/issues/35404) (Complete) and will follow up with adding a notification when an auto-rollback accord via [gitlab#292019](https://gitlab.com/gitlab-org/gitlab/-/issues/292019).

## Top Customer Issue(s)

The most requested customer issue is [gitlab#5902](https://gitlab.com/gitlab-org/gitlab/-/issues/5902) which adds the ability to create [Deploy Tokens](https://docs.gitlab.com/ee/user/project/deploy_tokens/) with functionality similar to the Deploy Keys, where the admin can create and assign Deploy Tokens per project which will grant non-personal registry-only access to the images without needing an extra seat.

## Top Internal Customer Issue(s)

Adding a check for maximum commits before merge via [gitlab#26691](https://gitlab.com/gitlab-org/gitlab/-/issues/26691) is our most popular internal issue. This adds a validation check, to make sure that your merge request is not too far behind master before merging in order to avoid breaking master

## Top Vision Item(s)

Our top vision item is to [Natively support hypercloud deployments](https://gitlab.com/groups/gitlab-org/-/epics/1804), and specifically deploying to [AWS](https://gitlab.com/groups/gitlab-org/-/epics/2351) we want to help make it easier and quicker to get started and deploy to any one of the big cloud providers using GitLab's CI/CD.

We are planning to research user needs for multi-cloud deployments. If you are interested in participating in this user research, please leave a comment in [ux-research#1249](https://gitlab.com/gitlab-org/ux-research/-/issues/1249). 
