---
layout: markdown_page
title: Product Stage Direction - Foundations
description: "The Foundations stage in GitLab delights business stakeholders and enables organizations to work more efficiently"
canonical_path: "/direction/foundations/"
---

## On this page
{:.no_toc}

- TOC
{:toc}

## Vision

**Foundations helps enterprise customers setup and adopt GitLab quickly, efficiently and securely.**
    

The Foundations Stage is at the core of the GitLab platform. It is a glue that spans across different stages and enables our customers to setup and adopt GitLab by providing a frictionless [Import](/direction/foundations/import_and_integrate/importers/) experience to bring your applications into GitLab, [Integrations](/direction/foundations/import_and_integrate/integrations/) with your ecosystem and an intuitive and effective [Navigation](/direction/foundations/personal_productivity/navigation/) system.

## Groups
The Foundations stage is made up of four groups. You can find the direction pages of these groups here:

* [Import and Integrate](/direction/foundations/import_and_integrate/)
* [Personal productivity](/direction/foundations/personal_productivity/)
* [Design System](/direction/foundations/design_system/)
* [UX Paper Cuts](/direction/foundations/ux-paper-cuts/)

The existing team members for the Foundations Stage can be found under the links below:

  * [Import and Integrate](https://handbook.gitlab.com/handbook/engineering/development/dev/manage/import-and-integrate/)
  * [Personal productivity](https://handbook.gitlab.com/handbook/engineering/development/dev/manage/personal_productivity/)
  * [Design System](https://handbook.gitlab.com/handbook/engineering/development/dev/manage/personal_productivity/)
  * [UX Paper Cuts](product/ux/product-design/#ux-paper-cuts-team)

## Stage Themes

#### Drive Adoption
Aligning with [Core Platform section](https://about.gitlab.com/direction/core_platform/) theme ["GitLab is easy to deploy and adopt"](https://about.gitlab.com/direction/core_platform/#gitlab-is-easy-to-deploy-and-operate), the foundations stage will aim to drive adoption of GitLab through a faster & smoother onboarding process. Our onboarding process will support our customers needs for lower downtime & improved reliability of importers. This will increase number of customers who onboard to GitLab as well as reduce the time it takes to onboard, increasing overall adoption of GitLab.

`- We will prioritize enhancing the experience for enterprise customers by developing tools that improve business continuity, reduce downtime, provide easy-to-understand error messages, and ensure reliable data migration. For instance, "Import Evaluation Tool" can be run before the migration and will help customers understand how long will migration take, what can and cannot be migrated, and possibly even suggest "migration waves" to break down a huge import into several chunks. This feature in combination with faster import reduces the downtime and allows flexibility to work through migration in off-hours improving business continuity
- Our goal is to enhance collaboration and productivity by creating integrations that help customers get more out of their GitLab experience. For example, rather than manually updating Jira ticket status upon code merge, GitLab for [Jira integration](https://docs.gitlab.com/ee/integration/jira/) automates this process. This removes redundancy and saves up to 30 minutes per day of the development time per developer.
- Customers will be able to customize & extend GitLab for their unique needs by using APIs and Webhooks. For instance, an internal process can be run by utilizing webhook that triggers the [event on pipeline status change](https://docs.gitlab.com/ee/user/project/integrations/webhook_events.html#pipeline-events).


#### Security and Compliance
Typically, an enterprise will have a security team, DevOps teams, and an internal compliance officer. They collectively try to understand how the product in the organization is being delivered and have manual processes to examine compliance. By automating some of these tasks, we can accelerate the time to delivery for our customers and reduce the cost of compliance.  For instance, security standards & best practices defined at project, group or organization level could be applied automatically to detect if the code merged is compliant or not. Additional security measures could be applied to prevent the branch from being merged if a certain level of compliance is not met. This DevOps automation could be applied to organization-specific, industry-specific ( e.g. [PCI-DSS](https://www.pcisecuritystandards.org/)), or government-related ( e.g. [GDPR](https://gdpr-info.eu/) ) regulations to increase operational efficiency and bake in security as part of the development lifecycle.

#### Help Customers Deliver Faster
The Foundations stage is uniquely positioned to minimize the time it takes for our customers to deliver throughout the DevSecOps life cycle. We will help our customers deliver faster by
- Making it easier for everyone to contribute.
  - For instance, build modular & easy to plug-and-play infrastructure for “onboarding”. This will accelerate process of maturing onboarding platform by increasing the number of 3rd party tools we can migrate from while improving maintainability. In the future, importing from Jenkins, GitHub Actions and Jira can be easily added by introducing field mapping from respective tools to GitLab. This will make it easier for community, partners & internal teams to contribute and help customers deliver faster.
- Reducing the time taken to complete your day-to-day tasks in GitLab. Here are few use-cases:
  - For a system admin, Setting up approvers or changing Jira integration settings by improving the usability & accessibility of Settings.
  - For a product manager or developer, to access issues or MRs using Pinning.
  - Using AI to automate workflows. For instance, suggest fixes for vulnerability finds, build automated test cases to speed up the development process, execute those test cases async & even create issues and suggests fixes for bugs found.


#### Improve SUS (System Usability Score)
This theme is directly aligned with ["World Class DevSecOps experience"](https://about.gitlab.com/direction/#world-class-devsecops-experience). The foundations stage spans across different stages of the DevSecOps lifecycle. Our goal is to improve the overall user experience by improving the usability & accessibility of GitLab with our continued efforts on [design system adoption](https://handbook.gitlab.com/handbook/product/ux/pajamas-design-system/) & [new and improved navigation](https://gitlab.com/groups/gitlab-org/-/epics/9044). We will continue to make it easier for our users to find what they are looking for, to pick up where they left off, and to orient them in GitLab. For instance, If you're a System Admin who updates MR settings annually (such as merging only on a successful pipeline or with approval from 2+ reviewers), we aim to simplify the process. No need to recall previous actions or sift through notes.

### 3 Year Strategy

In three years, we expect :
* Onboarding to Gitlab from other platforms (such as GitHub, Bitbucket) to SaaS/Dedicated will be predictable & 80% faster than in FY23.
* Onboarding journey will cover wider use-cases than importing groups & projects to support customers in getting the most out of their GitLab instance. For instance, importing Github Actions and Jira issues.
* To integrate with third-party tools that are consistent with the [vision of AllOps](https://about.gitlab.com/company/vision/) platform, ensuring that they complement the DevSecOps journey and promote collaboration. Notably, tools such as Jira, Slack, and ServiceNow will be integrated in alignment with our overarching one-platform strategy.
* System administrators will have Enterprise User management tools for easy, secure, and automated user lifecycle management, minimizing the need for manual work. For instance, Automated off-boarding processes we introduce aim to reduce risk of unauthorized access, data loss and security exposures.
* To improve learnability & reduce cognitive load on users through intuitive, easy-to-use, and accessible Navigation.
* Artificial Intelligence will increase automation and make it easier and faster for users to manage their DevSecOps tasks. For instance, a personal assistant for the devOps team that automates the test cases for the code, determines the test coverage and suggests ways to improve it.


## 1 Year Plan

### Import and Integrate

In 2024, we are focused on two main areas:

- Bringing [project migration by direct transfer](https://docs.gitlab.com/ee/user/group/import/index.html#migrated-project-items-beta) to [general availability](https://docs.gitlab.com/ee/policy/experiment-beta-support.html#generally-available-ga), so that we offer production-quality, easy to use tool for migrating GitLab resources between instances of GitLab. It should gracefully recover from errors and import over nearly 100% of relevant objects.

Ability to migrate projects by direct transfer was released as Beta (available to everyone) [in GitLab 15.8](https://about.gitlab.com/blog/2023/01/18/try-out-new-way-to-migrate-projects/).

- Improving high-priority Integrations, Atlassian Jira and Slack in order to reach Complete [maturity level](../../../../maturity).


### Personal productivity

The Personal productivity team will continue to build cross-stage UIs and user workflows that should be consistent, clearly designed, and iterated on like a feature to improve the overall user experience of GitLab. In rest of the FY24 and FY25, we will work on
* Enhancing the navigation experience of the super sidebar.
* Continue to build consistent user experience across GitLab by increasing Pajamas adoption.
* Enable Dark Mode as color theme in New Navigation
* Continue to enhance the design system with the goal of improving overall SUS
* Improve usability of Settings
* Build The Message Center for personalized notifications to the users.

## Target audience

GitLab identifies who our DevSecOps application is built for utilizing the following categorization. We list our view of who we will support when in priority order.
* 🟩 - Targeted with strong support
* 🟨 - Targeted but incomplete support
* ⬜️ - Not targeted but might find value

### Today

1. 🟩 [Compliance Managers](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)
1. 🟩 [Systems Administrator](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)
1. 🟨 [Application Ops](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops)
1. 🟨 [Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
1. 🟩 [Software Developers](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
1. 🟩 [Development Team Leads](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
1. 🟨 [Application Development Director](https://handbook.gitlab.com/handbook/product/personas/#dakota-application-development-director)
1. ⬜️ [Product Managers](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)
1. ⬜️ [Software Engineer in Test](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
1. ⬜️ [Product Designers](https://handbook.gitlab.com/handbook/product/personas/#presley-product-designer)
1. 🟨 [DevOps Engineers](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
1. 🟨 [Security Operations Engineers](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer)
1. 🟩 [Security Analysts](https://handbook.gitlab.com/handbook/product/personas/#sam-security-analyst)
1. 🟨 [Release Manager](https://handbook.gitlab.com/handbook/product/personas/#rachel-release-manager)


## Metrics

Manage uses [Stage MAU](https://handbook.gitlab.com/handbook/product/performance-indicators/) as a primary measure of success. This represents the unique number of users getting value from the stage; all groups should be able to contribute to improving this number.

Individual groups track progress against a number of group-specific [performance indicators](https://handbook.gitlab.com/handbook/product/performance-indicators/) _All links are to the internal handbook_:

| Group | Dashboard URL |
| ------ | ------ |
| Import | [MAU importing](https://handbook.gitlab.com/handbook/product/dev-section-performance-indicators/)|
| Integrations | [GMAU - MAU for Jira and Slack Integrations](https://internal.gitlab.com/handbook/company/performance-indicators/product/dev-section/#manageintegrations---smau---gmau---mau-for-jira-and-slack-integrations)
| Personal productivity | [Percentage views on New Nav vs. Old Nav](https://internal.gitlab.com/handbook/company/performance-indicators/product/dev-section/#managefoundations---ppi---saas-percentage-of-page-views-from-navigation) |


## How we operate

Manage operates under GitLab's values, but is a stage that seeks to particularly excel in certain areas that support our goals above. We seek to be leaders at GitLab by:

### Iterate on the essential
* Leading the way on iteration, regularly shooting for small but ambitious MVCs.
* Supporting iteration with a great planning and development process, giving us checkpoints to keep issues small and incremental. As a result, our throughput is high.
* Valuing the 1-year themes above, and deliberately deciding to not pursue initiatives that don’t support our 2020 goals. We'd rather do a few things well than a bunch of things poorly.
* Prioritizing depth over breadth. For the most part, we’re biased toward doubling down and investing on what’s working rather than extending the breadth of our stage.

### Measure what matters
* Prioritizing instrumentation through our North Star dashboards, which we regularly monitor to keep our priorities in check.
* Measuring business value by tying customer delight and revenue to our priorities.

### Great team
* Aspiring to be the happiest team at GitLab, with high individual job satisfaction.
* Having great work-life balance, ensuring that we [value friends and family above work](https://handbook.gitlab.com/handbook/values/#family-and-friends-first-work-second) and avoid individual burnout.


## Categories



## Pricing

The Foundations stage has several features that enable users to quickly get started with using GitLab. These features are available in Core and are Free. However, as we move into specific use-cases for Enterprise customers that need to manage their GitLab organization at scale, features will be introduced into paid tiers as well and are intended to drive [company-level financial goals](https://about.gitlab.com/company/okrs/).

Full list of features by tier under Foundations stage are [here](https://handbook.gitlab.com/handbook/product/categories/features/#foundations) 





## Upcoming Releases




*Last Updated: 2024-01-03*
</p>
