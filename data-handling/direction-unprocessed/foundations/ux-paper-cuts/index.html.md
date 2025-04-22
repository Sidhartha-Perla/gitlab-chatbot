---
layout: markdown_page
title: Product Direction - UX Paper Cuts
description: "The UX Paper Cuts team is responsible for identifying and fixing small but impactful usability issues in the GitLab product."
---

## On this page
{:.no_toc}

- TOC
{:toc}

## UX Paper Cuts overview

The UX Paper Cuts team has a unique scope; we are responsible for identifying and fixing small yet impactful usability issues across the GitLab product. The term “paper cut” refers to a small usability or accessibility issue that can cause annoyance or frustration for our users and customers. In aggregate, these paper cuts can impact the overall impression users have of the product and brand.

## Mission and vision

The UX Paper Cuts team continuously improves the user experience by addressing small usability, accessibility and design consistency issues. By focusing on small details across the entire product, the team helps create a more polished and user-friendly interface, leading to increased user satisfaction, engagement, and ultimately a more successful product.

## What we work on

- By default, the UX Paper Cuts team does not take on new feature work, nor is the team used as a resource for another Group. Instead, the team focuses on usability and accessibility issues, design inconsistencies, and out-of-date UI across the entire product.
- The typical or canonical UX paper cut is a small or seemingly insignificant problem that can cause annoyance or frustration for users but paper cuts can at times be larger in scope, and for these the team partners with Product and UX Research.
- Like the [Personal productivity team](https://handbook.gitlab.com/handbook/engineering/development/dev/manage/personal_productivity/), UX Paper Cuts doesn’t work within a specific product area, but across the product as a whole.
- UX Paper Cuts work can look like (smallest to biggest):
  - A small paper cut such as migrating components to the [Pajamas design system](https://design.gitlab.com/), improving product accessibility and increasing design consistency.
  - A larger design change to a component or feature.
  - A series of many similar paper cuts and design updates with a theme. See [accessibility](https://gitlab.com/gitlab-org/gitlab/-/issues/424396).
  - Helping to refresh an entire product area. See [Settings UI](https://gitlab.com/gitlab-org/gitlab/-/issues/398215).

## How we work

- Each [UX Paper Cuts designer](https://handbook.gitlab.com/job-families/product/product-designer/#ux-paper-cuts-specialty) is responsible for all the design and development updates needed to fix the paper cut, acting as a [manager of one](https://handbook.gitlab.com/handbook/leadership/#managers-of-one).
- The team finds or receives paper cuts from around the product and maintains their own roadmap without a PM or engineers.
- The team collaborates with Groups responsible for their areas of the product, acting as an informed partner.
- The UX Paper Cuts team does not have the final say on work done by a Group and does not override decisions by a Group.

## How we plan

DRI: Manager of Product Design

- The UX Paper Cuts team updates our plan quarterly and follows a yearly roadmap.
- The team works in monthly [milestones](https://about.gitlab.com/releases/), each with a specific theme.
- The aim of using themes in milestones is to focus the work in one area (vs spreading paper cuts across the whole product), increasing the chances it will have an noticeable impact for our users.
- Examples of themes include:
   - Areas of high traffic.
   - Areas that don't currently have design resources.
   - Areas that are out-of-date or are inconsistent in their use of our design guidelines or design system.
   - Areas that are deprioritized by a PM or where we are invited in to help by a PM.
   - Areas with recent feature releases.
- The goal is to always be planning 3 milestone in advance (in quarterly planning issues e.g. like [this one](https://gitlab.com/gitlab-org/foundations/ux-paper-cuts/team-tasks/-/issues/31 "FY26 Q2 Paper Cuts Quarterly Planning (covers milestones 18.1, 18.2, 18.3)")).
- We will solicit theme ideas from counterparts and keep a [list of milestones and potential milestones](https://gitlab.com/groups/gitlab-org/-/epics/16631 "✂ UX Paper Cuts").
- We will review the backlog of issues, feedback, research, and bug reports to map them to the upcoming themed issues.

## How we communicate

DRI: Manager of Product Design

- Our default is to communicate the milestones to the product team in the `#product` Slack channel, and ensure Groups affected by any particular theme or issue are aware of the upcoming milestones.
- We try to ping the relevant Group again a week before the planned milestone starts.
- We will also ping the stage group PM and designers (if there are any) on the larger paper cuts work before the work starts, and ask for input to give Groups more awareness of upcoming work.
  - Note: the UX Paper Cuts team is designed to move quickly and not get locked into the red tape and thus doesn't need explicit approvals before work.
   - We do however have to have high confidence in our solutions.
   - We have to ensure we're not introducing something that goes in the opposite direction the PM has set.
   - And if UX Paper Cuts is working on something with lower confidence (or no data) then we do have to validate first (via PM, UX research, feature flags, etc.) before creating MRs.

## How we collaborate

DRI: UX Paper Cuts designers

- All UX Paper Cuts team members work from the same milestone planning document and are responsible for adding and describing upcoming issues or tasks, so we can communicate and collaborate with affected Groups in advance.
- Since we work in other Group's areas, we make an extra effort in our MR descriptions. We explain the what and the _why_ behind the proposed changes.
- Each team member will make sure designer and engineer in affected Group is either set as a merge request reviewer or pinged in a thread for awareness (each Group can decide their preference).
- The UX Paper Cuts team will pre-plan most of the work for each milestone and spend the majority of the milestone working on work related to the theme.
- On larger changes, the UX Paper Cuts team will meaningfully communicate and collaborate with affected Groups, ensuring they are aware of upcoming work and are given the opportunity to participate in solutions.
- The UX Paper Cuts team will monitor feedback after MRs are merged and continue to update and support that work.
- The UX Paper Cuts team will follow our standard development practices including updating front-end tests.

## Where we look for UX paper cuts (and how to send them to us)

- [Paper Cuts Possibilities issue](https://gitlab.com/gitlab-org/gitlab/-/issues/417911 "💬 Paper cuts possibilities & requests")
- Issue labels
  - [Issues labeled `UX Paper Cuts`](https://gitlab.com/groups/gitlab-org/-/issues/?label_name%5B%5D=UX%20Paper%20Cuts)
  - [Open UX bugs](https://gitlab.com/groups/gitlab-org/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=bug%3A%3Aux&first_page_size=100)
  - [Sev 4 UX issues](https://gitlab.com/groups/gitlab-org/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=UX&label_name%5B%5D=severity%3A%3A4&first_page_size=100)
- UX Research: SUS verbatim, CSAT verbatim and Usability Benchmarks reports
  - Past examples include:
    - [Q1 FY24 SUS Verbatim Product Level Analysis - Papercut Possibilities](https://gitlab.com/gitlab-org/ux-research/-/issues/2429 "📘 Q1 FY24 SUS Verbatim Product Level Analysis - Papercut Possibilties")
    - [Q2 FY24 SUS Verbatim Product Level Analysis - Papercut Possibilities](https://gitlab.com/gitlab-org/ux-research/-/issues/2611 "📘 Q2 FY24 SUS Verbatim Product Level Analysis - Papercut Possibilties")
    - [Q3FY23 Secure Stage Benchmarking Report](https://docs.google.com/presentation/d/1qJ6u0llZfwcwu60axRHVirQCdRhTKvroXvvDc9Awc3A/edit#slide=id.p1)
    - [FY24-Q3 Quarterly Navigation Survey Insight: Address potential Paper Cuts candidates related to the GitLab navigation](https://gitlab.com/gitlab-org/ux-research/-/issues/2823 "FY24-Q3 Quarterly Navigation Survey Insight: Address potential Paper Cuts candidates related to the GitLab navigation")
- Posts in `#is-this-known` Slack channel
- Posts in `#g_ux_paper_cuts` Slack channel
- Twitter / X 
- Customer feedback

You can find changes made by UX Paper Cuts by following along in the [GitLab UI Polish Gallery](https://papercuts.gitlab.com/), the internal Slack channel `#ux_paper_cuts_mrs`, or by searching the GitLab label [UX Paper Cuts](https://gitlab.com/groups/gitlab-org/-/merge_requests/?sort=updated_desc&state=opened&label_name%5B%5D=UX%20Paper%20Cuts&first_page_size=100).