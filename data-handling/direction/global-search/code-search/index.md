---
layout: markdown_page
title: "Category Strategy - Code Search"
description: "GitLab Code Search provides a way to search all the code in GitLab."
canonical_path: "/direction/global-search/code-search/"
---

- TOC
{:toc}

## Code Search

| | |
| --- | --- |
| Stage | [Enablement](/direction/enablement/) |
| Maturity | [Viable](/direction/#maturity) |
| Content Last Reviewed | `2023-01-24` |
| Content Last Updated | `2023-01-24` |

### Overview

GitLab’s Code Search allows users to search all the code contained within a GitLab instance. As individual codebases, the number of projects, and the number of employees grow within an organization, the ability to easily search all of an organization's code becomes increasingly important.

As part of GitLab's single application vision, GitLab must provide a rich and seamless code search experience so that customers do not have to rely on using external solutions for Code Search. The more source code that is added to GitLab and an organization, the more useful Code Search becomes, as searching across repositories or large monorepos can otherwise be time consuming or impractical.

There are two primary use cases for Code Search:
* Code Maintenance: The more code there is to manage, the more of a challenge code maintenance can become. Being able to quickly find call patterns, references, vulnerabilities, or specific text quickly across a wide range of repositories reduces the maintenance burden and can help users better onboard and understand a complex code base.
* Code Reusability & Innersourcing: Referencing examples from other projects can help users learn new techniques and best practices for performing certain tasks. These examples can help when learning something new, like a service or a different programming language, or onboarding into a new codebase.

### Vision

Code Search will become the tool for developers to quickly learn about all the Source Code in their organization. Users will navigate through the code and quickly filter to their desired line(s) of code. Users can then track the relationships of the code to all other GitLab content, like Commits, Issues, and Merge Requests, to understand the origin and reason for a change.

GitLab is in a unique position to deliver high-quality Code Search. All code is already stored in GitLab, along with other supporting content related to code like merge requests, commits, and issues. This provides two key advantages above a local editor: the ability to quickly search across the entirety of an organization, as well as the fusing of content and context from content other than the code itself, such as merge requests. Understanding these relationships and eventually understanding clusters from these relationships correlate with the visions across many areas of GitLab.

[A vision for Code Search in GitLab](https://www.youtube.com/embed/pPooxvnsGS4)

#### Collaboration

There are many stages and categories that are solving parts of the problem of [Big Code](https://about.gitlab.com/direction/global-search/code-search/#challenges-to-address). Collaboration with these stages and categories is imperative to success, as we are solving adjacent problems.

* [Group Direction - AI Assisted](https://about.gitlab.com/direction/modelops/ai_assisted/)
* [Code to issue audit](https://gitlab.com/gitlab-org/gitlab/-/issues/740)
* [Product Stage Direction - Secure](https://about.gitlab.com/direction/application_security_testing/)
    * [Category Direction - Secret Detection](https://about.gitlab.com/direction/application_security_testing/secret-detection/secret-detection/)
    * [Category Direction - Static Application Security Testing (SAST)](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/)
    * [Category Direction - Vulnerability Management](https://about.gitlab.com/direction/security_risk_management/security-insights/vulnerability_management/)
    * [Category Direction - GitLab Advisory Database](https://about.gitlab.com/direction/application_security_testing/vulnerability-research/advisory-database/)
    * [Category Direction - Software Composition Analysis](https://about.gitlab.com/direction/application_security_testing/composition-analysis/software-composition-analysis/)

### Challenges to address

[Code Search for Big Code](https://gitlab.com/groups/gitlab-org/-/epics/6220) - The code that companies maintain is rapidly increasing in complexity and volume. The rapid increase brings on a series of unique challenges in how to address these needs.

* Opening multiple files across repositories create difficulties with context switching.
* Documentation often includes no examples or one example. Finding all the examples helps understand the uses and can expose caveats not yet documented.
* Copying and pasting code, "Code Cloning", breaks historical reference of code, or "Code Provenance.” Code Provenance reviews, or understanding the source of code like open source projects or online communities, are increasing in frequency and importance.
* Learning a codebase usually requires downloading and opening it in your local IDE, creating inefficiencies and challenges with collaborations like remote pairing, especially with larger repositories.
* Finding unused code - Unused code increases over time and adds to the complexity of maintaining the overall codebase
* Finding code comments - Code comments are often used to help other developers find and understand the code
* Understanding what will be impacted by microservice changes - With the increased reuse of microservices, ensuring that a change will not negatively impact other downstream or upstream services.
* Engineering solutions can often be limited by what is unknown about existing code - this can lead to bugs and more complex solutions that in turn can be more challenging to maintain
* Auditing for development policies - Commonly, teams will create frameworks to reduce the complexity of the many ways to build the same type of thing
* Determining when these frameworks are used and where there are gaps is growingly more difficult

[Insights from code search research for Global Search](https://gitlab.com/groups/gitlab-org/-/epics/5476) - We have conducted studies with our customers to identify and better understand the needs for code Search today.

### One-year plan

Our goal for this year is to provide a code search solution which can reliably and comprehensively find specific strings, substrings, and regular expressions. Today this is not possible due to our use of Elasticsearch, but we plan to implement a new code search infrastructure which will allow us to provide a solid foundation and address key workflows.

* [Switch from Elasticsearch to Zoekt for Code Search](https://gitlab.com/groups/gitlab-org/-/epics/9404)
* [Search results should provide expected results](https://gitlab.com/groups/gitlab-org/-/epics/8268)
* [Support for the new navigation and command palette workflow](https://gitlab.com/gitlab-org/gitlab/-/issues/382328)
* [Code Language Filtering](https://gitlab.com/groups/gitlab-org/-/epics/6236)

#### Desired Results

We expect two key results from this year:

* To provide a reliable and complete code search solution
* Integrate with the new navigation design, where search is a key workflow and powers the new command palette

By solving the problems with code search we will address the adoption drain where users need to use an alternative solution, and with the new navigation we will have prominent placement of search which will increase initial adoption and awareness.

#### Measuring Success - Target PI's / Metrics

The performance and success of Code Search can be measured:

* Changes in the Code Search GMAU and Global Search GMAU
* Quarterly Customer feedback will be collected and reviewed in a comparative nature through the SUS scores
* Code Search will become identified with a higher frequency as a revenue driver

### Target Audience and Experience

Code Search is primarily valuable to organizations with more than 200 users.

#### User personas

1. [Sasha](https://handbook.gitlab.com/handbook/marketing/strategic-marketing/persona-snippets/user-personas/sasha), the Software Developer
2. [Devon](https://handbook.gitlab.com/handbook/marketing/strategic-marketing/persona-snippets/user-personas/devon) the DevOps Engineer
3. [Delaney](https://handbook.gitlab.com/handbook/marketing/strategic-marketing/persona-snippets/user-personas/delaney), the Development Team Lead

#### Buyer personas

1. [Alex](https://handbook.gitlab.com/handbook/marketing/strategic-marketing/persona-snippets/buyer-personas/alex) the Application Development Manager
2. [Dakota](https://handbook.gitlab.com/handbook/marketing/strategic-marketing/persona-snippets/buyer-personas/dakota) the Application Development Director
3. [Erin](https://handbook.gitlab.com/handbook/marketing/strategic-marketing/persona-snippets/buyer-personas/erin), the Application Development Executive (VP, etc.)

### Maturity

Currently, GitLab's maturity for Code Search is Minimal. The functionality of searching code across repositories is not reliable and results can be missed, leading to a lack of confidence.

Advancing Code Search from “Minimal” to “Viable” will include:

* [Switch from Elasticsearch to Zoekt for Code Search](https://gitlab.com/groups/gitlab-org/-/epics/9404)
* [Search results should provide expected results](https://gitlab.com/groups/gitlab-org/-/epics/8268)

### What's Next & Why

We are currently focused on two key projects which are fundamental to improving the code search experience and adoption:

1. [Switching from Elasticsearch to Zoekt](https://gitlab.com/groups/gitlab-org/-/epics/9404)
1. [Integrate with the new navigation workflow](https://gitlab.com/gitlab-org/gitlab/-/issues/382328)

### What we are not focused on

Right now we are focused on building a strong foundation for our search services, indexing content and ensuring results are complete and reliable. We are not focused on providing [Search-as-a-Service to other components of the single platform](https://gitlab.com/groups/gitlab-org/-/epics/7660), which will come later.

### Competitive Landscape

Code Search is part of the [Global Search competitive landscape](https://about.gitlab.com/direction/global-search/#competitive-landscape)
