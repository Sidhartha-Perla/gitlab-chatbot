---
layout: sec_direction
title: "Category Direction - Permissions"
description: "GitLab's Permissions category provides both default roles and custom roles to enable organizations to set up least-privileged users across their GitLab environment."
---

- TOC
{:toc}

## Permissions

| | |
| --- | --- |
| Stage | [Govern](https://about.gitlab.com/direction/software_supply_chain_security/) |
| Maturity | [Viable](/direction/#maturity/) |
| Content Last Reviewed | `2024-10-28` |

### Introduction and how you can help
This direction page describes GitLab's plans for the permissions category that supports the following features:
\* [Default roles](https://docs.gitlab.com/ee/user/permissions.html)
\* [Custom roles](https://docs.gitlab.com/ee/user/custom\_roles.html).
\* Token Permissions
This direction page is a work in progress, and everyone can contribute:
\* Comment on existing [Authorization issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created\_date&state=opened&label\_name[]=group%3A%3Aauthorization) in the public gitlab-org/gitlab issue tracker. If you don't see an issue that matches, file [a new issue](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable\_template=Feature Proposal - basic), then post a comment that says @gitlab-bot label ~"group::authorization" ~"Category:Permissions" so your issue lands in our triage workflow.
\* Please share feedback directly via [email](mailto:jrandazzo@gitlab.com) or schedule a[ video call](https://calendly.com/joerandazzo/30min). If you're a GitLab user and have direct knowledge of your need for permissions, default roles, custom roles, RBAC, or access management, we’d love to hear from you.
This page belongs to the Authorization group and is maintained by the Product Manager, [Joe Randazzo](https://gitlab.com/jrandazzo).
### Overview
The Authorization team will be addressing critical gaps in the permission category by focusing on enhancing support for custom roles, token permissions, and granular permissions on the admin page. The team's mission is to enable principle of least privielge, improve efficiency by access, and streamline compliance.
The Permissions category does not include Login, SAML, LDAP, Enterprise Users, User Management, or Tokens. These features can be found in the [Authentication group](https://about.gitlab.com/direction/software\_supply\_chain\_security/authentication/).
### Customer experience and challenges to address
Customers encounter several permission challenges while operating in GitLab including:
#### Lack of granular permissions for users
\* Customers, especially those in regulated environments expect to be able to reduce overprivileged access. The default roles including Owner and Maintainer for groups and projects can access a long list of settings that can lead to misconfiguration or abuse.
\* The [Admin area](https://docs.gitlab.com/ee/administration/admin\_area.html) for self-managed installations has many centralized views that makes it easy to quickly troubleshoot or report on metrics. Customers have several teams such as platform, support, or leadership that require access to the Admin Area to perform their job. This can lead to overprivileged access, inefficiencies in internal access requests, and negatively impact operations.
\* Customers have unique permission requirements ranging from separation of duties to adding or removing access from a default role. Examples include separating pipeline permissions from push/merge, permissions for project planning, and many more. As a result, various workarounds are suggested such as creating separate projects that results in isolated workflows and a disjointed user experience.
#### Lack of granular permissions for tokens
\* Tokens by default come with limited scopes and are often overprivileged with the `api` scope. In the event that a token is leaked, that token has a large blast radius to GitLab resources with potential for misconfiguration or abuse.
\* Job tokens are the preferred token in CI/CD workflows given its ephemeral nature. Today, the job token permissions are based on the user role who triggered the pipeline. Customers prefer to narrowly define the access to specific resources. In addition, the lack of API support for job tokens have pushed users to rely on long-lived tokens or group tokens that have security implications.
\* Internal customers or product groups do not have the ability to quickly add permissions to tokens. This makes it difficult for teams to prioritize and implement in their roadmap.
#### Missing custom role support across the platform
\* Customers rely on access controls to assign a role to a set of users. For example, customers currently assign a role (developer or maintainer) on who is allowed to merge into a protected branch. Custom roles are not supported for this protected resource and others, which prevents adoption.
#### Lack of centralized access visibility and auditability
\* Customers requested they need to understand who has access to resources, unused access, and overprivileged users during audit reviews. For example, whether John Doe still using permissions at the Owner level or could be demoted to Maintainer, or why Jane has Owner access?
#### Multiple layers of authorization causing confusion
\* Customers have shared that there is confusion in the permission system on who is authorized to do what based on the numerous authorization decision points, including:
\* Default roles
\* Custom roles
\* Protected resources such as branches or environments
\* Group or project access controls on what a role can do or not do.
\* Security policies
### 1 year plan
In FY25, we are planning to focus on the following Product Themes:
[Drive Use Case Adoption to Fully Realize Value](https://about.gitlab.com/direction/#drive-use-case-adoption-to-fully-realize-value) by continued expansion of user permissions:
#### What is next for us
With the customer challenges in mind, we will address the following:
- [Add support for granular token permissions to Job Tokens](https://gitlab.com/groups/gitlab-org/-/epics/14804) to allow for fine-grained access in CI/CD workflows.
- [Build Custom Admin Role to support granular permissions for the Admin Area](https://gitlab.com/groups/gitlab-org/-/epics/15069) to allow organizations to reduce the number of admins on self-managed environments.
- [Improve visibility by providing a breakdown of roles and assigned users](https://gitlab.com/groups/gitlab-org/-/epics/13434) to allow for organizations to identify and reduce overprivileged users.
See our prioritized roadmap in detail [here](https://about.gitlab.com/direction/software\_supply\_chain\_security/authorization/).
#### What we recently completed
- [Allow organizations to reduce Owners + Maintainers](https://gitlab.com/groups/gitlab-org/-/epics/14086) by using Custom Roles with 16 new permisions available including a [custom Security and Compliance role](https://docs.gitlab.com/ee/user/application\_security/#custom-security-role).
- Support mapping of large sets of users to custom roles including [LDAP link](https://gitlab.com/gitlab-org/gitlab/-/issues/435229), and [assigning a custom role to a group](https://gitlab.com/gitlab-org/gitlab/-/issues/443369).
- [Move custom role creation to the instance level for self-managed environments](https://gitlab.com/groups/gitlab-org/-/epics/11851)
- [Filter role on membership page](https://gitlab.com/gitlab-org/gitlab/-/issues/431397)
- [Export accurate record of permissions](https://gitlab.com/gitlab-org/gitlab/-/issues/460477)
- [View list of default roles and custom roles](https://gitlab.com/groups/gitlab-org/-/epics/14172) on Roles and Permission pages to quickly determine how many users are assigned.
<!--
<summary>BIC Roadmap
Key deliverables we're focusing on to build a BIC solution. List the epics by title and link to the epic in GitLab. Minimize additional description here so that the epics can remain the SSOT. This may be duplicative to the 1 year section however for some categories the key deliverables required to become the BIC solution will extend beyond one year and we want to capture all of the gaps. Moreover, the 1 year section may contain work that is not directly related to closing gaps if we are already the BIC or if we are differentiating ourselves.-->

### Target Audience
<!--
List the personas (https://handbook.gitlab.com/handbook/marketing/strategic-marketing/roles-personas#user-personas) involved in this category.
Look for differences in user's goals or uses that would affect their use of the product. Separate users and customers into different types based on those differences that make a difference.
-->
1. [Sidney (System Administrator)](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)
1. [Issac(Infrastructure Security Engineer)](https://handbook.gitlab.com/handbook/product/personas/#isaac-infrastructure-security-engineer)
1. [Delaney (Development Team Lead)](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
1. [Devon (DevOps Engineer)](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
1. [Alex (Security Operations Engineer)](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer)
1. [Parker (Product Manager)](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)
1. [Cameron (Compliance Manager)](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)


### Pricing and Packaging
<!--
-->

Default roles are available for all tiers while free Guest users are for the Ultimate tier only.

Custom roles serve the need for Large Enterprise customers, Mid-Market customers, and those who operate in regulated industries such as Financial, Healthcare, or Public Sector. This feature is available for Ultimate tier only.

<!-- ### Analyst Landscape -->


