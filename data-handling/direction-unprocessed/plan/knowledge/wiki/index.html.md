---
layout: markdown_page
title: "Category Direction - Wiki"
description: "GitLab Wikis are a great way to share documentation and organize information via built-in functionality. View further information here!"
canonical_path: "/direction/plan/knowledge/wiki/"
---

- TOC
{:toc}

## Wiki

| | |
| --- | --- |
| Stage | [Plan](/direction/plan/) |
| Maturity | [Viable](/direction/#maturity) |
| Content Last Reviewed | `2025-02-06` |

### Introduction and how you can help
<!-- Introduce yourself and the category. Use this as an opportunity to point users to the right places for contributing and collaborating with you as the PM -->

Thanks for visiting the Wiki category direction page in GitLab. This page belongs to [Knowledge group](https://handbook.gitlab.com/handbook/product/categories/#knowledge-group) in Plan Stage. This page is maintained by Knowledge group PM Matthew Macfarlane ([E-Mail](mailto:mmacfarlane@gitlab.com)). More information can be found on the [Knowledge group direction page](/direction/plan/knowledge/).

This page and associated strategy are a work in progress, and everyone can contribute to it:

 - Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=Category%3AWiki) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=Category%3AWiki) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
 - Please share feedback directly via email, Twitter, or on a video call. If you're a GitLab user and have direct knowledge of your need for Wiki, we'd especially love to hear from you.

### Overview
<!-- A good description of what your category is today or in the near term. If there are
special considerations for your strategy or how you plan to prioritize, the
description is a great place to include it. Provide enough context that someone unfamiliar
with the details of the category can understand what is being discussed. -->

The GitLab Wiki transforms documentation by integrating it directly within your development platform, eliminating the need for separate tools like Confluence or Notion. Available in every GitLab project and group, Wiki brings documentation closer to your code and workflows, making knowledge sharing a seamless part of your development process.

### Where we are headed
<!-- Describe the future state for your category. What problems will you solve?
What will the category look like once you've achieved your strategy? Use narrative
techniques to paint a picture of how the lives of your users will benefit from using this
category once your strategy is fully realized -->

We want the wiki to serve as a single source of truth for project and group-level documentation that is approachable and easily accessibly by anyone. We are presently exploring ways to encourage collaboration across all personas by improving the editing and navigation experience.

