---
layout: sec_direction
title: Product Section Direction - Security
description: "Security visibility from development to operations to minimize risk"
canonical_path: "/direction/security/"
---

## On this page
{:.no_toc}

- TOC
{:toc}

**Security visibility from development to operations to minimize risk**
    

GitLab provides the single application organizations need to find, triage, and fix vulnerabilities, from development to production. This empowers organizations to apply repeatable, defensible processes that automate security and compliance policies that proactively reduce overall security risk.



## Section overview

The Sec section focuses on providing security and compliance visibility across the entire software development lifecycle.
We accomplish this by:
- [Shifting security testing left](#shift-left-no-more-left-than-that), enabling developers to begin security scanning as soon as they write their first line of code.
- Providing organizations with visibility and control over the security risk present across their environment.

### GitLab and the DevSecOps lifecycle

GitLab is uniquely positioned to fully support DevSecOps by providing a single application for the entire software development lifecycle. This includes both shifting Application Security Testing (AST) left as well as providing visibility and control over security and compliance findings, from first line of code to production.

GitLab's single application maps directly to the DevSecOps lifecycle. GitLab's AST stage focuses on pinpointing vulnerabilities and weaknesses, from development to production, while the Security Risk Management (SRM) stage provides visibility and control over the security findings AST detects. Software Supply Chain Security (SSCS) makes GitLab a verifiably secure foundation for software delivery. Together, GitLab supports all teams involved in delivering secure applications:

* Develop: Developers create new source code, including new features and bug fixes, and commit this code to a branch within the project. This step is supported by the [Create](https://about.gitlab.com/stages-devops-lifecycle/create/) stage of the DevOps lifecycle, providing developers with [source code management](https://about.gitlab.com/solutions/source-code-management/), [code editors](https://about.gitlab.com/direction/create/ide/web_ide/), and [code review](https://about.gitlab.com/stages-devops-lifecycle/create/) workflows.
* Analyze: Upon code commit, AST scanners kick off automatically and identify any new security findings with the delta code change. This enables developers to stay within context, enabling them to understand the cause and effect of their code change. AST scanners leverage the [Verify](https://about.gitlab.com/stages-devops-lifecycle/verify/) stage of the DevOps lifecycle to provide scanning within the [CI pipeline](https://about.gitlab.com/solutions/continuous-integration/).
* Mitigate: Developers are provided with the [details needed](https://docs.gitlab.com/ee/user/application_security/index.html#interacting-with-the-vulnerabilities) to understand how to remediate the newly introduced security findings. Developers are also offered [automatic remediation](https://docs.gitlab.com/ee/user/application_security/vulnerabilities/index.html#resolve-a-vulnerability), where applicable.
* Protect: AST scanners provide continuous scanning coverage for applications deployed to production, while SRM dashboards and policies and SSCS compliance frameworks help users implement their security and compliance requirements across their organization.

### Lowering the cost of remediation

Remediating security vulnerabilities earlier reduces risk and makes remediation cheaper.

![Cost of Remediation](/images/direction/sec/Cost_Of_Remediation.png)

When security vulnerabilities are identified at the time of code commit, developers can understand how their newly
introduced code has led to this new issue. This gives the developer a cause-and-effect enabling quicker resolution
while not having the time hit of context switching. This is not true as security scanning is performed later in the
software development lifecycle. New vulnerabilities may not be identified until weeks or months after they were added
to the application while under development.

Time is not the only savings when shifting security left.

![Stage of Remediation](/images/direction/sec/Stage_of_Remediation.png)

In [“The Economic Impacts of Inadequate Infrastructure for Software Testing”](https://www.nist.gov/system/files/documents/director/planning/report02-3.pdf), NIST estimated the cost of remediating software bugs at $59.5 billion/year. This is compounded when taking in the average time to remediate software bugs. In [“Software Development Price Guide & Hourly Rate Comparison”](https://www.fullstacklabs.co/blog/software-development-price-guide-hourly-rate-comparison), FullStack Labs estimates the average cost of a software developer at $300/hour. The following table outlines the cost to remediate software bugs at different stages of the software development lifecycle:

![Completed Loop](/images/direction/sec/costs_table.png)

These costs are just the start of the financial impact when the software bug is also a software vulnerability. IBM, in partnership with the Ponemon Institute, put the [average cost to remediate a data breach in 2020](https://www.ibm.com/security/digital-assets/cost-data-breach-report/#/) at $3.86 million (USD). This does not take into consideration the reputation impact to the organization.

### Closing the loop

Having visibility into security risk in just development only provides you with half of the picture. Development and
SecOps teams need to have a closed feedback loop enabling both teams to be successful. Development teams can gain
insight into attacks targeting the applications they develop. This allows them to prioritize vulnerabilities correctly,
enabling proactive resolutions to reduce risk. Likewise, SecOps teams can gain insight from their development
counterparts, providing them with visibility into how the application works. This allows them to best apply proactive
measures to mitigate attacks targeting the application until development can fix the vulnerability.

![Completed Loop](/images/direction/sec/Completed_Loop.png)

Closing the loop requires close collaboration, transparency, and efficiencies that only a single platform for the entire DevOps lifecycle can provide. Shifting security left while also providing protection for applications in production within a single application empowers teams to work closer together. Security is a team sport, and teams working together can best reduce their organization's overall security risk.

### Groups

The Sec section is made up of three stages of the DevSecOps lifecycle, along with the groups in those stages:

- [Application Security Testing (AST)](/direction/application_security_testing/)
- [Security Risk Management (SRM)](/direction/security_risk_management/)
- [Software Supply Chain Security (SSCS)](/direction/software_supply_chain_security/)

### Teams and Investments

#### Team members

Team members for the Sec Section can be found in the links below:

* [Development](https://about.gitlab.com/company/team/?department=sec-section)
* [User Experience](https://about.gitlab.com/company/team/?department=secure-ux-team)
* [Product Management](https://about.gitlab.com/company/team/?department=sec-pm-team)
* [Quality Engineering](https://about.gitlab.com/company/team/?department=sec-datascience-qe-team)

#### Investments

Team members can learn more about GitLab's investment into the Sec section by checking the
[Product Investment](https://internal.gitlab.com/handbook/product/investment/) page in the internal handbook.

### Accomplishments, News, and Updates

A complete list of released features can be found in the [Release Feature Overview](https://gitlab-com.gitlab.io/cs-tools/gitlab-cs-tools/what-is-new-since/?tab=features&selectedStages=application_security_testing&selectedStages=security_risk_management&selectedStages=software_supply_chain_security).

## 3 Year Section Themes

### Scan everything, but don't get in the way

The increasing pace of modern software development demands that we push security testing further left than before, integrating it into existing workflows rather than forcing teams to adapt their processes or context-switch to separate tools.

Moving security scanning directly into the IDE and pre-commit stages enables developers to catch vulnerabilities, exposed secrets, and dependency issues before they even enter the codebase, dramatically reducing remediation costs and team overhead.

For this proactive approach to succeed, security tools must provide clear, actionable feedback that developers can understand without deep security expertise, including precise code locations and step-by-step remediation guidance with examples of secure coding patterns.

By making security both approachable and efficient, we help organizations build a true DevSecOps culture where security becomes a natural part of every developer's daily work, transforming how organizations approach application security while significantly reducing the burden on overburdened security specialists.

**To achieve this theme, GitLab will pursue capabilities like:**

- Delivering scan results at the speed of software development by offering:
  - Real-time scanning for SAST and SCA vulnerabilities and leaked secrets.
  - Intelligent incremental scans that avoid re-scanning parts of the application that haven't changed.
- Identifying runtime security issues early in the development phase with DAST unit tests and by running DAST scans in development environments like \`localhost\`.
- Integrating Secret Detection scanning across the platform to prevent leaked secrets in every written place like descriptions and comments on issues, epics, and merge requests, wikis, and more.
- Automatically scanning for CVEs in repositories and registries for dependencies, packages, and containers.
- Detecting malicious packages and prevent them from entering your software supply chain

### Make better risk decisions with richer context

In today's complex security landscape, presenting raw vulnerability data without context can lead teams to work on less impactful tasks or accept risks without realizing the consequences. That doesn't work well for anyone.

By combining multiple security scanning methods and leveraging more advanced techniques like AI and machine learning, we can provide deeper context and more accurate risk assessments for each security finding. This intelligence-driven approach helps teams cut through the noise of security alerts, focusing remediation efforts on vulnerabilities that pose the greatest actual risk to their applications. Integration across different security disciplines creates a comprehensive view of each vulnerability's impact and exploitability, enabling more confident decision-making about when and how to remediate issues.

The power of machine learning transforms security scanning from a simple detection tool into an intelligent advisory system that helps teams make informed, strategic decisions about their security posture and resource allocation.

**To achieve this theme, GitLab will pursue capabilities like:**

- Integrating detection capabilities across scanning disciplines to provide more actionable outcomes.
- Using SAST for advanced tasks like reachability analysis and API discovery, so we can enrich DAST and other scanning processes.
- Correlating and deduplicating scanning outputs to reduce noise, uncover the most urgent exploitable issues, and focus attention on the most impactful remediations.
- Leveraging AI/ML to reduce false positives by understanding normal code structure, commit history, and runtime behavior.

### Take action, not just inventory

When tools identify vulnerabilities but don't provide a clear path to resolution, organizations end up exposed to security risks for longer than necessary. Worse still, as backlogs of security issues grow, organizations end up accepting risks without realizing it—an untriaged and unresolved vulnerability is one that's tacitly accepted.

Modern security tools must go beyond detection to provide automated remediation pathways that help both developers and security teams efficiently address vulnerabilities.

- Developers can make larger impacts when they receive automated merge requests for dependency updates, intelligent suggestions for fixing vulnerable code, and clear guidance on implementing secure alternatives directly within their development environment.
- Security professionals benefit from automated workflows that can immediately revoke exposed secrets, quarantine vulnerable dependencies, and orchestrate large-scale security updates across multiple repositories without manual legwork.

As applications and security threats grow more complex, effective security programs have to rely on automation to scale up. By transforming security findings into automated actions, intelligent tools help organizations dramatically reduce their mean time to remediation while allowing both development and security teams to focus on strategic work rather than routine maintenance.

**To achieve this theme, GitLab will pursue capabilities like:**

- Automating remediation actions like revoking exposed secrets, blocking insecure code, and upgrading vulnerable dependencies.
- Continuing to invest in GitLab Duo Vulnerability Explanation and Vulnerability Resolution to produce better recommendations.
- Providing automated system hardening, such as removing dependencies that are not in use.
- Improving AST scan results so that they are easier to understand and act on.


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


## Stages and Categories

The Sec section is composed of two stages, [Secure](https://about.gitlab.com/direction/application_security_testing/) and [Govern](https://about.gitlab.com/direction/software_supply_chain_security/), each of which contains several categories. Each stage has an overall
strategy statement below, aligned to the themes for Sec. Each category within each stage has a dedicated direction page
plus optional documentation, marketing pages, and other materials linked below.

### Application Security Testing (AST) stage
The Application Security Testing (AST) stage helps customers find vulnerabilities in applications before they reach production.
We focus on developing scanning capabilities to find these vulnerabilities, then we work closely with the [Security Risk Management](../security_risk_management/) and [Software Supply Chain Security](../software_supply_chain_security/) stages to ensure that organizations can take action on the vulnerabilities our scanners detect.

> GitLab was named as a [Challenger in the 2022 Magic Quadrant for Application Security Testing](https://page.gitlab.com/resources-report-gartner-magic-quadrant-ast-2023.html).


#### Categories


#### Pricing
Application Security Testing pricing and tiering reflects GitLab's overall [pricing model](https://handbook.gitlab.com/handbook/company/pricing/).

##### Ultimate

We focus our efforts primarily on Ultimate.
Advanced security is [an Ultimate pricing theme](https://handbook.gitlab.com/handbook/company/pricing/#ultimate) and helps customers deliver on organization-wide security and compliance priorities.

Advanced features, including technology developed in-house at GitLab and technology we've [acquired](https://handbook.gitlab.com/handbook/acquisitions/), are available only in Ultimate.

##### Free and Premium

We make a subset of our AST scanners available in all tiers (including Free).
We typically do this when the scanners are themselves open-source.

We do not specifically focus on Premium.



### Software Supply Chain Security (SSCS) stage
The Software Supply Chain Security (SSCS) stage helps organizations to reduce their overall risk by applying appropriate management and governance oversight across the entire DevSecOps lifecycle. SSCS provides management tools to secure the GitLab platform itself by restricting access to authenticated users and ensuring they are provisioned with the least amount of required privileges. To help manage and monitor risk levels, the SSCS stage provides visibility into user permissions and activity; project dependencies; security findings; and adherence to compliance standards. This visibility is then coupled with enforcement capabilities to proactively prevent risks by automating compliance and securing the software supply chain.


#### Categories


#### Pricing
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



*Last Updated: 2025-02-20*
</p>
