---
layout: markdown_page
title: "Category Direction - Secret Detection"
description: "Secret Detection helps you find and fix leaked secret values like API keys, tokens, and private keys in your GitLab repositories. Learn more about where we're going."
---

- TOC
{:toc}

## Secret Detection

| | |
| --- | --- |
| Stage | [Application Security Testing](/direction/application_security_testing/) |
| Maturity | [Viable](/direction/#maturity) |
| Content Last Reviewed | `2025-01-15` |

### Introduction and how you can help
This direction page describes GitLab's plans for the Secret Detection category, which protects you against leaking credentials, tokens, or other secrets on GitLab. Everyone can contribute to where GitLab Secret Detection goes next, and we'd love to hear from you. The best ways to participate in the conversation are to:
- Comment or contribute to existing [Secret Detection issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_date&state=opened&label_name%5B%5D=Category%3ASecret%20Detection) in the public `gitlab-org/gitlab` issue tracker.
- If you don't see an issue that matches, file [a new issue](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable_template=Feature%20Proposal%20-%20basic).
    - Post a comment that says `@gitlab-bot label ~"group::secret detection" ~"Category:Secret Detection"` so your issue lands in our triage workflow.
- If you're a GitLab customer, discuss your needs with your account team.

### Overview
GitLab Secret Detection helps prevent a critical mistake: leaking credentials or other secrets. We want GitLab to be a safe place to develop software, so we're working to make Secret Detection a standard part of the software development lifecycle (SDLC). No one should have to _think_ about secrets to be protected from _leaking_ them.

We believe that the world is safer when [everyone can contribute](https://handbook.gitlab.com/handbook/company/mission/#mission) to software security.
Our customers, and those they serve, are better protected when developers and security professionals can fix potential security risks earlier.

The earliest possible time to catch a security issue is when the code is first written. GitLab sees code very early in the software development lifecycle, since we store production code and also support customer workflows (like merge requests) for pre-production development.
Our group is uniquely positioned to integrate static analysis everywhere as part of a comprehensive DevSecOps platform.
Our unique position allows us to embed security seamlessly and support collaboration within the tools teams already use.

The Secret Detection group's _business_ purpose is to build value for GitLab and our customers by:
1. Driving adoption of GitLab Ultimate through integrated security tools and removing the need for "point solutions".
1. Help teams confidently secure their code from the moment it’s written.

#### The problem
Even experienced developers and teams can slip up and cause serious risk by committing secrets into their code repositories.

The potential damage is significant:
- Secrets often provide access to sensitive data, production systems, or cloud resources that can be abused.
- If a repository is public, automated tools or malicious users can detect and abuse leaked secrets—there are public sites dedicated to listing these leaks.
- Even if a repository is private within a team or organization, leaked secrets can no longer be trusted to uniquely identify the authorized user(s) in a [non-repudiable](https://en.wikipedia.org/wiki/Non-repudiation) way.

#### GitLab's solution
GitLab Secret Detection helps you prevent the unintentional leak of sensitive information like authentication tokens and private keys.

Secret Detection checks your Git repositories to detect secrets or credentials, then it reports potential findings.
Today, Secret Detection jobs run in your CI/CD pipelines.

We want everyone to be secure, so:
- [Parts of Secret Detection](https://docs.gitlab.com/ee/user/application_security/secret_detection/#features-per-tier) are available in every GitLab tier.
- Secret Detection is on by default in [Auto DevOps](https://docs.gitlab.com/ee/topics/autodevops/).

In GitLab Ultimate, after you enable Secret Detection:
- You can see and address new Secret Detection findings in [merge requests](https://docs.gitlab.com/ee/user/application_security/#view-security-scan-information-in-merge-requests).
- Results appear in the [Vulnerability Report](https://docs.gitlab.com/ee/user/application_security/vulnerability_report/).
- [Automatic responses](https://docs.gitlab.com/ee/user/application_security/secret_detection/automatic_response.html) help mitigate leaks as soon as they occur.
- [Push protection](https://docs.gitlab.com/ee/user/application_security/secret_detection/secret_push_protection/) blocks secrets from being pushed to your GitLab repository.

Secret Detection doesn't target a specific language, so you can easily [enable it in any project](https://docs.gitlab.com/ee/user/application_security/secret_detection/).
Our approach takes advantage of [patterns for well-identifiable credentials](https://docs.gitlab.com/ee/user/application_security/secret_detection/detected_secrets.html) like service account keys and API tokens, but also searches for more generic secret types like passwords in certain contexts.

Our approach emphasizes the value of the most comprehensive DevSecOps platform by:
- Protecting the entire DevSecOps lifecycle, including code, issues, and other content.
- Shifting security earlier in the development process, so everyone can contribute to security.

To learn more, check the [Secret Detection documentation](https://docs.gitlab.com/ee/user/application_security/secret_detection/).

Outside of the Secret Detection category, GitLab also offers other features that relate to secret values:
- [Push rules](https://docs.gitlab.com/ee/user/project/repository/push_rules.html#prevent-pushing-secrets-to-the-repository) block files with certain names from being pushed to your repositories.
- The [Secrets Management](/direction/software_supply_chain_security/pipeline_security/secrets_management/) category focuses on enabling GitLab to use and manage secret values.

### Vision
Our vision captures what we want to deliver to customers in the next 3-5 years.

1. GitLab users are protected from credential-related security breaches.
2. Secret detection is 100% adopted by all Ultimate namespaces.


### Strategy and Themes
<!-- Capture the main problems to be solved in market (themes). Describe how you intend to solve these with GitLab (strategy). Provide enough context that someone unfamiliar with the details of the category can understand what is being discussed. -->

We're focusing on addressing the following user problems:

- **Coverage**: Ensuring protection against credential leaks across all areas of a Git repository—whether in code, issues, job logs, or elsewhere.
- **Time to Remediate**: Reducing the amount of time between when a secret is leaked and when it no longer poses a threat.
- **Prioritization**: Enabling teams to identify and address the most critical leaks quickly.

Solving these user problems support two primary goals:

1. Helping organizations meet security and compliance requirements within a unified DevSecOps platform.
2. Making GitLab a secure environment for software development.

### 1 year plan
<!--
1 year plan for what we will be working on linked to up-to-date epics. This section will be most similar to a "road-map". Items in this section should be linked to issues or epics that are up to date. Indicate relative priority of initiatives in this section so that the audience understands the sequence in which you intend to work on them.
 -->

Over the next major milestone, 17.0 - 17.11 (May 2024 - April 2025), we will be investing in the [next generation of Secret Detection](https://gitlab.com/groups/gitlab-org/-/epics/8667).  This includes:
    - [Push protection](https://gitlab.com/groups/gitlab-org/-/epics/11439), which blocks commits from being pushed if they contain secrets.
    - [Pipelineless post-receive scanning](https://gitlab.com/groups/gitlab-org/-/epics/8626), which replaces the [existing scanning system](https://docs.gitlab.com/ee/user/application_security/secret_detection/) that runs in CI/CD pipelines after content is pushed.

Specifically, we plan to focus on:

1. [Tracking leaks better](https://gitlab.com/gitlab-org/gitlab/-/issues/387583) as they move through a codebase, to avoid repeatedly surfacing the same leaks.
1. Speeding triage by [allowing more exceptions and ruleset customization](https://gitlab.com/groups/gitlab-org/-/epics/10325).
1. Scanning codebases [without pipeline jobs](https://gitlab.com/groups/gitlab-org/-/epics/8626), replacing the current pipeline-based approach. This will likely involve rethinking the end-to-end [workflow](https://gitlab.com/gitlab-org/gitlab/-/issues/425994) for detected secrets. This includes providing better organization-wide visibility of possible leaks and better context as leaks are detected.

#### What is next for us
<!-- This is a 3 month look ahead for the next iteration that you have planned for the category. This section must provide links to issues or
or to [epics](https://handbook.gitlab.com/handbook/product/product-processes/#epics-for-a-single-iteration) that are scoped to a single iteration. Please do not link to epics encompass a vision that is a longer horizon and don't lay out an iteration plan. -->

In the next 3 months, we are planning to:
- [Verify validity of GitLab Secrets](https://gitlab.com/groups/gitlab-org/-/epics/13988)
- Continue to add support for [push protection default rules](https://gitlab.com/gitlab-org/gitlab/-/issues/504680)
- [Improve GitLab-maintained Secret Detection rulesets](https://gitlab.com/groups/gitlab-org/-/epics/14009)
- Conduct [performance testing of secret push protection](https://gitlab.com/gitlab-org/gitlab/-/issues/480688)

We are also _looking forward_ by refining the [system architecture](https://docs.gitlab.com/ee/architecture/blueprints/secret_detection/) for pipelineless post-receive scanning.  This will share significant architectural elements with the new pre-receive secret detection feature.

#### What we are currently working on
<!-- Scoped to the current month. This section can contain the items that you choose to highlight on the kickoff call. Only link to issues, not Epics.  -->

We are currently working on:
- [Improving GitLab-maintained Secret Detection rulesets](https://gitlab.com/groups/gitlab-org/-/epics/14009)
- Completing [performance testing of secret push protection](https://gitlab.com/gitlab-org/gitlab/-/issues/480688)
- Designing the vision for [validity checks for GitLab Secrets](https://gitlab.com/groups/gitlab-org/-/epics/13988) in the vulnerability report.

#### What we recently completed
<!-- Lookback limited to 3 months. Link to the relevant issues or release post items. -->

In the last three months we releaseed [secret push protection (SPP) to general availability](https://gitlab.com/groups/gitlab-org/-/epics/13107).  In addition we made enhancements to SPP including:

1. Added audit events whenever a push protection _exclusion_ occurs.  For example, we’ve detected a secret, but your _exclusion_ allowed the developer to push it anyway without being blocked.
2. Added REST API endpoints that make it easier to enable push protection:
   - Enable the feature in self-managed instance (so it can be enabled on project-by-project basis)
   - Check whether the feature has been enabled for a project
   - Enable the feature for a project and for all projects in a group

In early 2025, secret detection now includes remediation steps for each type of detected secret. This guidance helps you systematically address exposures and reduce the risk of security breaches. Remediation steps will appear on all vulnerabilities upon the completion of a pipeline.

Check [older release posts](https://gitlab-com.gitlab.io/cs-tools/gitlab-cs-tools/what-is-new-since/?tab=features&selectedCategories=Secret+Detection&minVersion=15_00) for our previous work in this area.

#### What is Not Planned Right Now
- **Repositories outside of GitLab:** We don't plan to offer protections for projects hosted outside of GitLab.
- **Credentials not common in software:** We plan to focus on the types of credentials that are most common in DevSecOps workflows and in software development.
This means we **won't** actively pursue rules that are:
    - For services unlikely to be used in a software project.
    - Closer to Data Loss Prevention, for example searching for personally identifiable information (PII) or credit card numbers.

### Best in Class Landscape
<!-- Blanket description consistent across all pages that clarifies what GitLab means when we say "best in class" -->

_ℹ️ Best In Class (BIC) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape._

#### Key Capabilities
Secret Detection products should:

- Help developers avoid making leaks in the first place.
- Enable quick responses to any leaks that are made.
- Deliver trustworthy, accurate findings, with appropriate priority, so that the right findings are remediated quickly.
- Automatically respond to leaks, without human intervention, when possible.
- Provide security users with overall visibility into exposures anywhere within their organization.

#### Roadmap
<!-- Key deliverables we're focusing on to build a BIC solution. List the epics by title and link to the epic in GitLab. Minimize additional description here so that the epics can remain the SSOT. This may be duplicative to the 1 year section however for some categories the key deliverables required to become the BIC solution will extend beyond one year and we want to capture all of the gaps. Moreover, the 1 year section may contain work that is not directly related to closing gaps if we are already the BIC or if we are differentiating ourselves.-->

See our [prioritized roadmap here](https://about.gitlab.com/direction/application_security_testing/secret-detection/#priorities).

In addition to those main themes, we are exploring additional detection techniques including:
- Checks for whether detected credentials are still active.
- Machine Learning or other solutions for identifying generic or lower-confidence secrets. These secrets, which include passwords and tokens that don't have an identifiable structure, are more difficult to detect while minimizing false-positive results.

#### Top Competitive Solutions
<!-- PMs can choose to highlight a primary BIC competitor--or more, if no single clear winner in the category exists; in this section we should indicate: 1. name of competitive product, 2. links to marketing website and documentation, 3. why we view them as the primary BIC competitor -->
There are dozens of vendors providing security detection as a standalone offering, integrated as a feature within the platforms they protect or as part of a larger solution. Here’s an overview of the top competitive tools for secret detection:

1. [Fortify](https://www.microfocus.com/en-us/cyberres/application-security/static-code-analyzer)
1. [Endor Labs](https://www.endorlabs.com/)
1. [GitGuardian](https://www.gitguardian.com/)
1. [GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)
1. [Gitleaks](https://github.com/gitleaks/gitleaks)
1. [Semgrep](https://semgrep.dev/products/semgrep-secrets/)
1. [Snyk](https://docs.snyk.io/scan-application-code/snyk-code/introducing-snyk-code/key-features/ai-engine#hardcoded-secrets)
1. [TruffleHog Enterprise](https://trufflesecurity.com/trufflehog/)
1. [Veracode](https://www.veracode.com/security/static-analysis-tool)

### Target Audience
The target audience for secret detection tools includes security-focused roles like [Alex, the Security Operations Engineer](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer), and [Sam, the Security Analyst](https://handbook.gitlab.com/handbook/product/personas/#sam-security-analyst). Their primary responsibility is to protect the organization from leaked secrets, which includes responding to alerts and managing incidents involving compromised credentials. Alex and Sam are instrumental in selecting, deploying, and fine-tuning tools like Secret Detection to enhance security posture.

In contrast, [Sasha, the Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer), may unintentionally expose credentials while coding or pushing updates. Although Sasha prioritizes security, her main focus is on building and shipping features, so she values tools that are effective yet minimally disruptive. Secret detection tools need to support Sasha's workflow by providing seamless, reliable protection without adding burdensome processes or frequent false positives.

### Pricing and Packaging
At GitLab, Secret Detection is primarily included in the Ultimate tier, though basic protection features are available across all tiers. We plan to enhance the level of protection provided in every tier, while continuing to offer distinct [organization-level value](https://handbook.gitlab.com/handbook/company/pricing/#three-tiers) in Ultimate.

|  | Free | Premium | Ultimate |
|--|------|---------|----------|
| Pipeline Secret Detection | ✅ | ✅ | ✅ |
| Push Protection |  |  | ✅ |
| Client-side warnings (UI) | ✅  | ✅ | ✅  |
| Automatic Response to leaked secrets (public projects) |  |  | ✅  |

### Analyst Landscape
Analysts usually include Secret Detection as a secondary feature of Application Security Testing (AST) coverage.
See [Category Direction - Static Application Security Testing (SAST)](https://about.gitlab.com/direction/application_security_testing/static-analysis/sast/) for up-to-date analyst coverage.
