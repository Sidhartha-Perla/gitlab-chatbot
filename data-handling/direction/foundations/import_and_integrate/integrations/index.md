---
layout: markdown_page
title: "Category Direction - Integrations"
description: "This GitLab product category is focused on enabling intuitive collaboration with tools GitLab's customers rely on. Find more information here!"
canonical_path: "/direction/foundations/import_and_integrate/integrations/"
---

- TOC
{:toc}

## Integrations

| | |
| --- | --- |
| Stage | [Foundations](/direction/foundations/) |
| Maturity | [Viable](/direction/#maturity) |
| Content Last Reviewed | `2025-04-07` |

### Introduction and how you can help

Thanks for visiting this category direction page on Integrations in GitLab. This page belongs to the [Import and Integrate](https://handbook.gitlab.com/handbook/product/categories/#import-and-integrate-group) group of the Foundations stage and is maintained by the group's Product Manager, [Magdalena Frankiewicz](https://gitlab.com/m_frankiewicz) ([E-mail](mailto:mfrankiewicz@gitlab.com), [Calendly](https://calendly.com/gitlab-magdalenafrankiewicz/45mins)).

This direction page is a work in progress, and everyone can contribute:
 
- Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=Category%3AIntegrations&first_page_size=20) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=Category:Integrations) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
 - Please share feedback directly via email, Twitter, or on a video call. If you're a GitLab user and want to discuss how GitLab can improve Importers, we'd especially love to hear from you.

### Strategy and Themes

<!-- Describe your category. Capture the main problems to be solved in market (themes). Describe how you intend to solve these with GitLab (strategy). Provide enough context that someone unfamiliar with the details of the category can understand what is being discussed. -->

GitLab's vision is to be the best [single application for every part of the DevOps toolchain](https://handbook.gitlab.com/handbook/product/categories/gitlab-the-product/single-application/). However, we acknowledge that to achieve this, there are many workflows, custom scripts, and nuanced integrations that customers require and GitLab may not be able to prioritize.
To make the most impact and keep the Integrations category sustainable, we have been focusing on improvements to the technical foundations of integrations as well as documentation, guides, and best practices to assist the broader community in contributing to integrations.
For FY26, the Import and Integrate team will be focusing primarily on improving migration capabilities between GitLab instances and from third-party tools to GitLab. Due to resource constraints and alignment with company objectives, we have deprioritized active development of integrations for this fiscal year.

<!--
1 year plan for what we will be working on linked to up-to-date epics. This section will be most similar to a "road-map". Items in this section should be linked to issues or epics that are up to date. Indicate relative priority of initiatives in this section so that the audience understands the sequence in which you intend to work on them. 
 -->

### Current Focus and Priorities

For FY26, the Import and Integrate team is prioritizing Importers Category:

- Strengthening customer confidence with migration by direct transfer General Availability
- Simplifying and speeding up contribution and membership mapping after imports
- Enabling semi-automated migrations between offline GitLab instances
- Providing a format for building importers for third-party software

These priorities align with GitLab's company objectives.

### Integrations Maintenance Status

We will continue to maintain existing integrations to ensure they remain functional, but we will not be actively developing new features for integrations during FY26. This approach allows us to focus our resources on migration capabilities while ensuring that existing integrations continue to work as expected.
Our popular integrations like GitLab for Slack and Jira integrations will be maintained, but new feature development is currently on hold.


### Integration Ownership

