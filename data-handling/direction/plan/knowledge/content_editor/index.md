---
layout: markdown_page
title: "Text Editors and Markdown Direction"
description: "This page dives into the Text Editors and Markdown direction."
canonical_path: "/direction/plan/knowledge/content_editor/"
---

- TOC
{:toc}

## Text Editors and Markdown

| | |
| --- | --- |
| Stage | [plan](/direction/dev/#plan) |
| Content Last Reviewed | `2025-01-09` |

### Introduction and how you can help

Thanks for visiting the Text Editors and Markdown direction page. Text Editors category contains the rich text editor (RTE) and the plain text editor (PTE). The RTE is a what-you-see-is-what-you-get (WYSIWYG) editor for Markdown content maintained by [Knowledge group](https://handbook.gitlab.com/handbook/product/categories/#knowledge-group). The RTE is a cornerstone of Knowledge group's contribution to helping GitLab become an [AllOps platform](https://handbook.gitlab.com/handbook/company/vision/). Much of this direction page will focus on the RTE and its development. More information about Knowledge grouo priorities and direction can be found on the [Knowledge group direction page](/direction/plan/knowledge/), and additional questions can be directed to Matthew Macfarlane, Product Manager in the Plan Stage for Knowledge group ([E-Mail](mailto:mmacfarlane@gitlab.com)).

### Who is the RTE built for?

**Everyone!**

For many, writing in Markdown is a barrier to collaboration. We recognize that as GitLab grows, so does the need for a more usable editing experience. Traditionally, we have served developers, but over time, we have begun serving more non-technical users. Remembering the syntax for image references or working with long tables can be tedious, even for those who are relatively experienced with the syntax. Still, Markdown as a common denominator for content enables efficient collaboration in a version-controlled environment. The RTE aims to break down these barriers by providing a rich editing experience and an extensible foundation on which we can build custom editing interfaces for things like diagrams, content embeds, media management, and more.

There are many contributors to GitLab for whom writing Markdown is like writing a second language. We don't want to take that super power away from anyone. That's why writing in the RTE will support standard Markdown shortcuts. For example, typing `## ` followed by your content will create a rendered Header 2 and let you continue working without removing your fingers from the keyboard.

### Where can I use the RTE?

We started by implementing the RTE  in the GitLab Wiki, MRs, Issues, and Epics in our 16.2 release. Since then we have added it to most other areas within the product. We are still working on [adding the rich text editor across the rest of GitLab](https://gitlab.com/groups/gitlab-org/-/epics/7098). The last places we added the RTE to are [design notes](https://gitlab.com/gitlab-org/gitlab/-/issues/407505), [comments templates](https://gitlab.com/gitlab-org/gitlab/-/issues/407504), [release descriptions](https://gitlab.com/gitlab-org/gitlab/-/issues/407494), and [requirement descriptions](https://gitlab.com/gitlab-org/gitlab/-/issues/407493).

We will [potentially](https://gitlab.com/gitlab-org/gitlab/-/issues/345073) make the RTE available in the Web Editor and Web IDE to make it easier for everyone to contribute to Markdown content in a repository. Seamless integration of the RTE in the web editing experience will realize nearly all the benefits of the Static Site Editor but we are no longer limiting it to Middleman-based projects configured to use the Static Site Editor. 

### What makes the GitLab RTE unique?

One aspect that sets GitLab's RTE apart is how it preserves Markdown format. While other editors use intermediate file formats or require saving changes to a database GitLab's text editor reads **and writes** valid Markdown, allowing collaboration from any editor and preserving the Markdown source. 

### How does the RTE work? 

At a really high level the RTE:

1. Takes the Markdown source and converts the document into nodes on a tree
2. Translates each node to HTML for presentation and editing
3. Provides a WYSIWYG HTML editing experience with custom UI
4. Translates the edited content back to Markdown and apply the changes to the source document 

We have written [comprehensive development guidelines](https://docs.gitlab.com/ee/user/rich_text_editor.html) that explain what's going on under the hood and can help get you up to speed if you're interested in contributing an extension to the RTE. 

### Recent items released related to the RTE

- [Downscale pasted retina images](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/134714)
- [Draggable Media in Rich Text Editor](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/134694)
- [All new rich text editor experience](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/126855#ec5328d883a8d56f0e029fa5d7c5d2bfb9a520f9)
- [Interactive diff suggestions in merge requests](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/126856/diffs)
- [Improve autocomplete results in rich text editor](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/131827)
- [Rich text editor broader availability](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/132890)

### What's next for the RTE? 

Our current focus is on expanding the [use of the RTE to edit Markdown across GitLab](https://gitlab.com/groups/gitlab-org/-/epics/7098), and [preserve markdown using the Rust backend based parser](https://gitlab.com/groups/gitlab-org/-/epics/7722). We're looking forward to releasing these improvements!

### What's next for the PTE and Markdown?

Our current focus with the PTE and Markdown is to [migrate EmojiFilter to use native support](https://gitlab.com/gitlab-org/gitlab/-/issues/465351) which will help to boost performance and security.
