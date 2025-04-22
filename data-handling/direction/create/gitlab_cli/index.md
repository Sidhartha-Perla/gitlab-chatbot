---
layout: markdown_page
title: "Category Direction - GitLab CLI"
description: "Get insights into GitLab's Command Line Interface (CLI) plans, providing developers with a powerful tool to interact with GitLab from the terminal."
---

- TOC
{:toc}

## GitLab CLI

|                       |                                  |
|-----------------------|----------------------------------|
| Stage                 | [Create](/direction/dev/#create) |
| Maturity              | [Viable](/direction/#maturity)   |
| Content Last Reviewed | `2025-04-04`                     |

### Introduction and how you can help

Thanks for visiting this direction page on the GitLab CLI. This page belongs to the [Code Review](https://handbook.gitlab.com/handbook/product/categories/#code-review-group) group of the Create stage and is maintained by Kai Armstrong ([E-Mail](mailto:karmstrong@gitlab.com)).

This direction is constantly evolving and everyone can contribute:

- Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/cli/-/issues) and epics on this page. Sharing your feedback directly on GitLab.com  or submitting a Merge Request to this page are the best ways to contribute to our strategy.
- Please share feedback directly via email, Twitter, or [schedule a video call](https://calendly.com/gitlabkai). If you're a GitLab user and have direct knowledge of your needs for the GitLab CLI, we'd especially love to hear from you.

### Strategy and Themes
The command line is one of the most important tools in a software engineer's toolkit and the majority of their process and work revolve around tools available there. They customize their CLI with styles and extend it through applications to ensure maximum efficiency while performing tasks. The CLI is the backbone of scripts and workflows developers depend on to complete their work.
Engineers working on contributions often collaborate with product managers, designers and other engineers to complete their work. Initially this collaboration takes place in issues where engineers can ask clarifying questions, review designs and discuss solutions. When engineers begin to work on these contributions, issues serve as the reference document and requirements to complete their task.
Once those contributions have been worked engineers contribute those via a Merge Request. Merge Requests are a collaborative process that involves getting feedback on the work completed and then responding to that feedback through additional revisions and comments.
Configuration files are also common to software development and the tools of the DevOps life cycle. In GitLab there are files like `.gitlab-ci.yml` and `CODEOWNERS` which have specific syntaxes and parameters to properly configure. Making changes to these files often involves having documentation available and then validating content through commits or tools outside the editor.
GitLab supports teams collaborating and building software together, however that collaboration is only available inside the GitLab application.
Developers, on the other hand, spend the majority of their time working locally implementing work outlined in issues, responding to merge request feedback and testing/debugging their applications. These tasks are the core of the developer experience, and GitLab should support developers closer to where they're doing their meaningful work to enable them to be more efficient in the delivery of that work.
\*\*Configuration\*\*
Users who configure projects or GitLab need tools to help them be efficient at this process. The GitLab CLI provides methods to create and then manage project configurations which can be important for instance management. Once your project is up and running you can easily manage and test your GitLab CI/CD configuration to ensure it is setup correctly.
\*\*Contribution\*\*
Engineering personas who work on contributing directly to the code in projects need to action feedback from the review process. The GitLab CLI makes it easy to view the contents of an issue you're working on, check the status of merge requests, get feedback and output from running pipelines, and much more.
\*\*Automation\*\*
Automating tasks is an important part of engineering process. The GitLab CLI supports users in both interactive and non-interactive workflows to script repetitive tasks for information during the development process, automate interactions in GitLab CI or produce reporting for external systems.
\*\*Flexibility\*\*
Flexibility in tooling is valuable to support a variety of different workflows and use cases. The GitLab CLI provides an opinionated set of commands for interacting with issues, merge request, and pipelines. However, we also provide a flexible tool that allows you to alias any API interaction to your own commands for your workflow.
### 1 year plan

 
</figure>

**In Progress:** [Stacked diffs via the GitLab CLI](https://gitlab.com/groups/gitlab-org/-/epics/12025) - we'll be exploring stacked diff workflows following up on our improvements to dependency management. We're initially looking at how to provide support via the CLI as an MVC.

#### What is next for us
<!-- This is a 3 month look ahead for the next iteration that you have planned for the category. This section must provide links to issues or
or to [epics](https://handbook.gitlab.com/handbook/product/product-processes/#epics-for-a-single-iteration) that are scoped to a single iteration. Please do not link to giant epics that lack clarity on what is next. -->

**Later:** Expand AI capabilities of `glab ask`

The GitLab CLI currently supports asking questions about how to accomplish some tasks with the usage of `git`. We'll look for more ways to expand this and potentially leverage GitLab Duo Chat in the future.

#### What we are currently working on
<!-- Scoped to the current month. This section can contain the items that you choose to highlight on the kickoff call. Only link to issues, not Epics.  -->

Current inflight work can be tracked via the [open merge request list](https://gitlab.com/gitlab-org/cli/-/merge_requests?scope=all&state=opened). This includes community contributions and other improvements to the GitLab CLI.

#### What we recently completed
<!-- Lookback limited to 3 months. -->

Other completed work can be seen by looking at the [merged](https://gitlab.com/gitlab-org/cli/-/merge_requests?scope=all&state=merged) items for the project.

#### What is Not Planned Right Now
<!--  Often it's just as important to talk about what you're not doing as it is to
discuss what you are. This section should include items that people might hope or think
we are working on as part of the category, but aren't, and it should help them understand why that's the case.
Also, thinking through these items can often help you catch something that you should
in fact do. We should limit this to a few items that are at a high enough level so
someone with not a lot of detailed information about the product can understand -->

We're currently only focused on the GitLab CLI and continuing to expand the experience for those users.

### Best in Class Landscape
<!-- Summary of the competitive landscape for top 3 competitors. Identification of the competitor which we consider to be "Best in Class" and why. Link to epics/issues that would close the gaps between and us and that competitor.

(For non-marketing categories this section is optional)
-->

BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

<!-- #### Key Capabilities -->
<!-- For this product area, these are the capabilities a best-in-class solution should provide -->

<!-- #### Roadmap -->
<!-- Key deliverables we're focusing on to build a BIC solution. List the epics by title and link to the epic in GitLab. Minimize additional description here so that the epics can remain the SSOT. -->

#### Top [1/2/3] Competitive Solutions
<!-- PMs can choose to highlight a primary BIC competitor--or more, if no single clear winner in the category exists; in this section we should indicate: 1. name of competitive product, 2. links to marketing website and documentation, 3. why we view them as the primary BIC competitor -->

- [GitHub CLI](https://cli.github.com/)

### Maturity Plan
<!-- It's important your users know where you're headed next. The maturity plan section captures this by showing what's required to achieve the next level. The
section should follow this format:

This category is currently at the XXXX maturity level, and our next maturity target is YYYY (see our [definitions of maturity levels](https://about.gitlab.com/direction/#maturity).

- Link to maturity epic if you are using one, otherwise list issues with maturity::YYYY labels)

(For non-marketing categories this section is optional)  -->

This category is currently at the Viable maturity level, and our next maturity target is Complete (see our [definitions of maturity levels](https://about.gitlab.com/direction/#maturity). We're continuing to evaluate required components to move to that level.

### Target Audience
<!--
List the personas (https://handbook.gitlab.com/handbook/marketing/strategic-marketing/roles-personas#user-personas) involved in this category.

Look for differences in user's goals or uses that would affect their use of the product. Separate users and customers into different types based on those differences that make a difference.
-->

The software development process involves many people working across various parts of configuration, contribution and review. All of these users work together to advance software projects in their organization.

Engineering personas who are contributing to development, configuring or interacting with continuous integration and reviewing contributions from other team members. Users performing these tasks need tools that allow them to deeply understand the changes and provide meaningful feedback of both comments and code suggestions. These are specifically addressed by the following GitLab Personas:

- [Sasha (Software Developer)](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
- [Devon (DevOps Engineer)](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