We continue to work to shift responsibilities as DRIs of integrations to individual product teams within the domain areas across GitLab. This gives groups full visibility and ownership in serving customers in their domains, based on each group's comprehensive strategy. This also helps to make the Integration category more sustainable.
Group Import and Integrate maintains ownership of the foundations of integrations and the [Integration development guidelines](https://docs.gitlab.com/ee/development/integrations/). We continue to offer guidance on integration best practices to anyone who contributes.

As we work to better define ownership of integrations across GitLab, the list below clarifies the current ownership of maintenance, security, and new feature development of each integration.

Security related integrations, owned by group Anti-Abuse:
- [Akismet](https://docs.gitlab.com/ee/integration/akismet.html)
- [Arkose Protect](https://docs.gitlab.com/ee/integration/arkose.html)
- [ReCAPTCHA](https://docs.gitlab.com/ee/integration/recaptcha.html)

CI/CD integrations, owned by group Pipeline Execution:
- [Bamboo CI](https://docs.gitlab.com/ee/user/project/integrations/bamboo.html)
- Drone CI
- [GitHub](https://docs.gitlab.com/ee/user/project/integrations/github.html)
- [Jenkins](https://docs.gitlab.com/ee/integration/jenkins.html)
- JetBrains TeamCity CI
- [Diffblue Cover](https://docs.gitlab.com/ee/integration/diffblue_cover.html)

Integrations owned by group Project Management:
- [Kroki diagrams](https://docs.gitlab.com/ee/administration/integration/kroki.html)
- [Mailgun](https://docs.gitlab.com/ee/administration/integration/mailgun.html)

Integrations owned by group Source Code:
- [PlantUML](https://docs.gitlab.com/ee/administration/integration/plantuml.html)
- [Sourcegraph](https://docs.gitlab.com/ee/integration/sourcegraph.html)
- [Beyond Identity](https://docs.gitlab.com/ee/user/project/integrations/beyond_identity.html)
- [GitGuardian](https://docs.gitlab.com/ee/user/project/integrations/git_guardian.html)

Integrations owned by group Incubation:
- [Apple App Store Connect](https://docs.gitlab.com/ee/user/project/integrations/apple_app_store.html)
- [Google Play](https://docs.gitlab.com/ee/user/project/integrations/google_play.html)

Integrations owner by group Container Registry:

- [Google Artifact Management integration](https://docs.gitlab.com/user/project/integrations/google_artifact_management)
- [Harbor integration](https://docs.gitlab.com/ee/user/project/integrations/harbor.html)

[Elasticsearch integration](https://docs.gitlab.com/ee/integration/elasticsearch.html) is owned by group Global Search.

[Datadog integration](https://docs.gitlab.com/ee/integration/datadog.html) is owned by group Runner.

[Gitpod integration](https://docs.gitlab.com/ee/integration/gitpod.html) is owned by group IDE.

[Google Cloud IAM](https://docs.gitlab.com/integration/google_cloud_iam/) integration is owned by group Authentication.

Packagist is owned by group Package Registry.

[Visual Studio Code extension](https://docs.gitlab.com/ee/user/project/repository/vscode.html) is owned by group Editor Extensions.

External issue trackers, ownership negotiated with group Project Management, currently maintained by group Import and Integrate:
- [Asana](https://docs.gitlab.com/ee/user/project/integrations/asana.html)
- [Bugzilla](https://docs.gitlab.com/ee/user/project/integrations/bugzilla.html)
- [ClickUp](https://docs.gitlab.com/ee/user/project/integrations/clickup.html)
- [Custom issue tracker](https://docs.gitlab.com/ee/user/project/integrations/custom_issue_tracker.html)
- [EWM - IBM Enginnering Workflow Management](https://docs.gitlab.com/ee/user/project/integrations/ewm.html)
- [Jira issue integration](https://docs.gitlab.com/ee/integration/jira/configure.html)
- [GitLab for Jira Cloud app](https://docs.gitlab.com/ee/integration/jira/development_panel.html)
- [Pivotal Tracker](https://docs.gitlab.com/ee/user/project/integrations/pivotal_tracker.html)
- [Redmine](https://docs.gitlab.com/ee/user/project/integrations/redmine.html)
- [YouTrack](https://docs.gitlab.com/ee/user/project/integrations/youtrack.html)

"Notification" integrations, maintained by group Import and Integrate:
- [Slack Notifications](https://docs.gitlab.com/ee/user/project/integrations/slack.html) (deprecated)
- [Slack slash commands](https://docs.gitlab.com/ee/user/project/integrations/slack_slash_commands.html)
- [GitLab for Slack app](https://docs.gitlab.com/ee/user/project/integrations/slack.html)
- [Discord](https://docs.gitlab.com/ee/user/project/integrations/discord_notifications.html)
- [Gooogle chat](https://docs.gitlab.com/ee/user/project/integrations/hangouts_chat.html)
- [Irker](https://docs.gitlab.com/ee/user/project/integrations/irker.html)
- [Mattermost notifications](https://docs.gitlab.com/ee/user/project/integrations/mattermost.html)
- [Mattermost slash commands](https://docs.gitlab.com/ee/user/project/integrations/mattermost.html)
- [Microsoft Teams](https://docs.gitlab.com/ee/user/project/integrations/microsoft_teams.html)
- [Pumble](https://docs.gitlab.com/ee/user/project/integrations/pumble.html)
- [Unify Circuit](https://docs.gitlab.com/ee/user/project/integrations/unify_circuit.html)
- [Webex Teams](https://docs.gitlab.com/ee/user/project/integrations/webex_teams.html)
- [Telegram](https://docs.gitlab.com/ee/user/project/integrations/telegram.html)

Other integrations, currently maintained by group Import and Integrate:
- [Trello PowerUp](https://docs.gitlab.com/ee/integration/trello_power_up.html) - ownership negotiated with group Project Management
- [Pipeline status emails](https://docs.gitlab.com/ee/user/project/integrations/pipeline_status_emails.html) - ownership negotiated with stage Verify
- [Emails on push](https://docs.gitlab.com/ee/user/project/integrations/emails_on_push.html)
- [Gmail Actions Buttons](https://docs.gitlab.com/ee/integration/gmail_action_buttons_for_gitlab.html)
- [Mock CI](https://docs.gitlab.com/ee/user/project/integrations/mock_ci.html)
- [Squash TM](https://docs.gitlab.com/ee/user/project/integrations/squash_tm.html) - ownership negotiated with group Product Planning

### What is Not Planned Right Now
<!--  Often it's just as important to talk about what you're not doing as it is to
discuss what you are. This section should include items that people might hope or think
we are working on as part of the category, but aren't, and it should help them understand why that's the case.
Also, thinking through these items can often help you catch something that you should
in fact do. We should limit this to a few items that are at a high enough level so
someone with not a lot of detailed information about the product can understand -->

#### Building a "marketplace"

While a marketplace for GitLab integrations and extensions could provide significant value in the future, it has been deprioritized for FY26. Our strategic brief considers this as a potential longer-term initiative, but current resource constraints prevent us from pursuing it at this time.

#### Improvements to GitLab for Slack and Microsoft Teams integrations

Although enhancing these integrations would support customer retention and satisfaction, we have deprioritized these improvements for FY26 to focus on migration capabilities.

#### Developing new domain-specific integrations

Import and Integrate group won't focus on developing new integrations, but we will continue to support other GitLab product groups, partners, and Community contributors in doing that.

### Future Direction

In the longer term, we recognize the potential value of:

- Improving GitLab for Slack and Microsoft Teams integrations to better serve customer retention
- Laying foundations for a scalable partner ecosystem, including APIs designed specifically for partners
- Creating a sustainable approach to expanding the GitLab ecosystem through a marketplace-like solution

These initiatives, while valuable, have been deprioritized for FY26 due to resource constraints and the need to focus on high-impact migration capabilities.

### Contributing

If you want to contribute to an existing integrations, you can look for open issues labelled with this integration name, e.g "Integration::Asana" or "Integration::Jira".

If you'd like to contribute a new integration, please first review [Integration development guidelines](https://docs.gitlab.com/ee/development/integrations/). Contact GitLab group owning the domain the new integration fits best, so that the group is aware of the planned contribution.  Import and Integrate offers guidance on integrations best practices during development, by reviewing MRs and answering technical questions.

If you're interested in general Integrations area, [you can find open issues with ~"Category:Integrations" label](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_date&state=opened&label_name%5B%5D=Category%3AIntegrations&first_page_size=20), however this list contains issues specific to particular integrations as well.

Feel free to reach out to the team directly if you need guidance or want
feedback on your work by using the ~"group::import and integrate" label on your open merge requests.

You can read more about our general contribution guidelines [here](https://gitlab.com/gitlab-org/gitlab/-/blob/master/CONTRIBUTING.md).

### Partnership

If your company is interested in partnering with GitLab, check out the [GitLab Partner Program](https://about.gitlab.com/partners/) page for more info.