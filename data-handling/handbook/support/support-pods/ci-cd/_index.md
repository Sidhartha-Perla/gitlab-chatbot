---
title: CI/CD Support Pod
description: Discuss CI/CD related tickets/issues, learn about CI/CD features and improve related documentation.
---

## Purpose

Discuss CI/CD related tickets/issues, learn about CI/CD features and improve related documentation.

## Scope

Topics in this pod will ideally align with these product groups:

- [Pipeline Authoring](/handbook/product/categories/#pipeline-authoring-group)
- [Pipeline Execution](/handbook/product/categories/#pipeline-execution-group)
- [Pipeline Security](/handbook/product/categories/#pipeline-security-group)

In the context of "CI/CD" it can be hard to pinpoint where exactly a problem fits in. This list is not meant to discourage anyone from seeking help in the pod – when in doubt, ask away! The worst that could happen is that someone suggest a better place for the question.

## Current objectives

- Keep regular meetings going
- Stay updated on all things CI/CD
- Help each other with CI/CD tickets!

## Support Pod members

- Lead: {{< member-by-name "Manuel Grabowski" >}} (`@manuelgrabowski`) (Interested in co-leading? Let me know!)
- {{< member-by-name "Cleveland Bledsoe Jr" >}} (`@cleveland`)
- {{< member-by-name "Ryan Kelly" >}} (`@rkelly`)
- {{< member-by-name "Elif Munn" >}} (`@e_munn`)
- {{< member-by-name "Edward Hilgendorf IV" >}} (`@edwardhilgendorf`)
- {{< member-by-name "Duncan Harris" >}} (`@duncan_harris`)
- {{< member-by-name "Alejandro Guerrero de Alba" >}} (`@alejguer`)
- {{< member-by-name "Segolene Bouly" >}} (`@sbouly`)
- {{< member-by-name "Charl Marais" >}} (`@cmarais`)
- {{< member-by-name "Sarah Crowle" >}} (`@sacrowle`)

## How to get involved

1. Talk with your manager.
1. Add CI to your knowledge areas in the [Support Team data](https://gitlab.com/gitlab-support-readiness/support-team/-/tree/master/data/agents?ref_type=heads). If it already exists, adjust your level accordingly.
1. Let your teammates and groupmates know about your new focus area.
1. Join the [#spt_pod_cicd](https://gitlab.slack.com/archives/C04DHQ91WJE) Slack channel.
1. Add yourself to this page.
1. Attend CI/CD pairing sessions if we can ever figure out how to work a calendar. See `Regular meetings` and check the GitLab Support calendar for up to date meeting times

## Regular meetings

- CI/CD Pod pairing session:
  - Mondays, 11:00 CET (09:00 / 10:00 UTC depending on DST, check the `GitLab Support` calendar)
  - Thursdays, 15:30 CET (13:30 / 14:30 UTC depending on DST, check the `GitLab Support` calendar)

## Collaboration channels

- Slack channel: [#spt_pod_cicd](https://gitlab.slack.com/archives/C04DHQ91WJE)

## Set up a CI/CD View in Zendesk

It's recommended to set up a personal view for all CI/CD related tickets.

1. Go to [Manage Views](https://gitlab.zendesk.com/admin/workspaces/agent-workspace/views)
2. Click Add View
3. Set up a view with the following parameters:
   - **Title**: CI/CD Pod
   - **Conditions**:
     - Tickets must meet all of these conditions to appear in the view:
       - Status is not Closed
       - Status is not Solved
       - Status is not pending
     - Tickets can meet any of these conditions to appear in the view:
       - Tags contains at least one of the following:
         - Add all `support_cicd_*` tags
         - Add `support_category_cicd`
   - **Columns** (Recommended but you can choose what you'd like):
     - Next SLA breach
     - Subject
     - Requester
     - Request date
     - Assignee
     - Priority
     - Organization
   - **Order by**:
     - Next SLA breach - Ascending
