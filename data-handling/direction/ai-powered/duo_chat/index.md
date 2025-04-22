---
layout: markdown_page
title: "Category Direction - GitLab Duo Chat"
description: "GitLab Duo Chat is your DevSecOps assistant"
canonical_path: "/direction/ai-powered/duo_chat/"
---

## On this page
{:.no_toc}

- TOC
{:toc}

## GitLab Duo Chat

| | |
| --- | --- |
| Stage | [AI-powered](/direction/ai-powered/) |
| Group | [Duo Chat](/direction/ai-powered/duo_chat) |
| Maturity | [Available](/direction/#maturity) |
| Content Last Reviewed | `2024-10-05` |

### Introduction and how you can help
<!-- Introduce yourself and the category. Use this as an opportunity to point users to the right places for contributing and collaborating with you as the PM -->

Thanks for visiting this category direction page on GitLab Duo Chat. This page belongs to the [Duo Chat group](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/duo-chat/) of the AI-powered stage and is maintained by [Torsten Linz](https://gitlab.com/tlinz) ([email](mailto:tlinz@gitlab.com>)).

This direction page is a work in progress, and everyone can contribute to our vision, architecture, and designs by commenting on the epic for the [GitLab Duo Chat](https://gitlab.com/groups/gitlab-org/-/epics/10219) and its sub-epics and issues.

 - Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
 - Alternatively, feel free to share feedback directly via [email](mailto:tlinz@gitlab.com>), or on a video call. If you're a GitLab user and have direct knowledge of your need for AI support, we'd especially love to hear from you.

### Overview
<!-- Describe your category so that someone who is not familiar with the market space can understand what the product does.
-->
The recent advent of very capable large language models presents an opportunity to improve the way users interact with data. It is now possible to employ such AI models to let users interactively explore data via natural language.

The vision: GitLab Duo Chat is a conversational AI assistant that simplifies tasks and reducing context switches to empower users to achieve their DevSecOps goals faster and streamlined.

Initially, Chat will be limited in the types of queries it can answer. Long-term we intend for Chat to also be able to carry out tasks for the user.

### Strategy and Themes
<!-- Capture the main problems to be solved in market (themes). Describe how you intend to solve these with GitLab (strategy). Provide enough context that someone unfamiliar with the details of the category can understand what is being discussed. -->

Let's face it DevSecOps tasks are hard and complex. Understanding code that others have written, comprehending reported vulnerabilities, reading through tons of comments, understanding why a pipeline failed. And this is just the beginning, ultimately one wants to contribute to such code, fix the vulnerability, draw conclusions from the comments, and fix the pipeline.

Yes, such work is being done every day by developers, security professionals, product managers, and all the other personas that work in the DevSecOps space. However, they could do all these tasks much more efficiently and with less context switching with the help of AI.

GitLab Duo Chat aims to do just that and is a cornerstone in our [FY25 Investment theme to make DevSecOps more efficient with AI](https://about.gitlab.com/direction/#enable-aiml-efficiencies-across-devsecops).

Our Duo Chat strategy is to assist users with AI in ideation and creation tasks as well as in learning tasks across the entire Software Development Lifecycle (SDLC) to make them faster and more efficient.

We aim to employ the Chat for all use cases and workflows that can benefit from a conversational interaction between a user and an AI that is driven by a large language model (LLM). Typically, these are:
- Complex creation and learning tasks that are more effectively and more efficiently solved through iteration than through a one-shot interaction.
- Tasks that are typically satisfiable with one-shot interactions but that might need refinement or could turn into a conversation.
- Among the latter are tasks where the AI may not get it right the first time but where users can easily course correct by telling the AI more precisely what they need. For instance, "Explain this code" is a common question that most of the time would result in a satisfying answer, but sometimes the user will have additional questions.
- Tasks that benefit from the history of a conversation, so neither the user nor the AI need to repeat themselves.

The Chat shall be context aware and ultimately have access to all the resources in GitLab that the user has access to. Initially, this context is limited to code files, code selections, the content of individual issues and epics, as well as the GitLab documentation.

To scale the context awareness and the supported use cases across the entire DevSecOps domain, Duo Chat aims to be a platform, that other GitLab teams and the wider community can contribute to. They are the experts for the use cases and workflows to accelerate.

### 1 year plan
<!--
1 year plan for what we will be working on linked to up-to-date epics. This section will be most similar to a "roadmap". Items in this section should be linked to issues or epics that are up to date. Indicate relative priority of initiatives in this section so that the audience understands the sequence in which you intend to work on them.
 -->

Over the next 12 months, we will focus on the following prioritized themes, which represent broad categories of user needs that evolve as the market and our product mature. While these themes may extend beyond the 12-month horizon, we will continuously iterate and deliver improvements within each theme:

- Support use cases that require automatically fetching relevant content. The initial use case is [chatting with your code base](https://gitlab.com/groups/gitlab-org/-/epics/16910).
- Enabling custom rules that applied for every conversation starting with supporting [custom style guides for Duo Chat](https://gitlab.com/gitlab-org/gitlab/-/issues/481841).
- Support use cases that require access to multiple GitLab resources starting with [enabling the planner persona to create status updates for work items in Duo Chat](https://gitlab.com/groups/gitlab-org/-/epics/16695).

#### What is next for us
<!-- This is a 3 month look ahead for the next iteration that you have planned for the category. This section must provide links to issues or
or to [epics](https://handbook.gitlab.com/handbook/product/product-processes/#epics-for-a-single-iteration) that are scoped to a single iteration. Please do not link to epics encompass a vision that is a longer horizon and don't lay out an iteration plan. -->
- [Provide means for users to add context to their chat conversations](https://gitlab.com/groups/gitlab-org/-/epics/15181)
- [Observability and Stability initiative for Duo Chat](https://gitlab.com/groups/gitlab-org/-/epics/16125)
- [Multi-threaded conversations in the chat](https://gitlab.com/groups/gitlab-org/-/epics/11449)
- [Evaluate the quality of answers to follow-up questions and potentially improve the experience with conversations](https://gitlab.com/groups/gitlab-org/modelops/ai-model-validation-and-research/ai-evaluation/-/epics/33)

#### What we are currently working on
<!-- Scoped to the current month. This section can contain the items that you choose to highlight on the kickoff call. Only link to issues, not Epics.  -->
- [Planning issue for GitLab Duo Chat 17.10](https://gitlab.com/gitlab-org/ai-powered/duo-chat/planning/-/issues/11)

#### What we recently completed
<!-- Lookback limited to 3 months. Link to the relevant issues or release post items. -->
- [Add project files to Duo Chat in VS Code and JetBrains IDEs](https://gitlab.com/groups/gitlab-org/-/epics/15183) (rolled out to .com; expected (but not committed) to be released in 17.10)
- [Chat can be resized in the GitLab UI to help users interact with chat and page content at the same time](https://gitlab.com/gitlab-org/gitlab/-/issues/499849) (rolled out to .com; expected (but not committed) to be released in 17.10)
- [New /help command in GitLab Duo Chat](https://gitlab.com/gitlab-org/gitlab/-/issues/462122)  (17.7)
- [Slash commands picker in GitLab UI shows relevant commands only depending on the page](https://gitlab.com/groups/gitlab-org/-/epics/15371)  (17.7)
- [Use self-hosted model for GitLab Duo Chat](https://gitlab.com/gitlab-org/gitlab/-/issues/501267) (17.6)
- [Have a conversation with GitLab Duo Chat about your pipeline job](https://gitlab.com/gitlab-org/gitlab/-/issues/468461) (17.6)
- [Have a conversation with GitLab Duo Chat about your commit](https://gitlab.com/gitlab-org/gitlab/-/issues/468460) (17.6)
- [AI Impact Analytics API for GitLab Duo Pro including Chat usage](https://gitlab.com/gitlab-org/gitlab/-/issues/498497#release-notes) (17.6)
- [Query user-level GitLab Duo Enterprise usage metrics including Chat usage](https://gitlab.com/gitlab-org/gitlab/-/issues/483049#release-notes) (17.6)
- [Have a conversation with GitLab Duo Chat about your merge request](https://gitlab.com/gitlab-org/gitlab/-/issues/464587) (17.5)
- [Duo Quick Chat: operates directly on the lines you’re editing](https://gitlab.com/groups/gitlab-org/-/epics/15218) (17.5)
- [Summarize issue discussions with GitLab Duo Chat](https://gitlab.com/gitlab-org/gitlab/-/issues/454550) (17.4)
- [Troubleshoot failed jobs with root cause analysis](https://gitlab.com/groups/gitlab-org/-/epics/13080) (17.3)
- [Gitlab Duo (including Duo Chat) disabling input and output logging by default](https://about.gitlab.com/releases/2024/07/18/gitlab-17-2-released/#gitlab-duo-disabling-input-and-output-logging-by-default) (17.2)
- [Vulnerability Explanation](https://gitlab.com/groups/gitlab-org/-/epics/10642) (17.2)
- [GitLab Duo Chat and Code Suggestions available in workspaces](https://gitlab.com/groups/gitlab-org/-/epics/12780) (17.2)
- [Moving chat from Anthropic Claude Sonnet 3 to 3.5](https://gitlab.com/gitlab-org/gitlab/-/issues/468936) (17.2)
- [Moving chat from Anthropic Claude 2.1 to Claude Sonnet 3](https://gitlab.com/gitlab-org/gitlab/-/issues/444629) (17.0)
- [How-to questions in GitLab Duo Chat supported on self-managed deployments](https://gitlab.com/gitlab-org/gitlab/-/issues/451215) (17.0)
- [GitLab Duo Chat GA release](https://gitlab.com/groups/gitlab-org/-/epics/13516) (16.11)
- [GitLab Duo Chat available in JetBrains IDEs](https://gitlab.com/gitlab-org/editor-extensions/gitlab-jetbrains-plugin/-/issues/307) (16.11)

#### What is Not Planned Right Now
<!--  Often it's just as important to talk about what you're not doing as it is to
discuss what you are. This section should include items that people might hope or think
we are working on as part of the category, but aren't, and it should help them understand why that's the case.
Also, thinking through these items can often help you catch something that you should
in fact do. We should limit this to a few items that are at a high enough level so
someone with not a lot of detailed information about the product can understand -->
 More details soon.

### Best in Class Landscape
<!-- Blanket description consistent across all pages that clarifies what GitLab means when we say "best in class" -->

<!-- BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape. -->
Details coming soon.

#### Key Capabilities
<!-- For this product area, these are the capabilities a best-in-class solution should provide -->
Details coming soon.

#### Roadmap
<!-- Key deliverables we're focusing on to build a BIC solution. List the epics by title and link to the epic in GitLab. Minimize additional description here so that the epics can remain the SSOT. This may be duplicative to the 1 year section however for some categories the key deliverables required to become the BIC solution will extend beyond one year and we want to capture all of the gaps. Moreover, the 1 year section may contain work that is not directly related to closing gaps if we are already the BIC or if we are differentiating ourselves.-->
Details coming soon.

#### Top Competitive Solutions
<!-- PMs can choose to highlight a primary BIC competitor--or more, if no single clear winner in the category exists; in this section we should indicate: 1. name of competitive product, 2. links to marketing website and documentation, 3. why we view them as the primary BIC competitor -->
Competitors in the space include Android Studio Bot, GitHub Copilot Chat, Tabnine Chat, and Sourcegraph Cody AI Assistant.

### Target Audience
<!--
List the personas (https://handbook.gitlab.com/handbook/marketing/strategic-marketing/roles-personas#user-personas) involved in this category.

Look for differences in user's goals or uses that would affect their use of the product. Separate users and customers into different types based on those differences that make a difference.
-->
GitLab Duo Chat aims to support across all there DevSecOps workflows. Therefore, all of GitLab's users are a target audience for the Chat. The initial focus is however on:
  1. [Sasha, Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
  1. [Parker, Product Manager](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)
  1. [Delaney, Development Team Lead](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
  1. [Simone, Software Engineer in Test](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
  1. [Amy, Application Security Engineer](https://handbook.gitlab.com/handbook/product/personas/#amy-application-security-engineer)
  1. [Alex, Security Operations Engineer](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer)

### Pricing and Packaging

Duo Chat is availible as part of both [Duo Pro and Duo Enterprise addons](#). Learn about how different [Duo Chat features are tiered between the Duo addons](#).

### Analyst Landscape
Details coming soon.
