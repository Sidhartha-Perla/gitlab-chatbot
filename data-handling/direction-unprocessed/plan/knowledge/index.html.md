---
layout: markdown_page
title: "Group Direction - Knowledge"
description: "Knowledge group direction page focusing on wiki, pages, markdown, and text editors"
canonical_path: "/direction/plan/knowledge/"
---

- TOC
{:toc}

## Knowledge group

| | |
| --- | --- |
| Stage | [Plan](/direction/plan/) |
| Content Last Reviewed | `2025-02-06` |

### Introduction

Welcome to the Knowledge Group direction page! Knowledge Group is in the Plan Stage of GitLab and contains the Wiki, Pages, Markdown, and Text Editors categories. Knowledge Group also manages the development of [GitLab Query Language](https://gitlab.com/groups/gitlab-org/gitlab-query-language/-/wikis/home) (GLQL), as well as Views, powered by GLQL. These categories, and GLQL, fall within the [knowledge management](https://www.gartner.com/reviews/market/knowledge-management-software) (KM) market as defined by Gartner. The focus of KM is to provide visibility and access to a flow of information across a variety of operations, enabling collaboration that has traditionally existed in silos. Commonly used products in the KM market include [Confluence](https://www.atlassian.com/software/confluence), and [Notion](https://www.notion.so/product). 

If you have feedback related to Knowledge Group please comment and/or contribute in these [Issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Aknowledge&first_page_size=20), or create a new issue if you find none fit your criteria. Make sure to tag `@mmacfarlane`, Product Manager for Knowledge Group, so he can read and respond to your comment. Sharing your feedback via Issues is the one of the best ways to contribute to our strategy and vision! 

### Our vision and current work

At GitLab, our [vision](https://about.gitlab.com/company/vision/) is to become the AllOps platform, a single application for all innovation.  Knowledge Group plays a pivotal role in this transformation by breaking down silos and enabling seamless collaboration across teams and roles. Here's how our Knowledge Group categories drive this vision forward:

Pages: GitLab Pages transforms web hosting by making it accessible to users of all skill levels. Our new Parallel Deployments feature significantly reduces deployment times and eliminates bottlenecks, letting you publish updates faster than ever. For teams managing multiple sites, we aim to develop robust user authentication and comprehensive audit logging to provide better security and governance. These improvements will give content teams more control while maintaining the technical flexibility developers love.

Text Editors and Markdown: Transform how your teams collaborate with GitLab's dual editing experience. Choose between our enhanced Rich Text Editor for intuitive WYSIWYG editing, or stick with our Plain Text Editor which used Markdown for precise control (both seamlessly integrated across the entire platform). Technical teams can work efficiently in Markdown while non-technical team members can use familiar formatting tools, all contributing to the same content. Switch between editors anytime, giving every user the flexibility to work their way. With advanced capabilities and lightning-fast performance in both editors, GitLab adapts to each user's preferences while maintaining consistency throughout your workflows. This unified yet flexible experience eliminates context switching and brings your entire organization into the same collaborative environment.

Wiki: GitLab's Wiki brings your documentation directly into your development workflow, making knowledge sharing natural and efficient. Create, edit, and collaborate on documentation using familiar tools - whether you prefer Markdown or our Rich Text Editor. New features like PDF export let you share documentation beyond GitLab, while customizable templates help teams maintain consistency. We're also experimenting with Wiki comments, enabling teams to discuss and refine documentation without leaving the context of their work. Based on extensive user research, these improvements transform GitLab's Wiki from a simple documentation tool into an integral part of your team's daily workflow.

### What we recently completed

Text Editors and Markdown: [Rich Text Editor: Release Rich Text Editor Generally](https://about.gitlab.com/releases/2023/07/22/gitlab-16-2-released/#:~:text=The%20rich%20text%20editor%20is%20a%20new%20way%20of%20editing,can%20follow%20our%20progress%20here.), [Display and Edit Markdown Comments in the Rich Text Editor](https://gitlab.com/gitlab-org/gitlab/-/issues/342173), [Insert Table of Contents in the Rich Text Editor](https://gitlab.com/gitlab-org/gitlab/-/issues/366525).

Wiki: [Draw.io/diagrams.net integration with wiki](https://gitlab.com/gitlab-org/gitlab/-/issues/20305/?_gl=1*lfhu8t*_ga*MTU5MDI5ODc5NS4xNjY1NTkyMzcy*_ga_ENFH3X7M5Y*MTY4MTQwNDI2MC40MDYuMS4xNjgxNDA1MzI3LjAuMC4w), [Editing Sidebar in Project or Group Wiki Removes Existing Sidebar](https://gitlab.com/gitlab-org/gitlab/-/issues/378028),Relative Links are [Broken On Wiki ASCII Pages](https://gitlab.com/gitlab-org/gitlab/-/issues/377976), [templates in wiki](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/133279), and [autocomplete](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/133281).

Pages: [GitLab Pages without DNS Wildcard](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/131947) and [GitLab Pages Parallel Deployments Beta](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/132384).

### What we are currently working on

Pages: [GitLab Pages Parallel Deployments GA](https://gitlab.com/groups/gitlab-org/-/epics/10914)
 
Rich Text Editor: [Enabling the rich text editor across GitLab](https://gitlab.com/groups/gitlab-org/-/epics/10378)

Wiki: [GLQL implementation in GitLab, including Wiki](https://gitlab.com/groups/gitlab-org/-/epics/14767), [Wiki Comments GA](https://gitlab.com/groups/gitlab-org/-/epics/14062)

### Competitive analysis and best-in-class landscape

GitLab's Knowledge tools break down information barriers by bringing documentation, planning, and collaboration into your development workflow. Unlike standalone solutions like Confluence, Notion, or GitHub, GitLab integrates knowledge sharing directly where work happens. Our unified platform combines powerful documentation capabilities through Pages, flexible editing with both Markdown and Rich Text, and collaborative Wikis - all in the same place where you plan, code, and deploy. This integration eliminates the context switching and fragmentation that comes from managing knowledge across multiple tools, making information naturally discoverable and actionable.

Pages: We are invested in supporting the process of developing and deploying code from a single place as a convenience for our users. Other providers, such as Netlify, deliver a more comprehensive solution. There are project templates available that offer the use of Netlify for static site CI/CD, while also still taking advantage of GitLab for SCM, merge requests, issues, and everything else. GitLab offers [configurable redirects](https://gitlab.com/gitlab-org/gitlab-pages/-/issues/24), a well-loved feature of Netlify, made available in gitlab-pages. We are seeing a rise in JAMStack and static site generators partnering in the media. This trend toward API-first, affirms our modernization effort of Pages, reinforcing our cloud native installation maturity plan. GitHub also offers hosting of static sites with GitHub Pages. Key differentiators between the two are that GitHub Pages configuration and deployment is more "automatic" in that it doesn't require you to edit a CI configuration file, and that GitHub Pages has limits placed on bandwidth, builds, and artifact size where GitLab currently does not.

Wiki: We currently most closely compete with GitHub Wiki but we would like to compete with Confluence, Notion, Roam Research, and Google Docs. We've heard from customers that managing wikis with tens of thousands of pages can be challenging. And while a full-featured product like Confluence has advanced features and integrations, the GitLab wiki would be a stronger competitor if we improved our sidebar structure and parity between Group and Project Wikis.