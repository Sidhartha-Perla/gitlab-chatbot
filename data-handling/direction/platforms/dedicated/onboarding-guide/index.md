---
layout: markdown_page
title: "GitLab Dedicated new customer onboarding guide"
description: "Follow GitLab’s onboarding guide for dedicated SaaS platforms, ensuring a smooth and efficient setup for new users on dedicated GitLab instances."
---

- TOC
{:toc}

## Goal

This guide can be used to help new GitLab Dedicated customers prepare for the creation of their GitLab Dedicated tenant instance. 

While the Switchboard onboarding flow will be used to complete the tenant instance creation process, there are key pieces of information needed from the customer in order to ensure the Switchboard onboarding flow is ready for use as soon as the sales process is complete.

More information about the GitLab Dedicated new customer process including onboarding can be found [here](https://internal.gitlab.com/handbook/engineering/horse/#new-customer-process) (internal only).

## Who is this guide for?

This is primarily intended for use by members of the account team (primarily the [Solutions Architect](https://handbook.gitlab.com/job-families/sales/solutions-architect/) and/or [Customer Success Manager](https://handbook.gitlab.com/job-families/sales/customer-success-management/)) working with new GitLab Dedicated customers. 

For [transparency](https://handbook.gitlab.com/handbook/values/#transparency), we have made this available in our public handbook so it can be shared with customers directly as needed to provide visibility into our onboarding process.

## How to use this guide

The checklists below can be provided to customers (along with the related documentation) to set expectations and define what information is needed to prepare for the initial tenant instance creation process.

The information a customer provides can then be transferred to the GitLab Dedicated [new tenant onboarding issue](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/blob/main/.gitlab/issue_templates/switchboard_tenant_onboarding_request.md) (internal only) which will be used to prepare the Switchboard onboarding flow.

## First steps

1. Review detailed instructions on how to [create a new GitLab Dedicated instance](https://docs.gitlab.com/ee/administration/dedicated/create_instance.html) using Switchboard.
2. Review the available [functionality of GitLab Dedicated](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/).

## Required information

Before opening an onboarding issue, be sure that you will be able to provide the [required information](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/blob/main/.gitlab/issue_templates/switchboard_tenant_onboarding_request.md#customer-information-required) in the first section of the onboarding issue.

NOTE:
This information must be included in the description of the [new tenant onboarding issue](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/blob/main/.gitlab/issue_templates/switchboard_tenant_onboarding_request.md) before the new user can be provisioned on Switchboard and invited to use the Switchboard onboarding flow.

Please confirm the following with your customer - feel free to copy the list below as is and send to your customer to complete.

~~~
- Email of the person/people who should receive the invitation to use the Switchboard onboarding flow and the root credentials for their instance once created.
- Number of users - this should correspond with the number of Ultimate licenses being purchased.
- Initial repository size - this should correspond with what has been agreed upon during the quoting process.

~~~


## Further Configuration

Configurations can be added by the Tenant Admin following the tenant instance creation via the Switchboard UI. 

Review detailed instructions on how to [configure a GitLab Dedicated instance](https://docs.gitlab.com/ee/administration/dedicated/configure_instance.html).

Any configuration not available via Switchboard can be requested via subsequent issues using the [corresponding issue template](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/tree/main/.gitlab/issue_templates?ref_type=heads).

These will not be configured in the customer's GitLab Dedicated instance during the initial provisioning, but can be completed as soon as the customer's tenant instance is created. If needed sooner, please specify in the issue.

## Have questions?

Contact the GitLab Dedicated team via [#f_gitlab_dedicated](https://gitlab.slack.com/archives/C01S0QNSYJ2) Slack channel.