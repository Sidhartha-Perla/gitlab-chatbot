---
layout: markdown_page
title: "Category Direction - Importers"
description: "This GitLab product category is about enabling adoption of GitLab offerings (SaaS, Dedicated, self-managed) by bring existing projects to GitLab, or copying GitLab groups and projects to a different location. Find more information here!"
canonical_path: "/direction/foundations/import_and_integrate/importers/"
---

- TOC
{:toc}

## Importers

| | |
| --- | --- |
| Stage | [Foundations](/direction/foundations/) |
| Maturity | N/A |
| Content Last Reviewed | `2025-04-07` |

### Introduction and how you can help

Thanks for visiting this category direction page on Importers in GitLab. This page belongs to the [Import and Integrate](https://handbook.gitlab.com/handbook/product/categories/#import-and-integrate-group) group of the Foundations stage and is maintained by the group's Product Manager, [Magdalena Frankiewicz](https://gitlab.com/m_frankiewicz) ([E-mail](mailto:mfrankiewicz@gitlab.com), [Calendly](https://calendly.com/gitlab-magdalenafrankiewicz/45mins)).

This direction page is a work in progress, and everyone can contribute:

- Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=Category%3AImporters&first_page_size=100) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=Category:Importers) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
 - Please share feedback directly via email, Twitter, or on a video call. If you're a GitLab user and want to discuss how GitLab can improve Importers, we'd especially love to hear from you.

### Strategy and Themes

