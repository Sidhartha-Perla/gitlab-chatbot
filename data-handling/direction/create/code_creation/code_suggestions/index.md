---
layout: markdown_page
title: "Category Direction - Code Suggestions"
description: "Create & maintain code more efficiently"
---

## On this page
{:.no_toc}

- TOC
{:toc}

# Code Suggestions

| | |
| --- | --- |
| Stage | [Create](/direction/create/) |
| Maturity | [viable](/direction/#maturity) |
| Content Last Reviewed | `2024-10-15` |

### Introduction and how you can help

Thanks for visiting this category direction page on Code Suggestions in GitLab. This page belongs to the [Code Creation](https://handbook.gitlab.com/handbook/product/categories/#code-creation-group) group of the Create stage, and is maintained by Jordan Janes ([@jordanjanes](https://gitlab.com/jordanjanes)).

## Overview

The Code Creation team focuses on helping developers create & maintain code more efficiently. We strive to help GitLab customers deliver value to their customers more quickly through an accelerated software development lifecycle.

We help developers understand, write, test, fix, refactor, and document code:

* Help developers understand and navigate their codebase, and plan changes. 
* Reduce the time spent writing code by generating code based on natural language instructions and suggesting code completions.
* Automate and accelerate development tasks by explaining and documenting code, generating unit tests, and fixing code.
* Improve code quality by refactoring inefficient code.

We believe there’s an opportunity to help developers with both narrowly scoped tasks - such as generating unit tests - and with broadly scoped tasks - such as evaluating and updating all tests across a codebase.

## Vision

GitLab Duo Code Suggestions helps teams accelerate code creation throughout their software development lifecycle, without sacrificing security, privacy, and enterprise control.

## Strategy & themes

We plan to improve the quality and latency of code suggestions, expand the breadth of customer use cases we support, and ensure our customers have sufficient administrative controls. To make progress towards our vision, our investments are organized into these primary themes: 

### Latency

Code suggestions, and specifically inline code completions, have to keep up with the pace of the user. Delays in presenting useful suggestions often result in the user manually continuing their workflow, and this impairs our opportunity to help our customers accelerate their development. 

Code generation is often less latency sensitive, though we still strive to quickly deliver generated code to the user. We will often stream the responses so the developer can start to assess the results, and this also improves the latency when generating large blocks of code. 

GitLab has customers across the globe, and we’re committed to optimizing latency for all customers. We’ve invested in globally distributed infrastructure, and we prioritize model providers who can mitigate network latency with globally deployed models. 

We consider fast latency a tablestakes expectation from our customers, and we carefully manage latency tradeoffs when considering larger and more capable models. 

### Quality

Improving the quality of code suggestions is a primary focus. We think of quality as providing useful suggestions, which our users accept to accelerate their workflow. For code completion, this could be 1 line of code that perfectly matches what the user wanted. For code generation, this could be dozens of lines of code, and the user may sometimes edit a few specifics before moving forward. Over time, we want to provide exactly what the user needs. 

We plan to make progress on this goal by leveraging context throughout the customer’s codebase, continuing to invest in our internal evaluation suite, and continually assessing new AI models. 

**Context**

Managing and providing relevant context - from relevant dependencies, files, and throughout a codebase - is the main tactic to improve code suggestion quality. We can greatly improve the quality of code suggestions by ensuring responses are aware of key dependencies, libraries, and systems. We plan to find the right portions of content, provide that as context to our AI models, and generate a better response. We’ll use a combination of implicit context sources - which require no action from the user - and user-selected context sources. 

We’ve made initial progress in this space and plan to broaden the aperture of local context. As we broaden the sources, we’ll improve our logic to rank the most relevant portions of content to be used as context. Ensuring we provide quality responses is ultimately a tablestakes expectation from our customers. We will also need to ensure quality improvements don’t cause latency penalties as we broaden context. 

**Internal evaluations**

We must be confident that we’re improving quality as we broaden Code Suggestions to include more context and support more customer use cases. We use a broad evaluation dataset to internally quantify quality before rolling out changes to our customers. We’ll continue to extend our evaluation dataset by curating and creating test scenarios that will help us confidently assess quality. 

**Models**

We continuously monitor and evaluate the latest AI models for opportunities to improve quality and latency. We provide full transparency to our customers on the models used within GitLab Duo, and we gladly take responsibility for keeping up to date on all of the latest breakthroughs in AI models and technology. With Duo Code Suggestions, our customers can focus on accelerating their software development lifecycle and not spend time reviewing the latest AI models. 

### Expand use cases

With the breadth of the GitLab DevSecOps platform, expanding to support more customer goals is a long term opportunity for differentiation.

**Broadly scoped tasks**

Today, most of our user interactions center around specifically scoped tasks. As an example, a user can select portions of code and use Duo Code Suggestions to create tests, or refactor the code. We will support more broadly scoped tasks from our users to further accelerate their workflow. An example might be helping a developer add a field to an existing API, then updating all queries to match the new schema. These broadly scoped tasks require more context and reasoning, and the ability to make edits among multiple files and locations within the files.

**Increase automation**

We will help developers further accelerate their workflow through increased automation. This might include searching an entire codebase to find code that needs improvement, or continuously scanning for bugs and surfacing those to our users. Duo can intelligently help our users find areas to improve, along with efficiently implementing the improvements. 

### Enterprise & administrator controls

Enterprise customers often have more needs for admin controls and auditing. We want to ensure Duo Code Suggestions meets our customers’ goals for compliance and administration. This section summarizes a few areas we’ve heard from customers, and is not fully comprehensive. 

GitLab Duo has a strict [data privacy and data retention policy](https://docs.gitlab.com/ee/user/gitlab_duo/data_usage.html) to ensure customers can be confident in our data protection agreements. Customers don’t need to manage administrator controls to ensure there’s data privacy. 

**Context and indexing controls**

As we broaden context sources, customers may want to exclude specific context sources. This will ensure Duo Code Suggestions doesn't use these context sources when generating a response. We'll need to extend these controls alongside the context sources.

**Audit logs**

This is an area where we’re gathering more customer input. We want to provide detailed visibility into how and where Duo Code Suggestions are used, while balancing data privacy. 

## 1 year plan

Our main focus will be improving suggestions quality through expanded context.

**What we recently completed**
* [Migrating Repository X-Ray to a background job](https://gitlab.com/groups/gitlab-org/-/epics/14100)
* [Improve code completion latency](https://gitlab.com/gitlab-org/gitlab/-/issues/509192)

**What we are currently working on**
* [Improving quality through context: Imports](https://gitlab.com/groups/gitlab-org/editor-extensions/-/epics/58)
* [Improve code base understanding & context - Knowledge Graph Validation](https://gitlab.com/groups/gitlab-org/-/epics/16583)
* [Improve code base understanding & context - Knowledge Graph Architecture](https://gitlab.com/groups/gitlab-org/-/epics/16584)

**What is next for us**
* [Knowledge Graph-based Code Intelligence](https://gitlab.com/groups/gitlab-org/-/epics/16210)

## Target audience

People who code:

1. [Sasha (Software Developer)](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
2. [Priyanka (Platform Engineer)](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
3. [Simone (Software Engineer in Test)](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)

## Success metrics

Success metrics & signals are organized around 2 broad goals:

1. Increasing developer productivity
2. Improving developer satisfaction

**Increasing developer productivity**

Signal: reduced time from task start to task finish

* Merge request throughput

Signal: more coding tasks are automated or accelerated

* % of code provided by AI
* Number of accepted suggestions per user
* Acceptance rate

**Improve developer satisfaction**

Signal: Developers consistently use code suggestions

* MAU
* MAU / Billable users
* Code completion usage
* Code generation usage

## Competitive landscape

Please see the content in our [internal handbook](https://internal.gitlab.com/handbook/product/best-in-class/create/code_suggestions/).
