---
title: Knowledge Base
description:
---

The knowledge base (KB) is a repository of solutions to commonly-encountered problems, created and
maintained by support engineers. In the KB, we turn the knowledge created when we solve a ticket for
one customer into a public resource that helps others self-serve &ndash; leveraging one-time effort
into an article that can be used multiple times independently from the ticket assignee.

## Principles

- **Turn it into a habit.** Write it down into the KB every time we solve a problem for customers,
  for a team member or for ourselves. The more we do it, the easier it becomes.
- **Accelerate knowledge capture.** Our tools and processes should enhance the speed at which we add
  knowledge to the KB, prioritizing capturing the right knowledge instead of capturing knowledge right.
- **Dogfood and update as we reuse.** The KB is as much for us as for our users. We review and
  update knowledge as we use and reuse it. If it isn't used, don't worry about it.

## How KB differs from the docs

The knowledge base and our product documentation are both key elements of GitLab's digital support
experience that serve different needs:

{{< cardpane >}}
{{% card header="**Docs**" %}}

- Learn about product features and how to use them.
- Provides an overview of the current version of our products.
- Used "ahead of time".

{{% /card %}}

{{% card header="**KB**" %}}

- Solve problems encountered while using our products.
- Includes solutions to problems in past versions of our products.
- Used "just in time".

{{% /card %}}
{{< /cardpane >}}

You can use this as a guide when deciding if you should contribute something to the KB or if you
should make it a docs update.

## Implementation

We use [Zendesk Guide](https://www.zendesk.com/sg/service/help-center/) to publish knowledge base
articles and suggest them to users who are seeking help.

A list of knowledge base articles can be found at:

- [Global support knowledge base](https://support.gitlab.com/hc/en-us/sections/15215649512604-Knowledge-Base)
- [US Government support knowledge base](https://federal-support.gitlab.com/hc/en-us/sections/29015014994068-Knowledge-Base)

Knowledge base articles are suggested when a user is submitting a ticket:

![Knowledge base suggestions in Zendesk](/images/support/kb-suggestions.gif)

We use the [Support Pages project](https://gitlab.com/gitlab-com/support/support-pages) to manage
knowledge base content. This has the following benefits:

- The project is open to public, allowing everyone to contribute.
- Avoid vendor lock-in of our knowledge base content.

## How to contribute

### Submitting a KB article

1. Pick the appropriate template in the [`/kb-documentation/templates`](https://gitlab.com/gitlab-com/support/support-pages/-/tree/master/kb-documentation/templates)
   directory:
   - [`break-fix.md`](https://gitlab.com/gitlab-com/support/support-pages/-/blob/master/kb-documentation/templates/break-fix.md): Issues encountered by users with one or more specific resolution steps.
   - [`deprecation-removal-breaking-change.md`](https://gitlab.com/gitlab-com/support/support-pages/-/blob/master/kb-documentation/templates/deprecation-removal-breaking-change.md): Information about how to assess and mitigate the impact of deprecations, removals and breaking changes.
   - [`how-to.md`](https://gitlab.com/gitlab-com/support/support-pages/-/blob/master/kb-documentation/templates/how-to.md): Steps to do a specific task. Does not need to be an issue.
   - [`question-answer.md`](https://gitlab.com/gitlab-com/support/support-pages/-/blob/master/kb-documentation/templates/question-answer.md): Simple article answering a question.
1. Duplicate the template, placing the new file in the appropriate directory:
   - [`/knowledge-base/all_instances`](https://gitlab.com/gitlab-com/support/support-pages/-/tree/master/knowledge-base/all_instances):
     This is where the majority of knowledge base articles will live.
   - [`/knowledge-base/global_only`](https://gitlab.com/gitlab-com/support/support-pages/-/tree/master/knowledge-base/global_only):
     Typically for content specific to GitLab.com.
   - [`/knowledge-base/us_government_only`](https://gitlab.com/gitlab-com/support/support-pages/-/tree/master/knowledge-base/us_government_only):
     For content specific to our US Government product offerings.
1. Fill out the template with the content you'd like to contribute.
   - Focus more on the technical content.
   - Follow the [style and content guide](./kb-style-guide.md) as closely as you can.
   - Consider [using Duo](#using-ai-to-generate-content) as a first pass.
1. Create the merge request using the `Knowledge Base Article` template.
1. Assign reviewers:
   - If timeliness is important, assign a Staff Support Engineer or Support Manager for review.
   - Otherwise, the template will assign the KB editors: currently `@irisb` or `@weimeng-gtlb`.

### Reviewing a KB article

- Always. Be. Merging. Make suggestions and apply them yourself.
- It's more important to capture the knowledge than to capture it with the right style and formatting.

### Publishing a KB article

Publishing an article should be done by the person who merges a KB MR. After the KB article is merged:

1. Submit a request using the [Support Super Form](https://support-super-form-gitlab-com-support-support-op-651f22e90ce6d7.gitlab.io/), selecting `Create a Zendesk article` for the field "What is this request concerning?".
1. After successful submission, the Support Super Form will create an issue and post URLs to
   the published KB article. The sync may take 5 to 10 minutes to complete.

### Getting Help

Questions can be asked in the dedicated [#spt_knowledge-base](https://gitlab.enterprise.slack.com/archives/C07QDCG4AGH) Slack channel.

### Using AI to generate content

- You **must use Duo** for any customer related ([Red](../../security/data-classification-standard.md#red)) data. Claude is only approved for [Orange data](../../security/data-classification-standard.md#orange) at this time.
- Duo can help quickly generate a first pass of an article. **Always** review generated data by Duo for technical accuracy. You are still the SME of the article and original customer issue.
- You must be directly on the page of the article template, i.e. [break-fix.md](https://gitlab.com/gitlab-com/support/support-pages/-/blob/master/kb-documentation/templates/break-fix.md). If the request is made in another location, Duo may make up random sections in the article.
- Duo will not immediatly provide the output in plain text even if asked in the original prompt. Requesting "raw markdown" may work, but there is [an issue](https://gitlab.com/gitlab-org/gitlab/-/issues/482485) when code blocks are included.
- Examples:
  - [GitLab Unfiltered](https://www.youtube.com/watch?v=4z6Xnh3B-wU) video(requires authentication) demonstration creating an article by copying ticket data.
  - [GitLab issue](https://gitlab.com/gitlab-com/support/support-pages/-/issues/7) demonstrating text prompts and output.

## Roles

### Contributors

Everyone can contribute. The most important thing is to capture the knowledge you've created while
solving a problem. You don't need any special training to begin.

### Rapid reviewers

Staff Support Engineers and Support Managers are KB rapid reviewers who can be called on to approve
and merge content without needing to wait for an editor to become available.

Rapid reviewers should:

- Be called upon when there is advantage to publishing changes quickly, i.e. when new product issues
  are encountered by users or as part of incident response.
- Collaborate with KB contributors on the technical accuracy of the content, prioritizing having
  updates published as soon as possible.
- Tag a KB editor after approving and merging a KB article merge request to ask for a style and
  format review and edit.

### Editors

KB editors help ensure KB articles are accessible to readers and have consistent style and
formatting.

To become a KB editor:

- Contribute KB articles.
- Talk to {{< member-by-name "Wei-Meng Lee" >}}.

The current KB editors are:

- {{< member-by-name "Iris Blackburn" >}}
- {{< member-by-name "Wei-Meng Lee" >}}
