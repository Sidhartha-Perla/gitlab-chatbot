---
layout: markdown_page
title: "Group Direction - Remote Development"
description: "Overall direction for the Remote Development group"
canonical_path: "/direction/create/remote_development/"
---

- TOC
{:toc}

## The Remote Development group

**Content last reviewed on 2024-08-26**

This is the direction page for the Remote Development group which is part of the [Create stage](/direction/dev/index.html#create) of the DevOps lifecycle and is responsible for:

|  Category   |   Direction  |  Description |
|  ---   |   ---   |   ---   |  ---  |
| Web IDE | [Direction page](/direction/create/remote_development/web_ide/) | A web-based multi-file code editor |
| Workspaces | [Direction page](/direction/create/remote_development/workspaces/) | Server-side runtime environments |

## What are we working on and why?

### Web IDE

The GitLab Web IDE is a powerful browser-based multi-file editor based on the open source [Visual Studio Code](https://github.com/microsoft/vscode) project. As an entirely client-side solution, the Web IDE does not consume any additional server or database resources or require any additional configuration to get started. Developers and non-developers alike can quickly access a project's entire file system and commit directly from their web browser.

### Workspaces

While the Web IDE makes it possible for anyone to contribute to a project right from their web browser, editing the actual code is only a small part of a developer's workflow. Local IDEs, combined with properly-configured development environments, make it possible to run tests, lint code, generate previews, and offer features that improve developer efficiency like code completion. Without these productivity-boosting features, developers won't fully adopt a tool.

GitLab Workspaces provide a server-based runtime environment that can be accessed from the Web IDE or your local IDE, eliminating the need for managing a complex set of dependencies on your local machine. These Workspaces are defined in code and deployed as needed on a cloud provider via the GitLab Agent for Kubernetes.

## Recent opportunity canvases (GitLab internal)

1. [Quickly get started developing in standardized environments](https://docs.google.com/document/d/1t1j98Wl1erG9b8cUT77yDsNUEPvCOMOp0ktbOkYZfWc/edit#heading=h.4mt5fmtn0ax4)

## Links and resources

- [Remote Development Group HQ - group strategy epic](https://gitlab.com/groups/gitlab-org/-/epics/5065)
- [Remote Development Team Handbook page](https://handbook.gitlab.com/handbook/engineering/development/dev/create/remote-development/)
- [GitLab Unfiltered Playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0KrRQhnSYRNh1s1mEUypx67-)
