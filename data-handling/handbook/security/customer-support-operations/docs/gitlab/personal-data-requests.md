---
title: Personal Data Requests
description: Operations documentation page for the components of personal data requests we manage
canonical_path: "/handbook/security/customer-support-operations/docs/gitlab/personal-data-requests"
---

{{% pageinfo color="warning" %}}

This is an information page for the various components of personal data requests we manage.

If you are looking for information about working the Operations components of personal data requests, please see [Working Personal Data Requests](../../workflows/personal-data-requests).

If you are looking for information about managing the components described on this page, please see [workflows](../../workflows).

{{% /pageinfo %}}

## Form

<sup>*Introduced via [support-team-meta#1329](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/1329)*</sup>

The Personal Data Request form (formerly Account Deletion form) is a simple HTMl form generated via GitLab Pages that is used for personal data requests.

The source code for it is located [here](https://gitlab.com/gitlab-support-readiness/forms/account-deletion-form).

## Form submission processor

<sup>*Introduced via [support-team-meta#1329](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/1329)*</sup>

When the form is submitted, the [Account Deletion Processor](https://gitlab.com/gitlab-support-readiness/processors/account-deletion-processor) is what processes those request.

## Issue processor

<sup>*Introduced via [support-team-meta#1329](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/1329)*</sup>

This runs every hour to process the issues in the [tracker](https://gitlab.com/gitlab-support-readiness/processors/account-deletion-processor).

It handles the assignment of issues to those who will work them and the tagging of the issues.

## Triage policies

<sup>*Introduced via [support-team-meta#1329](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/1329)*</sup>

Utilizing the [GitLab Triage Gem](https://gitlab.com/gitlab-org/ruby/gems/gitlab-triage), the triage policies are a group of conditions and actions that are enacted upon issues within the [Account Deletion and Other Requests project](https://gitlab.com/gitlab-com/gdpr-request).

The source code for it is located [here](https://gitlab.com/gitlab-com/gdpr-request/-/blob/master/.triage-policies.yml)
