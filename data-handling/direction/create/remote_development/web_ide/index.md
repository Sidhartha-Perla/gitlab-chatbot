---
layout: markdown_page
title: "Category Direction - Web IDE"
description: "Discover GitLab's Web IDE for remote development, offering a cloud-based coding environment for seamless collaboration and development from anywhere."
---

- TOC
{:toc}

## Web IDE

| | |
| --- | --- |
| Stage | [Create](/direction/create/) |
| Maturity | [Complete](/direction/#maturity) |
| Content Last Reviewed | `2025-03-11` |

### Introduction and how you can help

Thanks for visiting the category direction page for the GitLab Web IDE. This page belongs to the [Remote Deveopment group](https://handbook.gitlab.com/handbook/product/categories/#remote-development-group) of the [Create stage](https://handbook.gitlab.com/handbook/engineering/development/dev/create/) and is maintained by Senior Product Manager, Michelle Chen ([@michelle-chen](https://gitlab.com/michelle-chen)).

This direction page is a work in progress, and everyone can contribute:

- Please comment and contribute to issues linked througout this page or contained in our [category strategy epic](https://gitlab.com/groups/gitlab-org/-/epics/170). Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
- If you would like to share your feedback directly or schedule a video call, please reach out directly to Michelle Chen via [email](mailto:mchen@gitlab.com).

### Overview
<!-- Describe your category so that someone who is not familar with the market space can understand what the product does.
-->

A code editor is one of the most important tools in a software developer's toolkit. With the Web IDE, we want to meet the developers where they are and offer a mature, feature-rich editing experience in the browser. By replacing the current Web IDE with a browser-based instance of VS Code, the [most popular code editor](https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-integrated-development-environment), we can enable developers to complete more complex tasks and work more efficiently inside GitLab.

Software development is an iterative process that involves requesting and responding to feedback from Developers, Designers, Product Managers, or other peers. While a desktop editor is often optimized with extensions to support specific programming languages, coding standards, or frameworks, they are often not ideal for the frequent context switching and rapid feedback cycles in the review phase. GitLab's Web IDE offers a familiar workflow to developers while remaining easy to use for designers, product managers and more. It brings editing capabilities into the context of their current task in GitLab, by providing an editing experience designed for the workflow they're trying to accomplish.

### Strategy and Themes
<!-- Describe your category. Capture the main problems to be solved in market (themes). Describe how you intend to solve these with GitLab (strategy). Provide enough context that someone unfamiliar with the details of the category can understand what is being discussed. -->

There are three critical workflows we aim to support in the Web IDE.

**Configuration**

Users who configure projects or GitLab need editing tools to help them be efficient at this process. Creating specialized configuration files for working with GitLab CI or other areas of GitLab benefit from feedback provided directly in the editor.

Configuration files are common to software development and the tools of the DevSecOps life cycle. Files like `gitlab-ci.yml` or `CODEOWNERS` can be difficult to manage because they need to be both syntactically (correct commas, quotes, value types etc) and semantically valid (expresses what you intended it to). Local development environments can be configured with syntax checkers, and schemas to help verify syntactic correctness, but lack the context for deeper features.

Once your GitLab CI configuration has been created and validated, it may be responsible for providing review applications for previewing changes, code quality and coverage reports or vulnerability information. As an engineer who is working on a contribution information contained on these reports must be reconciled within their editor.

**Contribution**

Developers who work on contributing directly to the code in projects need to action feedback from the review process. This often involves leaving MR feedback open in one window while working in an editor in a different window. Feedback in the form of suggestions and patch files needs to be handled outside of the MR interface and back in the local development environment. At the same time some feedback requires manually updating comments and threads that feedback has been actioned after the changes have been pushed back to the MR. Having easy access to the feedback from reviewers and CI jobs inside of the editor should ensure that it's easy to action.

**Feedback & Review**

The code review process encompasses both engineering personas and non-engineering personas who contribute through design, product and other feedback.

A developer reviewing a merge request often needs to check the code out locally and create an environment for that review. Sometimes this process can be complicated by conflicts with local dependencies, their own local development branch, database migrations and other issues which prevent just cleanly changing branches.

A designer or product manager may not have the time or experience required to set up and maintain an environment to perform reviews. Reviewing these changes inside of a review application is valuable, but it can be hard to provide as actionable comments back to the MR.

In solving for both these users and workflows, it will be important to make sure that people who want to give feedback are able to easily accomplish that.

**Strategic Focus Areas**
To address these themes, we will focus on the following strategic areas, which will resemble phases of the product and work prioritization:

![Web IDE Strategic Focus Areas](../../../images/remote_development/webide-strategic-areas.png)

#### GitLab Workflow for Visual Studio Code

The [GitLab Workflow extension for VS Code](https://docs.gitlab.com/ee/editor_extensions/visual_studio_code/) is available on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=GitLab.gitlab-workflow) and enables you to interact with merge request discussions, issues, and pipelines directly from VS Code.

One of the benefits of [replacing the Web IDE with a VS Code instance](https://gitlab.com/groups/gitlab-org/-/epics/7683) is that you will be able to install compatible extensions in the browser-based Web IDE. By [bundling the GitLab Workflow extension in the Web IDE](https://gitlab.com/gitlab-org/gitlab/-/issues/355054), we will enable new functionality and provide consistency across the desktop and web editing experience. Functionality contributed by the community and additional investments in the capabilities of the extension will then be available on both platforms. The GitLab Workflow extension is maintained by the [Editor Extensions](/direction/create/editor_extensions/) group.

### 1 year plan
<!--
1 year plan for what we will be working on linked to up-to-date epics. This section will be most similar to a "road-map". Items in this section should be linked to issues or epics that are up to date. Indicate relative priority of initiatives in this section so that the audience understands the sequence in which you intend to work on them.
 -->

- [Don't require accepting third-party cookies to run Web IDE](https://gitlab.com/gitlab-org/gitlab-web-ide/-/issues/270)
- [1st Class Editing Experiences for GitLab features](https://gitlab.com/groups/gitlab-org/-/epics/2707)
- [Add additional source control operations to the Web IDE](https://gitlab.com/groups/gitlab-org/-/epics/11142)

#### What is next for us
<!-- This is a 3 month look ahead for the next iteration that you have planned for the category. This section must provide links to issues or
or to [epics](https://handbook.gitlab.com/handbook/product/product-processes/#epics-for-a-single-iteration) that are scoped to a single iteration. Please do not link to epics encompass a vision that is a longer horizon and don't lay out an iteration plan. -->

- [Search across all files in a project from within the Web IDE](https://gitlab.com/groups/gitlab-org/-/epics/9466)
- [Consistent UI for Web IDE Loader and Error State](https://gitlab.com/groups/gitlab-org/-/epics/14944)
- [Fix: Theme images are broken on the VS Code welcome page](https://gitlab.com/groups/gitlab-org/-/epics/14997)

#### What we are currently working on
<!-- Scoped to the current month. This section can contain the items that you choose to highlight on the kickoff call. Only link to issues, not Epics.  -->

- [Enable Web IDE Extension Marketplace for Self-Managed](https://gitlab.com/groups/gitlab-org/-/epics/11770)
- [Prevent different Web IDE Extensions Marketplace contexts from overwriting Settings Sync store](https://gitlab.com/groups/gitlab-org/-/epics/15216)
- [Host the Web IDE on a new domain or subdomain](https://gitlab.com/groups/gitlab-org/-/epics/11972)


#### What we recently completed
<!-- Lookback limited to 3 months. Link to the relevant issues or release post items. -->

- [Settings Sync for the Web IDE](https://gitlab.com/groups/gitlab-org/-/epics/11147)
- [Enable Web IDE Extension Marketplace for GitLab.com](https://gitlab.com/groups/gitlab-org/-/epics/11769)
- [Enable OAuth authentication by default on the Web IDE](https://gitlab.com/groups/gitlab-org/-/epics/14941)
- [Investigate hosting Web IDE on new domain](https://gitlab.com/gitlab-org/gitlab/-/issues/464082)


#### What is Not Planned Right Now
<!--  Often it's just as important to talk about what you're not doing as it is to
discuss what you are. This section should include items that people might hope or think
we are working on as part of the category, but aren't, and it should help them understand why that's the case.
Also, thinking through these items can often help you catch something that you should
in fact do. We should limit this to a few items that are at a high enough level so
someone with not a lot of detailed information about the product can understand -->

While our [complete maturity](/direction/create/remote_development/web_ide/#maturity) plan also aims to ensure some [compatibility with the iPad](https://gitlab.com/groups/gitlab-org/-/epics/756). We won't be focusing on making the iPad or other mobile devices 1st class devices due to our upstream dependencies on VS Code. We also do not have sufficient evidence to support mobile devices as code creation devices inside the Web IDE. As our research in this area continues to expand we may revisit mobile support.

We do not have plans to bring real-time collaborative coding features to the Web IDE at this time. We'll continue to evaluate the space and may revisit this use case at a later date, especially as it relates to [workspaces](/direction/create/remote_development/workspaces/).

### Target Audience
<!--
List the personas (https://handbook.gitlab.com/handbook/marketing/strategic-marketing/roles-personas#user-personas) involved in this category.

Look for differences in user's goals or uses that would affect their use of the product. Separate users and customers into different types based on those differences that make a difference.
-->

The Web IDE primarily serves engineering personas who are contributing to development, configuring or interacting with continuous integration and reviewing contributions from other team members. Personas like [Sasha (Software Developer)](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer) and [Devon (DevOps Engineer)](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer) need tools that allow them to deeply understand the changes and provide meaningful feedback of both comments and code suggestions.

The Web IDE also serves non-engineer personas who are focused on reviewing and providing feedback for contributions. Personas like [Parker (Product Manager)](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager), [Presley (Product Designer)](https://handbook.gitlab.com/handbook/product/personas/#presley-product-designer), and [Delaney (Development Team Lead)](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead) need tools and features that help them preform reviews of code, documentation and interfaces without requiring local environments or complex configurations. Feedback should be easy to leave and actionable by engineers within their editor.

### Pricing and Packaging

The Web IDE is available to everyone on SaaS and Self-managed as part of the Free tier.
