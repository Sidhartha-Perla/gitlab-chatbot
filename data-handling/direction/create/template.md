---
layout: markdown_page
title: "Product Stage Vision - Create"
description: "Discover GitLab’s roadmap for creation features, empowering developers with advanced tools for seamless software development and collaboration."
---

## On this page
{:.no_toc}

- TOC
{:toc}

Content last reviewed 2025-03-12



## Stage Overview

The Create stage helps teams accelerate software delivery and reduce cycle times, by improving efficiency and collaboration. Essential to software delivery, is the process of **creating** each improvement. The Create stage delights engineers, designers, and product managers with tools to design, develop, and review these improvements efficiently.


### Groups

The Create stage is made up of one DevOps stage, Create, and five groups including:

* Code Creation
* Code Review
* Editor Extensions
* Remote Development
* Source Code

### Resourcing and Investment

The existing team members for the Create stage can be found in the links below:

* [Code Creation](https://handbook.gitlab.com/handbook/engineering/development/dev/create/code-creation/)
* [Code Review](https://handbook.gitlab.com/handbook/engineering/development/dev/create/code-review/)
   * [BE](https://handbook.gitlab.com/handbook/engineering/development/dev/create/code-review/backend/)
   * [FE](https://handbook.gitlab.com/handbook/engineering/development/dev/create/code-review/frontend/)
* [Editor Extensions](https://handbook.gitlab.com/handbook/engineering/development/dev/create/editor-extensions/)
* [Remote Development](https://handbook.gitlab.com/handbook/engineering/development/dev/create/remote-development/)
* Source Code
   * [BE](https://handbook.gitlab.com/handbook/engineering/development/dev/create/source-code-be/)
   * [FE](https://handbook.gitlab.com/handbook/engineering/development/dev/create/create-source-code-fe)

## 3 Year Stage Themes
### Enterprise Source Code Management

[Source code management (SCM)](https://about.gitlab.com/solutions/source-code-management/) is the foundation of an organization's software development practice. SCM tools provide the interface and controls that teams use to define the rules and workflows their developers operate within to write code and collaboratively produce software. At any size of company, it is critical that the SCM tool be intuitive to aid in productivity, streamline collaboration for reviews across teams and functions, ensure compliance, and enable best development and security practices. However, these challenges become more acute and more difficult to solve at the enterprise level. The larger an organization becomes, the greater their communication and coordination overhead is since there are more numerous, bigger, and broadly distributed teams trying to work together. To address this, the industry is adopting DevSecOps practices to increase velocity and reduce cycle time. Selecting an SCM tool is the first step on that journey.

As examples, GitLab will provide:
- Enterprise-grade administration for configuring rules and controls across hundreds of teams
- A library of project templates that allow the bulk creation of repositories
- Different merge strategies to enable teams that work linearly and nonlinearly
- Support for git forking workflows for teams that rely on restricting write access to the official codebase 
- Support for development in monolithic repositories and binary assets for those working in the digital media space 
- Streamlined code review workflows enhanced with automation 
- A remote development platform that enables the onboarding of developers in a single day

### Security built-in, not bolted on

Security is a team sport and organizations benefit the most when the developers have it top of mind. The most successful teams integrate security practices into code reviews and even into the actual writing of code. Source code management platforms typically offer this functionality via integration with multiple other tools, bolted on. This creates context-switching and inefficiencies. SCM tools that offer security testing natively understand how critical a developer’s time and attention span are to producing great software rapidly. By purchasing tools that make the “required tasks” (i.e. approvals, security, compliance) enjoyable and low-effort, companies retain happy development talent while meeting regulations, preventing breaches, and shipping software frequently. [You can read more about shifting left on the Secure stage vision.](https://about.gitlab.com/direction/application_security_testing/#shift-left-no-more-left-than-that)

As examples, GitLab will provide:
- Security scan results in the merge request
- Real-time feedback in the Web IDE allowing developer to write secure code prior to code review
- Centralized management of libraries & dependencies via Workspaces to secure the software supply chain

### The Developer Experience

The developer experience is defined by development velocity, safety, and how it enables innovation and iteration. Investing in the Developer Experience therefore drives revenue and reduces risk for organizations. To provide a strong DX, a company must purchase tools that are highly usable & reliable, organized to support the developer journey, reduce context switching, and minimize decision fatigue. Such tools can significantly increase developer productivity by automating the manual repetitive tasks, removing the need for the individual developer to maintain local environments or worry about keeping libraries and dependencies up-to-date, and providing a central internal developer portal for project, process, product, and API documentation with an intuitive and beautiful UI. 

As examples, GitLab will provide:
- Remote development option that enables developers to quickly spin up environments to develop cloud native applications
- A CLI equipped with native tools for the developer, operations, and security personas
- AI assisted suggestions for best practices, performance, & security
- Lightning fast and accurate code search
- Code review workflows that reduce review rounds and that offer intelligent suggestions for appropriate reviewers
- Extensions for GitLab to the tools where developers work
- A robust and easy to use embedded Web IDE







## 3 Year Strategy

In three years the Create stage market will:
   - Still be focused on Git as the superior version-control system
   - Evolve [Git](https://git-scm.com/) to efficiently support monorepos and take market in the movie and video game industry from other version control systems
   - Experience enormous performance and accuracy leaps in code search
   - Incoporate ML/AI in every part of the DevSecOps life cycle
   - Embrace cloud-based development environments

As a result, in three years GitLab will:
   - Be the market default tool for [Source Code management](https://about.gitlab.com/direction/create/source_code_management/source_code_management/) in all industries including Entertainment and other sectors that depend upon binary assets
   - [Provide strong support for monorepos](https://gitlab.com/groups/gitlab-org/-/epics/773) by extending commands and workflows in git that make working with enourmous repositories fast and efficient
   - Provide a [browser-based IDE](https://about.gitlab.com/direction/create/remote_development/web_ide/) that provides reliable and secure access to pre-configured development environments
   - Provide [cloud-based remote development environments](https://about.gitlab.com/direction/create/remote_development/workspaces/) to improve security and efficiency for development teams during software development
   - Offer more options for developers to do their work completely [within their chose IDEs](https://about.gitlab.com/direction/create/editor_extensions/) without switching context to the GitLab UI through our Editor Extensions.








## 1 Year Plan

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



## Target Audience

GitLab identifies who our DevSecOps application is built for utilizing the following categorization. We list our view of who we will support when in priority order.
* 🟩 - Targeted with strong support
* 🟨 - Targeted but incomplete support
* ⬜️ - Not targeted but might find value

### Today

1. 🟩 [Software Developers](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
1. 🟩 [Development Team Leads](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
1. 🟩 [Software Engineer in Test](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
1. 🟩 [DevOps Engineers](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
1. 🟨 [Application Development Director](https://handbook.gitlab.com/handbook/product/personas/#dakota-application-development-director)
1. 🟨 [System Administrator](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)
1. 🟨 [Security Operations Engineers](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer)
1. ⬜️ [Application Ops](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops)
1. ⬜️ [Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
1. ⬜️ [Compliance Managers](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)

### Medium Term (1-2 years)

1. 🟩 [Software Developers](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
1. 🟩 [Development Team Leads](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
1. 🟩 [Software Engineer in Test](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
1. 🟩 [DevOps Engineers](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
1. 🟩 [Application Development Director](https://handbook.gitlab.com/handbook/product/personas/#dakota-application-development-director)
1. 🟩 [System Administrator](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)
1. 🟨 [Security Operations Engineers](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer)
1. 🟨 [Application Ops](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops)
1. 🟨 [Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
1. 🟨 [Compliance Managers](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)

## Categories in Create



## Jobs to be Done




## Pricing

The Create stage pricing strategy balances the needs of individual contributors, with the needs of enterprises, to create a cycle where individual contributors gladly and rapidly adopt GitLab, and naturally create the business case for upgrading to a suitable tier, typically Premium and above. The core pillar of the Create stage is the merge request based development workflow. This touches Source Code Management, Code Review and the Web IDE, and is heavily influenced by individual developers, and managers who implement access controls for efficiency, security, quality and compliance purposes. Our investment and pricing philosophy is to:

- Invest in the Free tier to drive adoption by individual contributors like developers and designers
- Drive adoption of Premium from the Free tier by providing more control to managers and administrators
- Retain customers which drives expansion of more users and cross-stage efficiency with Ops, Secure and Govern

### Free

The tier for **individual contributors, personal projects, or small teams trialing GitLab**. Free is important for retaining our core users Developers (SCM, Code Review, Web IDE) and exploring different avenues of expansion in the types of personas who contribute to GitLab and their use cases. Expanding support for different markets and use cases through improved binary file and monolithic repository workflows and more accessible editing tools begins at the individual contributor level, as does supporting new personas like designers and marketers.

Examples:

- [Web IDE](https://docs.gitlab.com/ee/user/project/web_ide)
- [Powerful Branching](https://docs.gitlab.com/ee/topics/git)
- [Merge requests](https://docs.gitlab.com/ee/user/project/merge_requests/)

### Premium

The tier for **teams**, Premium is enterprise ready and delivers important access controls and workflow controls needed for multiple teams to collaborate on the same large project. The Premium tier features for Source Code Management and Code Review are already mature, and very valuable to medium and large enterprises. Many feature requests and improvements driven by Premium customers are improvements to the experience of individual developers, which facilitates growth through expansion and standardization on GitLab.

Examples:

- [Approval Rules for Code Review](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/rules)
- [CODEOWNERs](https://docs.gitlab.com/ee/user/project/code_owners)
- [Custom group-level project templates](https://docs.gitlab.com/ee/user/group/custom_project_templates.html#custom-group-level-project-templates)

### Ultimate

The tier for **Executive buyers with strategic objects for their business**, this tier is primarily supported through Audit and Compliance capabilities that extend project level access control features.

Examples:

- [Security findings integrated in the IDE](https://docs.gitlab.com/ee/editor_extensions/visual_studio_code/#view-security-findings)
- [Real-time SAST scanning in the IDE](https://docs.gitlab.com/ee/editor_extensions/visual_studio_code/#perform-sast-scanning)


## Upcoming Releases




