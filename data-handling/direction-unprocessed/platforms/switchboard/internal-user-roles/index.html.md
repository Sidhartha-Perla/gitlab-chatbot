---
layout: markdown_page
title: "Switchboard user roles for GitLab team members"
description: "Switchboard supports several roles that are specific to GitLab team members to enable them to support GitLab Dedicated customers."
---

- TOC
{:toc}

## Scope

Switchboard supports several roles that are specific to GitLab team members to enable them to support GitLab Dedicated customers. These are separate from the [user roles](https://docs.gitlab.com/ee/administration/dedicated/#add-users-to-a-tenant-instance) we make available to GitLab Dedicated customers which are specific to each customer's GitLab Dedicated instance.

GitLab team member roles currently apply to all tenants connected to a given Switchboard environment (e.g. Production), so a GitLab team member cannot have different levels of permissions for different GitLab Dedicated tenants within the same environment.

## How to request access as a GitLab team member

See [Requesting Access to the Switchboard application](https://handbook.gitlab.com/handbook/engineering/infrastructure/team/gitlab-dedicated/switchboard/#requesting-access-to-the-switchboard-application) on the Switchboard team page.

## GitLab team member roles and permissions

### Roles

- **Read only**: View tenant instance only. Example CSMs and Compliance team members.
- **Provisioner**: Provision accounts and manage users.
- **Support**: View tenant instance and manage users. Example: Professional Services (PS) and Support team members.
- **Operator**: Operate the tenant instance. This role is restricted to Site Reliability Engineers (SREs) and Switchboard team members.


### Permissions

| **Role** | Create tenant | View tenants | Edit tenant config | Create jobs | Add/modify GitLab users | Add/modify tenant users | Login with email/password | Create API Read Only Token | Read Only API Access |
|-----------------|---------------|--------------|--------------------|-------------|---------------------------|---------------------------|---------------------|------------|------------|
| **Read only** | No           | Yes          | No                 | No          | No                        | No                       | No                  | Yes        | Yes        |
| **Provisioner** | Yes           | Yes          | No                 | No          | No                        | Yes                       | No                  | Yes        | Yes        |
| **Support**     | No            | Yes          | No                 | No          | No                        | Yes                       | No                  | Yes        | Yes        |
| **Operator**    | Yes           | Yes          | Yes                | Yes         | Yes                       | Yes                       | Yes                 | Yes        | Yes        |
