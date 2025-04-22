---
layout: markdown_page
title: "CI Section Direction"
description: "This page highlights GitLab's continuous integration direction."
canonical_path: "/direction/ci/"
---

- TOC
{:toc}

# What we do 

The CI section is responsible for many of the experiences in GitLab after a developer commits changes to a project (source code repository). The DRI for this page is [Jackie Porter](mailto:jporter@gitlab.com), Director of Product and I welcome contributions - please open a merge request or send me an [email](mailto:<jporter@gitlab.com>). 

## CI Section Mission

Our mission for the CI Section is to empower all users to easily contribute to the automated building, testing, and optimization of code for GitLab customers and the Open Source Community.

## CI Section Vision

Our **vision** is that in the next five years, GitLab CI/CD is the brand synonymous with CI/CD and recognized as the industry standard. 
    
We are going to accomplish this by making the process of configuring, managing, and tuning CI/CD pipelines as frictionless as possible. 

The CI Section is comprised of two stages: Verify and Package. For a deeper view of the direction of each specific stage please visit the respective Direction Pages linked below:
- [Verify](/direction/verify/)
- [Package](/direction/package/)

### 3-year strategy 

Inherited from GitLab's company [mission](https://handbook.gitlab.com/handbook/company/mission/), the CI section aims to support universal contribution from everyone in the software build and packaging processes.
To accomplish this target, focusing on reducing complexity in the developer and platform operator workflow by prioritizing [simplicity](https://handbook.gitlab.com/handbook/handbook/product/product-principles/#simplicity) in our design,
building with flexibility in mind for the [enterprise workflow](https://handbook.gitlab.com/handbook/handbook/product/product-principles/#avoid-enforced-workflows-but-allow-enterprise-flexibility),
and becoming an ecosystem for CI tools by [thoughtfully integrating with other applications](https://handbook.gitlab.com/handbook/handbook/product/product-principles/#integrate-other-applications-thoughtfully) are the foundation for the strategy. 

In addition to enabling developers with CI capabilities, we will also focus on supporting platform engineers with best-in-class tools for managing code, artifacts, and costs.

Organizations need a solution to effectively manage two sides of the software cost picture: developer cost and compute cost. There is a high demand for a single source to view and optimize builds and infrastructure [internal research](https://docs.google.com/presentation/d/1QAO0m08Om15AC2W0pZp0cfxCImgmww-qvwyKtlMQIBk/edit#slide=id.g13a5341bed7_0_2). 

As we look into the future of build and package, migration and use case support will be a core focus. Journeys away from current tools are challenging. Our goal is to give you tools that can help make it easy to consolidate on GitLab so that you can save money on licensing costs and improve user experience.

With a win/win scenario in mind, the three year outcomes we would want to support as a section are as follows: 

- Manage code, binaries and packages at scale with actionable analytics and dashboards to support platform team decision making
- Enable platform teams to share operational definitions (infrastructure, environments, deployment pipelines, monitoring configuration) with development teams, and for development teams to easily contribute improvements to their definition
- Efficiency and cost optimizations are surfaced for action by operators
- Meet compliance and supply chain security requirements by improving the traceability of artifacts throughout the build, test, deploy process
- Build a system that supports the vendor ecosystem to meet enterprises where they are in their CI journey, helping teams onboard faster and more easily transition into GitLab's next-generation CI tools

### Market predictions 

In three years the CI market will:

- View CI a critical capability for bridging between Dev, Sec & Ops to create truly high-performing DevSecOps organizations
- View package management an integrated requirement for any CI/CD platform
- Have CI emerge as a critical lever for operational excellence in businesses 
- Demand a higher standard of security for the software build process
- Use AI in development best-practices and infrastructure automation - a new domain we intend to lead

### Themes

The CI Section is contributing actively to our [Yearly Themes](/direction/#fy24-product-investment-themes). In FY25, we plan to execute on:

1. Drive Use Case Adoption by delivering features that will amplify our paid usage as well as security and governance feature sets. The capabilities we expect to deliver in FY25 fall into two areas: 
    * Continuous Integration: [Merge Trains to Complete](https://gitlab.com/groups/gitlab-org/-/epics/11650), [External CI Jobs](https://gitlab.com/groups/gitlab-org/-/epics/10866), [Cache Service](https://gitlab.com/groups/gitlab-org/-/epics/11024), [GitLab Events](https://gitlab.com/groups/gitlab-org/-/epics/8349), [GitHub Actions compatibility](https://gitlab.com/groups/gitlab-org/-/epics/11535), [GitLab Secrets Manager](https://gitlab.com/groups/gitlab-org/-/epics/10723), [CI/CD Catalog to GA](https://gitlab.com/groups/gitlab-org/-/epics/11564), [CI/CD Insights](https://gitlab.com/groups/gitlab-org/-/epics/12070), and [Runner Fleet Dashboard to GA](https://gitlab.com/groups/gitlab-org/-/epics/12099)
    * Seamless migration from Artifactory: [Maven Dependency Proxy](https://gitlab.com/groups/gitlab-org/-/epics/3610), [npm Dependency Proxy](https://gitlab.com/groups/gitlab-org/-/epics/3608), [Container Registry for Self-Managed GA](https://gitlab.com/groups/gitlab-org/-/epics/5521), and [PyPI Dependency Proxy](https://gitlab.com/groups/gitlab-org/-/epics/3612)
1. Strengthen our SaaS Deployments to Drive SAM Growth by delivering [Custom Hosted Runners](https://gitlab.com/groups/gitlab-org/-/epics/10877) as the flagship capability.
    Runner SaaS will also extend reach by offering [hosted ARM compute](https://gitlab.com/groups/gitlab-org/-/epics/8442), [GA of macOS runners](https://gitlab.com/groups/gitlab-org/-/epics/8267), [large macOS M2 runners](https://gitlab.com/gitlab-org/ci-cd/shared-runners/infrastructure/-/issues/107), and [GA of Windows Runners](https://gitlab.com/groups/gitlab-org/-/epics/2162).

# Why we do it

### Market Landscape for Continuous Integration Tools

The total addressable market (TAMkt) for DevOps tools delivering against the Verify stage is $3.4B in 2024 and is expected to grow to $3.9B by 2026 (13.95% CAGR) and the Package stage is $1.39B in 2024 with growth to $2B in 2026 (18.30% CAGR)
[(i)](https://docs.google.com/spreadsheets/d/1LO57cmXHDjE4QRf6NscRilpYA1mlXHeLFwM_tWlzcwI/edit?ts=5ddb7489#gid=1474156035).
The Verify and Package Stages combined represents a significant portion of GitLab's expanding addressable market (23% of 2024 TAMkt).

### GitLab CI Section Current Position

The CI Section has continued to maintain a superior experience for individual and small teams of software and DevOps engineers with market share increasing each month as evidenced in our
[Verify product performance indicators (internal)](https://internal.gitlab.com/handbook/company/performance-indicators/product/ops-section/#verifypipeline-execution---gmau-smau---unique-users-triggering-pipelines) and [Package Product performance indicators(internal)](https://internal.gitlab.com/handbook/company/performance-indicators/product/ops-section/#packagepackage---smau-gmau---count-of-users-publishing-packages).

Delivering on the enterprise use case is steadily increasing as evidenced in our
[Verify Paid user-product performance indicators (internal)](https://app.periscopedata.com/app/gitlab/758607/Centralized-SMAU-GMAU-Dashboard?widget=10040188) and [Package Paid user product performance indicators (internal)](https://app.periscopedata.com/app/gitlab/758607/Centralized-SMAU-GMAU-Dashboard?widget=10123560&udv=0). 

To continue this growth, the CI Section needs to invest more in the scaling requirements for large organizations,
deliver on solutions for helping organizations build secure and compliant software, as well as prioritize the usability of our core CI and Packaging capabilities. 

#### Continuous Integration Adoption Path

Within the context of GitLab usage, there are three triggers for when CI/Packaging is an appropriate next step:

1. Pushing code
1. Creating a merge request
1. Automating repetitive tasks

The entry point for adoption is often through the [.gitlab-ci.yml](https://docs.gitlab.com/ee/ci/yaml/gitlab_ci_yaml.html), or [documentation](https://docs.gitlab.com/ee/ci/) and public forums.

Some prerequisites for adopting CI are as follows:

1. GitLab account
1. Familiarity with git
1. GitLab project
1. Enabled shared runners on GitLab SaaS OR configured self-managed runners

### SWOT

The CI vision has some significant strengths, weaknesses, opportunties, and threats to becoming the leading platform for building, testing, and optimizing code:

| STRENGTHS<br>Internal resources to exploit | WEAKNESSES<br>Internal Concerns to mitigate | OPPORTUNITIES<br>External resources to exploit | THREATS<br>External Concerns to mitigate |
| --- | --- | --- | --- |
| We are one of the core adoption paths for our users at GitLab<br><br>Developer first approach for experiences <br><br>Meaningful insights from use of the DevOps platform | Lack of usage data-informed product decisions <br><br>Ineffectively managed Technical debt/bugs<br><br>Over indexing to Enterprise Product Management | Reduce friction between all functions of development in a single-platform <br><br>Empower developers to manage operations, quality, and security by baking those activities into GitLab <br><br> Embrace platform engineering by making it easy to manage CI practices at scale| Competition is a concern for leaders in markets <br><br>GitHub<br><br>Circle CI<br><br>JFrog <br><br>HashiCorp<br><br>Public cloud providers<br><br>New market entrants |

#### Core competencies for CI Section

As organizations migrate to a [cloud-first strategy](https://about.gitlab.com/direction/#why-is-this-important), the CI Section must work to adapt to changing needs in scale, performance, and usability. The Verify and Package Stages must simultaneously support the trend toward microservices architecture and infrastructure as code while balancing the needs of monorepos. 

In response to the rise in supply chain attacks, there is an ever-increasing pace of government-issued [directives](https://www.whitehouse.gov/wp-content/uploads/2022/09/M-22-18.pdf), standards, and regulations focused on the security and integrity of the software supply chain. This means we must add features and capabilities that enable customers to efficiently meet the most stringent secure CI/CD and software chains of custody requirements. To adequately deliver on these expectations of the Enterprise market, the Verify and Package Stages must practice the following principles: **security on-by-default**, **developer productivity**, and **cost effectiveness**.

In FY25, we will achieve this by adding support for:

- [Continuous vulnerability scanning for the container registry](https://gitlab.com/groups/gitlab-org/-/epics/2340)
- [Improved UX for signed container registry images](https://gitlab.com/groups/gitlab-org/-/epics/7856)

#### Competitive Landscape

Our top competitors for the CI Section are GitHub and Jfrog. Secondarily, there are emerging competitors we are watching carefully such as JetBrains and Harness.io. In the install base, more specific to Verify Stage, we have strong users of Jenkins/Cloudbees, and for Package stage there is some usage of Nexus for Artifact management. 

See the Package competitor [page](/direction/package/#competitive-landscape-2)

#### CI Section Jobs To Be Done

Some of the core JTBDs for our three year vision and strategies are as follows:

- Once I have a stable development and operations organization, I want to author a CI pipeline so others in my team can leverage CI to increase the efficiency of their tasks.
- When implementing CI/CD practices across the organization, I want to ensure consistency and standardization of CI/CD workflows to ensure compliance and to ease and increase CI/CD adoption across my teams.
- When I build my project, I want to review upstream dependencies and test result data, so that I can stop and review dependencies and test failures before bugs get into production.
- When analysing configured CI tasks at a higher level for my organization, I want an overall understanding of the historical data about them, so I can identify trends and opportunities for improvements.
- When administering runners for a GitLab instance or group, I need to perform general administrative functions as quickly and efficiently as possible.
- When securing an end-to-end software supply chain I want to access immutable historical verisons of builds, artifacts, dependencies, so that I can fulfill legal or regulatory requirements. 

### Who is it for?

We identify the [personas](https://handbook.gitlab.com/handbook/handbook/product/personas/#user-personas) the CI Section features are built for. In order to be transparent about personas we support today and personas we aim to support in the future we use the following categorization of personas listed in priority order.

- 🟩- Targeted with strong support
- 🟨- Targeted but incomplete support
- ⬜️- Not targeted but might find value

#### Today

To capitalize on the [opportunities](#opportunities) listed above, the Ops section has features that make it useful to the following personas today.

1. 🟩 [Sasha - Software Developer](https://handbook.gitlab.com/handbook/handbook/product/personas/#sasha-software-developer)
1. 🟩 [Devon - DevOps Engineer](https://handbook.gitlab.com/handbook/handbook/product/personas/#devon-devops-engineer)
1. 🟨 [Allison - Application Ops](https://handbook.gitlab.com/handbook/handbook/product/personas/#allison-application-ops)
1. 🟨 [Ingrid - Infrastructure Operator](https://handbook.gitlab.com/handbook/handbook/product/personas/#ingrid-infrastructure-operator)
1. 🟨 [Simone - Software Engineer in Test](https://handbook.gitlab.com/handbook/handbook/product/personas/#simone-software-engineer-in-test)
1. ⬜️ [Delaney - Development Team Lead](https://handbook.gitlab.com/handbook/handbook/product/personas/#delaney-development-team-lead)

#### Medium Term (1-2 years)

As we execute our [3-year strategy](#3-year-strategy), our medium term (1-2 year) goal is to provide a single application that enables collaboration between cloud native development and platform teams.

1. 🟩 [Sasha - Software Developer](https://handbook.gitlab.com/handbook/handbook/product/personas/#sasha-software-developer)
1. 🟩 [Devon - DevOps Engineer](https://handbook.gitlab.com/handbook/handbook/product/personas/#devon-devops-engineer)
1. 🟩 [Allison - Application Ops](https://handbook.gitlab.com/handbook/handbook/product/personas/#allison-application-ops)
1. 🟨 [Ingrid - Infrastructure Operator](https://handbook.gitlab.com/handbook/handbook/product/personas/#ingrid-infrastructure-operator)
1. 🟨 [Simone - Software Engineer in Test](https://handbook.gitlab.com/handbook/handbook/product/personas/#simone-software-engineer-in-test)
1. 🟨 [Delaney - Development Team Lead](https://handbook.gitlab.com/handbook/handbook/product/personas/#delaney-development-team-lead)

## How we do it 

### Cross-section efforts 

There are several key cross-functional investments that will further our competitive position, security posture, and customer experience. The efforts are outlined below: 

| Area | Teams | Target Investment Year |
| --- | --- | --- |
| CI Steps | Pipeline Authoring; Runner Core | FY24 |
| CI/CD Migration Tooling  | Pipeline Execution; Pipeline Authoring | Not Yet Defined  |
| CI/CD Visibility | Pipeline Execution; Observability; Runner Fleet | FY25 |
| Observability and AI Optimization | Pipeline Execution; Observability; Runner Fleet | FY26 |
| Caching | Pipeline Authoring; Runner Core | FY25 |
| CI job queueing | Pipeline Execution; Runner Core; Runner SaaS? | FY26 |
| Runner priority - routing jobs to a specific runner | Pipeline Execution; Runner Core; Runner SaaS? | FY25 |
| CI log rendering user experience | Pipeline Execution; Pipeline Authoring; Runner Core | FY25 |
| Events  | Pipeline Execution; Package; Runner SaaS | FY25 |
| Runner Next (re-architecture of Runner Core) | Runner Core | FY24-FY25 |
| GCP/GitLab Console Integration | Runner Core; Package | FY24-FY25 |
