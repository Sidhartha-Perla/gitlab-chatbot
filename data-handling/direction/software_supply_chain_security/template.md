---
layout: sec_direction
title: Product Stage Direction - Software Supply Chain Security
description: "GitLab Govern helps organizations manage security vulnerabilities, policies, compliance, and users across their enterprise. Learn more!"
canonical_path: "/direction/software_supply_chain_security/"
---

## On this page
{:.no_toc}

- TOC
{:toc}

**Organization-wide security vulnerability, policy, compliance, and user management**
    

| | |
| --- | --- |
| Section | [Sec](/direction/sec) |
| Content Last Reviewed | `2025-04-15` |
| Content Last Updated | `2025-04-15` |

The Software Supply Chain Security (SSCS) stage helps organizations to reduce their overall risk by applying appropriate management and governance oversight across the entire DevSecOps lifecycle. SSCS provides management tools to secure the GitLab platform itself by restricting access to authenticated users and ensuring they are provisioned with the least amount of required privileges. To help manage and monitor risk levels, the SSCS stage provides visibility into user permissions and activity; project dependencies; security findings; and adherence to compliance standards. This visibility is then coupled with enforcement capabilities to proactively prevent risks by automating compliance and securing the software supply chain.




## Stage Overview

The Software Supply Chain Security (SSCS) stage provides the capabilities necessary to meet security and compliance requirements for organizations at any scale.

### Groups

The SSCS Stage is made up of four groups:

