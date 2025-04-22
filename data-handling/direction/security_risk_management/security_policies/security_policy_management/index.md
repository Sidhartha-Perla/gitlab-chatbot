---
layout: sec_direction
title: "Category Direction - Security Policy Management"
description: "GitLab's Security Policy Management category provides unified policy and alert orchestration capabilities that span across the breadth of GitLab's security offerings."
canonical_path: "/direction/security_risk_management/security_policies/security_policy_management/"
---

- TOC
{:toc}

## Security Risk Management

| | |
| --- | --- |
| Stage | [Security Risk Management](/direction/security_risk_management/) |
| Maturity | [Minimal](/direction/#maturity) |
| Content Last Reviewed | `2025-01-14` |

### Introduction and how you can help
Thanks for visiting this category direction page on Security Policy Management in GitLab. This page belongs to the Security Policies group of the Security Risk Management stage and is maintained by Grant Hickman ([ghickman@gitlab.com](mailto:)).
This direction page is a work in progress, and everyone can contribute. We welcome feedback, bug reports, feature requests, and community contributions.
- Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/gitlab/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label\_name[]=Category%3ASecurity%20Policy%20Management) and [epics](https://gitlab.com/groups/gitlab-org/-/epics/4592) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
- [Schedule a video call](https://calendly.com/g-hickman) with the Security Policies Product Manager. If you're a GitLab user and have direct knowledge of your need for security policies, we'd especially love to hear from you.
- [Email the Security Policies Product Manager, Grant](mailto:).
- Can't find an issue? Make a [feature proposal](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable\_template=Feature%20proposal%20-%20detailed) or a [bug report](https://gitlab.com/gitlab-org/gitlab/-/issues/new?&issuable\_template=Bug). Please add the appropriate labels by adding this line to the bottom of your new issue `/label ~"devops::security risk management" ~"Category:Security Policy Management" ~"group::security policies"`.
- Consider signing up for [First Look](https://about.gitlab.com/community/gitlab-first-look/).
We believe [everyone can contribute](https://handbook.gitlab.com/handbook/company/mission/#contribute-to-gitlab-application) and so if you wish to contribute [here is how to get started](https://about.gitlab.com/community/contribute/).
### Overview
Security Policy Management enables security and compliance teams to manage and mitigate risk at scale through vulnerability management workflow automation, DevSecOps configuration automation, and tools for ensuring security by default.
Security policies empower AppSec teams to effectively and efficiently adhere to organizational security standards at scale.
Additionally, the Security Policies group supports the underlying framework for enforcing default settings and configuration, ensuring vulnerabilities cannot be introduced through misconfiguration throughout the DevSecOps lifecycle.
GitLab was recently named as a [Challenger in the 2022 Magic Quadrant for Application Security Testing](https://page.gitlab.com/resources-report-gartner-magic-quadrant-ast-2023.html). As highlighted by Gartner, "It's not enough to automate the process of scanning. When and how policies are applied, and how exceptions are handled, also needs to be automated to bring consistency and auditability. GitLab provides a broad range of policies and common controls for compliance." With GitLab's Security Policy Management, you can leverage automation to efficiently improve your security posture and gain some clarity amidst the chaos.
Current Capabilities

#### Security Policies

Security policies allow users to use a single, simple UI to define rules and actions that are then enforced. Four types of security policies are currently supported:

1) Scan execution policy
2) Pipeline execution policy
3) Merge request approval policy
4) Vulnerability management policy

Security policies themselves are fully audited and can be configured to go through a two-step approval process before any changes are made.  All policies are supported at the group, sub-group, and project levels, and you can enforce policies across your entire GitLab instance or namespace.

**Scan Execution Policies** allow users to require vulnerability scans to be run, either on a specified schedule or as part of a pipeline job. Currently we support requiring the execution of [SAST, Secret Detection, Container Scanning, Dependency Scanning, and DAST scans](https://docs.gitlab.com/ee/user/application_security/policies/scan-execution-policies.html).  We do not plan on adding support for License Compliance as its functionality is [planned to be merged into Dependency Scanning](https://gitlab.com/groups/gitlab-org/-/epics/8072) ([now supported for SaaS behind feature flag](https://about.gitlab.com/releases/2023/02/22/gitlab-15-9-released/#new-license-compliance-scanner)).  We do intend to add support for Fuzzing; however, this is not on our near-term roadmap.

**Pipeline Execution Policies** ensure enforcement of custom CI within project pipelines, allowing for enforcement of customized GitLab security scan templates, 3rd party security scans, and custom CI scripts/jobs that support security and compliance use cases.

**Merge Request Approval Policies** allow users to enforce approval on a merge request when policy conditions are violated. Currently criteria related to both security and license scanners are supported.  For example, users can require approval on merge requests that introduce newly-detected, critical vulnerabilities into their application. Additionally, you may enforce and override particular project settings, such as blocking push/force pushing and ensuring that approvals are now allowed by a merge request author or committer on the MR. Merge request approval policies have support multiple different rules: Security approvals, License approvals, and Compliance Approvals (via the "Any merge request" option).
**Vulnerability Management Policies** automate workflows for AppSec professionals, ensuring they can more efficiently narrow down and identify actionable vulnerabilities across their organizations assets. This policy type initially supports "auto-resolve" capabilities for filtering out vulnerabilities that are no longer detected and automatically marking them as resolved.

[Learn more](https://docs.gitlab.com/ee/user/application_security/policies/)

#### Security Approvals

![Security Approvals](/images(https://about.gitlab.com/direction/software_supply_chain_security/security-approvals.png)

Security approvals allow users to select the conditions that must be met to trigger the security approval rule, including which branches, scanners, vulnerability count, and vulnerability severity levels must be present in the MR.  If all conditions are met, then the merge request is blocked unless an eligible user approves the MR. This extra layer of oversight can serve as an enforcement mechanism as part of a strong security compliance program.

Security approvals are a type of merge request approval policy and can be configured in the **Security & Compliance > Policies** page.

[Learn more](https://docs.gitlab.com/ee/user/application_security/policies/scan-result-policies.html)



#### License Approvals

![License Approvals](/images(https://about.gitlab.com/direction/software_supply_chain_security/license-approvals.png)

License approvals allow users to select the conditions that must be met to trigger the license approval rule, including which licenses are expressly allowed or prohibited from being present in the MR.  If all conditions are met, then the merge request is blocked unless an eligible user approves the MR. This extra layer of oversight can serve as an enforcement mechanism as part of a strong legal compliance program.

License approvals are a type of merge request approval policy and can be configured in the **Security & Compliance > Policies** page.

[Learn more](https://docs.gitlab.com/ee/user/compliance/license_approval_policies.html)



#### Enforce Peer Review on Any Merge Request

By selecting "Any merge request" in the policy rules, you can enforce approvals on any merge request, regardless of any security scan or license results. This allows for enforcement of the "four eyes principle", which ensures that no code changes that will ultimately end up in a production environment can be merged without approval from at least two different people. Compliance requirements may vary, but this policy rule allows for enforcement of one or more approvals on a merge request that meets the specified criteria.


[Learn more](https://docs.gitlab.com/ee/user/application_security/policies/scan-result-policies.html#any_merge_request-rule-type)


### Strategy and Themes
As businesses typically struggle with inequitable gearing ratios between software engineers and security engineers ([20:1 or worse](https://engineering.gusto.com/security-is-testing/#:~:text=At%20many%20organizations%2C%20there%20is,software%20engineers%20to%20security%20engineers.)), GitLab's tools can help enterprises [automate and manage security risk at scale](https://about.gitlab.com/free-trial/devsecops/).
In spite of the size of an AppSec team compared to the number of applications they are responsible for securing, there are many challenges these individuals must overcome, which are ripe for automation and optimization via Security Policies and the broader suite of GitLab tools:
- Enabling and configuring security analyzers at scale: To get vulnerability data and perform a triage to prioritize and remediate these risks, AppSec teams must first be able to get the data to work with. Ensuring scanners are enabled on all GitLab repositories where required and also configured properly to generate useful data is fundamental to a strong vulnerability management process. And this effort in and of itself is not always intuitive - matter of fact, it can be fairly time-consuming and error-prone. Our Security Platform Management team will be responsible for improving capabilities here moving forward.
- Capturing accurate and actionable data by which to generate insights and prioritize: Next, AppSec teams must have confidence that they are utilizing data they can trust to be able to build a process of prioritizing and remediating vulnerabilities. Inaccurate data or false positives can displace and distract both security and development teams from spending effort on something truly actionable and impactful. Increased noise and false positives can result in frustration and wasted effort. Security policies, however, can help to automate the process of filtering out false positives, classes of vulnerabilities that may not apply case-by-case, tuning triage rules, layering business context into decisions, and more.
- Taking swift action: Once vulnerabilities are triaged, AppSec teams must then use various tools and approaches at their disposal to actually ensure security controls are adhered to. This can vary based on the type of vulnerability, where it's discovered, the risk/impact associated, and the step in the process the vuln was detected. Policies can help to automate tasks and ensure vulnerabilities are detected/prevented early in the process, or generate time-bound issues for remediation if it's too late to prevent it in the first place. Policies can further automate the process of detection and remediation through automated dependency/package versioning, or other more sophisticated workflows.
- Intelligent risk-based triage: Even with the most accurate of security scan data and amazing workflows for actioning detected findings, AppSec teams struggle to keep up. The sheer amount of code generated in the age of AI is increasing at a rapid pace and security tooling must scale at the same rate if AppSec teams are to be successful. Policies can help to ease the load by collecting and infusing inherent qualitied detected within the GitLab platform into the decisioning process of the policy engine. Policies can better understand when/where code is deployed, which environments, whose code and which 3rd party packages make up the build, and so much more. GitLab has the opportunity to connect dots across the entire DevSecOps workflow to give AppSec teams more insight to prioritize and triage risk, and potentially save their companies millions in damages.
Moving into 2025, Security Policies will have a heightened focus on simplifying and automating the process of triaging and resolving vulnerabilities. Security policies are a common feature found throughout AST and ASPM tools and help AppSec teams to translate their model for security risk into an engine for more efficiently identifying risk and prioritizing actions to take.
GitLab Security Policies will build on top of our existing capabilities to further accelerate AppSec teams' productivity, to enable policies gracefully across an organization at scale and reduce the vulnerabilities that poise the greatest risk.
Primary Themes for Security Policies include:
1) Continued improvement of Pipeline Execution Policies
2) Increased AppSec efficiency through Vulnerability Management Workflow Automation
3) Security Policy platform capabilities to enable GitLab teams
## Continued improvement of Pipeline Execution Policies
Pipeline execution policies continue to be a powerful feature for Enterprise customers as they allow for broad enforcement of custom CI throughout an organizations project's. Pipeline-based enforcement helps address numerous use cases for customers across multiple areas from Application Security Testing (enforcing customized GitLab security scans, 3rd party security scans, custom scanning rules), Application Security Posture Management (auto-remediation workflows, monitoring), Software Supply Chain Security (separation of duties, pipeline protections), and Compliance (enforcement of pipeline-based compliance checks/rules, reporting scripts).
As we sunset Compliance Pipelines, we continue to expand on our capabilities for Pipeline Execution Policies to address more of these use cases in a stable and long-term implementation.
## Increased AppSec efficiency through Vulnerability Management Workflow Automation
As part of our focus on increasing AppSec efficiency, we're working on introducing new capabilities for automating vulnerability management workflows. This will help security teams more efficiently triage and resolve vulnerabilities at scale.
Key initiatives in this area include:
1. Auto-resolve policies: Automatically resolving vulnerabilities that are no longer detected in more recent scans.
2. Auto-dismiss policies: Automating the dismissal process of vulnerabilities based on certain attributes like directory, file path, and identifier. This policy could further be extended to dismiss low-severity vulnerabilities in non-critical projects, dismiss vulns for specific vulnerability classes, and automatically dismissing known false positives.
3. Auto-remediation policies: Automation policies that update dependencies with known fixes by bumping versions and generating MRs to test success, applying pre-defined patches for common vulnerabilities, and/or triggering remediation scripts globally for common issues effecting multiple repositories.
4. Additional tuning and policy actions within MR Approval Policies: New tuning options to more efficiently automate triage and new actions to facilitate where in GitLab the vulnerability data is actioned by AppSec teams and Developers. These improvements include:
- Excluding packages from License Approval Policies
- License Approval Policy severity filtering
- Security Approval filters for KEV/EPSS
- Automated filtering of policy exceptions from appearing in the Vulnerability Report if merged
- Tools for considering and integrating historical data/trends and threat intelligence feeds to assess real-world risk
5. Workflow automation integrations: Automated GitLab ticket creation, notification generation for critical vulnerabilities/findings, to relevant team members through collaboration platforms, custom workflow triggers that can be used for integration hooks.
6. Tighter integration with GitLab features, such as Merge Requests (MR widgets/Reports) and Pipelines (better visibility into security policy effects): By building more seamless integration into these GitLab features, we can reduce confusion, reduce false positive policy violations, and help AppSec and Development teams move more quickly with confidence. Key activities here include:
- Improved DevSecOps MR Experience, including clearer workflow for documented "exceptions" to policy violations and better integration of security violations and security scan results in the MR reports (moving noisy security findings outside of the MR widget and consolidating with policy violations details)
- Better policy rules for default policy exceptions
- Addressing foundational infrastructure/data challenges to ensure consistency in security findings in the MR vs security policies
By implementing these automation capabilities, we aim to significantly reduce the manual workload for AppSec teams, allowing them to focus on more strategic security initiatives while ensuring consistent and efficient vulnerability management across the organization.
## Security Policy platform capabilities to enable internal GitLab groups to contribute new policies
The final theme of prioritization for Security Policies is both foundational as well as forward-looking. Within this category, we'll ensure that all existing Security Policies, as well as new planned vulnerability management policies, operate in a seamless manner with a modern and intuitive UX that rivals available AppSec tools in the marketplace.
It's important and critical that it's easy for users to get started with GitLab Security Policies regardless of their frame of reference, whether their previous experience is with standard AST scanners, ASPM tools, or if they have a DevSecOps background. In this theme, we will build on our existing framework but will be willing to break the mold to introduce new concepts and simplify the experience.
Key capabilities here include:
1. Re-imaginging the concept of Security Policy Projects and reducing the dependency or "requirement" on YAML
2. Simplifying management of permissions/access for managing policies globally and at scale
3. Elevating policy management to instance or "organization" level for simpler global management
4. More intuitive, scalable, and re-usable policy interactions or interfaces that do not create exponential increase of dependencies to manage
5. Building a foundational framework that all GitLab teams can use to introduce new policy types to solve for security and compliance use cases
## Cross-functional Areas:
As we do work within a platform, it's also important to capture and track any cross-functional areas and plans or opportunities for collaboriation. Our key areas of collaboration include:
- Security Platform Management: We'll work very closely together with this team as we delineate policy enforcement and automation versus security scanner configuration. In the future, we are working to enable quicker/simpler configuration of security scanning at scale, while security policies will enable enforcement and assurance that security scanning is properly enabled.
- Code Review & Source Code: As the Code Review team and Source Code teams own capabilities such as MR approval and Repository settings, we'll continue to collaborate as policies use merge requests and repository rules to apply security enforcement and require MR approvals.
- Compliance: Security policies leverage Compliance Frameworks as an option for scoping and applying policies to projects. Likewise, Security Policies help compliance teams to ensure security-related controls are properly implemented and enforced. In this context, policies can help compliance teams to automate global rules to reduce risk categorically rather than managing enforcement project-by-project.
- Security Insights & Security Infrastructure: The interplay between the Vulnerability Report, MR Widgets in merge requests, and the backing databases that are storing vulnerability data will all be core to the inputs for Security Policies, as well as affected by policy automations.
- Other GitLab Groups: We'll continue to work and plan for long-term development of GitLab policies that can be used to enhance and automate security and compliance across the DevSecOps platform. Our goal is to introduce a surface area for cross-functional teams to develop and contribute their own policies through a singular interface for the security and compliance persona.
How Security Policies help GitLab Win

- Security Policies aligns with our efforts in [driving adoption of GitLab Ultimate](https://about.gitlab.com/direction/#drive-adoption-of-gitlab-ultimate), as we're satisfying a market need that truly differentiates GitLab as a DevSecOps platform.
- Security Policies is core to one of our FY24 Product Investment themes,["Advanced security and compliance"](https://about.gitlab.com/direction/#advanced-security-and-compliance).
- Investment in Security Policies is strategic as we focus on [depth over breadth](https://about.gitlab.com/direction/#depth-over-breadth) in the Security section and Security Risk Management stage to provide robust solutions that address [DevSecOps adoption challenges (internal)](https://internal.gitlab.com/handbook/product/devsecops-adoption/priorities/) (also highlighted as one of our [FY24 Yearlies](https://about.gitlab.com/company/yearlies/#fy24-yearlies)). Security Policies and the greater Security section vision will help reduce churn/contraction by delivering predictable high value to customers.

### 1 year plan
See our [prioritized roadmap here](https://about.gitlab.com/direction/software\_supply\_chain\_security/security\_policies/).
#### What we are currently working on
After introduction of pipeline execution policies in 17.2, we are adding new capabilities to ensure flexibility and better support less common use cases supported in compliance pipelines today. We are working to ensure seamless migration from compliance pipelines to pipeline execution policies for security and compliance use cases.
Improvements we are actively working on include:
1. [Configurable required stages in pipeline execution policies](https://gitlab.com/gitlab-org/gitlab/-/issues/475152)
1. [Compliance handling of `needs` statements for jobs executing in the `.pipeline-policy-pre` stage](https://gitlab.com/gitlab-org/gitlab/-/issues/469256)
1. [Scheduled Pipeline Execution Policies](https://gitlab.com/groups/gitlab-org/-/epics/14147)
1. The ability to enforce approval requirements in MR approval policies for users with a [custom role](https://gitlab.com/groups/gitlab-org/-/epics/13550).
1. [Improving compatibility between security policies and security analyzers](https://gitlab.com/groups/gitlab-org/-/epics/14119)
#### What is next for us
1. Usability improvements for seamlessly linking/scoping policies during policy creation.
1. Abstraction of security policy projects for simpler policy management.
1. Policy tuning capabilities - exclude components in License Approval Policies.
1. Policy tuning capabilities - configure License Approval Policies based on license severity.
1. Policy tuning capabilities - filter Security Scan Policies based on CVE/CWE, EPSS, and KEV.
1. More flexible trigger definitions in scan execution policies.
1. Auto-dismiss policies to help AppSec teams reduce noise around vulnerabilities based on filters for criteria including CVE/CWE and related identifiers and file paths.
1. Automated creation of GitLab issues for vulnerability resolution.
1. Critical actionable workflow notifications
#### What we recently completed
1. In 17.8, we've added support for [multiple distinct approvers](https://gitlab.com/groups/gitlab-org/-/epics/12319) in MR approval policies.
1. In 17.5, [we added groups as an option to policy scopes](https://gitlab.com/groups/gitlab-org/-/epics/14149), improving the ease of enforcing policies across many groups in an instance.
1. In 17.4, we've refined pipeline execution policies to allow for configuration of a [job suffix for handling job naming collisions](https://gitlab.com/gitlab-org/gitlab/-/issues/510305).
1. In 17.2, we introduced [Pipeline Execution Policies](https://docs.gitlab.com/ee/user/application\_security/policies/pipeline\_execution\_policies.html) that enable you to enforce custom CI jobs, security scans, and scripts in developer pipelines for security and compliance enforcement.
#### What is Not Planned Right Now
We do not plan to be a full-featured SOAR solution capable of aggregating, correlating, and enriching events from multiple security vendors. We intend to remain focused on providing security management and security orchestration for the security tools that are part of the GitLab product only.
We do not plan to support Network Policies (Container Host Security and Container Network Security). We previously offered this capability but learned that challenges related to GTM, pricing & packaging, and personas led to low adoption. This required a shift in our strategy. More details around the decision can be found [in this internal issue](https://gitlab.com/gitlab-com/Product/-/issues/3600).
We are not building a workflow engine for broad automation use cases in GitLab, but are focused on security policies that improve efficiency and achieve outcomes for AppSec teams.
While we see opportunity to improve the security and compliance posture of GitLab as a whole across the DevSecOps lifecycle, our group will not be responsible in the short-term for development of any new policies that do not benefit the AppSec persona directly (beyond continued support of pipeline execution policies). Long-term, we plan to provide more capabilities and support to aide in development of policies in these and other areas. Examples include:
- [Status Check Policies](https://gitlab.com/groups/gitlab-org/-/epics/10177) (enforcement of external or internal status checks within MRs)
- Deployment Policies (enforcement of deployment controls and approvals)
- Push Enforcement Policies (enforce settings/controls around pushing code)
- Access Control Policies (access right review policies or other controls/enforcement around access and authorization)
- Insider Threat Policies (policies to detect malicious patterns such as large scale code repo cloning)
- Further compliance enforcement of security scanning, such as enforcement when [CI is disabled](https://gitlab.com/groups/gitlab-org/-/epics/14057)
And lastly, we are no longer focused on the wide scale enablement and configuration of security scanners, rather this direction will be matrixed to the Security Platform Management group.
### Long-term Vision
Long-term, as part of the Security Risk Management stage, we aspire first to:
1. Provide an Enterprise-ready solution for automating prioritization, triage, handling and reporting of vulnerabilities that fully supports our Application Security Testing offering.
2. Enrich vulnerability / dependency data via additional metrics and security parameters for improved prioritization and triage.
3. Use the power of GitLab as platform to enhance prioritization, leveraging AI and creating inuitive workflows for automated triage and remediation. Examples may include:
- Automatic dependency versioning
- AI analysis/summaries of security posture - violations, vulnerabilities, etc
- Applying increased severity to vulnerabilities discovered in certain environments, and adjust risk levels depending on the build.
- Auto-remediation workflows when certain vulnerability classes are detected, such as package managers with known issues.
Combined with efforts across other groups in our stage, we plan to offer a robust AST offering that is deeply integrated within our platform and ensuring seamless consolidation, enablement, and management of security scans and findings/vulnerabilities through a single pane of glass.
In the future, Enterprise users will be able to simplify the process of creating global policies across their organization (from the Organization layer in GitLab), to manage security and compliance risk with ease, to gain insight into the health status of their organization, and to granularly enforce policy rules only where it's appropriate for the business.
We'll further improve upon the user experience of policies by reducing reliance on the `policy.yml` and reducing the number of steps required to create a policy (while maintaining benefits of policy-as-code).
As we work to mature our Security Policy Management category, we'll be providing additional support for gauging the impact (blast radius) a policy will have before it is deployed. Audit mode will give teams a method to roll out policies and observe before enforcing. Impact assessments will help users understand how many projects will be impacted and expected behavior before enforcing a policy.
We'll work cross-functionally with teams in GitLab to provide more visibility into how policies are applied and affect other features, such as how policies may affect project settings or modify behaviors in pipelines.
We'll also work to improve context and onboarding, making it easier to enable policies by default through compliance frameworks, or identify where policies should be applied.
Integration between security policies and our compliance features (including compliance frameworks and standards adherence reporting) will continue to bridge the gap between compliance observability and reporting and security and compliance enforcement. Policies can be enforced against projects, linked up to compliance reporting, and used to remediate compliance violations. By leveraging security policies, alongside GitLab compliance features.
For each policy type, we'll work to provide deep capability that helps users filter and customize rules to address most common use cases and requirements for security and compliance enforcement.
As we achieve goals around AST and vulnerability management workflow automation, we'll work to further extend security policy capabilities by establishing a framework that facilitates development of policies across the DevSecOps lifecycle, where GitLab groups across the platform can contribute new policies that can be managed centrally/globally and through a consistent and flexible UX catered to security/compliance personas.
Policies then will continue to grow to become more sophisticated and intelligent, leveraging the insight of an integrated DevSecOps platform to make decisions and enforce behaviors efficiently, contextually, and non-destructively. Policies will ensure that security and compliance are met globally, while increasing rather than disrupting velocity.
### Best in Class Landscape
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
BIC Capabilities 
Security Policy Management enables global control of settings across an organizations technology assets and can extend to the processes and procedures used to enforce particular policies.
For GitLab, our focus is on supporting DevSecOps personas, which specifically involves AppSec, Security Operations, Compliance, and InfraSec personas. Each of these users is tasked with ensuring a business' applications are secure and compliant by preventing or reducing the risk of introducing vulnerabilities into production code and live applications. This involves securing each step of the SDLC as well as ensuring proper access and compliance within GitLab itself.
The most critical capabilities for a best-in-class DevSecOps Policy Management solution are as follows:
- The ability to easily manage and enforce policies globally across all relevant development projects.
- Two person approval of code changes, or change management workflows to reduce risk of introducing vulnerabilities.
- Complete assurance that policies cannot be circumvented.
- Audit capabilities to record and produce proof of any policy changes.
- Granular configuration of policies to allow businesses to filter out false positives, non-material findings, or irrelevant changes.
- Enforcement of security scanning in development projects.
- Enforcement of various project settings and configurations, such as push rules.
- A mechanism for ensuring production environments can only be deployed from the default/protected branch (which is presumed secure/compliant from policies above).
- Thorough alerting and notification capabilities to communicate high-risk changes, violations, or other policy related data into the communication tool of choice.
- Risk-based Vulnerability Management workflows.
- Insider threat policies to identify and protect against potential attacks.
- Pipeline health policies that identify malicious or anomalous network/system calls.

BIC Roadmap


Top 2 BIC Competitive Solutions
Security Policy Management at GitLab is in a category of its own. It's not currently possible to fully orchestrate the enforcement of security policies across the entire Software Development Lifecycle in the way you can with GitLab. Often, enforcing security and compliance requirements requires identifying endpoints across many tools in your software toolchain and creating custom solutions to instantiate controls that you must maintain.
With GitLab Security Policy Management, we offer global enforcement of policies across the groups, subgroups, and projects in your GitLab instance (or namespace in the case of GitLab.com). GitLab is responsible for maintaining the UI and YAML editor that can be leveraged to create and enforce policies, and we continue to build more capabilities to optimize and simplify management for diverse use cases, which mitigates further development efforts to manage customization of policy logic.
While we offer a competitive solution that reduces toolchain complexity and eases global enforcement, some of our competitors have offerings with comparable functionality.
#### GitHub
We have a very competitive position against GitHub regarding policy management. We offer a UI for intuitively defining custom policies, in addition to YAML mode for advanced users. We're expanding to make group and organization-level management of policies a breeze across large organizations while increasing the accuracy and confidence in the enforcement of policies. GitHub offers a very basic solution for checking vulnerabilities and blocking the merge of a PR but lacks the depth as well as the strategic investment to solve this holistically for Enterprise customers.
GitHub includes the following capabilities today:
- Code scanning results check can be used to find problems in code by severity.
- Users can override default behaviors.
- CodeQL can be integrated to require approval based on vulnerabilities found. If the code scanning results check finds any problems with the severity of the error, critical or high, the check fails, and the error is reported in the check results. If all the results found by code scanning have lower severities, the alerts are treated as warnings or notes, and the check succeeds.
There are prerequisites to utilizing GitHub, however:
- Many types of scanning require integration with external scanners
- It lacks the visual editor and native management of policy as code
- The ability to intuitively manage policies across groups is limited or requires manual configuration and maintenance using CodeQL
- It lacks the ability to limit who can give approval for failed code scanning checks. When critical or high vulnerabilities are found, anyone who is eligible to approve the PR can approve and allow the code to be merged in.
#### Synopsys
Synopsys offers [Intelligent Orchestration](https://www.synopsys.com/software-integrity/intelligent-orchestration.html), which allows users to optimize pipeline usage, in turn reducing pipeline costs and potentially impacting developer velocity due to optimizing pipeline duration.
However, leveraging Synopsys requires integration with your CI/CD and maintaining enforcement across the toolchain.

### Target Audience
<!--
List the personas (https://handbook.gitlab.com/handbook/marketing/strategic-marketing/roles-personas#user-personas) involved in this category.

Look for differences in user's goals or uses that would affect their use of the product. Separate users and customers into different types based on those differences that make a difference.
-->


Primary:

- [Amy (Application Security Engineer)](https://handbook.gitlab.com/handbook/product/personas/#amy-application-security-engineer)

Secondary

- [Sasha (Software Developer)](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
- [Cameron (Compliance Manager)](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)


### Pricing and Packaging
<!--
-->

Security and Compliance policies are capabilities that serve the needs of Large, Ultimate tier customers, Mid-market customers, and customers working in highly regulated industries/sectors such as PubSec, Healthcare, and Financial Services.

All features under Security Policy Management target Ultimate-tier customers.

GitLab offers a [simple pricing model](https://about.gitlab.com/pricing/) based on monthly seats. Ultimate tier customers gain access to more powerful tools that unlock the power of DevSecOps, including Security Policy Management, Security Dashboards, Dependency Scanning, DAST, Fuzzing, and much more.

### Analyst Landscape

We are beginning to engage analysts on this topic, but do not currently have research to provide.
