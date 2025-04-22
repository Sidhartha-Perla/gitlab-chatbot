---
layout: markdown_page
title: "Group Direction - Project Management"
description: This is the group strategy for the Project Management group; which is part of the Plan stage within the Dev section.
canonical_path: "/direction/plan/project_management/"
---

This direction page was last reviewed on:
`2024-10-29`


- TOC
{:toc}

## Introduction and how you can help

👋 This is the group strategy for Project Management, which is part of the Plan stage. Please reach out to the group's Product Manager, [Gabe Weaver](https://gitlab.com/gweaver) ([E-mail](mailto:gweaver@gitlab.com)), if you'd like to provide feedback or ask any questions related to this product category.

This strategy is a work in progress and everyone can contribute:

- Please comment and contribute to the related [issues](https://gitlab.com/groups/gitlab-org/-/issues?sort=created_date&state=opened&label_name[]=group::project+management) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=group::project+management). Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
- Please share feedback directly via email, Twitter, or [schedule a quick Zoom for us to connect](https://calendly.com/gweaver/45-minute-meeting).

## Group Overview

[GitLab's mission](https://handbook.gitlab.com/handbook/company/mission/#mission) is to build software so that **everyone can contribute** and we aim to be the most popular collaboration platform for knowledge workers in any industry. The Project Management Group is a cross-departmental team focused on two primary categories -- [Team Planning](/direction/plan/project_management/team_planning) and [Service Desk](https://about.gitlab.com/direction/service_management/service_desk/)

### Team Planning

Team Planning's goal is to provide collaboration and planning capabilities to empower small, autonomous teams to continuously deliver customer and business value with the shortest possible cycle times. Features owned by the Team Planning category include [work items (issues)](https://docs.gitlab.com/ee/user/project/issues/), [tasks](https://docs.gitlab.com/ee/user/tasks.html), [milestones](https://docs.gitlab.com/ee/user/project/milestones/), [iterations](https://docs.gitlab.com/ee/user/group/iterations/), [boards](https://docs.gitlab.com/ee/user/project/issue_board.html), [discussions](https://docs.gitlab.com/ee/user/discussions/), [labels](https://docs.gitlab.com/ee/user/project/labels.html), [todos](https://docs.gitlab.com/ee/user/todos.html), [quick actions](https://docs.gitlab.com/ee/user/project/quick_actions.html), and [notifications](https://docs.gitlab.com/ee/user/profile/notifications.html).


### Service Desk

[View the Service Desk direction](../../service_management/service_desk)


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


## Current Investment Mix

| Category | Allocation |
| -------- | ---------- |
| Team Planning | 100%  |
| Service Desk | 0%  |

## What we recently completed

- **[Adds type attribute to issues webhook payloads (17.1)](https://gitlab.com/gitlab-org/gitlab/-/issues/467415)** -- Issues, tasks, incidents, requirements, objectives, and key results all trigger payloads under the Issues Events webhook category. Until now, there has been no way to quickly determine the type of object that triggered the webhook within the event payload. This release introduces an object_attributes.type attribute available on payloads within the Issues events, Comments, Confidential issues events, and Emoji events triggers.
- **[Resolve threads in tasks, objectives, and key results (17.3)](https://about.gitlab.com/releases/2024/08/15/gitlab-17-3-released/#resolve-threads-in-tasks-objectives-and-key-results)** -- You can now resolve threads in tasks, objectives, and key results, making it easier to manage and track important conversations. Resolved threads are collapsed by default, helping you focus on active discussions and streamline your collaboration workflows.
- **[Add Merge Requests to Tasks (17.3)](https://gitlab.com/gitlab-org/gitlab/-/issues/440851)** -- When referencing a task from within an MR description using the [closing pattern](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically), Merge Requests will now be linked to the task, providing better visibility and traceability between tasks and related code changes. This feature enhances project management by allowing teams to easily track which merge requests are associated with specific tasks, improving workflow and collaboration.
- **[Summarize Issue discussions GA (17.4)](https://gitlab.com/groups/gitlab-org/-/epics/10760)** -- View an AI generated summary of all threads and comments within an issue or epic to quickly get up to spead on the discussion. 



## What we are currently working on

Our group level [issue board](https://gitlab.com/groups/gitlab-org/-/boards/1235826?&label_name[]=devops%3A%3Aplan&label_name[]=group%3A%3Aproject%20management) provides detailed insight into everything currently in flight.

### Team Planning

- **[Work Item Enhancements](https://gitlab.com/groups/gitlab-org/-/epics/6033)** -- [Standardize the workflow for creating planning objects](https://gitlab.com/groups/gitlab-org/-/epics/11012) and [associate DevSecOps artifacts to supported work item types](https://gitlab.com/groups/gitlab-org/-/epics/7105).
- **[Add support for custom fields to work items](https://gitlab.com/groups/gitlab-org/-/epics/235)**. Provide teams with a more robust solution for associating business-specific meta-data to work items. We're starting with adding support for [basic custom fields](https://gitlab.com/groups/gitlab-org/-/epics/14904), which will be configurable within root groups. 
- **[Enable work items (Tasks) to be visible on Boards](https://gitlab.com/gitlab-org/gitlab/-/issues/368816)**. Teams can manage their tasks (and other work items) from within Boards. 
- **[Complete the migration of issues to work items](https://gitlab.com/groups/gitlab-org/-/epics/9584)**. Replace the legacy issue detail view with the new and improved real-time work item detail view. 


## What's next for us

### Team Planning

- **[Group issues](https://gitlab.com/groups/gitlab-org/-/epics/12320)**. Issues can be created within groups without depending on a project within the group. This will optionally allow teams to consolidate their planning workflows within a single location instead of spreading them across a group and a project.  
- **[Work items open in a drawer within boards and lists](https://gitlab.com/gitlab-org/gitlab/-/issues/387224)**. Reduce the context switching and tab fatique when drilling down into a work item detail view. 
- **[Customizable work item statuses](https://gitlab.com/gitlab-org/gitlab/-/issues/368290)**. Provide a foundation for building a more robust work item lifecycle management solution, and enable teams to mark work items as done or cancelled. 
- **[Report on iteration velocity and volatility](https://gitlab.com/groups/gitlab-org/-/epics/435)** -- Helps teams have meaningful discussions about trade-offs and estimations when planning upcoming iterations. Issues and tasks can be assigned to iterations, so our next step is [showing parent/child relationships in the iteration report](https://gitlab.com/gitlab-org/gitlab/-/issues/457538), followed by [displaying velocity and volatility](https://gitlab.com/gitlab-org/gitlab/-/issues/457094). 
- **[Work items are natively supported within Groups](https://gitlab.com/groups/gitlab-org/-/epics/8308)** -- Eliminate the need to maintain projects under groups solely for agile planning purposes, allow teams to consolidate their planning activities at the group level, and enable issues and epics to be migrated to work items. We're currently working on [the remaining blockers](https://gitlab.com/gitlab-org/gitlab/-/issues/458986) to feature parity between legacy issues and work item issues. Once issues are migrated to work items, we will be able to turn on native Group Issues. 


## What we're not doing

While we believe the following items are critically important to the long-term use cases we want to support within Plan, we currently are not focusing on solving them:

- Implementing a comprehensive resource management system within GitLab.
- Integrating a complex dependency management system across multiple projects.
- Building a native risk assessment and mitigation framework.
- Developing a comprehensive budgeting and cost management module.
- Creating an advanced project forecasting and scenario planning tool.
- Developing a complex change management tracking and approval workflow.
- Adding support for a native automation framework within GitLab. 
- Advanced team analytics. 



## Performance indicators

Check out our cross-functional [Project Management team handbook page](https://handbook.gitlab.com/handbook/product/groups/project-management/#performance-indicators) to view our current customer value, product quality, and process performance indicators (internal link).


## Competitive landscape

The [project management tools market](https://www.datanyze.com/market-share/project-management) is dominated by Jira (31%), Microsoft (18%), Smartsheet (6%), and Trello (5%). To be competitive, GitLab needs to solve for the following customer comments in the immediate future:

> We’ve been told to use gitlab’s milestones to capture agile sprints, as they’re the only thing that can have burn down, they work well with boards and have concepts of time.  The default way epics get their start/end dates is based on the milestones of the issues attached though – doesn’t make sense as an issue shouldn’t be assigned to an agile sprint until the sprint is eminent.  (root of problem is that gitlab milestone must either be equated to agile milestone or agile sprint, not both – you’re missing a concept)
>
> Needs to be a way to have a team velocity, as a scrum master be able to go through and say “This feature requires ~100 points of work, we can do 25 points per sprint, will take 4 sprints (8 weeks) – you want it done in 6 weeks, will either require to be simplified or increased resourcing.”
>
> Need burn-down chart/progress status of sprints, features, initiatives, and milestones.
>
> During sprint planning, need a way to see what my team’s velocity has been last several sprints to have a good idea of how much we should be planning for upcoming sprint.
>
> Need an easy way to see how much I’m assigning to each team member during sprint planning (team members aren’t interchangeable – sprint can have user stories less than velocity, but if user stories are only doable by one team member then the work can’t get done).
>
> Need to be able to answer questions around “which teams/members are working on this feature?”, “are we still on track to meet this milestone?”, “we want to add this new feature, how will that slow down other development?”, “This team is needed for another project, how will that effect timelines on this project?”, etc...

A comprehensive analysis comparing GitLab to best-in-class team planning solutions is available to internal team members [here](https://internal.gitlab.com/handbook/product/best-in-class/plan/)


## Analyst landscape

What they are saying:

- Within the next few years, over 2/3 of organisations will adopt a product-centric delivery model and move away from project management practices.
- "Agile" adoption remains strong and shows no signs of slowing down.
- Successful project/product management solutions must function as part of the overall Value Stream Delivery Platform and serve as a hub for planning and measuring value delivery.
- Competitive products should also provide feedback in the form of qualitative and quantitative metrics such as customer value and satisfaction, delivery velocity and volatility, business outcomes, cycle times, and organizational effectiveness around adopting modern DevOps and "Agile" practices.


## Most requested issues

- [All users](https://gitlab.com/gitlab-org/gitlab/-/issues?sort=popularity&state=opened&label_name[]=group::project+management)
- [Customer / Customer Success](https://gitlab.com/gitlab-org/gitlab/-/issues?sort=popularity&state=opened&label_name[]=group::project+management&label_name[]=customer)
- [Dogfooding](https://gitlab.com/gitlab-org/gitlab/-/issues?sort=popularity&state=opened&label_name[]=group::project+management&label_name[]=Dogfooding)

## Top strategy items

While we are not currently working on the items listed within this section, we believe that solving for them will significantly contribute to [Plan's 3-year strategy](https://about.gitlab.com/direction/plan/#3-year-strategy). Once validated and team capacity is available, we will move these strategic items into our queue for prioritization and implementation.

### Enterprise planning frameworks support

- **[Custom Fields & Data Tables](https://gitlab.com/groups/gitlab-org/-/epics/235)**
  - _Outcome:_ Teams can extend the core issue experience with custom data to better integrate planning in GitLab to the team's business domain.
- **[Extensible work items](https://gitlab.com/groups/gitlab-org/-/epics/3354)**
  - _Outcome:_ Teams can extend and customize default work item types to align to their specific business context and activities that the team needs to collaborate on. 
- **[Swimlanes on Issue Boards](https://gitlab.com/groups/gitlab-org/-/epics/328)**
  - _Outcome:_ Provide teams with more flexibility to visualize their workflows by organizing issues in horizontal lanes across lists that group issues according to different contexts such as epics, assignees, milestones, and label.
  - _Progress:_ The MVC for [Epic Swimlanes](https://docs.gitlab.com/ee/user/project/issue_board.html#group-issues-in-swimlanes) shipped in 13.6.
- **[Real-time Boards](https://gitlab.com/groups/gitlab-org/-/epics/382)**
  - _Outcome:_ To allow teams to collaborate in real time on Issue Boards to improve the efficiency and effectiveness of planning and staying in sync on who is working on what.




### Use DevOps data to guide planning

- **[Cumulative flow diagrams](https://gitlab.com/gitlab-org/gitlab/-/issues/7629)**
  - _Outcome:_ Teams have an additional sensing mechanism to diagnose overloaded queues so they can better diagnose and improve process stability. This is currently blocked by the implementation of [configurable work item statuses](https://gitlab.com/groups/gitlab-org/-/epics/5099)
- **[Capacity planning and management](https://gitlab.com/groups/gitlab-org/-/epics/1686)**
  - _Outcome:_ When planning work within timeboxes, the team can take the variable of team capacity into account when decided how much scope to take on for a given period. 
- **[Integrating analytics on Issue Boards](https://gitlab.com/groups/gitlab-org/-/epics/1956)**
  - _Outcome:_ Teams can access burndown charts and cumulative flow diagrams specific to their team and directly within the context where they are planning and visualizing the flow of their work items.


### Automation and machine learning to improve quality of life

- **[Automation Framework](https://gitlab.com/groups/gitlab-org/-/epics/218)**
  - _Outcome:_ Teams can create automation sequences for transitioning issues to different statuses, updating meta data based on given events, and self-serve creating solutions to help improve efficiencies around Issue management.
- **[Configurable Workflows](https://gitlab.com/gitlab-org/gitlab/-/issues/2059)**
  - _Outcome:_ Teams can sequence types of issues through different workflows / statuses. For those compliance minded organizations, workflows will optionally support [tollgates](https://gitlab.com/gitlab-org/gitlab/-/issues/273760#note_439052044).


## Jobs To Be Done

We are currently focused on providing industry-leading solutions for the following [Jobs To Be Done (JTBD)](https://handbook.gitlab.com/handbook/product/ux/jobs-to-be-done/):