* [Authentication](/direction/software_supply_chain_security/authentication/) - Complete user lifecycle management and assurance that all points of authentication into GitLab are performed securely.
* [Authorization](https://about.gitlab.com/direction/software_supply_chain_security/authorization/) - Ensure that users have roles and permissions that balance security and ease of performing their job within GitLab.
* [Compliance](https://about.gitlab.com/direction/software_supply_chain_security/compliance/tactical-priorities.html) - Provide users with the tools and features necessary to achieve visibility of checks, violations and audit events across the DevSecOps lifecycle.
* [Pipeline Security](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/) - Protect access to secrets and provide verifiable evidence that artifacts were created securely.

## 3 Year Stage Themes

### Top-down security controls

Security teams need centralized management for their security and compliance workflows.  Features such as user management, compliance labels, security policies, and the vulnerability and dependency lists need to allow for centralized management that applies across all of an organization&apos;s projects.

### No compromises with compliance

SSCS capabilities will ensure that compliance regulations are strictly followed in a way that they cannot be bypassed without the proper approvals. This includes providing the necessary tools to audit, monitor, and manage the compliance controls that are enforced.

### Coordinate governance across GitLab

SSCS capabilities will serve as a connection point for a seamless workflow spanning across the DevSecOps lifecycle.  By enabling collaboration between types of users, SSCS can help solidify the advantages GitLab has to offer as a single application.  For example, these areas might include the following:

  - Facilitating a continuous experience for scanning across repositories, registries, and production environments.
  - Centralizing security and compliance controls across GitLab, including merge request approvals, anomalous user activity, and anomalous pipeline/job activity.
  - Leveraging data about production environment configuration to reduce false positives in scanners.
  - Leveraging data about vulnerabilities in development to inform and drive threat mitigation in production.

### Emphasize usability and convention over configuration

SSCS capabilities will be [pre-configured with reasonable defaults](https://handbook.gitlab.com/handbook/product/product-principles/#convention-over-configuration) out-of-the-box whenever possible.  When not possible, they will be easy to configure either through code or through a guided UI workflow that is friendly to users without coding knowledge.  Regardless of how the capabilities are configured, they will be stored as code for ease of management.

For example, GitLab's [security policy editor](https://docs.gitlab.com/ee/user/application_security/policies/#policy-editor) supports editing policies in both a `rule mode` and in `yaml mode`.

### Secure the software supply chain

SSCS capabilities allow organizations to lock down every aspect of their supply chain. This includes securely authenticating users into GitLab, hardening the GitLab platform itself, and verifying every step along the DevSecOps lifecycle as code is created, built, and deployed.


## 3 Year Strategy

Building on those themes, some specific capabilities that we envision developing over the next 3 years include the following:

**Anti-Abuse**

1. Adaptive user-based rate limiting based on a trust score.
1. Insider threat policies to allow organizations to monitor and reduce risk.
1. Monitoring and alert system for new URLs in a pipeline network.

**Authentication**

1. Centralized management of users and tokens at scale, including visibility into access logs and automated notifications when credentials are required to be rotated.
1. Reduced friction from authentication flows across GitLab including support for new methods of authenticating.
1. Enforcement of authentication policies to increase security while minimizing disruption to automated workflows.

**Authorization**

1. Extended support for the Principle of Least Privilege to tokens in GitLab.
1. Improved management tools for custom roles as well as support for additional custom permissions.
1. More robust logic before granting access to a resource - consider not only the role of the user, but also other attributes such as security policies, trust score, etc.

**Compliance**

1. Added support to view how projects adhere to an expanded list of compliance and regulatory requirements.
1. Support for creating customized frameworks, with related requirements and checks to meet individual organizational needs.
1. Expanded support for out-of-the-box configurations that can be used to quickly bring projects into compliance.

**Pipeline Security**

1. Support for a GitLab-native secrets manager.
1. New tools to support SLSA L3 and automate generation of SLSA L3 compliant attestations.

## 1 Year Plan

Over the next 12 months, the SSCS stage is focused on addressing critical needs for security and compliance teams.  Some of the key initiatives include the following:

1. **Custom role improvements** - additional permissions, better management (bulk role assignment), support for LDAP sync.
1. **Compliance standards adherence report** - added support for requirements and checks as well as support for some customization.
1. **Enterprise token management** - gitlab.com support for the Credential Inventory, additional tools for managing access logs and for rotating tokens
1. **GitLab Secrets Manager** - a GitLab-native secrets manager that can be used to keep sensitive data secure.
1. **Expanded token security** - More granular permissioning for tokens across GitLab.

### What We're Not Doing

Although we will likely address many of these areas in the future (as described above in our [3 year strategy](https://about.gitlab.com/direction/software_supply_chain_security/#3-year-strategy)), we are not planning to make progress on the following initiatives in the next 12 months:
* Attempting to build our own Security Information and Event Management (SIEM) system
* Building analytics or algorithms to auto-tune or auto-recommend policy improvements

## Key Performance Metrics

The following metrics are used to evaluate the success of the Govern stage:

* Anti-Abuse: Monthly active users are not relevant for this group. Instead success is measured in the observed abuse rate combined with the impact to paid conversion.
* Authentication **Group Monthly Active Users**: This is the total number of users in a paid SAML group.
* Authorization **Group Monthly Active Users**: The number of unique users who are assigned to a custom role.
* Compliance **Group Monthly Active Users**: This is the total number of unique users viewing the Audit Events, Compliance Dashboard, or Credential Inventory pages in the last 28 days of the given month.
* Pipeline Security: TBD

Note: We do not yet have a single metric to track the success of the Govern stage as a whole.  This is being tracked in [this issue](https://gitlab.com/gitlab-data/product-analytics/-/issues/883).

## Target Audience
GitLab identifies who our DevSecOps application is built for utilizing the following categorization. We list our view of who we will support when in priority order.
* 🟩- Targeted with strong support
* 🟨- Targeted but incomplete support
* ⬜️- Not targeted but might find value

### Today
To capitalize on the opportunities listed above, the Govern Stage has features that make it useful to the following personas today.
1. 🟩  Developers / Development Teams
1. 🟩  Application Security Teams
1. 🟨️  Compliance Specialists / Manager
1. 🟨️  Legal Teams
1. 🟨  Infrastructure Security Teams

### Medium Term (1-2 years)
As we execute our [3 year strategy](#3-year-strategy), our medium term (1-2 year) goal is to provide a single DevSecOps application that enables SecOps to work collaboratively with DevOps and development to mitigate vulnerabilities in production environments.
1. 🟩  Developers / Development Teams
1. 🟩  Application Security Teams
1. 🟩  Compliance Specialists / Manager
1. 🟩  Legal Teams
1. 🟨  Infrastructure Security Teams

## Pricing

SSCS is focused on providing governance and compliance features that span across the DevSecOps lifecycle. SSCS's tiering strategy aligns with the GitLab approach of selecting the tier based on [who cares most about the feature](https://handbook.gitlab.com/handbook/company/pricing/#three-tiers).  Because Executives generally care most about governance features, it is expected that most SSCS features will land in the Ultimate tier.

##### Free
This tier is the primary way to increase broad adoption of the SSCS stage, as well as encouraging community contributions and improving security across the entire GitLab user base.

As a general rule of thumb, features will fall in the Free tier when they meet one or more of the following criteria:
* The feature is highly useful for an individual with a few small projects rather than meeting the needs of an organization or enterprise that is operating at scale.
* The feature is provided by an integration with an open source project rather than being natively developed by GitLab.

##### Premium
This tier is not a significant part of SSCS's pricing strategy; however, a few features features that primarily appeal to Directors rather than Executives may fall into the Premium tier. One example of this is our audit event functionality that is available in this tier.

##### Ultimate
This tier is the primary focus for the SSCS stage as most SSCS features enable executives to ensure that their organization meets compliance requirements and maintains an acceptable security posture.

As a general rule of thumb, features will fall in the Ultimate tier when they meet one or more of the following criteria:
* The feature is focused on enabling an organization or enterprise to operate at scale rather than an individual with a few small projects.
* The feature is natively developed by GitLab rather than being provided by an open source project.


## Categories


