---
layout: sec_direction
title: "Product Section Direction - Dev"
description: "The Dev Section is made up of the Manage, Plan, and Create stages of the DevOps lifecycle and encompasses a number of analyst categories"
canonical_path: "/direction/dev/"
---

- TOC
{:toc}

Last Reviewed: 2023-2-22



## Dev Section Overview

The Dev Section is made up of the [Plan](https://handbook.gitlab.com/handbook/product/categories/#plan-stage) and [Create](https://handbook.gitlab.com/handbook/product/categories/#create-stage) stages of the DevOps lifecycle. The scope for the Dev section is wide and encompasses a number of analyst categories including [Value Stream Management (VSM)](/solutions/value-stream-management/), Project Portfolio Management (PPM), Enterprise Agile Planning Tools (EAP), Source Code Management (SCM), Integrated Development Environments (IDEs) and Design Management. It is difficult to truly estimate Total Available Market (TAMkt) for the Dev Section, as our scope includes so many components from various industries, but market research from the analyst firm [IDC](https://www.idc.com/about) indicates the estimated [TAM](https://docs.google.com/spreadsheets/d/1LO57cmXHDjE4QRf6NscRilpYA1mlXHeLFwM_tWlzcwI/edit?ts=5ddb7489#gid=1474156035) in 2022 was roughly ~$4.1B, growing to ~$7.6B in 2026 (13.14% CAGR). Analysis: [Manage](https://docs.google.com/spreadsheets/d/1357Zwbf0yTjcFBuCdX2HnNLBaF9uWnW7Auv4F94aoSo/edit#gid=1753604861), [Plan](https://docs.google.com/spreadsheets/d/1dDNSR_mE4peeOc_3Xhqm_VLoTyk4gSbcbiGfuMrOg6g/edit#gid=982966394) and [Create](https://docs.google.com/spreadsheets/d/1KSwTVPIvMO8IXkMqA40Ms1rL-glmo-w7MjZvUrjMFGA/edit#gid=697056429).
Nearly [half of organizations](https://drive.google.com/file/d/17ZSI2hGg3RK168KHktFOiyyzRA93uMbd/view?usp=sharing) still have not adopted DevOps methodologies, despite [data](https://drive.google.com/file/d/17MNecg84AepxWlSDB5HjNBrCJggaS9tP/view?usp=sharing) that indicates far higher revenue growth for organizations that do so. Migrating a code base to a modern, Git-backed source control platform like GitLab can often be the first step in a DevOps transformation. As such, we must provide industry-leading solutions in source code and code review, as this is not only the entry into DevOps for our customers, but typically the entry into the GitLab platform. Once a user has begun utilizing repositories and code review features like Merge Requests, they often shift “left” and “right” to explore and utilize other capabilities in GitLab, such as CI and project management features.

Per our [Stage Monthly Active User data](https://internal.gitlab.com/handbook/company/performance-indicators/product/#stage-monthly-active-users-smau) (internal access only), we know that Create and Manage have the highest usage amongst GitLab stages. As such, these stages must focus on security fixes, bug fixes, performance improvements, UX improvements, and depth more than other areas of GitLab.

### Accomplishments, News, and Updates

The following are the updates from the Dev Section for December 2022 (as presented in the monthly
[Product Key Review](https://handbook.gitlab.com/handbook/key-review/)). A complete list of released features
can be found on the [Release Feature Overview](https://gitlab-com.gitlab.io/cs-tools/gitlab-cs-tools/what-is-new-since/?tab=features&selectedStages=create&selectedStages=manage&selectedStages=plan)
page and a complete list of upcoming features can be found on the [Upcoming Releases](https://about.gitlab.com/upcoming-releases/) page.

#### Section News & Team Member Updates

* The Organization group has been consolidated with the Pods group and moved to the Enablement section
* The Import & Integration groups have been merged together
* The Knowledge group that owns Wiki, Pages & content editor has moved from the Create stage to the Plan stage
* Plan:Optimize - Exec Dashboard: Beta - Beta program to validate and test the design, performance, and MVC readiness with real customers data.
* Manage:Personal productivity - Navigation Left side bar Experiment [Your work sidebar](https://about.gitlab.com/releases/2023/02/22/gitlab-15-9-released/#your-work-sidebar)
* Manage:Auth - [Users with the Guest role can view private repositories](https://about.gitlab.com/releases/2023/02/22/gitlab-15-9-released/#users-with-the-guest-role-can-view-private-repositories
* Create:Source Code - Improving Forking experience: [Fetch new upstream contents when fork is behind](https://gitlab.com/gitlab-org/gitlab/-/issues/330243)
* Create:Source Code [Require multiple approvals from Code Owners](https://about.gitlab.com/releases/2023/02/22/gitlab-15-9-released/#require-multiple-approvals-from-code-owners)
* Manage:Integrations - [Notifications now available in the GitLab for Slack app](https://about.gitlab.com/releases/2023/02/22/gitlab-15-9-released/#notifications-now-available-in-the-gitlab-for-slack-app)
* Create:Source Code - [Allow multiple approvals per CODEOWNER](https://gitlab.com/gitlab-org/gitlab/-/issues/335451)

#### Important PI Highlights

* Plan: Project Management - Congrats on a recorded MoM Paid new all time high!
* Plan::Optimiae - Congratulations on reaching an all time high MAU.
* Create Stage - Congratulations for reaching an all time high for SMAU & Paid SMAU!
* Create:: Congrats on reaching an all time high for VS Code extension, continuing to see steady adoption!

#### Recent Accomplishments

* [Migrating GitLab projects by direct transfer Beta](https://about.gitlab.com/releases/2023/01/22/gitlab-15-8-released/#migrating-gitlab-projects-by-direct-transfer-beta)
* [SCIM support for self-managed GitLab](https://about.gitlab.com/releases/2023/01/22/gitlab-15-8-released/#scim-support-for-self-managed-gitlab)
* [Selective SSO enforcement for group members](https://about.gitlab.com/releases/2023/01/22/gitlab-15-8-released/#selective-sso-enforcement-for-group-members)
* [GitLab CLI](https://about.gitlab.com/releases/2022/12/22/gitlab-15-7-released/#introducing-the-gitlab-cli)
* [Sign commits with your SSH key](https://about.gitlab.com/releases/2022/12/22/gitlab-15-7-released/#sign-commits-with-your-ssh-key)
* [Web IDE & Workspaces Beta](https://about.gitlab.com/releases/2022/12/22/gitlab-15-7-released/#experience-the-web-ide-beta-and-workspaces)
* [Self-managed support for the GitLab for Jira Cloud app](https://about.gitlab.com/releases/2022/12/22/gitlab-15-7-released/#self-managed-support-for-the-gitlab-for-jira-cloud-app)
* [Autocomplete suggestions in the Content Editor](https://about.gitlab.com/releases/2022/10/22/gitlab-15-5-released/#autocomplete-suggestions-in-the-content-editor)
* [Email notification when two-factor OTP attempt is wrong](https://about.gitlab.com/releases/2022/10/22/gitlab-15-5-released/#email-notification-when-two-factor-otp-attempt-is-wrong)
* [Add labels and dates to a task](https://about.gitlab.com/releases/2022/10/22/gitlab-15-5-released/#add-labels-and-dates-to-a-task)

#### What's Ahead

* [Jira Cloud App proxy for Self-managed GitLab users](https://gitlab.com/groups/gitlab-org/-/epics/5650)
* [API Support for user management - Max role](https://gitlab.com/gitlab-org/gitlab/-/issues/354749)
* [Create a custom source control module for VS Code](https://gitlab.com/groups/gitlab-org/-/epics/7684)
* [Highlight source code syntax on the frontend using HighlightJS](https://gitlab.com/groups/gitlab-org/-/epics/7146)
* [Enterprise Users - MVC: Claim management of existing users](https://gitlab.com/groups/gitlab-org/-/epics/9675)
* [Pages internal API caching](https://gitlab.com/groups/gitlab-org/-/epics/7920)
* [MVC: Branch Rules Overview](https://gitlab.com/groups/gitlab-org/-/epics/8578#release-post)
* [Restructure merge requests](https://gitlab.com/groups/gitlab-org/-/epics/5038)
* [Real-time merge request updates](https://gitlab.com/groups/gitlab-org/-/epics/1812)
* [Allow users to delete comments that they authored within Design Management](https://gitlab.com/gitlab-org/gitlab/-/issues/385100)
* [Consolidate Value Stream Analytics Group & Project into a single workspace](https://gitlab.com/gitlab-org/gitlab/-/issues/382496)
* [Fetch new upstream contents when fork is behind](https://gitlab.com/gitlab-org/gitlab/-/issues/330243)
* [Adding emoji reactions to work items](https://gitlab.com/gitlab-org/gitlab/-/issues/389967)
* [New exploration sidebar where users can go and discover various things within GitLab](https://gitlab.com/gitlab-org/gitlab/-/issues/384879)
* [Enterprise Users Badging](https://gitlab.com/gitlab-org/gitlab/-/issues/372895)

## Dev Section FY24 Themes

The primary [themes](https://about.gitlab.com/direction/#fy24-product-investment-themes) for the Product department in FY24 are:

1. [World-class DevSecOps experience](https://about.gitlab.com/direction/#world-class-devsecops-experience)
1. [Advanced security and compliance](https://about.gitlab.com/direction/#advanced-security-and-compliance)
1. [Observability, analytics, & feedback](https://about.gitlab.com/direction/#observability-analytics--feedback)
1. [GitLab for Data Science](https://about.gitlab.com/direction/#gitlab-for-data-science)

The Dev Section will primarily focus on [World-class DevSecOps experience](https://about.gitlab.com/direction/#world-class-devsecops-experience) which also includes improving our user experieince and better support for our Enterprise users.

#### World-class DevSecOps experience]

The Dev Section has the highest TMAU of all sections. Because of this, the Dev section will be highly focused on creating a lovable experience for several core workflows throughout the product. We'll also be focused on product architecture improvements, like simplifying groups/projects, which will enable efficiency gains of GitLab product teams as well as an easier to understand user experience for new users of GitLab. Here are the jobs to be done the Dev section will focus on to improve adoption through usability:

1. Easily understand how to set up and manage my organization and projects in GitLab - solved for via [groups and projects moving to namespaces](https://gitlab.com/groups/gitlab-org/-/epics/2885)
1. Easily find exactly what I'm looking for in GitLab - solved for via [improving settings and navigation](https://gitlab.com/groups/gitlab-org/-/epics/4831)
1. Provide an out of the box experience that requires little to no configuration - solved for via enabling all possible Dev section features to be [working by default](https://handbook.gitlab.com/handbook/product/product-principles/#configuration-principles)
1. Ensure I'm always looking at the most up to date information - solved for by focusing on realtime experiences
1. Conduct an efficient code review - solved for via code review usability improvements and MR reviewers
1. Easily manage my portfolio - solved for by work items, epic boards, roadmap improvements, and workflow automation
1. Reduce my development cycle time and time managing local environments - solved for by investing in Workspaces tools
1. Feature parity between groups and projects
1. New Navigation flow

#### Advanced security and compliance

The Dev section will be focused on providing a more secure development experience.

1. [Customizable Roles and Permisisons](https://gitlab.com/groups/gitlab-org/-/epics/4035)

#### Observability, analytics, & feedback

The Dev section will be creating a better holistic experience that ties the entire SDLC together connecting planning, source code, deployment and more. This will allow a unique view into the Software Delivery process, allowing you to tie OKRs and other business metrics into you feature development. This will also allow you to identify bottle necks as well as allow team to experiment with different processes to find what boosts their productivity and allow them to practice continuous improvement. DORA4 metrics will help create observability into deployments and production stability. Custom analytics reports will allow to tailor different views for different users of the platform.

1. Executive dashboards and Value Stream Analytics

### GitLab for Data Science

* AI assisted code suggestions

#### Stage focus

Within each stage, the listed items below are in **order of priority**. The top priority for each stage or group is:

* Manage: [Slack Integration](https://gitlab.com/groups/gitlab-org/-/epics/7536)
* Manage: [Customizable Roles & Permissions](https://gitlab.com/groups/gitlab-org/-/epics/4035)
* Plan: [Work Items](https://gitlab.com/groups/gitlab-org/-/epics/6033)
* Plan: [Support OKRs in GitLab](https://gitlab.com/groups/gitlab-org/-/epics/7864)
* Plan: [Value Streams Dashboard for Executive](https://gitlab.com/groups/gitlab-org/-/epics/8335)
* Create: [Workspaces](https://gitlab.com/groups/gitlab-org/-/epics/7948)
* Create: [Branch Rules Overview](https://gitlab.com/groups/gitlab-org/-/epics/8578#release-post)

## Who is the Dev section targeting?

We identify the [personas](https://handbook.gitlab.com/handbook/product/personas/#user-personas) the Dev section features are built for. In order to be transparent about personas we support today and personas we aim to support in the future we use the following categorization of personas listed in priority order.
* 🟩- Targeted with strong support
* 🟨- Targeted but incomplete support
* ⬜️- Not targeted but might find value

### Today
To capitalize on the [opportunities](#opportunities) listed above, the Dev section has features that make it useful to the following personas today.

* 🟩 [Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
* 🟩 [Devon - DevOps Engineer](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
* 🟩 [Delaney - Development Team Lead](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
* 🟩 [Parker - Product Manager](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)
* 🟩 [Cameron - Compliance Manager](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)
* 🟨 [Sam - Security Analyst](https://handbook.gitlab.com/handbook/product/personas/#sam-security-analyst)
* 🟨 [Presley - Product Designer](https://handbook.gitlab.com/handbook/product/personas/#presley-product-designer)
* 🟨 [Rachel - Release Manager](https://handbook.gitlab.com/handbook/product/personas/#rachel-release-manager)
* 🟨 [Simone - Software Engineer in Test](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
* 🟨 [Allison - Application Ops](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops)
* 🟨 [Priyanka - Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
* 🟨 [Sidney - Systems Administrator](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)

### Medium Term (1-2 years)
As we execute our [3-year strategy](#3-year-strategy), our medium term (1-2 year) goal is to provide a single application that enables collaboration between cloud native development and platform teams.

* 🟩 [Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
* 🟩 [Devon - DevOps Engineer](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
* 🟩 [Delaney - Development Team Lead](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
* 🟩 [Parker - Product Manager](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)
* 🟩 [Presley - Product Designer](https://handbook.gitlab.com/handbook/product/personas/#presley-product-designer)
* 🟩 [Cameron - Compliance Manager](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)
* 🟩 [Simone - Software Engineer in Test](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
* 🟨 [Rachel - Release Manager](https://handbook.gitlab.com/handbook/product/personas/#rachel-release-manager)
* 🟨 [Allison - Application Ops](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops)
* 🟨 [Priyanka - Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
* 🟨 [Sidney - Systems Administrator](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)

## 3 Year Strategy

In three years, the Dev Section market will:

* Centralize around Git as the version control of choice for design assets, gaming, silicon designs, and AI/ML models.
* Have a market leader emerge in the value stream management space. Currently, the market is fragmented with most players focused on integrations into various DevOps tools.
* Adopt a mindset shift from project management to product management.
* Recognize the value of a single platform for all software creation activities, including product management.
* See an uptick in startups, applications, and internal business logic being built on the backs of low or no-code platforms, which will give rise to the [citizen developer](https://www.gartner.com/en/information-technology/glossary/citizen-developer)
* See an increase in developer tools built on AI technology aimed at increasing efficiency, productivity, and security in code via automatic recommendations offered in-line in code editors
* Coalesce around the notion of a single platform for DevOps, also known as Value Stream Delivery Platforms.

As a result, in three years, GitLab will:

* Provide a next-generation, highly performant Git-backed version control system for large assets, such as ML models. Our goal in three years should be to host the most repositories of these non-code assets.
* Emerge as the leader in VSM and be recognized in the industry by customers and analysts as such. Our goal in three years should be to provide the best insights into the product development process that no other tool can come close to, as we have a [unified data model](https://www.ca.com/en/blog-itom/what-is-a-unified-data-model-and-why-would-you-use-it.html) due to GitLab being a single platform.
* Develop an industry-leading product management platform where multiple features and products can be measured and managed easily.
* Provide an exellent developer experience via a robust Web IDE, browser-based IDE, support for the citizen developer via a low-code offering, and features that offer AI assistance to developers
* Ensure we are the best VSDP on the market.

## 3 Year Themes

Our direction for the Dev section is to provide the world’s best product creation and management platform.
We believe we have a massive opportunity to change how cross-functional, multi-level teams collaborate by
providng a solution that breaks down organizational silos and enables maximum value delivery.
We want to provide a solution that enables higher-quality products to be quickly iterated upon. We also want to make it effortless for companies to migrate to GitLab. In order to obtain adoption from incumbent tools, GitLab has to provide *substantially more value*
than our competitors, but do so by maintaining simplicity. The following themes listed below represent how we believe we will deliver this value
and is our view of what will be important to the market and to GitLab over the next 3 to 5 years. As such,
they will be the cornerstone of our 3-year strategy, and all activities in the 1-year plan should advance
GitLab in one or more of these areas.

### Efficient and Automated Code Review

Code review should be a delightful experience for all involved in the process. Over time, we expect the code review process to evolve from where it is today to become a more automated process in the future. Along the way, incremental improvements will occur, where developer platforms like GitLab will focus on performance and usability of the code review tools. Code review should be an efficient process, and the easier GitLab can make code review, the more efficient dev teams become. [Research](https://blog.semmle.com/code-review-metrics/) has shown that better code review should reduce the number of bugs and increase the amount of higher-quality features an organization can ship. The code review process will continue to provide a venue for developers to learn and collaborate together.

As examples, GitLab will:

* Load large, multi-file diffs faster than any other comparable product on the market.
* Provide tailored insights to the code reviewer, alerting them to the most important areas to review.
* Provide ways to reduce the wait time in the code review process.
* Make the experience when browsing multi-file diffs delightful for the code reviewer.
* Provide a code review experience inside of VS Code to help devs stay in flow.


### Measurement and Increased Efficiency of the Value Stream

Peter Drucker has stated “If you can’t measure it, you can’t improve it.” Many software development teams have no way of measuring their efficiency, and even if they do, there is not enough feedback, information, or actionable insights to improve the efficiency of their team. Even then, once efficiency is improved, it can be difficult to tell if a team’s performance is good or bad, as there is often no point of comparison. Even the best performing team in an organization could be worse than the competition. Increasing efficiency is paramount to companies increasing their **time to value** and helping organizations answer **“Is my DevOps transformation working?”**

We believe efficiency can be improved in two ways. The first way is to reduce cycle times for existing value stream activities. The second is to question and optimize the value stream into higher value-added activities at each step. GitLab’s vision is to help answer both of these questions: “Am I doing things fast enough?” and “Am I doing the right things?” These two questions are intertwined because the faster an organization can ship, the quicker feedback will come in from users, creating a virtuous cycle of shipping things quickly as well as ensuring the things shipped are the right things.

Today, value stream management is largely focused on visualizing the value chain through deployment. GitLab is uniquely positioned to also visualize, track, and measure value chain activities from the strategic initiative level all the way to captured value from an organization's customer. For example, the value created by post launch activities, such as press releases, blog posts, marketing campaigns, and customer engagement should funnel into value stream management; providing the business with insights and data to continuously improve each step of their value chain.

The market for value stream tools has begun to bifurcate into value stream delivery platforms and value stream management platforms. GitLab can solve for both of the use cases of these markets. In order to become a more successful VSMP platform, we'll need to ensure that we provide support for calculating VSM metrics on 3rd party tools, for example, Jira issues.

As examples, GitLab will provide:

* Easy-to-use and customizable tools that measure the efficiency of the DevOps lifecycle.
* Insight into areas of waste where teams can improve.
* Recommendations based on large data sets of other teams using GitLab for comparison.
* A visual experience for value stream management that goes beyond code deployment.
* Provide VSM flow metric calculations based on 3rd party tools/integrations.


### DevOps for More Personas

DevOps started with the merging of Development and Operations and has since been augmented to include Security, highlighting DevSecOps as the next trend. There are many other personas that are involved in software development, such as product managers, project managers, product designers, finance, marketing, legal, procurement, etc. These personas will continue to expand until nearly every role at knowledge-work companies touches some facet of the DevOps lifecycle. Over time, organizations will realize that teams who work out of the same platform/set of tools are more efficient and deliver faster business and customer value.

Because of this trend, each persona of the DevOps lifecycle should ultimately be treated as a first-class citizen in GitLab. 

As examples, GitLab will provide:

* A better experience for project management workflows.
* A space for product designers to design and collaborate on designs with product managers and engineers.
* Financial reporting for things like resource allocation, capacity planning, and P & L analysis.  


### Enterprise Compliance

Most enterprise customers have custom requirements that need to be implemented inside of GitLab. Examples of these are controls that spans systems such as permissions, approvals, compliance, governance, workflows, and requirements mapping. It is our belief these needs will exist for many years to come, and we will need to incorporate these to truly become a complete DevOps platform that serves enterprise segments. We will strive to do this in ways that are modern and, where possible, adhere to a [“convention over configuration”](https://handbook.gitlab.com/handbook/product/product-principles/#convention-over-configuration) approach.

Additionally, compliance, auditing, and surfacing evidence of security/compliance posture to auditors will become more important as more GDPR-like legislation is enacted and passed into law. GitLab should make it easy to not only surface and deliver evidence for GitLab controls (i.e. who has access to GitLab, who did what on what group, etc.), but also to track and manage compliance requirements for various legislation our customers may be bound to for the applications they create inside of GitLab.

As examples, GitLab will provide:

* Customizable workflows and checkpoints, unlocking enforcement, approvals, and insight into these workflows.
* More customizable and fine-grained permissions.
* Logs for everything that happens within GitLab and allow those events to be accessible via the API and UI.
* Alerting on GitLab audit events.
* Providing a great requirements and quality management experience.
* Deliver chain of custody reporting.
* Provide simple compliance reporting and dashboarding views.


### Project to Product

Product Managers often struggle with answering the question, "Is the product or feature I just launched successful?" There are many sensing mechanisms to help answer this question, including revenue, users, customer feedback, NPS, etc., but no product currently helps product managers exhaustively manage the product development lifecycle from end-to-end. Many products assist with planning, delivery of code, and deployment, but feedback and iteration are equally as important to product managers as shipping the first iteration. Getting the first iteration out is traditionally celebrated, but is only one of many steps to true product development lifecycle management.

Imagine an experience where product managers can log in and view the "health" of their entire portfolio on one dashboard. It is clear which features have the most value to customers (and by extension to the business) as measured by key metrics, assisting PMs with priortization activities. PMs can quickly identify features or products within their portfolio that need more attention and drill into them, identifying the correct next action to take, whether it's iteration on the feature or perhaps sunsetting it. PMs can quickly create an issue for the next iteration, version control features, view security incidents, respond to customer feedback, drill down into analytics, control A/B tests of the feature, and even interact with users of the feature or product directly by creating ad-hoc surveys or questions for users to answer. Additionally, the experience should allow for ROI analysis and tracking of the ROI after capital has been expended.

Within three years, project management tools will begin evolving to provide this experience and help PMs answer tough product questions. These tools will also assist with measuring and predicting value to the organization before a feature is prioritized by the PM. The ideal solution most likely uses data science, natural language processing (NPL), machine learning, and predictive analytics to assist product managers with decisions both before and after a feature is launched.

As examples, by integrating with GitLab's [Analytics](/direction/analytics/) and [Plan](/direction/plan/) capabilities GitLab will provide:

* Feature management capabilities, including the ability to link a feature to a specific point in the user's journey. These live on after an issue is closed and contain rich meta-data about user interactions, business KPIs, and the value exchange system.
* An experience where PMs can quickly analyze the health of all relevant features.
* A framework that helps PMs with prioritization decisions.
* A framework for ROI analysis and measurement.


### Workspaces

Local dev environments can be tricky to set up and often require hours to troubleshoot to set up development kits. Even when successfully configured, the "works on my machine" problem can arise as there are likely many differences between production and local environments.

We believe Workspaces will become a more popular development paradigm over the next few years and will manifest itself in this way: devs will code in places they are comfortable, such as local IDEs and will run code in Kubernetes environments that their IDE is connected to. [Okteto](https://okteto.com/) is an interesting tool that is solving for this right now.

GitLab is uniquely positioned to serve Workspaces as a remote environment as we have a tight integration with Kubernetes as well as a VSCode Plugin in addition to an in-app editing experience in our Web IDE.

As examples, GitLab will provide:

* Workspaces environments powered by Kubernetes
* Workspaces environments that can be connected to a local VSCode editor
* Workspaces environments that can be connected to the Web IDE or a GitLab project



### User Management for Enterprises

Enterprise customers on Gitlab.com want to be able to fully manage the entire lifecycle of users in their groups. This desire is for efficiency, increased security protocols, and to protect their intellectual property. Typically, these customers will have centralized user management for their enterprise through an IdP like Okta or Azure and use GitLab SSO/SCIM.

We will provide group maintainers administrative control over users whose e-mail address matches a domain that they have proved ownership for. Today, any user provisioned through SCIM and/or an IdP are automatically Enterprise Users. The user claim process allows group owners to find any users that use their company e-mail address but have opened their accounts outside of the provisioning process, and exert ownership over them. 

Once users are Enterprise Users, we will provide enhanced management to group owners, for example:

- Enterprise Users do not have to validate their e-mail addresses
- Disable passworth Auth - Enterprise Users can sign in via IdP only
- Ability to block inviting users from outside the organization
- Prevent users from changing or adding e-mail addresses
- Policies for credential rotation for any user within the enterprise
- Ability for group owner impersonate enterprise user
- Login settings (Password Complexity, Auto log out, two factor authentication and more)


## 1 Year Plan: What’s Next for Dev

Please see the [categories page](https://handbook.gitlab.com/handbook/product/categories/#dev-section) for a more detailed look at Dev's plan by exploring `Direction` links in areas of interest. This page will highight direction themes for both one year and three year timelines.

### Import and Integrate

In 2024, we are focused on two main areas:

- Bringing [project migration by direct transfer](https://docs.gitlab.com/ee/user/group/import/index.html#migrated-project-items-beta) to [general availability](https://docs.gitlab.com/ee/policy/experiment-beta-support.html#generally-available-ga), so that we offer production-quality, easy to use tool for migrating GitLab resources between instances of GitLab. It should gracefully recover from errors and import over nearly 100% of relevant objects.

Ability to migrate projects by direct transfer was released as Beta (available to everyone) [in GitLab 15.8](https://about.gitlab.com/blog/2023/01/18/try-out-new-way-to-migrate-projects/).

- Improving high-priority Integrations, Atlassian Jira and Slack in order to reach Complete [maturity level](../../../../maturity).


### Personal productivity


Note, at GitLab we plan aggressively and we can make changes to this at any time!

View screenshot of roadmap - update Aug 11, 2023

![foundations-roadmap-screenshot.png](/direction/foundations/personal_productivity/foundations-roadmap-snapshot.png)

</details>

### Plan

### What's Next For Us

Over the next year, we are focused on the following:

- **[Group issues](https://gitlab.com/groups/gitlab-org/-/epics/12320)**. Issues can be created within groups without depending on a project within the group. This will optionally allow teams to consolidate their planning workflows within a single location instead of spreading them across a group and a project.  
- **[Work items open in a drawer within boards and lists](https://gitlab.com/gitlab-org/gitlab/-/issues/387224)**. Reduce the context switching and tab fatique when drilling down into a work item detail view. 
- **[Customizable work item statuses](https://gitlab.com/gitlab-org/gitlab/-/issues/368290)**. Provide a foundation for building a more robust work item lifecycle management solution, and enable teams to mark work items as done or cancelled. 
- **[Report on iteration velocity and volatility](https://gitlab.com/groups/gitlab-org/-/epics/435)** -- Helps teams have meaningful discussions about trade-offs and estimations when planning upcoming iterations. Issues and tasks can be assigned to iterations, so our next step is [showing parent/child relationships in the iteration report](https://gitlab.com/gitlab-org/gitlab/-/issues/457538), followed by [displaying velocity and volatility](https://gitlab.com/gitlab-org/gitlab/-/issues/457094). 
- **[Work items are natively supported within Groups](https://gitlab.com/groups/gitlab-org/-/epics/8308)** -- Eliminate the need to maintain projects under groups solely for agile planning purposes, allow teams to consolidate their planning activities at the group level, and enable issues and epics to be migrated to work items. We're currently working on [the remaining blockers](https://gitlab.com/gitlab-org/gitlab/-/issues/458986) to feature parity between legacy issues and work item issues. Once issues are migrated to work items, we will be able to turn on native Group Issues. 

- **Surface additional AI Impact Analytics metrics to help customers better understand the impact and ROI for using GitLab Duo Pro and Duo Enterpise** -- In addition to metrics for code suggestions and chat, we will provide insight into productivity gains from:
  - Adoption of [pipeline root cause analysis](https://gitlab.com/groups/gitlab-org/-/epics/15025).
  - Adoption of [vulnerability explanation/resolution](https://gitlab.com/groups/gitlab-org/-/epics/15024).
  - Adding [AI vs. Non-AI Cohort Analysis](https://gitlab.com/groups/gitlab-org/-/epics/15906).
  - Adding insight into ["language usage" of Code Suggestions](https://gitlab.com/gitlab-org/gitlab/-/issues/454809). 
  - Working on an update [UX vision for AI adoption dashboard](https://gitlab.com/gitlab-org/gitlab/-/issues/505532). 
- Mature [Value Streams Dashboard for Executives](https://gitlab.com/groups/gitlab-org/-/epics/9317) to enable decision-makers to identify trends, patterns, and opportunities for digital transformation improvements.In the next 1-3 milestones, we will focus on the following: 
  - [Consolidate Group::Optimize dashboards](https://gitlab.com/groups/gitlab-org/-/epics/13801) into the [Cross-stage Dashboards framework](https://gitlab.com/groups/gitlab-org/-/epics/13801). With the new framework, customers can visualize their DevSecOps data using built-in dashboards provided by GitLab or by creating custom dashboards with custom visualizations.
  - [Customizable widgets](https://gitlab.com/groups/gitlab-org/-/epics/8925) to show data that is relevant to user's goals and needs. Adding the ["Platform Insights" customizable UI capabilities](https://gitlab.com/groups/gitlab-org/-/epics/8925). Integrate the Value streams dashboard page into the [Platform Insights schema driven UI](https://docs.gitlab.com/ee/user/analytics/analytics_dashboards.html).
- Adding [VSA settings](https://gitlab.com/groups/gitlab-org/-/epics/9129) with label filters configuration. In a similar way to boards, teams want to use saved filtered labels with value streams.


- Moving DORA charts from the [CI/CD Analytics into the new dashboarding framework](https://gitlab.com/groups/gitlab-org/-/epics/16117)
- **Add a new [Dashboard for Executive](https://gitlab.com/groups/gitlab-org/-/epics/9317)** to enable decision-makers to identify trends, patterns, and opportunities for digital transformation improvements. In the next phases, we will focus on the following: 
  - Adding a [new DORA Metrics Overview page](https://gitlab.com/-/project/278964/uploads/9def9ff31b9812ad216043a40bdee5f9/DORA_metrics_-_Option_D.png) in the Value Stream Dashboard. This is related to https://gitlab.com/gitlab-org/gitlab/-/issues/453958. 
  - Adding a [new DORA Metrics Analytics page](https://gitlab.com/-/project/278964/uploads/11d6be804f65814c8ba9fe049338d4cc/DORA_metrics_-_Option_E.png) in the Value Stream Dashboard. This is related to https://gitlab.com/gitlab-org/gitlab/-/issues/453958. 
  - Adding [Custom Metrics Calculation Rules](https://gitlab.com/groups/gitlab-org/-/epics/11490) for DORA, to [support multiple environment branches](https://gitlab.com/gitlab-org/gitlab/-/issues/358385) (with GitLab flow), and [improve the metric calculation](https://gitlab.com/gitlab-org/gitlab/-/issues/444295) to effectively track incidents and deployments.
  - [Move DORA metrics to ClickHouse](https://gitlab.com/gitlab-org/gitlab/-/issues/451752) to provide best experience and robust indicators for measuring the metrics.
  - Adding the Fifth DORA Metric - [Reliability - Operational performance](https://gitlab.com/gitlab-org/gitlab/-/issues/393003)

- Enhancing our ability to [visualize data](https://gitlab.com/groups/gitlab-org/-/epics/5516) by providing a singular hub for accessing and presenting information, adaptable to different visualization preferences.
- Maturing our Wiki to satisfy more [jobs to be done](https://gitlab.com/groups/gitlab-org/-/epics/12826).

### What We're Not Doing

* GitLab will not provide extensive configuration options that complicate collaboration and increase the maintenance burden. Examples are:
   * Blocking users from editing work items due to field-level configuration.
   * Creation of state workflows with transition rules. 
   * Configuring screen field layouts.
* Plan functionality will be generic enough to allow its use by many personas and use cases. However, we will focus on optimizing for use cases for DevSecOps workflows in the immediate future. Our long-term vision is to become the system of record for planning across any function, but we are starting with DevSecOps teams as our target.  Example use cases that we are not focused on include:
   * Marketing
   * HR
   * Legal
   * Service Desk
* In order to meet the vision described in this page, we will decrease investment in our Requirements Management, Test Management, DevOps Reports, Design Management and Time Tracking categories. We will continue to address defects and support community contributions but we are not planning to make significant improvements. 


### Create

### What we recently completed

The Create stage has been actively delivering updates to help your development teams collaborate faster and more effectively. Here are some highlights from recent releases:

- [Workspace extensions now support proposed APIs](https://gitlab.com/gitlab-org/gitlab/-/issues/514741) - Workspace extensions now support enabling proposed APIs, improving compatibility and reliability in production environments. This update allows extensions that depend on proposed APIs to run without errors, including critical development tools like the Python Debugger.
- [Add project files to Duo Chat in VS Code and JetBrains IDEs](https://gitlab.com/groups/gitlab-org/editor-extensions/-/epics/97) - Add your project files directly to Duo Chat in VS Code and JetBrains to unlock more powerful, context-aware AI assistance.
- [Workspaces container support with Sysbox](https://gitlab.com/gitlab-org/gitlab/-/issues/452464) - GitLab workspaces now supports building and running containers directly in your development environment. When your workspace runs on a Kubernetes cluster configured with Sysbox, you can build and run containers without additional configuration.
- [Create workspaces without a custom devfile](https://gitlab.com/groups/gitlab-org/-/epics/14644) - GitLab now provides you with a default file that includes common development tools. This enhancement removes configuration barriers, enables you to create a workspace quickly from any project, includes common development tools pre-configured and ready to use, and lets you focus on development instead of configuration.
- [Use roles to define project members as Code Owners](https://gitlab.com/gitlab-org/gitlab/-/issues/282438) - You can now use roles as Code Owners in your CODEOWNERS file to manage role-based expertise and approvals more efficiently.
- [New `/help` command in GitLab Duo Chat](https://gitlab.com/gitlab-org/gitlab/-/issues/462122) - A new, powerful feature for Duo Chat! Just type /help in the chat message field to explore everything it can do for you.
- [Merge at a scheduled date and time](https://gitlab.com/gitlab-org/gitlab/-/issues/14380) - When you create or edit a merge request you can specify a merge after date. This date will be used to prevent the merge request from being merged until it has passed. Using this new capability with our previously released improvements to auto-merge gives you the flexibility to schedule merge requests to merge in the future.
- [Automated Repository X-Ray](https://gitlab.com/groups/gitlab-org/-/epics/14100) - When a new commit is pushed to the default branch of your project, Repository X-Ray automatically triggers a background job that scans and parses the applicable configuration files in your repository.


### What we are currently working on

- Source Code Management - [Branch rules for squash settings](https://gitlab.com/groups/gitlab-org/-/epics/15327) - This is the next iteration of the larger effort to establish a framework for source code rules. Now that rules are co-located, we are working on enabling the editing of additional settings from that interface.
- Code Review Workflow - [Duo Code Review](https://gitlab.com/groups/gitlab-org/-/epics/13008) and [Improved DevSecOps experience in merge requests](https://gitlab.com/groups/gitlab-org/-/epics/13808)
- GitLab CLI - [Stacked Diffs via the GitLab CLI](https://gitlab.com/groups/gitlab-org/-/epics/12025)
- Workspaces - [Workspaces Settings Configuration Infrastructure in GitLab](https://gitlab.com/groups/gitlab-org/-/epics/14186)
- Web IDE - [Enable the Web IDE Extension Marketplace for Self-managed](https://gitlab.com/groups/gitlab-org/-/epics/11770) and [Hosting the Web IDE on a new domain or subdomain](https://gitlab.com/groups/gitlab-org/-/epics/11972)
- Editor Extensions - [Remote SAST Scanning in VS Code](https://gitlab.com/groups/gitlab-org/-/epics/14984) and [Adding Duo Quick Chat into the Visual Studio extension](https://gitlab.com/groups/gitlab-org/editor-extensions/-/epics/94).

### What is next for us

The Create stage will focus on the following this year: 
- Source Code Management - [Branch rules for Merge Methods](https://gitlab.com/groups/gitlab-org/-/epics/15327)
- Code Review Workflow -  [Duo Code Review](https://gitlab.com/groups/gitlab-org/-/epics/9577)
- GitLab CLI - Expand AI capabilities of glab ask - The GitLab CLI currently supports asking questions about how to accomplish some tasks with the usage of git. We will look for more ways to expand this and potentially leverage GitLab Duo Chat in the future.
- Workspaces - [Support additional editors for workspaces](https://gitlab.com/groups/gitlab-org/-/epics/10635) and [Automatically suspend a workspace after a period of inactivity](https://gitlab.com/groups/gitlab-org/-/epics/10710)
- Web IDE - [Search across all files in a project from within the Web IDE](https://gitlab.com/groups/gitlab-org/-/epics/9466) and [1st Class Editing Experiences for GitLab features](https://gitlab.com/groups/gitlab-org/-/epics/2707)
- Editor Extensions -  [Deepen the integration with the core DevSecOps workflows of GitLab](https://gitlab.com/groups/gitlab-org/-/epics/9679) and [Continue to improve the usability, quality, and maturity of GitLab Duo features](https://gitlab.com/groups/gitlab-org/editor-extensions/-/epics/96)



### Themes that cross all Dev stages
**Performance and availability:** We must invest in the performance, stability, and availability of our application. We will do this by focusing on [application limits](https://gitlab.com/groups/gitlab-org/-/epics/1737), [diff load times](https://gitlab.com/groups/gitlab-org/-/epics/1816), and ensuring [availability](https://handbook.gitlab.com/handbook/product/product-processes/#how-we-prioritize-work) is top of mind.

Growth driver: Retention

### What we're not currently focusing on

Choosing to invest in the above areas in 2022 means we will choose not to:
* Efficiency recommendations: Provide recommendations where customers can improve their efficiency in the DevOps lifecycle. This will likely require comparisons amongst many GitLab users and an AI engine to make intelligent recommendations. We won't be working on features that help companies answer, “Am I doing the right activities?” These improvements will come in years two and three of the VSM plan.
* Feature objects: Creating first class feature objects per the project management morphs into product management block below. While we think this is important, we must spend this year building a better foundation in portfolio management by making our groups/projects structure more simple and delivering epic boards.
* Wikis: Investments in wikis such as WYSIWYG editing or real time collaboration ala Notion.

## Stages & Categories

### Manage

[Learn more about our vision for the Foundations stage](/direction/foundations/). 


### Plan

[Learn more about our vision for the Plan stage](/direction/plan/).


### Create

[Learn more about our vision for the Create stage](/direction/create/).


## What's Next