A typical organization looking to adopt GitLab already has many other tools. Artifacts such as code, issues, and epics may already exist and are being used daily. Seamless transition of work in progress is critically important, and a great experience during this migration creates a positive first impression of GitLab. Solving these transitions, even for complex cases, is crucial for GitLab's ability to expand in the market. Instilling confidence in users that their data will be migrated quickly and with maximum care is of utmost importance.
Supporting GitLab's objectives of driving first order growth, accelerating customer value, and enabling customer-focused innovation, the Import and Integrate group is focused on making imports reliable and performant at any scale. Large-scale moves to GitLab should be significantly easier and ultimately reach a first-class experience level.
Our focus areas for improvement include:
\* \*\*Ease of use\*\*
Customers looking to import their data sometimes struggle to find the place in GitLab where they can initiate imports. Once found, the user interactions are not always intuitive, and the flow is not fully user-friendly. Improving the user experience in this area will make our importers more lovable.
\* \*\*Reliability\*\*
A portion of our current issues are related to the solution's reliability. Imports don't always succeed, and when they fail, there is little guidance for users on steps they can take to remedy the failure. We are working on making our importers more reliable so that our customers can have confidence in the migration process.
\* \*\*Scalability and performance\*\*
Large organizations looking to move possibly hundreds or thousands of projects from tools like GitHub or Bitbucket to GitLab, or from self-managed GitLab instances to GitLab.com or [GitLab Dedicated](https://docs.gitlab.com/ee/subscriptions/gitlab\_dedicated/), need to be able to do so efficiently and reliably.
#### Current Focus Areas
The Import and Integration group is primarily focused on:
\* Migrations between GitLab instances - enabling seamless transitions between self-managed instances, GitLab.com, and GitLab Dedicated.
\* Imports from source control tools - supporting migrations from platforms like GitHub, Bitbucket, and others.
\* Standardizing importers - improving consistency, security, and performance across all importers.
### 1 year plan
Our roadmap for the upcoming year (rolling 12 months) is focused on three main initiatives:
\*\*1. Strengthen customer confidence with [migration by direct transfer General Availability](https://gitlab.com/groups/gitlab-org/-/epics/11398)\*\*
[Migration by direct transfer](https://docs.gitlab.com/ee/user/group/import/index.html#migrate-groups-by-direct-transfer-recommended) has been available as a Beta feature, but many enterprise customers avoid using it due to internal policies requiring GA products for mission-critical systems. We plan to bring Direct Transfer to GA status in Q2 FY26, providing enterprise customers with the assurance they need while delivering a smoother, more reliable migration experience.
Work includes:
- Completing reliability enhancements to ensure consistent migration results
- Polishing the new [user contributions mapping feature](https://docs.gitlab.com/user/project/import/#user-contribution-and-membership-mapping)
- Conducting thorough security reviews and performance testing
\*\*2. Enable migrations between offline GitLab instances\*\*
PubSec and highly regulated customers often maintain GitLab instances in offline environments. Currently migration by direct transfer require internet connectivity, making it difficult for these customers to move data between instances.
By implementing support for semi-automated migrations between offline instances in Q3 FY26, we'll address the needs of these customers.
\*\*3. Enable imports from various third-party providers\*\*
We're working on defining a standard data format and providing tools for contributors to build compatible importers outside of GitLab's main codebase. This will allow us to support imports from a wider range of platforms without increasing our maintenance burden.
\*\*Engineering-led Initiative: Standardizing Importers\*\*
In parallel with our product-led initiatives, our engineering team is working on standardizing importers to improve consistency, security, and performance by creating reusable components. This will:
- Create a more consistent user experience across importers
- Improve security and performance of all importers
- Reduce maintenance burden by centralizing common code
- Make it easier to implement new features and fix bugs
#### What is next for us
In Q2 we're working to strengthen customer confidence by [bringing migration by direct transfer to General Availability](https://gitlab.com/groups/gitlab-org/-/epics/11398).
#### What we recently completed
\*\*Simplify and speed up contribution and membership mapping after imports\*\*
Mapping user contributions after migrations was a manual, time-consuming process that must have beeen done through the UI one user at a time. For organizations with hundreds or thousands of users, this was a significant bottleneck.
We've implemented [bulk CSV-based mapping](https://gitlab.com/groups/gitlab-org/-/epics/16765) to dramatically reduce the effort required to preserve user contributions during migrations. This enhancement benefits not just migration by direct transfer between GitLab instances but also third-party importers, including those for GitHub, Bitbucket Server and Gitea.
This work has been delivered in Q1 FY26.
#### What is Not Planned Right Now
Given our focus on the initiatives above, we are not currently prioritizing:
- Implementing a Jira Server importer - This has been deprioritized for FY26 given resource constraints and other priorities.
- Improvements to GitLab for Slack and Microsoft Teams integrations - While important, these have been deprioritized due to resource constraints.
- Creating a GitLab marketplace for integrations - This longer-term initiative has been moved to future consideration.
The Import and Integrate group is not focused on the ability to regularly back up and restore your GitLab data, for example nightly backups of all your data. For more information on this use case, please see the [Backup and Restore category direction page](https://about.gitlab.com/direction/geo/backup\_restore/).
### Best in Class Landscape
BIC (Best In Class) is an indicator of forecated near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities
This table provides a quick overview of what GitLab importers exist today and which most important objects they each support. This list is not exhaustive and the detailed information can be found on the [Importers documentation page](https://docs.gitlab.com/ee/user/project/import/).
[tanuki]: https://about.gitlab.com/ico/favicon-16x16.png "GitLab"
[tan2]: *| Import source | Repos | MRs | Issues | Epics | Milestones | Wiki | Designs | API \** |
|-----------------------------------------------------------------------------------------------|-------------|------------|------------|-----------|------------|------------|-----------|------------|
| [ Group and project migration by direct transfer](https://docs.gitlab.com/ee/user/group/import/)           | ✅          | ✅          | ✅          | ✅       | ✅          | ✅         | ✅        | ✅         |
| [ Group migration with export files (deprecated)](https://docs.gitlab.com/ee/user/group/settings/import_export.html)     | ➖ | ➖         | ➖          | ✅       | ✅          | ➖         | ➖        | ✅         |
| [ Project migration with export files](https://docs.gitlab.com/ee/user/project/settings/import_export.html) | ✅ | ✅         | ✅          | ➖       | ✅          | ✅         | ✅        | ✅         |
| [GitHub](https://docs.gitlab.com/ee/user/project/import/github.html)                          | ✅          | ✅          | ✅          | ➖       | ✅          | ✅         | ➖        | ✅         |
| [Bitbucket Cloud](https://docs.gitlab.com/ee/user/project/import/bitbucket.html)              | ✅          | ✅          | ✅          | ➖       | ✅          | ✅         | ➖        | ✅         |
| [Bitbucket Server](https://docs.gitlab.com/ee/user/project/import/bitbucket_server.html)      | ✅          | ✅          | ❌          | ➖       | ❌          | ➖         | ➖        | ✅         |
| [Gitea](https://docs.gitlab.com/ee/user/project/import/gitea.html)                            | ✅          | ✅          | ✅          | ➖       | ✅          | ➖         | ➖        | ❌         |
| [Git (Repo by URL)](https://docs.gitlab.com/ee/user/project/import/repo_by_url.html)          | ✅          | ✅          | ➖          | ➖       | ➖          | ➖         | ➖        | ✅         |
| [Manifest file](https://docs.gitlab.com/ee/user/project/import/manifest.html)                 | ✅          | ✅          | ➖          | ➖       | ➖          | ➖         | ➖        | ❌         |
| [FogBugz](https://docs.gitlab.com/ee/user/project/import/fogbugz.html)                        | ➖          | ➖          | ✅          | ➖       | ➖          | ➖         | ➖        | ❌         |

* ✅ : Supported
* ❌ : Not supported
* ➖ : Not applicable

**_\* This column indicates whether this importer is accessible via API, in addition to the UI._**

### Target Audience
<!--
List the personas (https://handbook.gitlab.com/handbook/marketing/strategic-marketing/roles-personas#user-personas) involved in this category.

Look for differences in user's goals or uses that would affect their use of the product. Separate users and customers into different types based on those differences that make a difference.
-->

- [Delaney, Development Team Lead](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
- [Allison, Application Ops](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops)
- [Dakota, Application Development Director](https://handbook.gitlab.com/handbook/product/personas/#dakota-application-development-director)

### Professional Services and Migration Support

While our long-term goal is to provide all the GitLab importing capabilities needed by our customers in our application, we recognize that specific migration scenarios may require additional support.
GitLab [Professional Services](https://about.gitlab.com/services/) team uses the [Congregate](https://gitlab.com/gitlab-org/professional-services-automation/tools/migration/congregate) tool to orchestrate user, group, and project import API calls to help customers automate scaled migrations. With migration by direct transfer reaching GA status, we'll be able to enhance the capabilities of Congregate and provide a more reliable and scalable migration experience for our largest customers.

For complex migrations, especially for large enterprise customers moving to GitLab Dedicated, we recommend engaging with our Professional Services team to ensure a smooth transition.

### How to Provide Feedback

If you have feedback on our importers, please share it on our [feedback issue](https://gitlab.com/gitlab-org/gitlab/-/issues/284495). Your input helps us improve these tools for everyone.
