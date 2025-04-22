---
layout: markdown_page
title: "Category Direction - Pipeline Composition"
description: "Achieve superior developer efficiency by automating the authoring of CI/CD pipeline configuration."
---

- TOC
{:toc}

## Pipeline Composition 

|                       |                                 |
|-----------------------|---------------------------------|
| Stage                 | [verify](/direction/verify/)    |
| Maturity              | [Minimal](/direction/#maturity) |
| Content Last Updated  | `2025-01-26`                    |

### Introduction and how you can help

Thanks for visiting this category direction page on Pipeline Composition in GitLab. This page belongs to the [Pipeline Authoring](https://handbook.gitlab.com/handbook/product/categories/#pipeline-authoring-group) group of the Verify stage and is maintained by Dov Hershkovitch ([E-Mail](mailto:)).
This direction page is a work in progress, and everyone can contribute:
- Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=updated\_desc&state=opened&label\_name%5B%5D=developer%20automations&first\_page\_size=20) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
- Please share feedback directly via email, Twitter, or on a video call. If you're a GitLab user and want to discuss how GitLab can improve Variables, we'd especially love to hear from you.
### Overview
GitLab CI is the platform that you use to ship your software to your customers as fast as possible. As outlined in our [3 year strategy](direction/ci/#3-year-strategy), we want to enable platform teams to share operational definitions (infrastructure, environments, deployment pipelines, monitoring configuration) with development teams, and for development teams to easily contribute improvements. The Developer Automation category is the backbone to eliminating the user friction for authoring those pipeline configurations throughout the GitLab CI/CD journey.
### Strategy and Themes
Pipeline Composition is born from the need to solve how nearly 80% of a developer's time is spent on non-coding tasks, as shown in GitLab's [2024 Global DevSecOps Report](https://about.gitlab.com/developer-survey/). Eliminating the hurdles to authoring, editing, and updating of pipeline configuration by using "smarter" syntax or autocomplete features empowers our users to leverage GitLab's end-to-end DevSecOps platform more fully. Broadly, this category aims to deliver excellence in the following problem areas over the next three-years:
1. More actionable security worfklows for developers.
2. Eliminate the need to manually author new configuration by connecting CI steps, CI/CD components, the CI/CD catalog, and AI capabilities.
3. Surface cost and time saving opportunities that can be solved by updating pipeline configuration.
### 1 year plan
\*\*September to February 2025\*\*:
- Deliver on CI Steps Minimal Maturity by completing the foundations of the Architecture Blueprint via [CI Steps Minimal Maturity](https://gitlab.com/groups/gitlab-org/-/epics/15084).
- Dogfood CI steps and implement CI steps for technical roadmap items.
\*\*March 2025 to May 2025\*\*:
- Integrate [CI Steps into the CI/CD Catalog](https://gitlab.com/groups/gitlab-org/-/epics/13725).
- Complete the [CI steps Continuous Feedback Program](https://gitlab.com/gitlab-org/ux-research/-/issues/3007)
\*\*June 2025 to August 2025\*\*:
- Complete and grade [CI Steps Viable Maturity](https://gitlab.com/groups/gitlab-org/-/epics/15085).
#### What is next for us
For December to February 2025, we have the following items planned for the CI Automation category:
1. [Users can run steps in their own execution environment](https://gitlab.com/groups/gitlab-org/-/epics/15073)
1. [Steps supports multiple OS](https://gitlab.com/groups/gitlab-org/-/epics/15074)
#### What we are currently working on
In 17.9, the Pipeline Composition Category is continuing the work toward the [CI Steps Minimal Maturity](https://gitlab.com/groups/gitlab-org/-/epics/13725) plan, in addition, will aim to complete:
- [Pipeline creation performance improvements](https://gitlab.com/groups/gitlab-org/-/epics/14102)
#### What we recently completed
- 17.8: [Pre-requisite for CI steps continuous evaluation program](https://gitlab.com/groups/gitlab-org/-/epics/16303)
- 17.7: [CI Steps: Simplify Steps so that users have a more seamless experience](https://gitlab.com/groups/gitlab-org/-/epics/15669)
#### What is Not Planned Right Now
1. Pipeline editor improvements
1. Enhancements to existing keywords or introducing new keywords
1. Migration tooling for other pipeline syntax
### Best in Class Landscape
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities
#### Roadmap
#### Top [1/2/3] Competitive Solutions
##### Github Actions
Our main competitor doing innovative things in terms of pipeline authoring is GitHub, who have evolved Actions into more and more of a standalone CI/CD solution. GitLab remains far ahead in a lot of areas of CI/CD that they are going to have to catch up on, but Microsoft and GitHub have a lot of resources and have a large user base excited to use their product, especially when given away as part of a package. Actions has a more event-driven and community plugin-based approach than GitLab, whereas we take community contributions directly into the product where they can be maintained.
GitHub actions are a seemingly powerful toolkit with a high potential for low maintainability with community contributions as we have seen with Jenkins. We are monitoring to swiftly incorporate the best of their innovation into our product. We've already had some successes [running GitHub Actions directly in GitLab CI](https://gitlab.com/snippets/1988376) and will continue to explore that. We are also working on a [migration guide](https://gitlab.com/gitlab-org/gitlab/-/issues/228937) to help teams we're hearing from who are looking to move over to GitLab have an easier time. Features like [making the script section in containers optional](https://gitlab.com/gitlab-org/gitlab/-/issues/223203) would make it easier to build reusable plugins within GitLab that would behave more like Actions and [Allow `needs:` to refer to a job in the same stage](https://gitlab.com/gitlab-org/gitlab/-/issues/30632) to enable users to run an entire pipline without defining stages.
A limitation of the [GitHub Actions API](https://docs.github.com/en/rest/reference/actions) is the exclusiveness interaction with the service via a workflow YAML checked into a repository. By contrast, GitLab enables users to define units of work to execute as a service, for example, via [mutli-project pipelines](https://docs.gitlab.com/ee/ci/multi\_project\_pipelines.html), [dynamic child pipelines](https://docs.gitlab.com/ee/ci/parent\_child\_pipelines.html#dynamic-child-pipelines) and [parent-child pipelines](https://docs.gitlab.com/ee/ci/parent\_child\_pipelines.html).
Watch this walkthrough video of Github actions
 
##### Circle CI
Circle CI is a Continuous Integration platform that builds a robust process for using and contributing Orbs. Circle CI Orbs are reusable snippets of code packages as YAML configuration condenses repeated pieces of config into a single line of code. Once an orb is created, it could be published to the orb registry, which becomes available to any of the Circle CI user base.
Watch this walkthrough video of the different contribution frameworks available by GitHub Marketplace, Circle CI and CodeFresh.io.
 
</figure>

##### Gitea Actions 

[Gitea Actions](https://blog.gitea.io/2022/12/feature-preview-gitea-actions/) implements a similar event based system like GitHub Actions for CI/CD. The infrastructure features a runner, actions orchestration subsystem, and the action definition. 

### Target Audience

Check out our [CI Section Direction "Who is it for?"](/direction/ci/#who-is-it-for) for an in depth look at the our target personas across Ops. For Pipeline Authoring, our "What's Next & Why" are targeting the following personas, as ranked by priority for support: 

1. [Priyanka - Platform engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
1. [Devon - DevOps Engineer](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
1. [Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)

### Pricing and Packaging

Pipeline Composition features and CI Steps are a building blocks within the GitLab CI syntax model. This feature set will be offered in GitLab Free, and will work with other complimentary capabilities such as CI/CD components, compute minutes, AI experiences, and Analytics to offer feature discovery moments for Premium, Ultimate, and Duo licensed users. 

### Analyst Landscape

The Gartner Magic Quadrant evaluates leadership of Continuous Integration offerings within the [DevOps Platforms](https://about.gitlab.com/gartner-magic-quadrant/) landscape. GitLab is a leader in this space and this category aims to sustain our position in this by defending our strong hold in the following spaces: 

- Parallel builds 
- Multistage pipelines 
- Container Native CI 
- Build Caching 

CI Steps affords us a new technology to begin approaching and solving user needs with different use cases and problems than our install base. We can continue to support our current capabilities while also future-proofing and looking forward with more sustainable, smart solutions. 

CI Steps are reusable and composable pieces of a job. These are used within the GitLab project and will be used within the Component catalog for sharing. There are a few other benefits to CI Steps: 

1. CI Steps offer a wider array of composability, reusability, and definition that other syntax cannot support due to the step-runner and other already defined pieces within the Step
1. The way the step is authored follows the same patterns and workflows one would use for gitlab-ci.yml authoring
1. CI steps lean more toward the Platform Engineering practice because you can define steps and they can be reused and shared more broadly via inputs and outputs (https://docs.gitlab.com/ee/ci/steps/)