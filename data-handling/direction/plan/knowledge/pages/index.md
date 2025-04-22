---
layout: markdown_page
title: "Category Direction - GitLab Pages"
description: GitLab Pages allows you to create a statically generated website from your project that is automatically built using GitLab CI and hosted on our infrastructure.
canonical_path: "/direction/plan/knowledge/pages/"
---

- TOC
{:toc}

## GitLab Pages

| | |
| --- | --- |
| Stage | [plan](/direction/dev/#plan) |
| Maturity | [Complete](/direction/#maturity) |
| Content Last Reviewed | `2025-02-06` |

### Introduction and how you can help

Thank you for visiting the Pages direction page for GitLab. GitLab Pages allows you to create a statically generated website from your project that is automatically built using GitLab CI and hosted on our infrastructure. This category belongs to the [Knowledge group](https://handbook.gitlab.com/handbook/product/categories/#knowledge-group) within Plan stage. This direction page is maintained by the Product Manager for Knowledge group, Matthew Macfarlane ([E-Mail](mailto:mmacfarlane@gitlab.com)). More information about Knowledge group's priorities can be found on the [Knowledge group direction page](/direction/plan/knowledge/).

This direction page is a work in progress, and everyone can contribute:

- [Issue List](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=Category%3APages)
- [Category Maturity Epic](https://gitlab.com/groups/gitlab-org/-/epics/7766)
- [Documentation](https://docs.gitlab.com/ee/user/project/pages/) 

### Current prioritization

GitLab Pages exists at the intersection of multiple stages of the DevSecOps lifecycle. The long-term vision for Pages is to provide an experience that guides and supports you through Create, Verify, Package, and Release to host static assets on the web, regardless of your level of development experience. 

[Parallel Deployments GA](https://gitlab.com/groups/gitlab-org/-/epics/10914) is the primary focus for Milestone 17.9. We'll evaluate other opportunities, such as [offer large paid storage limits on tiers](https://gitlab.com/gitlab-org/gitlab/-/issues/426601), and [offering audit logs](https://gitlab.com/gitlab-org/gitlab/-/issues/426604), in the future.

## Long-term vision for pages category

A future state of Pages could be described as a lightweight content management system (CMS), abstracting away the repository and git terminology in favor of WYSIWYG editing and more accessible publishing workflows. [Netlify](https://www.netlifycms.org/), [TinaCMS](https://tina.io/), and [Stackbit](https://www.stackbit.com/) have successfully bridged the gap between git-backed repositories of static assets and visual editing workflows accessible to all. The ideal user journey may look something like: 

- You, a developer, create a new project on GitLab from a template pre-configured to publish to Pages.
- You configure the domains, visibility permissions, customize the project's theme, and populate the initial content in the repository.
- You preview the site and merge your branch into `main`.
- The site publishes automatically to Pages after the build is complete.
- You invite your colleague to collaborate on the content.
- Your colleague, a Product Manager unfamiliar with Markdown, opens a page in the rich text editor and adds their contribution.
- The changes are available to preview immediately and your colleague is confident in their contribution so they submit for review.
- You review the changes, accept them, and merge them into `main`, triggering another Pages deploy. 
- The new page is published in seconds!

## Maturity Plan

Pages is currently at Complete maturity level. This maturity score was taken several years ago, and depending upon our available capacity and priorities we would like to conduct a new [category maturity assessment](https://gitlab.com/gitlab-org/gitlab/-/issues/360965) in FY26.

## Competitive Landscape

We are invested in supporting the process of developing and deploying code from a single place as a convenience for our users. Other providers, such as [Netlify](https://www.netlify.com/), deliver a more comprehensive solution. There are project templates available that offer the use of [Netlify for static site CI/CD](https://gitlab.com/pages?filter=netlify), while also still taking advantage of GitLab for repository, merge requests, issues, and everything else. GitLab offers configurable redirects, a well-loved featured of Netlify, made available in [Add simple redirect configuration](https://gitlab.com/gitlab-org/gitlab-pages/-/issues/24).

We are seeing a rise in [JAMStack](https://jamstack.org/) and static site generators partnering in the media. This trend toward API-first, affirms our modernization effort of Pages, reinforcing our cloud native installation maturity plan. 

GitHub also offers hosting of static sites with [GitHub Pages](https://pages.github.com/). Key differentiators between the two are: 

- GitHub Pages configuration and deployment is more "automatic" in that it doesn't require you to edit a CI configuration file.
- GitHub Pages has limits placed on bandwidth, builds, and artifact size where GitLab currently does not.

## Top Customer Issue(s) and Top Customer Success/Sales Issue(s)

The most popular customer issues are:

1. [GitLab Pages Multiple Deployments General Availability](https://gitlab.com/groups/gitlab-org/-/epics/10914): This feature is estimated to be delivered GA in 17.9.

## Top Internal Customer Issue(s)

GitLab dogfoods Pages extensively, most prominently as the hosting platform for [docs.gitlab.com](https://docs.gitlab.com). Our top internal customer issue is [GitLab Pages Multiple Deployments General Availability](https://gitlab.com/groups/gitlab-org/-/epics/10914), which is estimated to be released GA in November 2024 with our 17.7 or 17.8 release.

### Recent Accomplishments

- [Allow different job names for Gitlab Pages deploy job](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/166731)
- [Pages support for mutual TLS in GitLab API calls](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/134697)
- [Update Pages UI](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/134695)
- [Use GitLab pages without a DNS wildcard experimental](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/131947)
- [Support domain-level redirects](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/132386)
- [Improved Pages visibility in sidebar](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/132386)