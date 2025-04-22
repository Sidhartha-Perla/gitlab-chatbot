---
layout: sec_direction
title: "Category Direction - Dynamic Application Security Testing"
description: "Dynamic application security testing (DAST) is a process of testing an application or software product using a hacker-like approach. Learn more here!"
---

- TOC
{:toc}

## DAST

| | |
| --- | --- |
| Stage | [Secure](https://about.gitlab.com/direction/application_security_testing/) |
| Maturity | [Viable](/direction/#maturity) |
| Content Last Reviewed | `2025-03-26` |

### Introduction and how you can help

Thank you for visiting this category direction page on Dynamic Application Security Testing (DAST) at GitLab. This page belongs to the Dynamic Analysis group of the Secure stage and is maintained by [John Crowley](https://gitlab.com/johncrowley).

This direction page is a work in progress and everyone can contribute:

 - Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/gitlab/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=Category%3ADAST) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
 - Please share feedback directly via email or on a video call. If you're a GitLab user and have direct knowledge of your need for DAST, we'd especially love to hear from you.

### Overview

Dynamic application security testing (DAST) runs automated penetration tests to find vulnerabilities in your web applications as they are running. DAST automates a hacker’s approach, simulates real-world attacks, and can identify critical threats such as cross-site scripting, SQL injection, and cross-site request forgery. DAST is language-agnostic and examines your application from the outside in.

We recommend adding DAST to your software development security alongside other foundational application security testing such as secret detection, dependency scanning, static application security testing (SAST), container scanning, and API security testing. Including DAST in this defense-in-depth approach ensures that your team can identify and mitigate the runtime vulnerabilities and misconfigurations DAST detects that other security tools cannot detect. With a running application in a test environment, DAST scans can be automated in a CI/CD pipeline, automated on a schedule, or run independently by using on-demand scans.

DAST has historically been the domain of security teams, rather than developers. Many organizational security teams are small and are not integrated into development teams, so they lack the resources to test applications for vulnerabilities before releasing them to a production environment. Discovering vulnerabilities in production or late in the development process is expensive and creates unnecessary risk for both the organization and the users of the application. GitLab DAST is designed to be managed by developers and run against a pre-production staging server, mitigating the risk of releasing vulnerable software to production.

### Strategy

Our goal is to help customers reduce the security risks and compliance challenges they face while building and maintaining web applications. We do this by focusing on the earliest phases of the software development lifecycle (SDLC) and by striving to improve collaboration between security teams and developers.

### 1 year plan

#### What we recently completed
<!-- Lookback limited to 3 months. Link to the relevant issues or release post items. -->
In GitLab 17.0 we [removed Proxy-based DAST](https://gitlab.com/groups/gitlab-org/-/epics/11426) which has been replaced with DAST (formerly named Browser-based DAST), a proprietary offering that provides full coverage for modern applications, including single-page web apps (SPAs).

Between 16.9-16.11, we completed a number of [DAST Performance improvements](https://gitlab.com/groups/gitlab-org/-/epics/12194), including:
1. Snip navigation paths to improve crawler performance, which reduced scan time by 20% according to our benchmark test. [See the issue](https://gitlab.com/gitlab-org/gitlab/-/issues/430815) for more details.
1. Optimize DAST reporting to reduce memory usage, which reduced runner memory spikes during DAST scans. [See the issue](https://gitlab.com/gitlab-org/gitlab/-/issues/444180) for more details.
1. Limit the number of goroutines created when crawling. [See the issue](https://gitlab.com/gitlab-org/gitlab/-/issues/440151) for more details.
1. Optimize finding elements to interact with. This reduced scan time by 6%. [See the issue](https://gitlab.com/gitlab-org/gitlab/-/issues/440295) for more details.
1. Optimize JSON unmarshalling of DevTools messages. This reduced scan time by 7%. [See the issue](https://gitlab.com/gitlab-org/gitlab/-/issues/439726) for more details.
1. Browser-based DAST crawl tasks are not running in parallel, causing performance degradation. [See the issue](https://gitlab.com/gitlab-org/gitlab/-/issues/435325) for more details.

#### Roadmap
See our [prioritized roadmap here](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/#priorities).

#### What's Next & Why

Over the next 3 months, we plan to:
- [Add 3 additional active checks](https://gitlab.com/groups/gitlab-org/-/epics/13411), which will strengthen the detections included in DAST and ensure full parity with the previous offering, proxy-based DAST.

With the remainder of the year, our focus is on:
- [Multi-factor Authentication support one-time password method](https://gitlab.com/groups/gitlab-org/-/epics/13633), which will enable teams to run DAST scans on test applications without disabling MFA for apps that utilize a one-time-password MFA authentication method.

### 3 year plan

Looking forward, we will continue to focus on features that enable customers to efficiently reduce risk. We want to ensure that it is easy to enable and run DAST scans, scan times are efficient, and security weaknesses identified via DAST are easy to prioritize and remediate. Future capabilities focus on reducing scan times, enabling greater flexibility with authentication, and providing better visibility into what has been scanned.

1. [Decrease need for support escalation for DAST](https://gitlab.com/groups/gitlab-org/-/epics/11230) will reduce the amount of time developers need to spend on support requests by improving error messages and documentation, and making it easier for developers to reproduce and troubleshoot issues that are escalated.
1. [DAST Pre-scan verification](https://gitlab.com/groups/gitlab-org/-/epics/7069) will reduce onboarding friction points by providing customers with verification that we can connect to their target site, authenticate, and follow links to crawl a few pages without errors. These confirmations will lead to greater feature adoption and reduced support times.
1. [On-demand DAST Configuration Parity](https://gitlab.com/gitlab-org/gitlab/-/issues/466299) will reduce onboarding friction by enabling customers who use On-Demand DAST scans to have full access to the same configuration settings that are currently available when DAST is configured via templates.
1. [Visibility within DAST](https://gitlab.com/groups/gitlab-org/-/epics/14028) enables customers to better understand how they can tune their configuration settings for more successful scans. We'll provide visibility into much of an applicaiton was crawled, how long it took to perform specific security checks, and when and why a scan failed.
1. [DAST Crawler Performance Improvements](https://gitlab.com/groups/gitlab-org/-/epics/12194) continues to focus on making DAST scans performant. DAST scans tend to take significantly longer than other secure scans, and reducing scan time is critical to ensuring customers can include DAST in their DevSecOps processes.

### Best in Class Landscape
<!-- Blanket description consistent across all pages that clarifies what GitLab means when we say "best in class" -->

BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

#### Key Capabilities

For this product area, these are the capabilities a best-in-class solution should provide:

1. The ability to accurately and comprehensively detect security weaknesses outlined in the OWASP Top 10:2021.
1. The ability to accurately and comprehensively detect security weaknesses outlined in the OWASP Top 10:2024.
1. Good crawling coverage for detecting weaknesses within modern, single-page web applications.
1. Reporting and filtering to allow users to easily see and prioritize security weaknesses in their applications.
1. Flexible scans that can be scheduled, enforced via MRs, or initiated manually.
1. Actionable remediation guidance explaining the steps developers need to take to remediate findings.
1. Support for shifting security results left into the IDE.
1. The ability to enforce policies preventing DAST security flaws from being merged into the default branch.

## Competitive Landscape

- [Veracode](https://www.veracode.com/products/dynamic-analysis-dast)
- [StackHawk](https://www.stackhawk.com/)
- [Bright Security](https://brightsec.com/)
- [Invicti (Netsparker)](https://www.invicti.com/)
- [Probely](https://probely.com/)
- [Microfocus Fortify WebInspect](https://software.microfocus.com/en-us/products/webinspect-dynamic-analysis-dast/overview)
- [IBM AppScan](https://www.ibm.com/security/application-security/appscan)
- [Rapid7 AppSpider](https://www.rapid7.com/products/appspider)
- [Detectify](https://detectify.com/)

We have an advantage of being able to provide testing results before the app is deployed into the production environment, by using Review Apps. This means that we can provide DAST results for every single commit. The easy integration of DAST early in the SDLC is a unique position that GitLab has in the DAST market. Integrating other tools at this stage of the SDLC is typically difficult, at best.

## Pricing and Packaging

The GitLab DAST features are all packaged as part of the [GitLab Ultimate tier](https://about.gitlab.com/pricing/ultimate/). This aligns with our [pricing strategy](https://handbook.gitlab.com/handbook/company/pricing/#pricing-strategy) as these features are relevant for executives who are concerned about keeping their organization secured from security weaknesses (CWEs).

## Analyst Landscape

DAST is not a standalone market evaluated by analysts, but is included in the analysis of DevSecOps and Application Security markets.

* [Gartner Application Security Testing Reviews](https://www.gartner.com/reviews/market/application-security-testing)
