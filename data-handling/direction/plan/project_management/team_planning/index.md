---
layout: markdown_page
title: "📝 Category Direction - Team Planning"
description: This is the category strategy for Team Planning in GitLab; which is part of the Plan stage's Project Management group. Learn more here!
canonical_path: "/direction/plan/project_management/team_planning/"
---

This direction page was last reviewed on:
`2024-10-29`



- TOC
{:toc}

## Team Planning

|  |               |
| -------- | -------------------------------- |
| Stage    | [Plan](/direction/plan/)         |
| Group | [Project Management](/direction/plan/project_management/) |
| Maturity | [Viable](/direction/#maturity) |


### Introduction and how you can help

👋 This is the category direction for Team Planning in GitLab, which is part of the Project Management group with the Plan stage. Please reach out to the group's Product Manager, [Gabe Weaver](https://gitlab.com/gweaver) ([E-mail](mailto:gweaver@gitlab.com)), if you'd like to provide feedback or ask any questions related to this product category.

This direction is a work in progress and everyone can contribute:

- Please comment and contribute to the related [issues](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=group%3A%3Aproject%20management) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=Category%3ATeam%20Planning). Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
- Please share feedback directly via email, Twitter, or [schedule a quick Zoom for us to connect](https://calendly.com/gweaver/45-minute-meeting).

### Category overview

Team Planning's goal is to provide collaboration and planning capabilities to empower small, autonomous teams to continuously deliver customer and business value with the shortest possible cycle times. Features owned by the Team Planning category include [work items (issues)](https://docs.gitlab.com/ee/user/project/issues/), [tasks](https://docs.gitlab.com/ee/user/tasks.html), [milestones](https://docs.gitlab.com/ee/user/project/milestones/), [iterations](https://docs.gitlab.com/ee/user/group/iterations/), [boards](https://docs.gitlab.com/ee/user/project/issue_board.html), [discussions](https://docs.gitlab.com/ee/user/discussions/), [labels](https://docs.gitlab.com/ee/user/project/labels.html), [todos](https://docs.gitlab.com/ee/user/todos.html), [quick actions](https://docs.gitlab.com/ee/user/project/quick_actions.html), and [notifications](https://docs.gitlab.com/ee/user/profile/notifications.html).


### Strategy and themes

Team Planning's strategy is aligned to [Plan's 3 year stage themes](https://about.gitlab.com/direction/plan/#3-year-stage-themes).

### 1 year plan

#### What's next for us

- **[Group issues](https://gitlab.com/groups/gitlab-org/-/epics/12320)**. Issues can be created within groups without depending on a project within the group. This will optionally allow teams to consolidate their planning workflows within a single location instead of spreading them across a group and a project.  
- **[Work items open in a drawer within boards and lists](https://gitlab.com/gitlab-org/gitlab/-/issues/387224)**. Reduce the context switching and tab fatique when drilling down into a work item detail view. 
- **[Customizable work item statuses](https://gitlab.com/gitlab-org/gitlab/-/issues/368290)**. Provide a foundation for building a more robust work item lifecycle management solution, and enable teams to mark work items as done or cancelled. 
- **[Report on iteration velocity and volatility](https://gitlab.com/groups/gitlab-org/-/epics/435)** -- Helps teams have meaningful discussions about trade-offs and estimations when planning upcoming iterations. Issues and tasks can be assigned to iterations, so our next step is [showing parent/child relationships in the iteration report](https://gitlab.com/gitlab-org/gitlab/-/issues/457538), followed by [displaying velocity and volatility](https://gitlab.com/gitlab-org/gitlab/-/issues/457094). 
- **[Work items are natively supported within Groups](https://gitlab.com/groups/gitlab-org/-/epics/8308)** -- Eliminate the need to maintain projects under groups solely for agile planning purposes, allow teams to consolidate their planning activities at the group level, and enable issues and epics to be migrated to work items. We're currently working on [the remaining blockers](https://gitlab.com/gitlab-org/gitlab/-/issues/458986) to feature parity between legacy issues and work item issues. Once issues are migrated to work items, we will be able to turn on native Group Issues. 


#### What we are currently working on

- **[Work Item Enhancements](https://gitlab.com/groups/gitlab-org/-/epics/6033)** -- [Standardize the workflow for creating planning objects](https://gitlab.com/groups/gitlab-org/-/epics/11012) and [associate DevSecOps artifacts to supported work item types](https://gitlab.com/groups/gitlab-org/-/epics/7105).
- **[Add support for custom fields to work items](https://gitlab.com/groups/gitlab-org/-/epics/235)**. Provide teams with a more robust solution for associating business-specific meta-data to work items. We're starting with adding support for [basic custom fields](https://gitlab.com/groups/gitlab-org/-/epics/14904), which will be configurable within root groups. 
- **[Enable work items (Tasks) to be visible on Boards](https://gitlab.com/gitlab-org/gitlab/-/issues/368816)**. Teams can manage their tasks (and other work items) from within Boards. 
- **[Complete the migration of issues to work items](https://gitlab.com/groups/gitlab-org/-/epics/9584)**. Replace the legacy issue detail view with the new and improved real-time work item detail view. 


Our group level [issue board](https://gitlab.com/groups/gitlab-org/-/boards/1235826?&label_name[]=devops%3A%3Aplan&label_name[]=group%3A%3Aproject%20management) provides detailed insight into everything currently in flight.

#### What we recently completed

- **[Adds type attribute to issues webhook payloads (17.1)](https://gitlab.com/gitlab-org/gitlab/-/issues/467415)** -- Issues, tasks, incidents, requirements, objectives, and key results all trigger payloads under the Issues Events webhook category. Until now, there has been no way to quickly determine the type of object that triggered the webhook within the event payload. This release introduces an object_attributes.type attribute available on payloads within the Issues events, Comments, Confidential issues events, and Emoji events triggers.
- **[Resolve threads in tasks, objectives, and key results (17.3)](https://about.gitlab.com/releases/2024/08/15/gitlab-17-3-released/#resolve-threads-in-tasks-objectives-and-key-results)** -- You can now resolve threads in tasks, objectives, and key results, making it easier to manage and track important conversations. Resolved threads are collapsed by default, helping you focus on active discussions and streamline your collaboration workflows.
- **[Add Merge Requests to Tasks (17.3)](https://gitlab.com/gitlab-org/gitlab/-/issues/440851)** -- When referencing a task from within an MR description using the [closing pattern](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically), Merge Requests will now be linked to the task, providing better visibility and traceability between tasks and related code changes. This feature enhances project management by allowing teams to easily track which merge requests are associated with specific tasks, improving workflow and collaboration.
- **[Summarize Issue discussions GA (17.4)](https://gitlab.com/groups/gitlab-org/-/epics/10760)** -- View an AI generated summary of all threads and comments within an issue or epic to quickly get up to spead on the discussion. 



#### What is not planned right now

While we believe the following items are critically important to the long-term use cases we want to support within Plan, we currently are not focusing on solving them:

- Implementing a comprehensive resource management system within GitLab.
- Integrating a complex dependency management system across multiple projects.
- Building a native risk assessment and mitigation framework.
- Developing a comprehensive budgeting and cost management module.
- Creating an advanced project forecasting and scenario planning tool.
- Developing a complex change management tracking and approval workflow.
- Adding support for a native automation framework within GitLab. 
- Advanced team analytics. 



### Best-in-class landscape

BIC (Best In Class) is an indicator of forecated near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

#### Key capabilities

This information is maintained on [this internal handbook page](https://internal.gitlab.com/handbook/product/best-in-class/plan/#how-we-reduce-lost-opportunities-to-jira)

#### Roadmap

This information is maintained on [this internal handbook page](https://internal.gitlab.com/handbook/product/best-in-class/plan/#product-priorities)

#### Top [1/2/3] Competitive Solutions

This information is maintained on [this internal handbook page](https://internal.gitlab.com/handbook/product/best-in-class/plan/#competitive-analysis-summary)


### Target audience

GitLab identifies who our DevSecOps application is built for utilizing the following categorization. We list our view of who we will support when in priority order.
* 🟩 - Targeted with strong support
* 🟨 - Targeted but incomplete support
* ⬜️ - Not targeted but might find value

### Today

1. 🟩 [Software Developers](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
1. 🟨 [Development Team Leads](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
1. 🟨 [Application Development Director](https://handbook.gitlab.com/handbook/product/personas/#dakota-application-development-director)
1. 🟨 [Product Managers](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)
1. 🟨 [Software Engineer in Test](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
1. 🟨 [Product Designers](https://handbook.gitlab.com/handbook/product/personas/#presley-product-designer)
1. 🟨 [DevOps Engineers](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
1. 🟨 [Security Operations Engineers](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer)
1. 🟨 [Release Manager](https://handbook.gitlab.com/handbook/product/personas/#rachel-release-manager)
1. 🟨 [Security Analysts](https://handbook.gitlab.com/handbook/product/personas/#sam-security-analyst)
1. ⬜️ [Application Ops](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops)
1. ⬜️ [Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
1. ⬜️ [Compliance Managers](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)
1. ⬜️ [Systems Administrator](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)

### Medium Term (1-2 years)

1. 🟩 [Software Developers](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
1. 🟩 [Development Team Leads](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
1. 🟩 [Application Development Director](https://handbook.gitlab.com/handbook/product/personas/#dakota-application-development-director)
1. 🟩 [Product Managers](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)
1. 🟨 [Software Engineer in Test](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
1. 🟨 [Product Designers](https://handbook.gitlab.com/handbook/product/personas/#presley-product-designer)
1. 🟨 [DevOps Engineers](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
1. 🟨 [Security Operations Engineers](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer)
1. 🟨 [Release Manager](https://handbook.gitlab.com/handbook/product/personas/#rachel-release-manager)
1. 🟩 [Security Analysts](https://handbook.gitlab.com/handbook/product/personas/#sam-security-analyst)
1. ⬜️ [Application Ops](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops)
1. ⬜️ [Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
1. 🟨 [Compliance Managers](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)
1. ⬜️ [Systems Administrator](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)


### Jobs To Be Done

We are currently focused on providing best-in-class solutions for the following [Jobs To Be Done (JTBD)](https://handbook.gitlab.com/handbook/product/ux/jobs-to-be-done/):


