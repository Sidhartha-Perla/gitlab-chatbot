---
title: SLAs
description: Operations workflow page for Zendesk SLAs
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/slas"
---

{{% alert title="Note" color="primary" %}}

All SLA changes are handled via a standard deployment.

{{% /alert %}}

{{% alert title="Note" color="danger" %}}

Exercise extreme caution in making SLA changes. This can directly impact contractual obligations GitLab has to its customers.

{{% /alert %}}

## Creating a SLA

For these, you will need to create a corresponding SLA file in the sync repo.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

## Editing a SLA

For these, you will need to locate the corresponding SLA file in the sync repo and make changes to it.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

## Deleting a SLA

The process to delete a SLA is exactly as described in the [SLA documentation page](../../docs/zendesk/slas#deleting-a-sla).

## Exception deployment

To perform an exception deployment for SLAs, navigate to the SLAs project in question, go to the scheduled pipelines page, and click the play button. This will trigger a sync job for the SLAs.

## Repo links

- [Zendesk Global sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-global/sla-policies)
- [Zendesk US Government sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/sla-policies)
