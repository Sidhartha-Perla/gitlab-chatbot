---
title: "Labels project management guidelines"
---

{{< include "includes/wip-notice.md" >}}

## Background

[Labels](https://docs.gitlab.com/ee/user/project/labels.html) are a powerful, flexible way to categorize epics, issues, and merge requests.

When applied appropriately and consistently, Labels enable GitLab users to discover, filter, manage, and report on issues, projects, or epics.

### Key things to know

#### Label hierarchy

There are two types of labels in GitLab:

- **Project labels** can be assigned to issues and merge requests in that project only.
- **Group labels** can be assigned to epics, issues and merge requests in any project in
  the selected group or its subgroups.

*([Learn more](/handbook/marketing/project-management-guidelines/groups/) about Groups and Projects)*

#### Label exclusivity

By default, Labels are not exclusive. An epic, issue, or merge request can be labeled multiple times by multiple people,
supporting many different use cases and views. The exception to this rule is the Scoped Label, which specifies a set of mutually
exclusive Labels. When one Scoped Label is applied, it automatically replaces any previous Label in that set. Scoped Labels are used
to assign status, support workflows, or otherwise segment items into "either / or" situations.

![Multiple Labels per issue](/images/marketing/project-management-guidelines/labels-multiple.png)

### Known limitations

## Guidelines

### Create Labels at the lowest possible level

Since Group-level labels cascade to every sub-group and project beneath them, unrestricted Group-level label creation can cause confusion
and clutter. For example, if multiple teams create 'high priority' labels at the group level, all of them would show up in the Label menu for
every project within the group.

Group-level Labels should *only* be used for tracking at the Group level, across multiple projects and/or subgroups. Examples of appropriate
group-level labels include:

1. Executive Interest labels (e.g. **CMO**, **CEO**, etc.). This indicates the epic or issue is an executive interest item and enables reporting and visibility of related issues and epics.
1. Executive Priority (**CMO-priority::1**, **CMO-priority::2**, etc.). These labels help the organization understand the priority of issues - mainly used by CMO Staff to communicate priority on CMO"s behalf.
1. Executive Theme (**CMO::Agility**, **CMO::Efficiency**, **CMO::Commit**, etc.). This small list of scoped labels help to flag specific CMO Interest themes based on top level initiatives and areas of focus
1. "Team" Labels. (**Product and Solution Marketing**, **Corporate Marketing**, etc.). This allows high-level work tracking within the greater Marketing organization.

If you are unsure whether you should create a group-level label or a project-level Label, **err on the side of caution and create a project-level Label**.
You can always promote it to a group-level Label in the future.

### Limit Label name character count

When creating a Label name, use the smallest possible number of characters. Labels longer than 25 characters may be truncated in the GitLab UI.

### Provide detailed descriptions

When you create a Label, ensure that the Description field contains the following information:

- When the Label should be applied
- Purpose or Goal
- DRI

This information will be presented in a tooltip above the Label throughout the UI.

### Group like Labels with naming conventions

If you are creating a collection of related Labels, group them using common prefix in the name. For example, if you are creating 'West' and 'East' to
describe territories, consider Labels such as 'Sales_Region_West' and 'Sales_Region_East' instead. This will provide immediate context to observers while
also grouping your Labels together in the UI.

### Templatize Label creation

Labels only work properly when they are applied consistently. Wherever possible, automate the creation of appropriate Labels by adding them to
[Issue templates](https://docs.gitlab.com/ee/user/project/description_templates.html#create-an-issue-template).

![Sample scoped labels](/images/marketing/project-management-guidelines/labels-template.png)

### Apply Scoped Labels to remove confusion

To minimize clutter and reduce the possibility of incorrect double-counts, always consider creating Scoped Labels to automate Label management,
rather than depending on users to remove invalid labels as they assign new ones.

![Sample scoped labels](/images/marketing/project-management-guidelines/labels-scoped.png)

### Automate Label Hygiene

The Triage Bot is an open source project that makes it possible to automate many issue and merge request hygiene tasks to ensure that your projects
are more consistently following a process. Use the [Triage Bot scripts](/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/getting-started/105/)
to minimize the impact of human error, automating proper Labeling and workflow. Common uses of the Triage Bot include identifying missing or improperly
applied Labels, notifying issue or merge request owners of Label-related problems, and applying Labels based on predefined criteria.

For more information, please refer to @johnjeremiah's [YouTube tutorial](https://www.youtube.com/watch?v=Tp79e5sgpao).

### Don't Delete, Deprecate

Deleting a Label will remove all prior associations of that Label with issues or merge requests, which can, in turn, break dependencies. All Label deletions
should be performed by the Label's DRI (should be listed in the Label description, as stated above).

If you are the DRI and wish to delete a Label, follow the following steps:

- Append the 'DEPRECATE_' tag to your Label (e.g., 'pMm' becomes 'DEPRECATE_pMm').
- Socialize the change within your group.
- Wait a calendar month before deleting the Label.
