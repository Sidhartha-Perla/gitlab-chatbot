---
layout: markdown_page
title: "Category Direction - Notifications"
description: "Stay organized with GitLab’s notifications system, designed to keep teams informed and productive without overwhelming your inbox."
---

- TOC
{:toc}

|                       |                               |
| -                     | -                             |
| **Stage** | [Foundations](/direction/foundations/) |
| **Maturity** | [Minimal](https://handbook.gitlab.com/handbook/product/ux/category-maturity/category-maturity-scorecards/) |
| **Last reviewed** | `2025-02-03` |

## Introduction and how you can help



## Strategy and themes

People using GitLab can guide work throughout the entire DevSecOps lifecycle &mdash; from planning, to development, verification, and ultimately delivery. Having all of these capabilities within a single tool is powerful and efficient, yet requires users to stay up-to-date on changes and discussion happening across many parts of the product.

GitLab to-dos are the product experience intended to address this need. However they were designed to adhere to the GTD model: the only "notifications" we surfaced within GitLab were actionable tasks for the user. Our research has found that deciding what's actionable is a very personal, subjective question that varies by person &mdash; what some users find actionable, others find as noise, and vice versa. Instead, users want more visibility into their notifications so _they_ can decide which they need to act on.

In contrast, email notifications provide an exhaustive set of notifications for nearly every event that happens in GitLab. Some GitLab users have abandoned to-dos entirely in favor of email notifications, as this gives a more thorough way to stay up-to-date. While this gives them more visibility into events occuring in their projects, they must spend significant time each day processing their email inbox to avoid missing an update. Additionally, they are required to jump between email and GitLab as they triage and take action on notifications.

We want users to stay up-to-date within GitLab more efficiently than they could via any other tool. We will do this by:

* Surfacing the notifications they need directly within GitLab
* Creating an integrated experience between notifications and the actions they prompt
* Providing capabilities that allow them to focus on relevant notifications

This work will deliver value to GitLab and our users in three time horizons:

* Short term: improves the customer experience by allowing users to receive the personal notifications they need without context-switching out of GitLab. This will primarily impact customer satisfaction (CSAT) by addressing user challenges around staying up-to-date on work happening in GitLab. These improvements will also increase adoption of the existing To-Do List to ensure we can capture the value described in later stages.
* Medium term: gives GitLab an avenue to send in-app messages to users across installations for e.g. breaking changes. We relied heavily on email notifications to communicate the breaking changes to CI Job Token expiration, yet heard from customers that the messages got lost in administrators' inboxes. Customers stated they wanted to receive these notifications directly within the GitLab UI in the future. This capability will be generic enough to support a myriad of use cases beyond breaking changes, like upgrade notices and new feature announcements.
* Long term: centralizes all end-user notifications into a single framework, which both ensures a consistent approach for communicating with users, as well as providing us the framework to push personal notifications to any third-party tools customers use for communication. Integrations into third-party tools have a large impact on customer stickiness and retention, and with this work, we can ensure individuals are directly prompted to return to GitLab.

### Experience goals

The way each person uses the current email notification system and To-Do List features are highly personal. Our goal is to create a notification system that people can trust, and that's flexible enough to accomodate these many different ways of working.

The current To-Do List is used primarily by internal GitLab team members, but not by external customers. There are also issues with retention on the current To-Do List. With these improvement efforts, our focus is to increase customer usage and retention, and we are prioritizing efforts that will aid that longer-term goal. However, we will do our best to minimize the impact on internal users as we make these improvements, so as not to disrupt existing workflows.

### Ownership model

GitLab publishes email notifications and to-do items for features across the entire product suite. The ~"group::personal productivity" team does not have the subject matter expertise to make good decisions about the conditions that trigger these notifications or the content they contain. Instead, we expect the teams that raise these notifications to be responsible for the content and trigger conditions of their notifications. In general, we will determine ownership of notifications based on the primary topic of the notification (e.g. to-do items about a merge request will be owned by the ~"group::code review" team). The ~"group::personal productivity" team will be responsible for the overall structure and capabilities of the notifications system.
  
## 1 year plan

To begin, we will focus on the [Delaney (Development Team Lead)](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead) and [Parker (Product Manager)](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager) personas, as these are the two personas whose workflows will be most impacted by these changes. See [Target Audience](#target-audience) to learn how we will expand to support other personas.

Our key initiatives will include:

[**Mature the To-Do List experience**](https://gitlab.com/groups/gitlab-org/-/epics/14661)

We will iterate on the existing To-Do List during this phase, with each iteration available to all users. We intend to add features that have been highly-requested, and do not anticipate any need for breaking changes or deprecations. This includes features like:
        
* Snooze notifications (gitlab#17712)
* Automatically refresh/show new items in the not... (gitlab#23084)
* Give project/group notification grouping options (gitlab#413106)
* Bulk edit to-dos (gitlab#16564)

We will introduce few (if any) new to-do types during this phase to ensure we avoid overwhelming end users with a noisy inbox.

The end goal of this work is to improve weekly user retention for the existing To-Do List by providing the functionality users need to manage notifications effectively.

[**Rename "to-dos" to "notifications"**](https://gitlab.com/groups/gitlab-org/-/epics/14673)

Next, we will transition to using the word "notification" in the product instead of "to-do". We are doing this for two reasons:
        
1. The existing to-do list has relatively low customer adoption. When interviewing customers about this, we found that they didn't expect to find notifications in a "to-do list." When showing them the functionality that was there, they noted that it did meet many of their needs - they just would have never discovered it on their own.
1. The existing to-do list is not a to-do list: it does not provide any of the functionality users expect in personal task management software - features like creating new to-dos and breaking down existing ones, setting dates and priorities, and collaborating with others via comments and assignment. By freeing up the name "to-do", we give ourselves space to explore offering that sort of functionality in the future, possibly building on top of custom work items.

This will involve cross-stage changes, like updating the sidebar on issues and merge requests. Given the potential disruption these changes could cause to users, we will bundle these changes into a single public release. Once this goes live, we will market the change as "introducing web notifications".

The goal of this work is to increase weekly active users (WAU) of the To-Do List by making it more discoverable to end users.

[**Provide fine-grained control for web notifications**](https://gitlab.com/groups/gitlab-org/-/epics/13796)

Introducing more notifications into GitLab risks creating a new problem: making noise that distracts users from focusing on creating software. The types of notifications that users care about vary from person to person, so we need to provide tooling that allows users to tailor their notifications to exactly what they need to remain productive. Once this stage is complete, we will be able to introduce new notifications into the product while ensuring the notification list remains focused and action-oriented for our users.

[**Keep discussions in GitLab**](https://gitlab.com/groups/gitlab-org/-/epics/13580)

Team leads want to be notified of all comments in a discussion so they can take action even when they're not explicitly mentioned. Currently, GitLab only creates todos to review a comment when you are directly mentioned. This drives team leads rely on email notifications, which leaves them bouncing back and forth between GitLab and their email inbox.

GitLab users should be able to keep up with conversations within GitLab. We will introduce additional web notifications for replies to discussions you've participated in, and improve the behavior for automatically resolving notifications to work better with discussion threads.

[**Integrate broadcast messaging with the notification center**](https://gitlab.com/groups/gitlab-org/-/epics/14928)

You'll now have more control over important updates within GitLab, as we're enhancing broadcast messaging for admins. This improvement allows GitLab to communicate crucial information directly in the UI without hard-coding banners, and extends the functionality to GitLab.com administrators, ensuring you stay informed about essential updates while we work on reducing banner clutter for a better user experience.

[**Internal framework for notifications**](https://gitlab.com/groups/gitlab-org/-/epics/14087)

Currently, email notifications and to-dos are managed by completely separate systems. As we seek to gain parity between these channels, we need a way for teams to surface new notifications without having to do so in two places. This framework will enable teams to maintain the content and logic for their notifications without needing to deal with the underlying notification infrastructure.

We are working to track how these improvements impact people as we iteratively add them into GitLab. We will periodically conduct [UX Scorecards](https://gitlab.com/gitlab-org/gitlab/-/issues/456997) to assess the experiences. We are also working to create a [baseline metric](https://gitlab.com/gitlab-org/ux-research/-/issues/3148) for this experience that we can track over time. 

### Beyond 1 year

[**Quickly review a large volume of notifications**](https://gitlab.com/groups/gitlab-org/-/epics/13797)

Even with support for customizing notifications, people can still end up with a large inbox of notifications to review. We want to provide ways for users to quickly review a large volume of notifications. We are considering ideas like:

* Summarizing notifications with GitLab Duo
* More hueristics for automatically clearing irrelevant notifications
* Email digests

### What we recently completed

**Problem validation**

We have audited previous research, user comments, and internal explorations to understand the core challenges and opportunities in this space. We are now conducting light-weight user research to validate the key themes we uncovered before moving forward to address them.

**Initial design discovery**

We have designed an initial [full notification workflow](https://gitlab.com/gitlab-org/gitlab/-/issues/456349). We are continuing to refine this design, and to assess how we can iteratively introduce these proposed features into GitLab. 

### What is next for us

See our [roadmap in GitLab](https://gitlab.com/groups/gitlab-org/-/roadmap?state=all&sort=start_date_asc&layout=QUARTERS&timeframe_range_type=THREE_YEARS&label_name%5B%5D=group::personal%20productivity&label_name%5B%5D=direction&label_name%5B%5D=Category:Notifications&progress=COUNT&show_progress=true&show_milestones=false&milestones_type=GROUP&show_labels=false).

### What we are currently working on



## Target audience

Notifications are used by all users, so our long-term vision must accomodate a variety of needs. In order to make progress, we will focus on a subset of personas that have a pressing need to remain up-to-date with work happening in GitLab:

* [Parker (Product Manager)](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)
* [Delaney (Development Team Lead)](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)

Once we have created an experience that they love, we will broaden our focus to other people that use GitLab daily. We see the following personas as being our key targets in this second phase:

* [Presley (Product Designer)](https://handbook.gitlab.com/handbook/product/personas/#presley-product-designer)
* [Sasha (Software Developer)](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
* [Priyanka (Platform Engineer)](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
* [Rachel (Release Manager)](https://handbook.gitlab.com/handbook/product/personas/#rachel-release-manager)
* [Simone (Software Engineer in Test)](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
* [Amy (Application Security Engineer)](https://handbook.gitlab.com/handbook/product/personas/#amy-application-security-engineer)
* [Isaac (Infrastructure Engineer)](https://handbook.gitlab.com/handbook/product/personas/#isaac-infrastructure-security-engineer)
* [Alex (Security Operations Engineer)](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer)

## Best in class landscape

While Notifications doesn't represent a competitive category, the core user experience of GitLab will impact how well GitLab performs in the market. We take inspiration from others in the field that are delivering exceptional notification experiences.

**GitHub**

GitHub introduced their current notifications experience in [2020](https://github.blog/2020-04-22-improving-notifications-for-everyone/). They received significant praise for this upon launch, and we continue to hear requests from customers to bring an equivalent experience to GitLab. There are a few key details that we've noted as being particularly impactful:

* Allowing users to view notifications in the web or their email inbox, based on their preference
* Providing granular notification settings all the way down to the issue level
* Offering a slick mobile interface to support on-the-go conversations

**Linear**

The [founder and original designer](https://www.linkedin.com/in/karrisaarinen/) of Linear had years of experience as a designer before starting Linear, so it's no surprise their product is beautifully and thoughtfully designed. The [inbox view](https://linear.app/docs/inbox) is a core part of the Linear workflow, so it is a mature feature packed with innovative details:

* Master / detail view for efficient notification triage
* Keyboard actions to further speed up triage
* Snoozing notifications to follow up on them later

**GitDock**

Built by GitLab Team Member [Marcel van Remmerden](https://gitlab.com/mvanremmerden), [GitDock](https://gitlab.com/mvanremmerden/gitdock) is a MacOS/Windows/Linux app that displays all your GitLab activities in one place. Instead of the GitLab typical project- or group-centric approach, it collects all your information from a user-centric perspective.

**GitLight**

GitLight is an [open-source tool](https://github.com/colinlienard/gitlight) for managing notifications from GitHub and GitLab in a single interface. Like GitDock, this tool is building on top of the concepts offered by GitLab to create new experiences. It has some advanced concepts that make it stand out:

* Kanban-like interface for notifications
* Grouping of notifications by issue
* Sophisticated system for prioritizing notifications based on user-defined rules

**Honorable mentions**

Notification experiences are not unique to developer tools &mdash; they're a common feature in collaboration software. We're looking beyond tools in our space to see how other domains are solving this problem as well.

* Slack & various Slack apps
* Almanac.io
* HEY.com