---
layout: markdown_page
title: "Category Direction - Editor Extensions"
description: "Our strategic vision focuses on the seamless integration of the GitLab platform into developers' daily workflows, aiming to significantly increase their productivity and collaboration."
---

- TOC
{:toc}

## Editor Extensions

|                       |                                  |
|-----------------------|----------------------------------|
| Stage                 | [Create](/direction/dev/#create) |
| Content Last Reviewed | `2024-10-01`                     |

### Introduction and how you can help

Thanks for visiting our direction page. This page belongs to the [Editor Extensions](https://handbook.gitlab.com/handbook/product/categories/#editor-extensions-group) group of the Create stage and is maintained by Dasha Adushkina ([E-Mail](mailto:dadushkina@gitlab.com)).

This direction is constantly evolving and everyone can contribute:

- Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Aeditor%20extensions&first_page_size=100) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=group::editor+extensions) on this page. Sharing your feedback directly on GitLab.com  or submitting a Merge Request to this page are the best ways to contribute to our strategy.
- Please share feedback directly via email or [schedule a video call](https://calendly.com/dashaadu).

### Strategy and Themes
<!-- Describe your category. Capture the main problems to be solved in market (themes). Describe how you intend to solve these with GitLab (strategy). Provide enough context that someone unfamiliar with the details of the category can understand what is being discussed. -->
Our strategic vision focuses on the seamless integration of the GitLab platform into developers' daily workflows, aiming to significantly increase their productivity and collaboration. By embedding [GitLab Duo features](https://docs.gitlab.com/ee/user/gitlab_duo/index.html), such as Code Suggestions and Duo Chat, directly within IDEs, we strive to transform how developers interact with their tools, reduce context switching, and bring AI-driven capabilities within easy reach.

#### Strategic Pillars
- **Deep Integration with Coding Environments**: We recognize the indispensable role of IDEs and Code Editors in a developer's toolkit. Our strategy includes developing extensions that support various programming languages, standards, and frameworks. This way, developers can stay in one consistent environment for their entire workflow.

- **Facilitating Collaborative Development**: At the heart of our strategy is the enhancement of collaborative workflows. By optimizing how engineers interact with one another from initial discussion in issues to significant contributions via merge requests, we aim to make collaborative work more efficient and transparent.

- **Extending GitLab's Reach Beyond the Core Platform**: Understanding that developers spend considerable time outside the GitLab platform, we are dedicated to extending GitLab's collaborative and development features closer to where the actual work happens. This approach is designed to not only improve productivity but also enrich the overall development experience.

### 1 year plan
<!--
1 year plan for what we will be working on linked to up-to-date epics. This section will be most similar to a "road-map". Items in this section should be linked to issues or epics that are up to date. Indicate relative priority of initiatives in this section so that the audience understands the sequence in which you intend to work on them.
 -->
**Enhance the developer experience with AI with a focus on usability**
- Integrate [GitLab Duo](https://docs.gitlab.com/ee/user/gitlab_duo/index.html) directly into IDEs via editor extensions to offer instant access to GitLab's AI-driven capabilities.
- Focus on enhancing [Code Suggestions](https://docs.gitlab.com/ee/user/project/repository/code_suggestions/) with fine-tuned controls, customizable hotkeys, and streaming capabilities.

**Deepen GitLab integration within IDEs**
- [Integrate Static Application Security Testing (SAST)](https://gitlab.com/groups/gitlab-org/-/epics/10283) directly into the IDE to instantly identify and address security flaws in code.
- Expand pipeline editor functionalities into IDEs, leveraging features like [config validation](https://gitlab.com/gitlab-org/gitlab-vscode-extension#validate-gitlab-cicd-configuration), [displaying consolidated CI/CD configuration](https://gitlab.com/gitlab-org/gitlab-vscode-extension#validate-gitlab-cicd-configuration), and [variable autocomplete](https://gitlab.com/gitlab-org/gitlab-vscode-extension#validate-gitlab-cicd-configuration) currently in VS Code and extending them to other IDEs.

#### What is next for us
<!-- This is a 3 month look ahead for the next iteration that you have planned for the category. This section must provide links to issues or
or to [epics](https://handbook.gitlab.com/handbook/product/product-processes/#epics-for-a-single-iteration) that are scoped to a single iteration. Please do not link to giant epics that lack clarity on what is next. -->

- [Integrate Duo Chat into Visual Studio](https://gitlab.com/groups/gitlab-org/editor-extensions/-/epics/22)

- [Real-time SAST scanning](https://gitlab.com/groups/gitlab-org/-/epics/10283): Partnering with the [static analysis group](https://handbook.gitlab.com/handbook/product/categories/#static-analysis-group), we'll work to extend the work they're targeting for SAST scanning to reach more users across IDEs.


#### What we are currently working on

<!-- Scoped to the current month. This section can contain the items that you choose to highlight on the kickoff call. Only link to issues, not Epics.  -->



1. [Enable Duo Quick Chat in VS Code](https://gitlab.com/groups/gitlab-org/-/epics/15218)
2. [Integrate Duo Chat into Visual Studio](https://gitlab.com/groups/gitlab-org/editor-extensions/-/epics/77)
3. [SAST scanning in VS Code](https://gitlab.com/groups/gitlab-org/-/epics/14984)
<!-- #### What we recently completed -->
<!-- Lookback limited to 3 months. -->

#### What is Not Planned Right Now
<!--  Often it's just as important to talk about what you're not doing as it is to
discuss what you are. This section should include items that people might hope or think
we are working on as part of the category, but aren't, and it should help them understand why that's the case.
Also, thinking through these items can often help you catch something that you should
in fact do. We should limit this to a few items that are at a high enough level so
someone with not a lot of detailed information about the product can understand -->

We are exploring support for additional IDEs. If you would like to let us know what IDEs or Code Editors you want to see supported, please add a comment to [this epic](https://gitlab.com/groups/gitlab-org/-/epics/2431).

<!-- ### Target Audience -->
<!--
List the personas (https://handbook.gitlab.com/handbook/marketing/strategic-marketing/roles-personas#user-personas) involved in this category.

Look for differences in user's goals or uses that would affect their use of the product. Separate users and customers into different types based on those differences that make a difference.
-->

<!--
The software development process involves many people working across various parts of configuration, contribution and review. All of these users work together to advance software projects in their organization.

Engineering personas who are contributing to development, configuring or interacting with continuous integration and reviewing contributions from other team members. Users performing these tasks need tools that allow them to deeply understand the changes and provide meaningful feedback of both comments and code suggestions. These are specifically addressed by the following GitLab Personas:

- [Sasha (Software Developer)](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
- [Devon (DevOps Engineer)](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
-->