Specifically, we are looking to better integrate the wiki experience with the rest of GitLab. One immediate opportunity is to introduce [commenting on wiki pages](https://gitlab.com/groups/gitlab-org/-/epics/14461).

### Target audience and experience
<!-- An overview of the personas (https://handbook.gitlab.com/handbook/product/personas/#user-personas) involved in this category. An overview
of the evolving use cases and user journeys as the category progresses through minimal,
viable, complete and lovable maturity levels. -->
One of our primary personas is Sasha, the [Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer), but all personas can use wikis for storing information. Everyone should be able to quickly and easily contribute to a wiki page. As the wiki matures we may need to investigate other non-developer personas as our research found they are frequent users of wikis.

Another of our primary personas is Parker, the [Product Manager](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager). Product Managers require a place to develop, organize, and share their knowledge, and a wiki is often considered a perfect location. Leveraging templates, autocomplete connection of Wiki pages to GitLab Issues and Epics, Product Managers can seamlessly plan and develop their ideas using the GitLab wiki.

### What's next & why
<!-- This is almost always sourced from the following sections, which describe top
priorities for a few stakeholders. This section must provide a link to an issue
or [epic](https://handbook.gitlab.com/handbook/product/product-processes/#epics-for-a-single-iteration) for the MVC or first/next iteration in the category.-->

Last fiscal year we [finalized](https://gitlab.com/groups/gitlab-org/-/epics/12826) Jobs to Be Done (JTBD) for the category which help us to narrow down customer priorities. Some recent items that we've completed as a result include, [improvements to the wiki sidebar](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/134716), [separate wiki page title and url fields](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/134715), and [improved wiki user experience](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/134696).

Currently, we are working on [comments on wiki pages](https://gitlab.com/groups/gitlab-org/-/epics/14461). Comments provide an avenue for effective discussion, questions, and collaboration, and ultimately allow projects to move forward more efficiently.

### Wiki Jobs to Be Done 

A Job to be Done (JTBD) is a framework, or lens, for viewing products and solutions in terms of the jobs customers are trying to achieve. It's about understanding the goals that people want to accomplish. It lets us step back from our business and understand the objectives of the people we serve. It opens the door to innovation.

At GitLab, we have our own flavor of JTBD and use it throughout the design process, but most notably to:

- Define scope
- Validate direction
- Evaluate existing experiences
- Assess category maturity

JTBD come directly from research and customer conversations with those people who do the tasks/jobs we need to design for. Problem validation is one of the most effective ways to confidently inform the writing of a JTBD.

For wiki category we've identified 9 core JTBD after two research studies. The following [Epic](https://gitlab.com/groups/gitlab-org/-/epics/12826) provides additional details about the construction of and research behind Wiki JTBD.

| Job Performer                    | Description                                           |
| ------------------------ | -------------------------------------------------- | 
| Knowledge Consumer       | When I am writing code, I want to find knowledge related to common roadblocks, so that I can minimize the likelihood of a security incident and increase development efficiency.| 
| Knowledge Admin         | When I am onboarding a new colleague, I want to ensure they are provided the right view and edit permissions related to knowledge we have stored, so I can minimize the likelihood of a security incident or release of material non public information. | 
| Knowledge Documenter               | When I am conducting a retrospective, I want to document the situation in a manner consistent with other retrospectives, so I can ensure colleagues are easily able to understand the situation and path to resolution. |
| Knowledge Admin          | When I am reviewing knowledge my team is consuming, I want to review which assets are utilized the most, so I can ensure the content most digested is accurate and providing insights that create informed decisions.|
| Knowledge Consumer            | When I am examining open work items for my engineering team, I want to review the knowledge documented for each item, so I can understand the broader context around prioritization and background knowledge for resolution.|
| Knowledge Admin            | When I am tasked with importing knowledge from one tool to another tool, I want to efficiently view what knowledge has moved, so I can ensure that no knowledge was lost in transition. |
| Knowledge Consumer | When I am on call, I want to understand who created the documentation in the knowledge base, so I can easily reach out to them if the incident becomes critical.   |
| Knowledge Documenter | When I am reviewing a document, I want to understand who is actively contributing to the documentation, so I can ensure I do not overlap with their changes and am more efficient with my efforts.|
| Knowledge Documenter | When I am reviewing a Page I want to be able to comment my thoughts on improvements or ask questions related to the documentation, so I can improve my own efficiency and the efficiency of the organization.|

### Maturity plan

We are actively working on maturing the Wiki category. In the past the category was in maintenance mode, however, due to reprioritization and a need for a competitive tool to compete against Confluence we have been actively investing in the category. We recently completed advancements in our product via the introduction of [templates](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/133279) and an [autocomplete feature](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/133281). We are using our [JTBD Epic](https://gitlab.com/groups/gitlab-org/-/epics/12826) to drive progress forward for the category. Please take a look at that Epic to view some of our priorities.


### Competitive landscape
<!-- The top two or three competitors, and what the next one or two items we should
work on to displace the competitor at customers, ideally discovered through
[customer meetings](https://handbook.gitlab.com/handbook/product/product-processes/#customer-meetings). We’re not aiming for feature parity with competitors, and we’re not just looking at the features competitors talk
about, but we’re talking with customers about what they actually use, and
ultimately what they need.-->

We compete with the following knowledge management tools (not and exclusive list):

- [Confluence](https://www.atlassian.com/software/confluence)
- [Notion](https://www.notion.so/)
- [GitHub Wiki](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis)

<!-- ### Analyst Landscape -->
<!-- What analysts and/or thought leaders in the space talking about, what are one or two issues
that will help us stay relevant from their perspective.-->

<!-- TBD -->

### Recent Accomplishments

- In 17.4 we released a [resizable wiki sidebar](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/136154)
- In 17.2 we improved the wiki via [separating the wiki page title and URL fields](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/134715)
- In 17.2 we [released improvements to the wiki sidebar](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/134716).
- In 17.1 we [released an improved wiki user experience](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/134696).
- In 16.11 we [released](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/133281) autocomplete features for the wiki.
- In 16.10 we [released](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/133279) template capabilities for the wiki. 
- In 16.6 we [released](https://gitlab.com/gitlab-org/gitlab/-/issues/422093) a print wiki page to PDF feature.
- In 15.10 we [released](https://gitlab.com/gitlab-org/gitlab/-/issues/20305/?_gl=1*17d6cyx*_ga*MTU5MDI5ODc5NS4xNjY1NTkyMzcy*_ga_ENFH3X7M5Y*MTY4MDcyMDIxOC4zOTUuMS4xNjgwNzIxMTIzLjAuMC4w) the capability to easily create and edit diagrams in wikis by using the diagrams.net GUI editor. This feature is available in the Markdown editor and the content editor, and was implemented in close collaboration with the GitLab wider community.

### Top user issue(s)
<!-- This is probably the top popular issue from the category (i.e. the one with the most
thumbs-up), but you may have a different item coming out of customer calls.-->

- [Make it possible to edit wiki through CI](https://gitlab.com/gitlab-org/gitlab/-/issues/16261). This item has over 200 upvotes, making it a priority in the near an long term. The challenge with this item is that is doesn not clearly fall under the JTBD we've identified. We have added this under our [co-create initiative](https://handbook.gitlab.com/handbook/marketing/developer-relations/cocreate/) and welcome contributions toward it.

### Top dogfooding issues
<!-- These are sourced from internal customers wanting to [dogfood](https://handbook.gitlab.com/handbook/values/#dogfooding)
the product.-->

Knowledge group [utilizes the GitLab Wiki](https://gitlab.com/gitlab-org/plan-stage/knowledge-group/-/wikis/Knowledge-Group-Home) for Opportunity Mapping via the recent introduction of diagrams.net. More information can be found on this integration via our Unfiltered channel. One Issue that we could wrap up that would support more dogfooding could be [comments on wiki pages](https://gitlab.com/groups/gitlab-org/-/epics/14461). Comments provide an avenue for effective discussion, questions, and collaboration, and ultimately allow projects to move forward more efficiently.


### Top strategy item(s)
<!-- What's the most important thing to move your strategy forward?-->

Our top strategy item is to continue addressing the identified JTBD for the category. This includes wiki [advanced page permissions](https://gitlab.com/groups/gitlab-org/-/epics/12832), [page analytics](https://gitlab.com/groups/gitlab-org/-/epics/12834), and [real time collaboration](https://gitlab.com/groups/gitlab-org/-/epics/12828). 
