---
layout: sec_direction
title: "Category Direction - API Security"
description: "API Security is focused on securing APIs"
---

- TOC
{:toc}

## API Security

| | |
| --- | --- |
| Stage | [Secure](https://about.gitlab.com/direction/application_security_testing/) |
| Maturity | [Viable](/direction/#maturity) |
| Content Last Reviewed | `2024-04-24` |

### Introduction and how you can help

Thank you for visiting this category direction page on API Security Testing at GitLab. This page belongs to the Dynamic Analysis group of the Secure stage and is maintained by [John Crowley](https://gitlab.com/johncrowley).

This direction page is a work in progress and everyone can contribute:

 - Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/gitlab/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=Category%3AAPI%20Security) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
 - Please share feedback directly via email or on a video call. If you're a GitLab user and have direct knowledge of your need for API Security, we'd especially love to hear from you.

### Overview

API Security encompasses many features that reduce security risks in Application Programming Interfaces (APIs) and protect them from attacks.  Modern applications consist of numerous APIs, which make it efficient for software programs to interact with one another. APIs make it easy for developers to build and maintain applications, and they make it easy for machines to share and modify data. APIs frequently transmit sensitive data and expose business logic, making them attractive targets for hackers.  Traditional application security techniques should be used in the API development phase, and WAFs and gateways should be used in production, but these methods must also be augmented by additional API-focused security tools and techniques. As API security has historically been the domain of security teams, rather than developers, testing the API in its running state often is overlooked during the development process. Yet, the shift-right methods that many organizations use, including WAFs and gateways, have proven to be insufficient to stop security incidents on their own. It's clear that a shift-everywhere, defense-in-depth approach, which includes identifying and remediating security weaknesses early in the API management lifecycle is critical.

As a category, API Security includes: API Security Testing (dynamic) and API Fuzz Testing for REST, GraphQL, and SOAP APIs. Future capabilities include: [API Discovery](https://www.akamai.com/glossary/what-is-api-discovery), [API Inventory](https://www.cequence.ai/blog/api-security/what-is-api-inventory), API [Risk Scoring](https://www.crowdstrike.com/cybersecurity-101/risk-based-vulnerability-management), API Analysis, [ABAC API Service Mesh](https://www.cncf.io/blog/2019/04/25/simplifying-microservices-security-with-a-service-mesh), [OpenAPI Spec Audit](https://docs.42crunch.com/latest/content/concepts/api_contract_security_audit.htm#), and [gRPC support](https://grpc.io/docs/what-is-grpc/introduction) . This feature set will evolve over time to address the most pressing API Security issues.

- API Security Testing includes dynamic tests that simulate the way a hacker would make malicious requests. The goal is to identify weaknesses (CWEs) that could be exploited and lead to data breaches or other security incidents.
- API Fuzz Testing sets operation parameters to unexpected values in an effort to cause unexpected behavior and errors in the API backend. This helps identify bugs and potential security issues that other QA processes may miss.

### Strategy and Themes

Our goal is to help customers reduce the security risks and compliance challenges they face while building and maintaining APIs. We do this by focusing on the earliest phases of the API lifecycle including: design, build, and test. By incorporating security testing early in the API lifecycle, we can help organizations become secure by design. Our themes include:

1. **Shifting API Security Testing and Compliance left** - Our goal is to provide API Security scanning as part of the standard development process. This means that API security is executed every time a new review app is available or a build is deployed to a server.
1. **Accurate API Specifications** - Strong API security begins with a well-defined OpenAPI spec. Open API specifications define the expected behavior of an API. Our goal is to be able to analyze pre-existing API specifications and to automatically generate accurate API specifications where they do not exist, to help enable API Security Testing. Accurately defining the expected behavior helps to identify potential authorization and authentication, data validation, and other security risks in APIs.
1. **Accurate API Inventory** - Our goal is to be able to identify all of the APIs in an organization because one cannot protect what one cannot see. Many organizations today do not have visibility into their API attack surface.
1. **Continuous scanning** - Scanning for security weaknesses needs to be a continuous effort because the list of API-based threats is constantly growing. To stay secure, users need a solution that will be updated constantly with the latest detections.
1. **Secure by Design** - Providing API design and build guardrails within a DevSecOps platform, can help developers and security teams greatly reduce the biggest security gaps that impact APIs today--authentication and authorization failures.

### 1 year plan

#### What we recently completed
<!-- Lookback limited to 3 months. Link to the relevant issues or release post items. -->
In GitLab 16.10 we collaborated with Vulnerability Research to [Comprehensively Review API Security Testing Checks](https://gitlab.com/gitlab-org/gitlab/-/issues/441687) which will enable us to add additional security checks in the near future.

#### Roadmap
See our [prioritized roadmap here](https://about.gitlab.com/direction/application_security_testing/dynamic-analysis/#priorities).

#### What's Next & Why

Our primary focus for FY2025 is on modernizing our core API Security capabilities. The category has not seen much recent investment due to other pressing priorities. Over the next 3 months, we plan to:

- [Add TLS 1.3-only support for API Security Testing](https://gitlab.com/gitlab-org/gitlab/-/issues/441470) to reduce adoption barriers.
- [Granular Pass/Fail configuration for API Security Testing jobs](https://gitlab.com/gitlab-org/gitlab/-/issues/442219) provides greater configurability and visibility to identify whether an API Security test was successful or not.
- [Migrate API Checks to YAML](https://gitlab.com/groups/gitlab-org/-/epics/13133) will enable our Vulnerability Research team to regularly contribute to our API Security Testing checks so our detections are updated more frequently. This will also give us [Custom API Security Checks](https://gitlab.com/gitlab-org/gitlab/-/issues/434265) for free, which allows customers to write their own security checks in YAML format. Once available, we would like to create a way for customers to share suggested custom checks with one another--essentially open sourcing potential detections.
- [Update API Security Checks](https://gitlab.com/groups/gitlab-org/-/epics/12905) to ensure our detections cover not only the OWASP Top 10:2021 list, but also the newer OWASP Top 10 API:2023 list. In collaboration with VR, we recently outlined a number of additional checks that should be added to help protect our customers from a broader set of risks.

With the remainder of the year, our focus is on ensuring customers have full visibility into the APIs in their projects and are able to easily onboard API Security Testing for all supported APIs (REST, GraphQL, SOAP). To accomplish that, we are focused on:

- [API Discovery](https://gitlab.com/groups/gitlab-org/-/epics/7539) will leverage Static Analysis techniques to help identify all APIs (REST, GraphQL, SOAP) in a project and automatically generate an accurate OpenAPI spec, which can then be ingested by API Security Testing.
- [API Inventory](https://gitlab.com/gitlab-org/gitlab/-/issues/442827) will provide a new page so customers can view all of their APIs within the GitLab UI. This page will be similar to the dependency list in intent. It will list all API endpoints, indicate when the endpoint was last tested, and include any relevant security findings. This page will provide greater detail for APIs than the Vulnerability Report does today, and eventually additional features (Risk score, API Analysis, etc.) will generate other data that is populated on this page.

### 3 year plan

Looking forward, we will continue to focus on features that enable customers to efficiently reduce risk. We want to ensure API security risks are easy to prioritize and remediate, and easy to address earlier in the API management lifecycle. Future capabilities focus on helping teams design and build secure APIs, and perform security testing that is as close to real-world API requests as possible.

1. [API Risk Score](https://gitlab.com/gitlab-org/gitlab/-/issues/442808) will enable customers to better prioritize API Security findings based on the risk associated with each API endpoint. Risk scores will be affected by whether an API transmits sensitive data and by what kind of security testing has been performed. Customers will also be able to influence the score by marking APIs as business critical.
1. [API Analysis](https://gitlab.com/groups/gitlab-org/-/epics/10504) expands the depth of our API Security Testing by correctly determining how a sequence of API calls should be tested together. Rather than assessing the security results of one API call via one check, this enables testing to more accurately emmulate the API calls real-world users might make, and the responses they would get.
1. [ABAC API Service Mesh](https://gitlab.com/gitlab-org/gitlab/-/issues/455929) would enable customers to configure and maintain a YAML-based service mesh from within GitLab's UI. This would help shift security left by centralizing API authorization policies early in the development lifecycle. This would help reduce customer risk for 3 out of the top 10 OWASP API Top 10 risks (authorization risks).
1. [OpenAPI Spec Audit](https://gitlab.com/gitlab-org/gitlab/-/issues/442776) is related to API Discovery, but approaches the problem from a different angle. API Discovery assumes an OpenAPI spec has not yet been generated for an API, whereas OpenAPI Spec Audit applies whenever a spec already exists. This feature is most relevant for large enterprises that have API management teams. The audit score analyses an OpenAPI spec and identifies security gaps, validation gaps, and the level of data validation that's defined, so that customers can remediate issues with their OpenAPI specs and ensure that API Security Testing provides as much coverage as possible.
1. [gRPC support](https://gitlab.com/gitlab-org/gitlab/-/issues/442507) will ensure all API formats can be analyzed by API Security Testing so customers have full coverage for identifying security issues in their APIs.

### Best in Class Landscape
<!-- Blanket description consistent across all pages that clarifies what GitLab means when we say "best in class" -->

BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

#### Key Capabilities

For this product area, these are the capabilities a best-in-class solution should provide:

1. The ability to accurately and comprehensively detect security weaknesses outlined in the OWASP Top 10:2021.
1. The ability to accurately and comprehensively detect security weaknesses outlined in the OWASP Top 10:2024.
1. The ability to accurately and comprehensively detect security weaknesses outlined in the OWASP API Top 10:2023.
1. Support for detecting weaknesses across REST, GraphQL, SOAP, and gRPC APIs.
1. Support for detecting API business logic flaws.
1. The ability to automatically generate OpenAPI specifications for APIs that are not documented and to automatically enable security testing on those specs.
1. The ability to analyze pre-existing OpenAPI specifications for security flaws and to provide remediation recommendations.
1. The ability to accurately and comprehensively provide an inventory of APIs.
1. Support for shifting security results left into the IDE.
1. Extensive analysis of other risk factors (business logic, sensitive data, PII, etc.).
1. The ability to enforce policies preventing API security flaws from being merged into the default branch.
1. Reporting and filtering to allow users to easily see the security posture of their APIs.
1. The ability to provide mature security analysis of multiple API calls to replicate real-world attacks.
1. The ability to enforce ABAC policies to reduce the liklihood of API authorization security flaws.

## Competitive Landscape

- [Noname Security](https://nonamesecurity.com/)
- [Salt Security](https://salt.security/)
- [TraceableAI](https://www.traceable.ai/)
- [Cequence Security](https://www.cequence.ai/)
- [42Crunch](https://42crunch.com/)
- [APIsec](https://www.apisec.ai/)
- [Akto](https://www.akto.io/)
- [Firetail](https://www.firetail.io/)
- [Wallarm](https://www.wallarm.com/)
- [Synopsys](https://www.synopsys.com/software-integrity/security-testing/api-security-testing.html)
- [Netsparker](https://www.netsparker.com/)
- [StackHawk](https://www.stackhawk.com/)

We have an advantage of being able to provide testing results before the app is deployed into the production environment, by using Review Apps. This means that we can provide API security scan results for every single commit. The easy integration of API security scanning early in the software development life cycle is a unique position that GitLab has in the API Security market. We also have the advantage of being able to provide secure design and build guardrails within our platform as developers and security teams are outlining requirements and developing APIs. Integrating other tools at this stage of the SDLC is typically difficult, at best.

## Pricing and Packaging

The GitLab API Security features are all packaged as part of the [GitLab Ultimate tier](https://about.gitlab.com/pricing/ultimate/). This aligns with our [pricing strategy](https://handbook.gitlab.com/handbook/company/pricing/#pricing-strategy) as these features are relevant for executives who are concerned about keeping their organization secured from security weaknesses (CWEs).

## Analyst Landscape

API Security is not a standalone market evaluated by analysts, but is included in the analysis of DevSecOps, Application Security, and API Management markets.

* [Gartner Application Security Testing Reviews](https://www.gartner.com/reviews/market/application-security-testing)
