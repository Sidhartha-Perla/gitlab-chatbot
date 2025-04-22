---
layout: handbook-page-toc
title: "Verify Stage Direction"
description: "Check out GitLab's Direction for automatically building, testing, and optimizing code."
canonical_path: "/direction/verify/"
---

- TOC
{:toc}

## Overview

Everyone can contribute! Feel free to comment on our [async AMA issue](https://gitlab.com/gitlab-com/Product/-/issues/3278), [email Jackie Porter](mailto:jporter@gitlab.com),
and [propose an MR](https://gitlab.com/gitlab-com/www-gitlab-com/-/edit/master/source/direction/verify/index.html.md.erb) to this page!



- Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=devops%3A%3Averify&first_page_size=20) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
- Please share feedback directly via email, Twitter, or on a video call. If you're a GitLab user and want to discuss how GitLab can improve Variables, we'd especially love to hear from you.

### What is Verify?

The Verify Stage is responsible for executing on the market needs for continuous integration.

From our Continuous Integration [use case](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/usecase-gtm/ci/#continuous-integration):

_When practicing Continuous Integration, teams collaborate on projects using a shared repository to store, modify, and track frequent changes to their codebase. Developers check in or integrate their code into the repository multiple times daily and rely on automated tests to run in the background. These automated tests verify the changes by checking for potential bugs and security vulnerabilities, as well as performance and code quality degradations. Running tests as early in the software development lifecycle as possible is advantageous to detect problems before they intensify._

### Verify Vision

### Continuous Integration Vision

From this [mission](/direction/verify/#continuous-integration-mission), our vision is that by 2028, GitLab CI will be seen as the market leader for programmable AI-powered CI/CD, proven to run at scale for all software development use cases.

We will execute this vision by:
1. Introducing AI-powered pipeline authoring workflows to enable development teams to focus on delivering business value instead of pipeline configurations.
1. Allowing a seamless migration from other CI tools to GitLab CI as organizations consolidate their toolchains onto the GitLab DevSecOps platform.
1. Delivering the best experience for pipelines as code, improving how Software Developers alongside DevOps Engineers author pipelines and configure their `.gitlab-ci.yml` files.
1. Empowering visibility to changes made to code before production, compute minutes consumption, as well as natively compliant, secure supply chain workflows to support the building, testing, and optimizing of code from a single CI tool.
1. Leverage the data in the end-to-end GitLab DevOps platform to inform optimizations that result in fast, reliable pipelines and eliminate developer pain points that impact productivity.
1. Growing GitLab.com users by investing in [GitLab-hosted first](/direction/#product-strategy) and scaling our capabilities to meet Enterprise-level needs.

In addition to the vision outlined above, another goal is for CI/CD to be a critical enabler of the GitLab three-year strategy. Now, a CI/CD pipeline on its own, while critically valuable to the modern DevSecOps lifecycle, only tells part of the story of whether a software development team is delivering value as efficiently as possible. Therefore, our strategy over the next three years is to help businesses realize value faster by integrating the GitLab pipeline experience into areas of the platform focused on software delivery practice. 

For example, a developer can view DevOps Research and Assessment (DORA) metrics at the aggregate level in the [Value Streams Dashboard](https://docs.gitlab.com/ee/user/analytics/value_streams_dashboard.html). However, providing the developer with the DORA metric for a specific commit within the CI/CD pipeline experience offers real-time visibility and empowers the developer to make immediate changes to improve business results.

The rationale for this strategy is as follows. There are various approaches in the industry today for authoring CI/CD workflows. Those options range from a declarative language such as YAML, an actions-style DSL, to procedural programming languages like Starlark. At the core of these various approaches is one constant - developers want simple-to-learn and use automation solutions regardless of the type of application they are developing. In the future, there will undoubtedly be new approaches for CI/CD pipelines entering the market. So, while the underlying automation authoring engine may change, the end goal of what we must achieve as software developers will remain the same.

Thus, the fundamental pillar of the GitLab Verify stage differentiation and platform support strategy is integrating the CI/CD experience at the developer persona level with other areas of the GitLab platform to enable the efficient delivery of secure software at scale.

### Stage Strategy

### Verify

To define our top focuses and initiatives, the Verify Stage needs to have a concerted perspective on what GitLab will offer for the
Continuous Integration [use case](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/usecase-gtm/ci/).
We are targeting the [Ops Section Direction personas](/direction/ops/#medium-term-1-2-years) and will support these users with our
Continuous Integration [mission](/direction/verify/#continuous-integration-mission), [vision](/direction/verify/#continuous-integration-vision), and one-year direction.

#### One-year direction

GitLab CI/CD unlocks the DevSecOps workflow. A key focus for the Verify Stage is supporting the automation of secure workflows in GitLab while delivering ease of use across GitLab CI/CD.
Our goal is to be the best-in-class CI/CD platform of choice. To support this goal, we are investing in the following areas next year:

**[World-class DevSecOps experience](/direction/#world-class-devsecops-experience)**
1. Evolve the discoverability and reusability of syntax with the [CI/CD Catalog](https://about.gitlab.com/blog/2024/05/08/ci-cd-catalog-goes-ga-no-more-building-pipelines-from-scratch/)
1. Improve job composability and extensibilty of GitLab CI/CD with [GitLab Steps](https://gitlab.com/groups/gitlab-org/-/epics/115359) and [GitLab Events](https://gitlab.com/groups/gitlab-org/-/epics/8349)
1. Deliver superior build speed by offering expanded machine types and sizes for [GitLab-hosted runners](/direction/verify/hosted_runners/) and improving [pipeline execution speeds](https://gitlab.com/groups/gitlab-org/-/epics/7290)
1. Release a next-generation container registry with [garbage collection, improved performance](https://gitlab.com/groups/gitlab-org/-/epics/5521) and a [new UX](https://gitlab.com/groups/gitlab-org/-/epics/3211)

**[Advanced Security & Compliance](/direction/#advanced-security-and-compliance)**
1. [Full integration with Google Cloud](https://about.gitlab.com/blog/2024/04/09/gitlab-google-cloud-integrations-now-in-public-beta/) with access control using Google Cloud Console for enhanced security

**[Observability & Analytics](/direction/#observability-analytics--feedback)**
1. Better visibility into [runner health](https://gitlab.com/gitlab-org/gitlab/-/issues/421372) with the runner fleet dashboards for [instance administrators](https://docs.gitlab.com/ee/ci/runners/runner_fleet_dashboard.html) and [groups](https://docs.gitlab.com/ee/ci/runners/runner_fleet_dashboard_groups.html).

For a view of all the issues we have planned by quarter in FY25, check out our [Verify Roadmap Issue Board](https://gitlab.com/groups/gitlab-org/-/boards/7642988?label_name[]=devops%3A%3Averify&label_name[]=direction).

#### What we aren't focused on now

There are important things we won't work on to focus on our one year plan.

1. **[Code Testing and Coverage](https://about.gitlab.com/direction/verify/code_testing/)** - Our users are looking for improved experiences in Review Apps and Build Artifacts. We are trading off investing in other visualizations and testing capabilities to unlock those features.
1. **[Review Apps](https://about.gitlab.com/direction/verify/review_apps/)** - We are shifting focus on differentiators for GitLab CI/CD related to reusability, security, and speed.
1. **[Build Artifacts](https://about.gitlab.com/direction/verify/build_artifacts/)** - while a critical experience, we will not be investing in any new experiences for Build Artifacts.


#### Verify Stage Categories



#### Pricing

The Verify group is at the entrypoint to the funnel in our [user adoption journey](/direction/ops/#user-adoption-journey), so our features are an critical enabler for users seeking a [complete DevOps platform](/solutions/devops-platform/). While we do try to drive adoption in order to support multi-stage growth at least partially through features at the free tier, it's also important for us that we have features at the paid tiers. For our group, these will typically be cross-department and cross-company views related to CI templates, quality and pipelines. See below for the how we are thinking about each of the tiers, and the kinds of features that will be included.

##### Free

The foundation of the Free strategy for Verify is that enhancements to baseline CI YAML features will be available in this tier by default. The rationale for this approach is that we want to preserve a consistent experience. Users must always be able to use the same `.gitlab-ci.yml` in all tiers.

Beyond this, features that drive broad adoption and help with onboarding (including generally making it easier to get started with GitLab CI) are also good candidates for inclusion in this tier. Providing solutions to simplify the deployment and management of Runners at scale for self-managed is also critical for all tiers of users.

##### Premium

The default paid tier for enterprises, Premium will cater to directors operating a medium to large instance. We will focus on features that solve for typical entry-level enterprise needs: reporting and analytics supporting [Ops Insights](https://handbook.gitlab.com/handbook/company/pricing/#premium), operational efficiency driving effective project management, and supporting visibility in consumption related to 10,000 compute minutes per month medium to large organizations.

You can see features that we are considering including in this tier in this [issue search](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=devops%3A%3Averify&label_name%5B%5D=GitLab%20Premium).

##### Ultimate

Using GitLab CI across hundreds or thousands of projects in large enterprises means a greater need for portfolio management and consistency of experience in development practices. This is accomplished by making templates discoverable via [gitlab#320698](https://gitlab.com/gitlab-org/gitlab/-/issues/320698) and a consistent authoring experience such as in [these issues](https://gitlab.com/gitlab-org/gitlab/-/issues?scope=all&state=opened&label_name[]=GitLab%20Ultimate&label_name[]=Category%3APipeline%20Authoring). Additionally, the larger the organization the greater the need for regulation and compliance which is where features like Protected Runners captured in [gitlab&6058](https://gitlab.com/groups/gitlab-org/-/epics/6058) or better integrations with Compliance Pipelines become especially attractive. For customers who self-manage a Runner Fleet, ensuring the security and compliance of the Runner execution environment is critical. Features such as the [auto-removal of inactive runners](https://gitlab.com/groups/gitlab-org/-/epics/8055) and providing [reporting](https://gitlab.com/gitlab-org/gitlab/-/issues/339523) and automation to manage outdated runner versions are just a few examples of features coming in Ultimate aimed at simplifying Runner operations and maintenance. To secure the flows for HashiCorp Vault users, we would like to [automatically mask](https://gitlab.com/gitlab-org/gitlab/-/issues/255186) any Vault secrets that are fetched by GitLab CI. To ensure better pipeline compliance we plan to provide you with the ability to enforce the [presence of specific variables when validating pipeline configuration](https://gitlab.com/gitlab-org/gitlab/-/issues/21299). Lastly, our core promise for the Ultimate tier is enabling users to effectively monitor and best use their 50,000 compute minutes by setting [compute minutes limits](https://gitlab.com/gitlab-org/gitlab/-/issues/357760) on their projects.

You can see features that we are considering including in this tier in this [issue search](https://gitlab.com/groups/gitlab-org/-/issues?sort=milestone&state=opened&label_name[]=devops::verify&label_name[]=GitLab+Ultimate&not[label_name][]=GitLab+Free&not[label_name][]=GitLab+Premium). 


