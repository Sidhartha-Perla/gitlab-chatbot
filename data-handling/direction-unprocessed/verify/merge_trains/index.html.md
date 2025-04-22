---
layout: markdown_page
title: "Category Direction - Merge Trains"
description: "Learn about GitLab’s Merge Trains, an innovative feature that improves pipeline efficiency by automating merge request sequencing."
---

- TOC
{:toc}

## Merge Trains

| | |
| --- | --- |
| Stage | [Verify](/direction/verify/) |
| Maturity | [Viable](/direction/#maturity) |
| Content Last Reviewed | 2025-01-21 |

### Introduction and how you can help

Thanks for visiting this category direction page on Merge Trains in GitLab. This page belongs to the [Pipeline Execution](https://handbook.gitlab.com/handbook/product/categories/#pipeline-execution-group) group of the Verify stage and is maintained by Rutvik Shah ([E-Mail](mailto:<rutshah@gitlab.com>)).

This direction page is a work in progress, and everyone can contribute:

- Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=Category%3AMerge%20Trains&first_page_size=50) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=Category:Merge+Trains) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
- Please share feedback directly via email, Twitter, or on a video call. If you're a GitLab user and want to discuss how GitLab can improve Review Apps, we'd especially love to hear from you.

### Overview

We aim to help you balance speed with reliability, keeping your pipelines green. This ultimately supports the stability of collaboration across branches and GitLab has introduced Merge Trains as the mechanism to accomplish this. When merge trains are used, each merge request joins as the last item in that train. Each merge request is processed in order and is added to the merge result of the last successful merge request. The merge request adds its changes, and starts the pipeline immediately under the assumption that everything is going to pass. If the merge request fails, it is kicked out of the train and the next merge request continues the pipeline of the last successful merge result. 

- [Maturity Plan](#maturity-plan)
- [Issue List](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=Category%3AMerge%20Trains)
- [Overall Vision](/direction/ops/)
- [UX Research](https://gitlab.com/groups/gitlab-org/-/epics/594)
- [Documentation](https://docs.gitlab.com/ee/ci/pipelines/merge_trains.html)

### Strategy and Themes

For an overview of our plans for Merge Trains, see epic [Merge Trains Vision](https://gitlab.com/groups/gitlab-org/-/epics/5122) 


### 1 year plan

We do not have plans to deliver new features for Merge Trains in the upcoming year. However, Pipeline Execution will continue to support high priority bug fixes for this category. Our team will also support community contributions that help advance this category.


<!--#### What we are currently working on-->




#### What we recently completed
<!-- Lookback limited to 3 months. Link to the relevant issues or release post items. -->
Improved Merge Train Reliability with fixes that can result in stuck merge trains (e.g. https://gitlab.com/gitlab-org/gitlab/-/issues/500887) and [Improved messaging for merge train related auto merge removals](https://gitlab.com/gitlab-org/gitlab/-/issues/467300)

### Best in Class Landscape
<!-- Blanket description consistent across all pages that clarifies what GitLab means when we say "best in class" -->

BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

#### Key Capabilities 

* Queue merge requests and verify their changes work together before they are merged to the target branch
* Leverage merged results pipelines
* Support fast-forward and semi-linear merge requests
* Provide marge train visualisation and administration capabilities

#### Roadmap

This category is currently at the "Viable" maturity level, and our next maturity target is "Complete" ([see our definitions of maturity levels](https://about.gitlab.com/direction/#maturity). We currently have basic capabilities and want to continue and extend these in future milestones.

Key deliverables to achieve this are:

- Completed - [Simplify merge strategies with Auto-merge](https://gitlab.com/groups/gitlab-org/-/epics/6687)
- Completed - [Merge Trains should support fast forward merge](https://gitlab.com/groups/gitlab-org/-/epics/4911)
- [API support for merge trains](https://gitlab.com/groups/gitlab-org/-/epics/5864)
- [Resolving Severity 1 and 2 bugs](https://gitlab.com/gitlab-org/gitlab/-/issues?sort=milestone_due_desc&state=opened&label_name[]=Category:Merge+Trains&label_name[]=type::bug&not[label_name][]=severity::3&not[label_name][]=severity::4)

#### Top Competitive Solutions

It looks like GitLab is the first to provide this functionality, although GitHub has annouced a [public beta](https://github.blog/changelog/2023-02-08-pull-request-merge-queue-public-beta/) for Merge Queue which includes fast-forward merge train support and visualizations of the queue.

[Aviator](https://www.aviator.co/) is the most comparable offering against Merge Trains, promising to "keep builds green forever", much like how we [positioned Merge Trains in 2020](https://about.gitlab.com/blog/2020/01/30/all-aboard-merge-trains/) during their release. Today, Merge Queues seem to support parity of Merge Trains for GitHub repositories. 

[marge-bot](https://github.com/smarkets/marge-bot) is a popular open source program that works with GitLab to manage merge requests.

[Mergify](https://mergify.com/features/merge-queue) is another offering that integrates with GitHub repositories and multiple CI providers to supporty queued pull requests.

[Graphite](https://graphite.dev/features#merge-queue) offers similar capabilities as Merge Trains

### Target Audience

Check out our [Ops Section Direction "Who's is it for?"](/direction/ops/#who-is-it-for) for an in depth look at the our target personas across Ops. For Merge Trains, our "What's Next & Why" are targeting the following personas, as ranked by priority for support: 

1. [Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
1. [Priyanka - Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)

<!--### Pricing and Packaging


### Analyst Landscape
-->

### Top Internal Customer Issue(s)

In an effort to dogfood our own features, we are actively working on using [merge trains internally on gitlab-org](https://gitlab.com/gitlab-org/quality/engineering-productivity/team/-/issues/513). 
