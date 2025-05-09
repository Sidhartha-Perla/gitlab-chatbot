---
title: "Milestones project management guidelines"
---

{{< include "includes/wip-notice.md" >}}

## Background

There are two concepts of time-based tracking in GitLab.

* [Milestones](/handbook/marketing/project-management-guidelines/milestones/#milestones): useful for tracking the progress of multiple issues across a specific time period, and when planning and managing epics.
* [Iterations](/handbook/marketing/project-management-guidelines/milestones/#iterations): useful for planning agile or agile-like sprints to capture action items to be completed within a specific time period.

## Milestones

[Milestones](https://docs.gitlab.com/ee/user/project/milestones/) are a great way to track the progress of multiple related issues across a specific time period.  With milestones, you can see how fast issues are being completed in that time period ([burndown chart](https://docs.gitlab.com/ee/user/project/milestones/burndown_and_burnup_charts.html)), and you can view the issues grouped by labels, and grouped by status (unassigned, assigned, and completed)

Milestones are **very useful** when tracking the progress of multiple issues and when planning and managing epics.

![Milestone4](/images/marketing/project-management-guidelines/milestone.png)

Here are two examples of milestones:

1. [Product and Solution Marketing Quarterly Milestone](https://gitlab.com/gitlab-com/marketing/product-marketing/-/milestones/6) - showing the bulk of strategic marketing work for a given quarter.
1. [UseCase Monthly Sprint Milestone](https://gitlab.com/gitlab-com/marketing/product-marketing/-/milestones/12)

### Key things to know

1. Milestones can be created at **both** `Project` and `Group` levels.
1. Milestones can be used to establish dates for epics (where the epic inherits the dates from the issues and associated milestones)
1. Milestones set a date range (start date and end date)
1. Issues are added to milestones
1. Milestone lists can be sorted **only** by **name** and **date** (either `due date` or `start date`)

### Known limitations

1. Milestone lists **cannot be filtered** and have limited sorting
1. Milestones **do not have labels** and cannot be filtered by labels
1. Milestones **do not track history of changes** or **who created/changed** the milestone
1. On issues - when adding an issue to a milestone, the list of milestones is **ALL** of the milestones in that project and the parent groups (potentially LOTS AND LOTS of milestones)
1. On groups - the list of milestones is **ALL** of the milestones defined in that group and below that group (potentially LOTS AND LOTS of milestones) - [This feature request addresses this limitation.](https://gitlab.com/gitlab-org/gitlab/-/issues/214652)
1. On Projects - the list of milestones is **ONLY** the milestones defined in that project (deceptively very few milestones.) see [feature request](https://gitlab.com/gitlab-org/gitlab/-/issues/214901)

## Guidelines

### Define milestone at lowest level needed

Define milestones at the LOWEST level of the organization as possible.

* If the milestone ONLY applies to a specific project, then create the milestone there
* If the milestone applies to a group of projects, then create the milestone at the lowest possible group.

This will mean that the lists of milestones available to a given Issue (when adding an issue to a milestone) will be limited to a smaller list of relevant milestones. (though the list might still be very long)

### Milestone Naming Convention - prefix in name

Because of the filtering limitations and the massive volume of potential milestones, a consistent **Naming Convention** is very, very, very helpful in finding the right milestones.

* All Milestone names should start with either the group or project abbreviation. The recommendation is to prepend the name with a two-letter abbreviation followed by underscore: `gg_`.

For example:

* A **project** milestone in the **"Revenue Marketing"** project should be named:
  * `**rm_**Milestone Name`
* A **group** milestone in the **"Product and Solution Marketing"** group should be named:
  * `**sm_**Milestone Name`

This will help in two ways.  First, when looking at lists of milestones, they can be sorted and put the related milestones together.   Second, in issues, when adding a milestone, you can search by name, which will make it easy to find the right subset of milestones (either for the project or group)

### Milestone Description - Include milestone history and who owns

Because the milestone does not yet include change history or details about who created it or why, we should use the description field to fill in the blanks.

* In the description field describe the purpose of the milestone and who is milestone owner/manager

### Milestones Details

* **Use for**: larger units of work (in scope and duration) that resemble a release. E.g. an executive topic or campaign
* **Implement with**: [milestones](https://docs.gitlab.com/ee/user/project/milestones/)
* **Time and duration**: variable
* **Naming convention**: `teamprefix: MilestoneName`
* **Issue management**: via workflow and iteration issue boards
* **Scope**: default to lowest scope. Define at the [top `marketing` group](https://gitlab.com/groups/gitlab-com/marketing/-/milestones/) for executive topics and integrated campaigns.

![Project Milestone](/images/marketing/project-management-guidelines/project-milestones.png)

Recommended dates and duration: it depends, though shorter is often better. Because the milestone has dates for start and finish, the implication is that issues and MRs in the milestone are completed in this time window.  If the milestone window is 3 weeks, then the expectation is that the work in the milestone is completed in that time frame.

Every team and every project is unique and there is no one answer for milestone duration.  Some teams have had milestones as long as a quarter, others 4 weeks and others 1 week.  Choose the duration that works for your team, learn, and evolve.

## Iterations

### Define iterations at highest level required

Define iterations at the HIGHEST level required of the organization as possible (for a cohesive approach using the same time-basis).

### Iteration Naming Convention - Mktg in name

A consistent **Naming Convention** is helpful to ensure similar iterations (i.e. not including `Mktg:` are used by only the Marketing department at GitLab.

### Iterations Details

* **Use for**: planning agile or agile-like sprints to capture tasks/user stories that can be completed within the iteration.
* **Implement with**: [iterations](https://docs.gitlab.com/ee/user/group/iterations/)
* **Time and duration**: 2 weeks, from Mondays to the following Sunday
* **Naming convention**: `Mktg: YYYY-MM-DD`, with the ISO-formatted date being the **end date** of the milestone. `Mktg:` allows for filtering to only the Marketing-wide iterations, and the ISO date can help further filtering on month/day when assigning the milestone to an issue.
* **Issue management**: via [workflow](/handbook/marketing/project-management-guidelines/boards/#workflow-board) and [iteration](/handbook/marketing/project-management-guidelines/boards/#iteration-board) issue boards
* **Scope**: defined at the [top `marketing` group](https://gitlab.com/groups/gitlab-com/marketing/-/milestones/), essentially for executive topics and integrated campaigns, but it is encouraged that all groups in Marketing use this one set of iterations for a unified workflow. These are the only iterations that will be defined at this level.

![Iterations](/images/marketing/project-management-guidelines/iterations.png)

### Backlog

* **Use for**: issues that are either not ready to be scheduled or not planned yet. Also as a bucket to choose and schedule issues for the next iteration(s) or milestone(s)
* **Implement with**: [milestones](https://docs.gitlab.com/ee/user/project/milestones/) at present.
* **Time and duration**: undefined. Start and due dates are not set.
* **Naming convention**: `Backlog`
* **Issue management**: see TBD: backlog refinement
* **Scope**: defined at the [top `marketing` group](https://gitlab.com/groups/gitlab-com/marketing/-/milestones/). When scheduling backlog issues on an issue board or on an issue list, the backlog can be further filtered by team.
