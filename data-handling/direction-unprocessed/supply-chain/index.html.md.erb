---
layout: markdown_page
title: "Software Supply Chain Security Direction"
description: "Software needs to be developed in a way that properly protects it from supply chain attacks. This page highlights GitLab's direction."
canonical_path: "/direction/supply-chain/"
---

- TOC
{:toc}

The [Sec Section](https://about.gitlab.com/direction/security/) coordinates GitLab's overall direction for [Software Supply Chain Security (SSCS)](/solutions/supply-chain/).
Many groups are involved in delivering a comprehensive, quality secure supply chain experience at GitLab.

Our goal is to deliver capabilities in the GitLab platform that gives users confidence in the integrity and security of their software supply chain.
This direction page is intended to facilitate collaboration and describe the product capabilities that would contribute to this vision.

## Background

In today's software-driven world, your applications aren't just what you code - they're built from hundreds of components from across the global software supply chain. While this accelerates innovation, it also introduces new risks. GitLab gives you visibility into these risks and provides ways to remediate them.

Software Supply Chain Security (SSCS) seeks to manage the full spectrum of security risks that may be introduced by people, processes, or technology throughout planning, building, deploying, and operating an application, from concept to sunset. Recent high-profile attacks like SolarWinds have shown that compromised dependencies can have devastating consequences. Meanwhile, new regulations like the [US Executive Order on Cybersecurity](https://www.cisa.gov/topics/cybersecurity-best-practices/executive-order-improving-nations-cybersecurity) and [EU Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) are making supply chain security a compliance requirement.

Shared understanding of SSCS's scope has evolved significantly over the past few years. What was once rooted rather narrowly in managing third-party dependency risk has evolved into a robust set of standards and approaches that address practices across the full spectrum of software development activities. A central concern of SSCS and its primary "output" is a software artifact's[^1] chain of custody. This chain of custody materializes in a variety of ways:

* A software bill of materials (SBoM) specifies what comprises a software artifact, including any third-party code, along with other facts about where it's coming from and how it was produced—analogous to an "ingredient label" for the product.
* [Supply-chain Levels for Software Artifacts](https://slsa.dev/spec/v1.0/levels) (SLSA) specifies guidelines and appropriate types of evidence about other parts of the software production process. Continuing the SBOM-as-ingredient-list analogy, SLSA [is described](https://slsa.dev/spec/v1.0/about#slsa-in-laypersons-terms) as "the food safety handling guidelines that make an ingredient list credible". SLSA is not a single standard, so organizations and products satisfy different tracks and levels of its guidelines.
* NIST's [Secure Software Development Framework](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf) (SSDF) and accompanying practical guides from the Enduring Security Framework partnership ([example](https://www.cisa.gov/sites/default/files/publications/ESF_SECURING_THE_SOFTWARE_SUPPLY_CHAIN_DEVELOPERS.PDF)) outline a core set of high-level secure software development practices that can be integrated into any SDLC implementation. They categorize these practices into four groups: prepare the organization, protect the software, produce well-secured software, and respond to vulnerabilities.

Together, these concepts, documents, and standards are increasingly being embedded in industry requirements and regulations. Although the supply chain security space is still rapidly evolving, the U.S. Government has already begun implementing requirements for federal vendors. We expect that supply chain requirements will continue to evolve for the foreseeable future as part of federal regulations, regulated-industry standards, and individual organizational requirements.

[^1]:  A "software artifact" is a generic term that may refer to software binaries, container images, packages, or other ways of distributing software.

As a single application for the DevSecOps lifecycle, GitLab is uniquely positioned to meet all of the requirements.

## How SSCS applies to GitLab

SSCS applies to GitLab in more than one way:

1. As a company building a product:
   1. We produce software artifacts for customers, and these customers require us to make assertions about the quality and provenance of the artifacts we provide.
   2. We consume software artifacts from other sources, including open-source software that we redistribute to our customers as part of our product.
2. As a product enabling customers to build their own products:
   1. We enable customers to securely produce and consume software.
   2. We host software projects, and build and distribute software artifacts, making us a key part of the supply chain.

This direction focuses on the capabilities we provide to customers, so they can securely produce and consume software.

## Current Position and Vision

We believe that there are five main aspects to consider when providing for a secure end-to-end software supply chain.
1. **Source** - includes the controls needed to be confident that both internal and external source code is safe from vulnerabilities and has not been compromised in any way.
1. **Build** - includes rigorous requirements for the security and isolation of build environments as well as the automatic generation of provenance.
1. **Consumption** - includes the ability to validate authenticity and source of any executed binaries. Supports requirements for securing the underlying host infrastructure itself.
1. **Management Process** - this component spans across all other aspects of SSCS and includes both the tools and processes necessary to provide for ongoing visibility into compliance SSCS requirements.
1. **Tool Security** - this component spans across all other aspects of SSCS and includes the adoption of best practices for managing the security of the underlying tools themselves.

The state of GitLab product capabilities required to address each of the five aspects of SSCS currently spans the spectrum from vision items to complete features:

### Source

The approach for protecting code sources can be subdivided by thinking about protection for Internal Sources separately from protection for External Sources.

**Status Legend / Key**

| Icon | Meaning |
| ------ | ------ |
| ✅ | Feature is considered complete |
| 🔨 | Feature exists and still has areas for improvement |
| ⌛ | Feature is part of the vision and has not yet been built inside GitLab |

#### Internal Sources

| Key Requirements | Status | GitLab Group | Current Capabilities | Future Vision                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------ | ------ | ------ | ------ |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version control and code history | ✅ | `Create:Source Code` | [Version control](https://about.gitlab.com/topics/version-control/how-implement-version-control/) and code history retention is fully supported in GitLab as part of Git. |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Developer identity verification | ✅ | `Create:Source Code` | [GPG key signing](https://docs.gitlab.com/ee/user/project/repository/signed_commits/gpg.html) is and [SSH key signing](https://docs.gitlab.com/ee/user/project/repository/signed_commits/ssh.html) are both fully supported by GitLab. Additionally, [push rules](https://docs.gitlab.com/ee/push_rules/push_rules.html) can be configured to reject commits that are not GPG key signed. On GitLab.com, commits made through the webUI are signed by default using an SSH key. Self managed instance administrators can configure default signing through the webUI to happen through either SSH or openPGP. | To further mature in this area, we are [considering also adding support for GitSign](https://gitlab.com/gitlab-org/gitlab/-/issues/364428) to sign all commits that are made in the GitLab UI by using the user&apos;s GitLab OIDC identity. This work is blocked due to the lack of a Ruby Sigstore library. |
| Enforced two-person code review and security review for vulnerabilities | ✅ | `Create:Code Review` | GitLab has a [robust approval system](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/) capable of requiring two-person review, including from an approver who is also not the code owner. | Although this feature is generally considered to be complete, improvements are ongoing. |
| Branch protection rules and vulnerability approval rules | ✅ | `Create:Source Code` and `SRM:Security Policies` | GitLab fully supports the ability to create [branch protection rules](https://docs.gitlab.com/ee/push_rules/push_rules.html#enabling-push-rules) and [approval rules](https://docs.gitlab.com/ee/user/application_security/#security-approvals-in-merge-requests) |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Dependency protection rules | ⌛  | `Package:Package` |  | The vision is to empower users to create [container image](https://gitlab.com/groups/gitlab-org/-/epics/9825) and [package](https://gitlab.com/groups/gitlab-org/-/epics/5574) protection rules to further restrict who can update your critical dependencies. |
| Ability to restrict merge access by defining project maintainers | ✅ | `SSCS:Authorization` | GitLab fully [supports this requirement](https://docs.gitlab.com/ee/user/project/members/). |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Multiple types of code scanning: Secret Detection, SAST, DAST, API Fuzzing, Coverage Guided Fuzzing | ✅ | `AST` | Users can run a wide variety of scanners natively through GitLab. They can manage the results and require approval for merge requests where new vulnerabilities are identified. | Although this feature is generally considered to be complete for the purposes of SSCS, improvements are ongoing. Among other things, GitLab strives to continually expand the coverage, accuracy, and language support of our scanners.                                                                                                                                                                                        |
| Controlled development environments | ⌛ | `Create:Remote Development` | Currently GitLab has integrations with tools such as [GitPod](https://docs.gitlab.com/ee/integration/gitpod.html) that allow software engineers to do their development in a remote environment. | The [future vision](https://about.gitlab.com/direction/create/remote_development/workspaces) is for GitLab to host a remote environment that is tightly integrated with GitLab and that can be managed and updated centrally. Centrally managing this environment reduces the number of tools that need to be installed on individual development environments and can help to protect against malware and code tampering. |

#### External Sources

| Key Requirements | Status | GitLab Group | Current Capabilities | Future Vision |
| ------ | ------ | ------ | ------ | ------ |
| SCA scanning | ✅ | `AST:Composition Analysis` | Users can continuously scan both their application dependencies and their system dependencies for vulnerabilities. They can manage the results of these scans within GitLab and can require approval for merge requests where new vulnerabilities are identified. | Although this feature is generally considered to be complete for the purposes of SSCS, improvements are ongoing. Among other things, GitLab strives to continually expand the coverage, accuracy, and language support of our scanners. |
| Dependency risk analysis | ⌛ | `AST:Composition Analysis` | | This includes the ability to analyze metadata available for a dependency, as well as analyzing the source code itself to generate an overarching risk score for the dependency. Among other things, some of this data might include whether or not the dependency is well maintained, whether it has supply chain security protections in place, whether not not it contains known malicious code or obfuscated code.  |
| Automated dependency updates | ⌛ | `AST:Composition Analysis` | GitLab has the ability to [generate merge requests](https://docs.gitlab.com/ee/user/application_security/vulnerabilities/index.html#resolve-a-vulnerability) that can attempt to fix container scanning and some dependency scanning vulnerabilities. | The vision is to automatically generate merge requests to keep dependencies up-to-date with the latest versions. |
| Dependency graph | ⌛ | `AST:Composition Analysis` | | GitLab has plans to add a [dependency tree visualization](https://gitlab.com/gitlab-org/gitlab/-/issues/366168) feature into GitLab for easier visualization of the dependencies that exist between external sources. |
| Binary scanning of dependencies | ⌛ | `AST:Composition Analysis` | | Basic SCA scanning compares installed package names and versions to a database of known vulnerabilities. Binary scanning takes this one step further by inspecting the contents of the binary itself using static analysis tools to detect potential vulnerabilities. |
| Behavioral analysis of dependencies | ⌛ | `AST:Composition Analysis` | | The vision is for users to be able to analyze the behavior of their dependencies using GitLab. Observing key events such as system calls, network connectivity, and file reads during the test stage of the CI pipeline can provide insights into whether or not an upstream dependency has potentially become compromised in some way. |
| Verification of provenance | ⌛ | `AST:Composition Analysis` | | The vision is to allow users to verify and validate published attestation or provenance for upstream dependencies (if it exists) as part of the CI pipeline and alert on any dependencies that do not meet established criteria. |
| Dependency firewall | ⌛ | `Package:Package` | | The vision is to [build a dependency firewall into GitLab](https://gitlab.com/groups/gitlab-org/-/epics/5133). This would allow users to configure rules to prevent use of dependencies that do not match established rules. This can help protect against typosquatting attacks and can block packages that have concerning characteristics. |

### Build

#### Build Execution

| Key Requirements | Status | GitLab Group | Current Capabilities | Future Vision |
| ------ | ------ | ------ | ------ | ------ |
| Support for scripted builds from code | ✅ | `Verify` | GitLab supports the ability to run [CI/CD pipelines](https://docs.gitlab.com/ee/ci/) and both execute and deploy scripted builds from code. | |
| Secure, ephemeral, and isolated build environment | ✅ | `Verify:Runner` | This is supported as long as the runners are [properly secured](https://docs.gitlab.com/runner/security/). Use of non-privileged Docker executors is recommended. | |
| Support for hermetic builds | ✅ | `Verify:Runner` | GitLab supports the ability to [limit network access to runners](https://docs.gitlab.com/runner/security/#network-segmentation). Runners do require connectivity to the GitLab server. | |
| Machine identity verification for all sources | ⌛ | `Verify` | Users who desire this feature would currently need to build/script this verification themselves. | The vision for this is to include some additional verification checks to be confident that all sources are coming from trusted, verified locations. |

#### Provenance and Signing

| Key Requirements | Status | GitLab Group | Current Capabilities | Future Vision |
| ------ | ------ | ------ | ------ | ------ |
| Build output signing | ⌛ | `Verify:Runner` | GitLab currently supports a [native integration with Sigstore](https://docs.gitlab.com/ee/ci/yaml/signing_examples.html) which allows users to easily sign their builds through Cosign. | Future work is planned to allow the GitLab Runner to [sign build outputs automatically](https://gitlab.com/groups/gitlab-org/-/epics/9212) without requiring manual configuration on the part of users. |
| Provenance/Attestation generation for build outputs | 🔨 | `Verify:Runner` | Currently GitLab can be used to [generate a provenance metadata document](https://docs.gitlab.com/ee/ci/runners/configure_runners.html#artifact-provenance-metadata) for all build artifacts.  Users who wish to have this document signed can do so through our [integration with Sigstore](https://gitlab.com/groups/gitlab-org/-/epics/9212). | Future work is planned to allow the GitLab Runner to [sign attestation files automatically](https://gitlab.com/groups/gitlab-org/-/epics/9212) without requiring manual configuration on the part of users. |
| Release evidence generation | 🔨 | `Release:Release` | Generation and publication of [release evidence](https://docs.gitlab.com/ee/user/project/releases/#release-evidence) is currently supported. | Release evidence will ideally be expanded to include an SBOM of all dependencies as well as the provenance/attestation that was generated at the time the build was created. |
| SBOM generation and management | 🔨 | `AST:Composition Analysis` | GitLab is currently able to generate a SBOM of application and system dependencies. This is displayed on the Dependency List page where users can easily view all the included packages along with their version and any vulnerabilities that have been detected. Additionally, a JSON CycloneDX formatted artifact can be produced in the CI pipeline. | In the future, GitLab plans to add support for [exporting the dependency list](https://gitlab.com/gitlab-org/gitlab/-/issues/407453) in SPDX and CycloneDX formats. Eventually this SBOM is envisioned to be signed and included in any generated provenance/attestation documents that are produced. |

### Consumption

#### Binary Acceptance

| Key Requirements | Status | GitLab Group | Current Capabilities | Future Vision |
| ------ | ------ | ------ | ------ | ------ |
| Binary authorization enforcement to validate and verify provenance | ⌛ | `Configure:Configure` | | GitLab already supports continuous deployment through the GitLab Kubernetes Agent. Ideally this will be extended to validate and verify the provenance/attestation for container images prior to deploying them in production. In addition, regular scans might be done to verify on an ongoing basis that Binary Authorization has been set up within the production environment and to further validate and confirm that all running deployments meet established policies. One tool that might be used for this in the future is [Kritis](https://github.com/grafeas/kritis) |
| Validation and verification of source machine identities | ✅ | `Configure:Configure` | This requirement is met by default for users who deploy to production using GitLab for continuous deployment. The [GitLab Kubernetes Agent](https://docs.gitlab.com/ee/user/clusters/agent/) automatically verifies and validates the authenticity of the GitLab server certificate that it connects to. | |

### Management Process

| Key Requirements | Status | GitLab Group | Current Capabilities | Future Vision |
| ------ | ------ | ------ | ------ | ------ |
| Reporting on adherence to compliance standards | 🔨 | `SSCS:Compliance` | GitLab support several [compliance reports](https://docs.gitlab.com/ee/user/compliance/compliance_report) natively in GitLab.  Additional data can also be collected through the API or monitored through GitLab Audit Events. | Work on a centralized dashboard showing compliance with [SLSA](https://slsa.dev/) and other similar standards is part of GitLab&apos;s vision. |
| Enforcement of secure settings | 🔨 | `SRM:Security Policies` | Security and compliance teams can currently enforce a wide variety of controls, including requiring scans to be run, enforcing security-related configuration settings, and maintaining requirements related to merge request approvals. | The vision is for Security and Compliance teams to be able to enforce **all** aspects of SSCS in a way that other users are unable to disable or change those settings. |
| Credential management | 🔨 | `SSCS:Authentication` | Self managed users are currently able to enforce requirements related to [SSH keys](https://docs.gitlab.com/ee/security/ssh_keys_restrictions.html), [SSH access](https://docs.gitlab.com/ee/administration/settings/account_and_limit_settings.html#limit-the-lifetime-of-ssh-keys), and [Personal Access Tokens (PAT)](https://docs.gitlab.com/ee/administration/settings/account_and_limit_settings.html#limit-the-lifetime-of-personal-access-tokens). | The vision is to [provide SaaS users with feature parity](https://gitlab.com/groups/gitlab-org/-/epics/5188) for managing SSH keys, SSH access, and PAT access policies. |

### Tool Security

| Key Requirements | Status | GitLab Group | Current Capabilities | Future Vision |
| ------ | ------ | ------ | ------ | ------ |
| Audit logs | 🔨 | `SSCS:Compliance` | GitLab has a robust [audit logging system](https://docs.gitlab.com/ee/administration/audit_events.html) in place today. | Additional audit events are regularly being added into GitLab. |
| Access controls | 🔨 | `SSCS:Authorization` | GitLab supports multiple [authentication and authorization](https://docs.gitlab.com/ee/administration/auth/) options today, including [support for custom roles](https://docs.gitlab.com/ee/user/custom_roles.html). | GitLab is planning to add support for [additional custom permissions](https://gitlab.com/groups/gitlab-org/-/epics/12264) so that users can be configured with the least privileges required to do their job. |
| Threat detection | ⌛ | `SSCS:Authentication` and `SSCS:Compliance` | Users can integrate external systems with GitLab to analyze suspicious behavior. | GitLab has an opportunity to leverage anomaly detection and machine learning to detect and stop threats. This can be used to analyze user behavior as well as activity on the GitLab server itself. |

## Strategy

In the long-term, our strategy is to become a complete provider for all aspects of software supply chain security. Providing all of these aspects within a single application not only supports GitLab&apos;s broader [Single Application Strategy](https://handbook.gitlab.com/handbook/source/handbook/product/single-application) but also provides numerous tangible benefits for users.

Among other things, using a single application:
* minimizes the number of different tools that need to be hardened and monitored.
* reduces the number of potential points of security failure as data is transferred between various tools.
* enables seamless interoperability.
* simplifies visibility and traceability for audits.

## Highlighted epics and issues

There are a few epics and important issues you can check out to see where we&apos;re headed. More will be added here as we develop this vision further.

- [Dependency Management Vision](https://gitlab.com/groups/gitlab-org/-/epics/8226)
- [Artifact Data Store](https://gitlab.com/groups/gitlab-org/-/epics/6207)
- [Release Evidence Viability](https://gitlab.com/groups/gitlab-org/-/epics/5135)

## What&apos;s next & why

Although we support [signing of build artifacts through Sigstore](https://docs.gitlab.com/ee/ci/yaml/signing_examples.html), the user experience for signed container images in GitLab is not ideal as signatures show up on a separate line item from the container image that they have signed.  In 16.11 we plan to address this by associating container images with their signatures in the UI to make it easier to see which images are signed and to more easily validate those signatures.

Additionally, we are continuing ongoing work to explore whether we can automatically sign build artifacts natively in the GitLab Runner.  Automatic signing is believed to be the best way to get widespread adoption of signing.

A full list of the SSCS working group&apos;s current priorities can be viewed [on this working group page](https://handbook.gitlab.com/handbook/company/working-groups/software-supply-chain-security/#priorities-and-progress).

## What are we not doing

Sigstore currently has two key limitations that impact GitLab:
1. Sigstore does not have a Ruby library
1. Sigstore does not have good support for deploying and running a self managed Sigstore instance

We do not currently plan to address either of these limitations directly and instead are hoping to work with the wider community to find alternate solutions.  Because of these feature gaps, we do not plan on adding support for our Sigstore integration for self managed instances.  We also are limited in our ability to natively validate Sigstore signatures within GitLab due to the lack of Ruby support.

## Competitive landscape

There have been indications that Tekton and Sigstore are tools representing a leader in software supply chain security. One example of how this has been used in practice can be found in this [blog](https://dlorenc.medium.com/zero-trust-supply-chain-security-e3fb8b6973b8).

[CoSign](https://github.com/sigstore/cosign#registry-support) is an open source tool that can be used for container signing.

[Grafeas](https://grafeas.io/) is an open-source artifact metadata datastore tool which offers flexible, universal artifact metadata storage - a key foundation for software supply chain security.

## Frameworks

**Supply chain Levels for Software Artifacts (SLSA)**

The [SLSA framework](https://slsa.dev/) is an open source specification that is primarily focused on preventing artifacts from being tampered with as they are coded, developed, and published.  Our vision for SSCS includes adding native support for SLSA with the objective of eventually fully supporting all the way up to SLSA level 3.  GitLab already supports users who want to attain SLSA L1.  GitLab is currently exploring ways to natively generate the required provenance data for SLSA as part of its Runner that does the build.  For more details on SLSA, view the [SLSA requirements](https://slsa.dev/spec/v1.0/requirements).

**The Update Framework (TUF)**

[The Update Framework (TUF)](https://github.com/theupdateframework/specification/blob/master/tuf-spec.md#the-update-framework-specification) is an open source specification for that provides instructions on how to organize, sign, and interact with metadata to secure package managers. Our vision for SSCS includes adding native support for TUF in the future by including the required metadata in the software provenance that we plan to generate and by validating signatures at each step of the software lifecycle. TUF leverages a Kritis store to manage metadata from in-toto. TUF recommends the use of an OCI image-spec container registry, aligned with our Container Registry's [documentation](https://docs.gitlab.com/ee/architecture/blueprints/container_registry_metadata_database/#new-features-and-breaking-changes). Some gaps to consider for GitLab are the rotation of secrets and key management, which is a part of [Secrets Management direction](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/secrets_management/).
TUF also recommends the [verification of deployments](/direction/delivery/deployment_management/).
For more details on TUF, view the [CNCF TUF specifications](https://project.linuxfoundation.org/hubfs/CNCF_SSCP_v1.pdf).

## North Stars

A FY23 theme for the [Verify Stage](/direction/verify/verify) is to support pipeline safety throughout the software development lifecycle to automatically ensure compliance and security. This is complimented by Software Composition Analysis Group&apos;s [Dependency Scanning direction](https://about.gitlab.com/direction/application_security_testing/composition-analysis/dependency-scanning/) on SBOM.

We aim to make a seamless experience for verifying trust at every step in the software chain.

## Analyst Landscape

Gartner has published some information on this topic in a paper titled [How Software Engineering Leaders Can Mitigate Software Supply Chain Security Risks](https://www.gartner.com/en/documents/4003625-how-software-engineering-leaders-can-mitigate-software-supply-chain-security-risks). Gartner has also published a market guide for [Compliance Automation Tools in DevOps](https://www.gartner.com/en/documents/3986057/market-guide-for-compliance-automation-tools-in-devops).

Last Reviewed: 2025-02-10

Last Updated: 2025-02-10
