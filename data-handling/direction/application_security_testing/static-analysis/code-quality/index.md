---
layout: markdown_page
title: "Category Direction - Code Quality"
description: "Eliminate bugs, style violations, and mistakes before they're merged. Learn more about where GitLab Code Quality is going."
---

- TOC
{:toc}

This direction page describes GitLab's plans for the Code Quality category.

## Overview

GitLab Code Quality helps code authors and reviewers eliminate bugs, style violations, and other mistakes before they're merged.

Code Quality results are processed and displayed in an MR widget, in the MR Changes view, in a pipeline report, and in a project-level quality summary.

To learn more, check the [Code Quality documentation](https://docs.gitlab.com/ee/ci/testing/code_quality.html).

## Roadmap

Looking forward:

1. We are **deprecating and removing CodeClimate-based scanning** and moving toward a flexible, open, community-oriented design that emphasizes using quality tools directly as CI jobs.

   - To learn more about the change, please see the following public resources:
     - [Deprecation announcement](https://docs.gitlab.com/ee/update/deprecations.html#codeclimate-based-code-quality-scanning-will-be-removed)
     - [Restructured Code Quality documentation](https://docs.gitlab.com/ee/ci/testing/code_quality.html#scan-code-for-quality-violations) explaining the options for scanning
     - [List of documented integrations](https://docs.gitlab.com/ee/ci/testing/code_quality.html#integrate-common-tools-with-code-quality) (more MRs welcome!)
     - [Migration cross-reference](https://docs.gitlab.com/ee/ci/testing/code_quality.html#migrate-from-codeclimate-based-scanning) in documentation
   - Team members have access to additional resources, including enablement training, in [the Field Guide for this change, on Highspot](https://gitlab.highspot.com/items/673ce2479dee95f62d5b1f2b?lfrm=srp.0#1).
   - We published the [deprecation announcement](https://docs.gitlab.com/ee/update/deprecations.html#codeclimate-based-code-quality-scanning-will-be-removed) for this change in July 2024. [End of Support](https://docs.gitlab.com/ee/update/terminology.html#end-of-support) and associated removals are scheduled for GitLab 18.0 (May 2025).
2. We are not currently planning improvements in result display, and we do not expect to make significant investments in this area in the next 12 months.

## What we recently completed

Check [release posts](https://gitlab-com.gitlab.io/cs-tools/gitlab-cs-tools/what-is-new-since/?tab=features&selectedCategories=Code+Quality&minVersion=13_00) for our previous work in this area.

## What is not planned right now

- **Proprietary quality analysis:** We currently plan to focus on integrating with existing quality tools instead of creating our own quality-focused analyzer.
  - We believe that improving the experience for users of all quality tools—including open-source linters, third-party products, and custom tools—delivers value sooner, and doesn't detract from our ability to bring a proprietary tool to market later.
- **Mixing quality and security:** We aren't planning to blur the lines between security and quality findings. We believe it's valuable to keep quality and security findings distinct, since these tools and processes are maintained by different personas and are subject to different organizational requirements.
  - For example, while quality tools and their rules are typically managed by software engineering departments, security tools (and rules about how to handle security findings) typically involve security professionals and are monitored for adherence to compliance controls.
  - However, users should see a consistent user experience for quality and security findings, and we shouldn't have to inefficiently build each workflow feature twice either. We will consider ways to align the experience between quality and security in the future.
- **Modifications to CodeClimate:** We don't believe we have an effective path forward to modify CodeClimate or its plugins. This conclusion is based on the collective weight of a mix of factors:
  - We don't have a clear technical path toward removing the Docker-in-Docker requirement, despite more than one [investigation](https://gitlab.com/gitlab-org/gitlab/-/issues/357464).
  - The AGPL license used for most CodeClimate core components and plugins makes contributions and operations more difficult for GitLab and for customers.
  - Many existing plugins do not have active communities and [do not receive regular updates](https://gitlab.com/groups/gitlab-org/-/epics/8790#the-status-quo).
  - The workflow for typical development tool usage includes development teams updating and maintaining their project configurations to use tools in many contexts, rather than just in CI. (See [UX research](https://gitlab.com/gitlab-org/ux-research/-/issues/1886).)
  - It is simpler and more efficient to run tools like `eslint` directly, rather than mediating their configuration and operation through multiple layers of indirection.
  - Mediating access through CodeClimate doesn't provide unique capabilities: the underlying tools for each [official CodeClimate plugin](https://docs.codeclimate.com/docs/list-of-engines) are each available to use directly.

## Dogfooding

GitLab teams collaborate more efficiently by using Code Quality to surface issues during code review. Team members have integrated:

- The `vale` linter [for product documentation](https://gitlab.com/gitlab-org/gitlab/-/blob/ddd03bc0552ad4c53483d3e79d52aa56c70b8c57/.gitlab/ci/docs.gitlab-ci.yml#L71-87).
- The `markdownlint`, `vale`, and `hugolint` linters, and a custom linter, [in the GitLab internal handbook](https://gitlab.com/gitlab-com/content-sites/internal-handbook/-/blob/fb10dd82c2ffeee536ec2d5b818a76696dc3dd5f/.gitlab-ci.yml#L168-261) (accessible to team members only).
- golangic-lint in [security analyzers](https://gitlab.com/gitlab-org/security-products/ci-templates/-/blob/3c3d9ddf6c901ab5c253e095828425d59393baf8/includes-dev/go.yml#L35-45).
- ESLint for JavaScript [in gitlab-org/gitlab](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/172592).
- Stylelint for CSS [in gitlab-org/gitlab-ui](https://gitlab.com/gitlab-org/gitlab-ui/-/merge_requests/4870).
- markdownlint2-cli [in the public handbook](https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/e40174f450dd57ab76e81987a6369e31b9f2610f/.markdownlint-cli2.jsonc#L2-15).
- A custom linter [in the public handbook](https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/e40174f450dd57ab76e81987a6369e31b9f2610f/scripts/handbook-lint.sh).

## Related categories

Outside of the Code Quality category, GitLab also offers other features that help you build quality software:

- [Advanced security and compliance](https://docs.gitlab.com/ee/user/application_security/).
- [CI/CD](https://docs.gitlab.com/ee/ci/).
- [Code coverage reports](https://docs.gitlab.com/ee/ci/testing/code_coverage.html) and [test coverage visualization](https://docs.gitlab.com/ee/ci/testing/test_coverage_visualization.html).
- [Test case management](https://docs.gitlab.com/ee/ci/test_cases/).
- [Unit test reports](https://docs.gitlab.com/ee/ci/testing/unit_test_reports.html).

## Get involved

You can contribute to where GitLab Code Quality goes next by:

- Commenting or contributing to existing [Code Quality issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_date&state=opened&label_name%5B%5D=Category%3ACode%20Quality) in the public `gitlab-org/gitlab` issue tracker.
- If you don't see an issue that matches, filing [a new issue](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable_template=Feature%20Proposal%20-%20basic).
  - Post a comment that says `@gitlab-bot label ~"group::static analysis" ~"Category:Code Quality"` so your issue lands in our triage workflow.
- If you're a GitLab customer, discussing your needs with your account team.

## Page updates

| | |
| --- | --- |
| Stage | [Application Security Testing](/direction/application_security_testing/) |
| Content Last Reviewed | `2025-02-06` |
