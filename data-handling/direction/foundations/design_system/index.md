---
layout: markdown_page
title: "Group Direction - Design System"
description: "Explore GitLab’s design system, providing a unified framework for building consistent, intuitive, and accessible user interfaces across GitLab products."
---

- TOC
{:toc}

|                       |                               |
| -                     | -                             |
| **Stage** | [Foundations](/direction/foundations/) |
| **Maturity** | [Viable](/direction/#maturity) |
| **Last reviewed** | `2025-02-05` |

## Introduction and how you can help

Thanks for visiting this direction page on the Design System category in GitLab. This page belongs to the [Foundations Stage](https://handbook.gitlab.com/handbook/product/categories/#foundations-stage) and is maintained by [Jeff Tucker](https://gitlab.com/jtucker_gl).

This direction page is a work in progress, and everyone can contribute:

- Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues/?sort=weight&state=opened&label_name%5B%5D=Category%3ADesign%20System&first_page_size=20) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=Category:Design+System).
- Please share feedback directly via email or [on a video call](https://calendly.com/jtucker-gitlab/30min). If you contribute to Pajamas, the GitLab Design System, we'd especially love to hear from you.
- Learn more about the [Pajamas Design System](https://handbook.gitlab.com/handbook/product/ux/pajamas-design-system/) in the handbook, or go to [design.gitlab.com](https://design.gitlab.com/).

## Overview

The goal of the Design System category is to enhance efficiency and quality for product designers, engineers, and product managers by developing and maintaining an integral piece of UX, design, and frontend infrastructure.

As the GitLab product expands to include offerings for the entire DevSecOps lifecycle, it's critical to provide support for teams building a cohesive experience. To serve these needs, the Design System category defines guidelines, best practices, and provides resources that inform how teams design and build products.

There are two focus areas:

1. Pajamas Design System
1. Pajamas adoption across GitLab

### Pajamas Design System

The design system is a collection of resources, components, and guidelines used to make a consistent user experience in GitLab. Contributors focus on the building blocks that makes GitLab more usable, accessible, beautiful, performant, and robust. View Pajamas at [design.gitlab.com](https://design.gitlab.com/).

### Pajamas adoption across GitLab

The value of a design system is only realized when it's being used consistently and accurately in the product that consumes it. By focusing on component migrations (adoption), implementation, and tooling, the design system moves the product closer to using a single source of truth and increases our ability to make coordinated improvements.

## Strategy and themes

Our design system has matured. With a robust foundation and a dedicated stage group, we’re ready to expand beyond our traditional focus on efficiency and work towards a future where the design system is a leader in craft and enabler of product quality at GitLab. This means evolving both our systems and team to better facilitate quality contribution, fostering a shared language with engineering, and ensuring our foundational pieces fit together to support an elevated GitLab experience.

We will be focused on the following challenges in FY26:

* **Overemphasis on Components**: An overemphasis on individual components along with underemphasis on guidance for patterns and templates results in inconsistent implementations that undermine the overall product quality at GitLab.
* **High Effort for Contribution**: The design systems stage group lacks the capacity to maintain and improve all aspects of the design system independently. Contributions are crucial; however, the full process demands significant effort, causing some individuals to avoid it and others to bypass it entirely.
* **Platform Fragmentation and Ownership**: The design system spans three platforms with differing levels of ownership between UX, engineering and the design systems group. This reduces efficiency while adding a significant maintenance overhead.
* **Unclear Boundaries for Reusable Elements**: A lack of separation between the design system and other reusable elements creates a perception of quality, support, and stability that is not always accurate. There is no clear process for adopting locally-relevant components, causing confusion and leading to inappropriate one-off changes that pollute the system.

## 1 year plan

[**Improved dark mode**](https://gitlab.com/groups/gitlab-org/-/epics/2902)

Dark mode is a fan-favorite among software developers – the [original issue for dark mode](https://gitlab.com/gitlab-org/gitlab/-/issues/14531) collected nearly 1,000 positive reactions from the community. We introduced an alpha version of dark mode as a result of that work. However, we have some long-standing issues with our alpha that have kept us from driving adoption of dark mode (e.g. by respecting UA preferences for dark mode). We will revisit our current dark mode implementation once we have implemented design tokens for Pajamas and GitLab UI. Our key goal from this work will be to both improve the end-user experience for dark mode and to reduce the overhead on other GitLab teams that introduce new features.

[**Unified source of truth for the design system**](https://gitlab.com/groups/gitlab-org/-/epics/15339)

By consolidating all design assets, guidelines, and component documentation into a single, authoritative resource, we can eliminate discrepancies and reduce confusion among team members. This centralized approach will not only streamline workflows but also ensure that all stakeholders have access to the most up-to-date information, ultimately leading to a more cohesive and polished user experience.

[**Introduce more patterns and guidelines**](https://gitlab.com/groups/gitlab-org/-/epics/15264)

Expanding our Pajamas design system guidelines is essential for enhancing consistency and efficiency across GitLab's user interface. More comprehensive guidelines will provide clearer direction on component usage, accessibility standards, and interaction patterns, streamlining the design and development process. This will not only ensure a more cohesive user experience but also facilitate better collaboration between teams and faster onboarding of new members.

[**Measure and publish component health**](https://gitlab.com/gitlab-org/gitlab-services/design.gitlab.com/-/issues/1739)

Quality of individual components in Pajamas Design System varies and we do not have a way to communicate that maturity to consumers. By regularly assessing factors such as usage, performance, accessibility, and consistency with design principles, we can identify areas for improvement and prioritize updates effectively. Transparently sharing these health metrics not only fosters trust among users of the design system but also encourages collaborative efforts to enhance and refine components, ultimately leading to a more efficient and user-friendly product development process.

**Support frontend working groups**

Several teams across GitLab are contributing to [working groups](https://handbook.gitlab.com/handbook/company/working-groups/) that impact the GitLab frontend. While the Design System group does not specifically own these projects, we are actively supporting them:

* [Include axe automated accessibility checks in GitLab UI and write tests for components](https://gitlab.com/groups/gitlab-org/-/epics/11127) to increase accessibility coverage and compliance.
* [Migrate to Tailwind CSS](https://gitlab.com/groups/gitlab-org/-/epics/10980) to improve developer productivity and UI consistency. See [our architecture blueprint](https://docs.gitlab.com/ee/architecture/blueprints/tailwindcss) for more details.

## What we are currently working on

Watch our latest kickoff video to see our plans for the current milestone.


</figure>

## What we recently completed

* [Remove dependency on Bootstrap](https://gitlab.com/groups/gitlab-org/-/epics/13075)
* [Introduce design tokens](https://gitlab.com/groups/gitlab-org/-/epics/10238)
* 33 of GitLab groups have [achieved >95% Pajamas adoption](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/6610), with only 10 groups falling below the 95% threshold.
* We [reached a minimum of 50% dropdown component adoption per group](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/3885#note_1631721630).
* As part of the [Google summer of code](https://gitlab.com/gitlab-org/developer-relations/google-summer-of-code-2023/-/issues/5), we selected two intens who helped with component migrations over the summer.
* Add smart semgrep package and see if we can replace all 500 button components.
* 16.2 we completed  [research](https://gitlab.com/gitlab-org/ux-research/-/issues/2413) on our Pajamas Design System internal sentiment and are using this feedback to address our roadmap where we learned about how users interact with our design system. There are [5 key results](https://gitlab.com/gitlab-org/ux-research/-/issues/2413#what-did-we-learn) from the research and we will plan to address: reduce the load between 3 separate systems, address major gaps in documentation, and review the overall effort of contributions and how to make them easier.
* 16.0 we completed our latest [VPAT evaluation](https://gitlab.com/gitlab-org/gitlab-services/design.gitlab.com/-/merge_requests/3425) which included both the Section 508 and WCAG templates.
* In 15.8, we released [two new fonts](https://gitlab.com/groups/gitlab-org/-/epics/8972) into GitLab.
* In 15.7, we hit a milestone of having all tracked components in the pajamas adoption scanner and we now have a completed the `SCAN:SEMGREP` phase of our pajamas component spreadsheet. This means we have accurate counts to determine when we are done. Our MVC of the [Pajamas Adoption scanner](https://gitlab-org.gitlab.io/frontend/pajamas-adoption-scanner/) is also now out of "MVC" as we will look at capacity to schedule improvements to the UI.

## What is not planned right now

- Building and integrating all components across GitLab. The scope of this group is to provide guidance and governance for our design system and related tooling, and is staffed with dedicated product designers and engineers to support that. However, creating those components and implementing them throughout the application is a large effort that requires participation from every [group and category](https://handbook.gitlab.com/handbook/product/categories/).

## Roadmap

See our [roadmap in GitLab](https://gitlab.com/groups/gitlab-org/-/roadmap?state=all&sort=start_date_asc&layout=QUARTERS&timeframe_range_type=THREE_YEARS&label_name%5B%5D=group::design%20system&label_name%5B%5D=direction&label_name%5B%5D=Category:Design+System&progress=COUNT&show_progress=true&show_milestones=false&milestones_type=GROUP&show_labels=false).

## Target audience

Internal product designers, technical writers, engineers, and product managers.
