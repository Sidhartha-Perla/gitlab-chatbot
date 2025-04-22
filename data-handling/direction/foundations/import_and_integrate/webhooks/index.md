---
layout: markdown_page
title: "Category Direction - Webhooks"
description: "This GitLab product category is focused on enabling integration with custom applications that GitLab's customers rely on. Find more information here!"
canonical_path: "/direction/foundations/import_and_integrate/webhooks/"
---

- TOC
{:toc}

## Webhooks

| | |
| --- | --- |
| Stage | [Foundations](/direction/foundations/) |
| Maturity | [Viable](/direction/#maturity) |
| Content Last Reviewed | `2025-04-07` |

### Introduction and how you can help

Thanks for visiting this category direction page on Webhooks in GitLab. This page belongs to the [Import and Integrate](https://handbook.gitlab.com/handbook/product/categories/#import-and-integrate-group) group of the Foundations stage and is maintained by the group's Product Manager, [Magdalena Frankiewicz](https://gitlab.com/m_frankiewicz) ([E-mail](mailto:mfrankiewicz@gitlab.com), [Calendly](https://calendly.com/gitlab-magdalenafrankiewicz/45mins)).

This direction page is a work in progress, and everyone can contribute:
 
- Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=Category%3AWebhooks&first_page_size=20) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=Category:Webhooks) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
 - Please share feedback directly via email, Twitter, or on a video call. If you're a GitLab user and want to discuss how GitLab can improve Importers, we'd especially love to hear from you.

### Strategy and Themes

<!-- Describe your category. Capture the main problems to be solved in market (themes). Describe how you intend to solve these with GitLab (strategy). Provide enough context that someone unfamiliar with the details of the category can understand what is being discussed. -->

Webhooks are a generic way for projects to be integrated with any other service. GitLab's APIs allow other services to reach in to our data, whereas Webhooks proactively send data to another service when certain events happen. These are increasingly important for external vendors, as they offer a key way to integrate with GitLab that doesn't require them building inside our codebase. Webhooks also give users, customers, and partners a more efficient pattern for receiving data triggered based on events, rather than inefficiently polling to see if any new events are available.

While we recognize the importance of robust webhook functionality for enabling integrations and partner ecosystems, the Import and Integrate team has prioritized migration capabilities for FY26 in alignment with GitLab's company objectives. This means that Webhooks will continue to remain in maintenance mode.

<!--
1 year plan for what we will be working on linked to up-to-date epics. This section will be most similar to a "road-map". Items in this section should be linked to issues or epics that are up to date. Indicate relative priority of initiatives in this section so that the audience understands the sequence in which you intend to work on them. 
 -->

### Webhooks Maintenance Status

For FY26, the Webhooks category will remain in maintenance mode due to the Import and Integrate team's focus on migration capabilities, within Importers category.

We will continue to:

- Maintain existing webhook functionality
- Support community contributions
- Address critical bugs and security issues

However, active development of new webhook features by the Import and Integrate team is not planned for FY26.

### Long-term Vision

In our long-term vision, we aim to:

1. Increase the robustness of our webhook offering
2. Align with other teams on how best to achieve an event-driven architecture
3. Make it easier to configure and maintain webhooks, troubleshoot issues, and redeliver events
4. Coordinate webhooks into usable workflows

Our customers should enjoy learning about and using our webhooks to design creative solutions and intelligent workflows, and be motivated to share GitLab as an example of an incredible third-party developer experience.

### Webhooks Development Guide

To facilitate future contributions and ensure consistency, we've created a comprehensive [Webhooks Development Guide](https://docs.gitlab.com/development/webhooks/) containing details on aspects like recommended payload schema, performance considerations, and flow of trigger and execution.
Please keep this guide in mind when implementing or reviewing changes to webhooks. This standardized documentation enables teams across different domains to implement their own webhook requirements while maintaining consistency with our established patterns. The guide also facilitates more community contributions by providing clear implementation standards and best practices.

### Community Contributions Welcome

We strongly encourage and welcome community contributions to the Webhooks category. The significant enhancements made in recent releases through community contributions, like [introducing changes to webhook self-healing behavior, which reduce manual intervention and improve reliability](https://about.gitlab.com/blog/2024/11/14/gitlab-webhooks-get-smarter-with-self-healing-capabilities/), demonstrate the value of this collaborative approach.

#### How to Contribute

If you're interested in contributing to Webhooks, please:

- Review the [Webhooks Development Guide](https://docs.gitlab.com/development/webhooks/)
- Look for open issues with the ~"Category:Webhooks" label

Feel free to reach out to the team directly if you need guidance or want feedback on your work by using the ~"group::import and integrate" label on your open merge requests

You can find the most requested improvements in this [list](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=popularity&state=opened&label_name%5B%5D=group%3A%3Aimport%20and%20integrate&label_name%5B%5D=Category%3AWebhooks&last_page_size=20&page_before=MjE) of most looked after improvements and the [epic](https://gitlab.com/groups/gitlab-org/-/epics/2318) gathering webhooks improvements themes.