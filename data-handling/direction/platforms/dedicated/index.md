---
layout: markdown_page
title: "Category Direction - GitLab Dedicated"
description: "GitLab Dedicated is GitLab's single-tenant, Software as a Service (SaaS) offering"
canonical_path: "/direction/saas-platforms/dedicated/"
---

- TOC
{:toc}

{::options parse_block_html="true" /}

This page outlines the Direction for the GitLab Dedicated category and belongs to the [GitLab Dedicated](https://handbook.gitlab.com/handbook/product/categories/#gitlab-dedicated-group) group. To provide feedback or ask questions about this product category, reach out to the [Product Manager](mailto:cbalane@gitlab.com).

This document and linked pages contain information related to upcoming products, features, and functionality. It is important to note that the information presented is for informational purposes only. Please do not rely on this information for purchasing or planning purposes. As with all projects, the items mentioned in this document and linked pages are subject to change or delay. The development, release, and timing of any products, features, or functionality remain at the sole discretion of GitLab Inc.

You can contribute to this category by:
- Commenting on a relevant epic or issue in [our project](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team)(GitLab internal), or opening a new issue in the [GitLab Dedicated issue tracker](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues/new?issue%5Bmilestone\_id%5D=).
- Joining the discussion in the [#f\_gitlab\_dedicated](https://gitlab.slack.com/archives/C01S0QNSYJ2) Slack channel
## Overview
### Solution
GitLab Dedicated combines the low overhead and efficiency of a SaaS platform with the flexibility and privacy benefits of self hosting. A single-tenant SaaS instance, fully managed and hosted by GitLab in any cloud region, is updated regularly to give you access to our latest product improvements — without the need to manage security, scalability, availability, and performance on your own. It's the offering of choice for enterprises and organizations in highly regulated industries that have complex regulatory, compliance, and data residency requirements. If you're a customer that's interested in Dedicated, make sure to also check-out [the website for Dedicated](/single-tenant-saas/).
### Background
GitLab Dedicated's objective is to provide a GitLab SaaS offering to large enterprises and customers in industries with strict security and compliance requirements. When adopting DevOps tools, customers [increasingly prefer SaaS](https://about.gitlab.com/direction/enablement/dotcom/#market-opportunity) to reduce operational cost, but customers in highly-regulated industries (e.g. Healthcare, Finance, and Public sectors) can't compromise on their security and compliance requirements when moving to SaaS. These requirements (e.g. isolated storage of source code IP) often dictate the need to be on separate Cloud Infrastructure from other tenants. This makes it challenging for these customers to adopt a shared-tenancy SaaS solution like GitLab.com.
Additionally, customers in regulated industries often require the ability to connect users or services running in their corporate network to their source code repositories running in the cloud via a private network connection. As a public-facing SaaS service, GitLab.com can't support this type of private connectivity easily by default. Finally, large, globally-distributed enterprises need the ability to control the location and number of Geo Replica sites to reduce latency for their workforce around the world. Some of our Self-Managed customers have 5+ Geo sites, and for them to consume SaaS they may need more global coverage than [what we offer on GitLab.com today](https://about.gitlab.com/direction/enablement/dotcom/#overview).
For these customers, a higher level of tenant isolation and deployment customization is required. While some customers may be satisfied leveraging a [partner MSP](#channel-partner-role-in-gitlab-dedicated), customers may prefer to consume the service directly from GitLab so that they have a single-point of contact for operational accountability.
GitLab Dedicated will solve these needs by offering a fully isolated, private GitLab instance, deployed in the customer's cloud regions of choice. The instance is fully hosted and managed by GitLab Inc., enabling customers to offload operational overhead and focus on more business-critical tasks. GitLab Dedicated tenant operators (e.g. a system administrator) will retain the ability to quickly make changes to their Dedicated tenant's configurations in the course of their daily work using the [Switchboard](https://about.gitlab.com/direction/saas-platforms/switchboard/) portal.
In addition to delivering customer value, GitLab Dedicated will also benefit internal GitLab teams. We envision the tooling we build for Dedicated being used as the single method going forward for running all of GitLab Inc.'s SaaS services. This will allow us to achieve even greater returns on our initial investment by enabling any future SaaS services to quickly get started with a robust and standardized foundation.
## Why is this important?
There are two major trends emerging when it comes to the delivery of Cloud based solutions:
- Move to SaaS [as detailed in the .com strategy](https://about.gitlab.com/direction/enablement/dotcom/#market-opportunity) (IDC predicts that the market for SaaS-based DevOps tools (52% of the market in 2021) will continue to accelerate and account for \*\*$20.0B in revenue\*\* (or 61% of DevOps software tools market) by 2026).[1](#footnotes)
- Adoption of Private Cloud, which makes it easier for enterprises to meet their security and compliance needs. Increasing fragmentation of global policy [regarding data protection](https://insights.comforte.com/13-countries-with-gdpr-like-data-privacy-laws) drives new compliance requirements, which can be better met with Private Cloud deployments. 16% of cloud services are expected to be delivered as a hosted private cloud offering [by 2025](https://www.reportlinker.com/p05826094/Global-Private-Cloud-Server-Market.html?utm_source=PRN).

GitLab Dedicated is for organizations that want to benefit from both SaaS and Private Cloud. By delivering this offering we will set ourselves up to achieve customer success as these two trends further accelerate in 2025.

### Challenges to address
Overall, the main challenge our target customer has is maintaining an up-to-date GitLab instance that fulfills their security and compliance requirements. More granular customer needs are documented in the sections below.
Note, this section does not reflect the list of currently available features within the GitLab Dedicated offering; rather, it contains the needs we're hearing from our customer base. The list of currently supported features in GitLab Dedicated is documented here: [https://docs.gitlab.com/ee/subscriptions/gitlab\_dedicated/#available-features](https://docs.gitlab.com/ee/subscriptions/gitlab\_dedicated/#available-features).
#### Migration
- Users want to seamlessly migrate their data, which can exceed many TBs in size, to GitLab Dedicated in a timely and reliable fashion from their existing DevOps solution, whether it's a third-party offering like BitBucket, a self-managed GitLab instance, or GitLab.com.
#### Security and Compliance
- Our [target customer base](#target-customer), large enterprises and customers in highly-regulated industries, expect the offering to implement security best practices including encryption of data at rest and in transit, periodic encryption key rotation, ability to specify their own encryption key, integration with their own identity management systems, protection against DDoS attacks, intrusion detection, role-based access control for operators, segregation of duties with least privilege access configured among operator accounts, and approved escalation in order to access customer environments during break-glass scenarios.
- Upgrades: Customers want regular, zero-downtime upgrades to their instance along with timely security patches for high-sev issues when necessary.
- Data residency/data sovereignty: Customers want their Dedicated instance and data (including logs and backups) to be hosted in their cloud region of choice to help meet their security and compliance requirements.
- Private Networking: Customers want to be able to securely connect applications running in their VPC including their Runner pool to GitLab Dedicated via a private connection without the traffic leaving the Cloud Provider backbone.
- Public Networking: Some customers work with third-parties (e.g. contractors), who do not authenticate through their main network and thus need to access the GitLab Dedicated instance over the public internet. In this scenario, customers need the ability to restrict access to their instance based on an allowlist of trusted IP ranges.
#### Observability
- Customer admins want to access telemetry data including health metrics and application/system logs so that they can monitor their instance and keep their internal teams informed regarding an outage or performance degradations with their DevOps environment. Users also want access to audit logs to achieve compliance requirements and the ability to monitor network flow (e.g. VPC flow logs) to ensure outbound connections are made to only known/trusted hosts.
#### Scalability
- Large enterprises want their chosen DevOps solution to automatically scale based on their number of users and usage patterns.
#### Availability
Large enterprises demand strict uptime SLAs (at least 'three-nines') and expect the following capabilities related to system availability:
- High Availability Deployment (especially their code repositories) including leveraging multiple availability zones within a region to mitigate against an AZ outage.
- Disaster Recovery: Failovers to the included secondary site in case the primary instance experiences an unrecoverable outage and guaranteed recovery times.
- Backups: customers expect their data to be backed up on a regular basis in case of a data loss event and to meet committed recovery point and time objectives during restoration.
#### Performance
- Customers want replicas of their instance to be deployed in multiple regions around the globe to reduce latency for their global user base.
## Positioning
### Target Customer
Customer Requirements

To be a good fit for Dedicated a customer **must** have the characteristics below:
1. Require at least 1000 seats. Note: 500 seat opportunities will be considered on a case-by-case basis.
2. Require the security and compliance features offered in the Ultimate tier.
3. Require a single-tenant solution or has compliance requirements around data residency.

In addition to customers looking to solve the above [challenges](#challenges-to-address), below are some additional characteristics of customers we are targeting with this offering:

\*\*Target Customer Characteristics\*\*
{: .panel-heading}

1. \*\*Industries\*\* - Regulated industries with complex security and compliance requirements like:
1. Healthcare
2. Finance (Banking and Insurance)
3. Public sectors
4. Public Utility
5. Transportation
6. Manufacturing
2. \*\*Good fit characteristics\*\*
1. Looking for Ultimate tier features and is comfortable with 500 Ultimate seat minimum order — plus an [additional fee](#pricing) - otherwise GitLab Dedicated is cost prohibitive.
2. Highly value a secure SCM foundation; have concerns around leaks and the inability to isolate repositories within the enterprise.
3. Aim to improve developer productivity and user experience translating to unparalleled collaboration with observability.
4. Want SaaS but object to GitLab.com. The customer would prefer single-tenant SaaS due to strict security and compliance requirements
5. Have data residency compliance requirements where instance and data (including logs and backups) need to be hosted in customer's cloud region of choice.
6. Is looking for all the benefits of SaaS with the security/compliance rigor of self-managed.
7. Looking for savings on costs and operational efficiencies; do not want to manage the DevSecOps platform. The customer sees the benefit of regular updates and infrastructure maintenance are managed by GitLab.
8.Looking for an isolated, single tenant deployment
9. Looking for a proven product with [high availability](https://handbook.gitlab.com/handbook/engineering/infrastructure/team/gitlab-dedicated/slas/) - GitLab has multiple large customers that have been using Dedicated for over a year (ie: [NatWest](https://about.gitlab.com/press/releases/2022-11-30-gitlab-dedicated-launches-to-meet-complex-compliance-requirements/)
10. Want replicas of their instance to be deployed in multiple regions around the globe to meet disaster recovery requirements.
11. Require access to logs and backups.
12. Require advanced scale of GitLab’s distributed architecture, managed by subject matter experts.
Companies that want options for deploying GitLab without sacrificing feature parity.
2. \*\*May not be a good fit\*\*
1. Open to (or required to) undertaking the operational costs and management of a fully self-managed solution and related infrastructure.
2. Would like more control over upgrades - e.g. needing to review and approve ahead of time.
3. \_Do not\_ have a need for:
- Ultimate OR
- A single tenant SaaS offering OR
- Strict data residency, compliance and heightened security requirements OR
- The minimum 1,000 User count threshold
</div>

#### Target User Persona

- [Sidney (Systems Administrator)](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)

#### Target Buyer

- CTO/CIO - Goals (Minimize OpEx while enhancing compliance & security, with near zero downtime)
- VP of Application Development - Goals (Shifting security left and focus on development vs. hosting, upgrading, securing, patching, etc. GitLab)
- CISO - Goals (Embedding application security early in the SDLC, while minimizing risk & cost from infrastructure security & compliance)
- [Tech Exec Tristan](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/roles-personas/buyer-persona/#tech-exec-tristan) - CIO/ CTO
- [Platform Perry](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/roles-personas/buyer-persona/#platform-perry) - Typical roles - Infrastructure Engineering, Platform Engineering
- [Back Office Blake](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/roles-personas/buyer-persona/#back-office-blake) -  Typical roles - Head of Procurement

### Shared Responsibility

As a SaaS solution, our customers should not have to worry about the details of operating GitLab. The goal is for them to have minimal management overhead. Having said that, the successful operation of GitLab Dedicated still requires a shared responsibility.

*GitLab Dedicated Responsibility*
1. Managing updates of underlying software such as PostgreSQL, Kubernetes, Redis, OpenSearch, and GitLab itself
1. Infrastructure operational monitoring and incident response
1. Capacity planning based on historical trends
1. Ensuring the Security of the Infrastructure and Network layer

*Customer Responsibility*
1. Adhering to performance GitLab practices, including but not limited to:
  1. Only storing [large blobs](https://docs.gitlab.com/ee/user/project/repository/monorepos/#large-blobs) with [_Large File Storage (LFS) objects_](https://docs.gitlab.com/ee/topics/git/lfs/index.html)
  1. For large [monorepos](https://docs.gitlab.com/ee/user/project/repository/monorepos/index.html) (larger than several gigabytes), reducing concurrent clones wherever possible, especially in CI/CD pipelines, to avoid potential bandwidth saturation
  1. Avoiding large spikes in concurrent CI jobs (e.g. hundreds launching at the same time of day)
  1. Limiting hundreds of concurrent CI jobs for [large repositories](https://docs.gitlab.com/ee/user/project/repository/monorepos/index.html)
  1. Optimizing custom scripts that run at high frequency
  1. Managing [integrations](https://docs.gitlab.com/ee/integration/index.html) in many large projects
  1. Properly configuring [server hooks](https://docs.gitlab.com/ee/administration/server_hooks.html)
  1. Carefully implementing [system hooks](https://docs.gitlab.com/ee/administration/system_hooks.html)
1. Implementing best practices for Security at the [application layer](https://about.gitlab.com/blog/2022/03/21/security-hygiene-best-practices-for-gitlab-users/) such as least privilege access


### Comparison to other Deployment Options

On GitLab Dedicated, customers are the administrators of their instance with full access to the [Admin area](https://docs.gitlab.com/ee/administration/) of their tenant. This is different from GitLab.com, where administration is owned by the GitLab Infrastructure team.

Availability will not be a point of differentiation between GitLab Dedicated and GitLab.com as both offerings target a 99.95% Availability SLA.

**See below for a comparison of the different ways to deploy GitLab:**

![alt text](./Deployment_Options_GitLab_Dedicated.png "GitLab Deployment Options")

## Where we are Headed
<!--
Describe the future state for your category.
- What problems are we intending to solve?
- How will GitLab uniquely address them?
- What is the resulting benefits and value to users and their organizations?

Use narrative techniques to paint a picture of how the lives of your users will benefit from using this
category once your strategy is at least minimally realized. In order to challenge your level of ambition
(with the goal to make it sufficiently high), link to the current market leaders long-term vision and address how
we plan to displace them. -->

Now that GitLab Dedicated has graduated from Limited Availability to General Availability, it can scale to meet the expected customer demand of the service. Customers who want a production-quality GitLab Dedicated instance and are willing to pay for it can now get one.

Next, we plan to focus on improving the onboarding and configuration management experiences by delivering the Switchboard management console. Additionally, we plan to add several highly requested features that were deferred in the lead up to GA. See the roadmap section below for more details.

### Prioritization Framework

Because Dedicated is a SaaS offering, we prioritize "Keep the lights on" activities (e.g. operating customer environments, tech debt, and corrective actions) above all else to ensure we provide customers a high level of service that continually meets our [platform SL0](https://handbook.gitlab.com/handbook/engineering/infrastructure/team/gitlab-dedicated/slas/#current-service-level-objective).

When it comes to customer feature requests, we prioritize features that [will benefit the most customers](https://handbook.gitlab.com/handbook/product/product-processes/#using-the-rice-framework). As a result, we will not build any custom capabilities or one-off features for individual customers. This includes not making modifications to individual tenants. Feature requests that meet our prioritization criteria but are not currently on the roadmap will be slotted in [after other committed roadmap items](#roadmap) have been delivered. For more information about feature requests for Dedicated, see the [feature request tracking issue](https://gitlab.com/gitlab-com/Product/-/issues/13856).

| Priority | Category | Description |
|-----------------------------|--------------------------|-----------------------|
| 1 | KTLO - On Call | Operating Tenant Production Environments, Handling new tenant onboarding and config change requests |
| 2 | Security, Reliability, Performance | Initiatives tied to increasing overall security (e.g. third party compliance certifications and addressing security findings), reliability (including improvements to Availability SLAs and disaster recovery procedures and targets), and scalability (ability to better scale underlying tenant infrastructure to support new customers as well as existing tenants ad their workloads and usage patterns increase) |
| 3 | Automation | Reduce toil required to operate the GitLab Dedicated platform and improve internal developer experience |
| 4 | Customer Feature Requests | Delivering new customer-facing platform capabilities as well as enabling GitLab functionality such as Pages, advanced search, reply-by email, service desk |
| 5 | Technical Debt | Initiatives tied to increasing speed of development, overall efficiency |


### Currently Available Features
Please see list of [Available Features](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/#available-features) in our documentation.


### What is Not Planned Right Now
<!-- Often it's just as important to talk about what you're not doing as it is to
discuss what you are. This section should include items that people might hope or think
we are working on as part of the category, but aren't, and it should help them understand why that's the case.
Also, thinking through these items can often help you catch something that you should
in fact do. We should limit this to a few items that are at a high enough level so
someone with not a lot of detailed information about the product can understand
the reasoning-->

Please see list of [Features that are not available](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/#features-that-are-not-available) in our documentation. While the most requested of these have been incorporated into the [roadmap](#roadmap) below, we are not currently focused on delivering the other features mentioned in that list. These will be considered for next year based on customer demand.

## Roadmap

The key capabilities we plan to deliver in Environment Automation for the first half of FY25 are summarized below. The roadmap for Switchboard can be found on the [Switchboard Direction Page](https://about.gitlab.com/direction/saas-platforms/switchboard/#where-are-we-headed).

### FY25

#### Q1

* [RTO and RPO improvements](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/325) - Complete
* [Next Iteration of Dedicated Runners Beta](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/324) - Complete
* [Support Bring your own Domain on Tenant Instances](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/244) - Complete

#### Q2
* [Next Iteration of Dedicated Runners Beta](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/324) (continued)
* [RTO and RPO improvements](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/446) (continued) - Complete
* GitLab 17.0 upgrade - Complete

#### Q3
* RTO and RPO improvements - Will continue
* OIDC Auth when using IP AllowLists - Complete
* Multiple SAML providers - Complete

#### Q4
* Web application firewall MVC - Complete
* SCIM Auth when using IP AllowLists - Complete
* OpenSSL v3 preparation - Complete

#### Future

##### Theme: Disaster Recovery
* Point in time restore
* RTO and RPO improvements

##### Theme: Feature Parity
* Multiple login providers

##### Theme: Global availability
* Additional region support
* Geo for global acceleration

##### Theme: Customer experience
* [Pre-production instances](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/317) (pricing and packaging, version n)
* Log sharing notifications for customers
* Improved SLAs
* [Make Dedicated Repos Public](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/33)

##### Hosted runners for GitLab Dedicated

The following features are currently planned for FY26
* [Hosted runners on Linux - General Availability](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/382)
* [Hosted runners outbound network control](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/583)
* [Hosted runners on macOS - Beta](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/392)
* [Hosted runners on Windows - Beta](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/397)

### Supporting AI Features on GitLab Dedicated

GitLab [AI features](https://docs.gitlab.com/ee/user/gitlab_duo/index.html) improve DevSecOps workflow efficiency and velocity by applying AI assisted workflows to all teams involved in delivering software value.

As a cloud-based Saas service, GitLab Dedicated is a natural fit to deliver cloud-based AI services to customers. However, as a single-tenant service we need to design a solution that maintains single-tenancy and does not compromise on customer compliance requirements like data residency and isolation, and predictability.

Short term, our goal is to bring AI features to GitLab Dedicated starting with Code Suggestions, followed by Suggested Reviewers. That effort can be tracked [via this epic](https://gitlab.com/groups/gitlab-org/-/epics/10516).

Long term, our vision is to design native AI capbilities for single-tenant SaaS deployments. This may include training models inside tenant environments to generate tailored insights and suggestions while keeping data private. This will allow enterprises and regulated industries to more easily adopt AI-assisted workflows while maintaining compliance requirements around data residency, privacy, and isolation.

While we don't have any specific timelines to share for bringing all AI features to GitLab Dedicated at this time, as these features become Generally Available, we will be working on a plan to enable them in GitLab Dedicated.

#### Parity between self-managed, multi-tenant SaaS and Dedicated

GitLab strives to maintain [parity between self-managed and SaaS](https://handbook.gitlab.com/handbook/product/product-principles/#parity-between-saas-and-self-managed-deployments). This can be challenging for certain features, like AI. From a Dedicated perspective, we adhere to the following principles:

1. We intend to make all AI features available to all platforms. We want to solve customer problems on all platforms.
1. In line, with our [SaaS First](https://handbook.gitlab.com/handbook/product/product-principles/#saas-first) principle, GitLab Dedicated may support certain features before self-managed.
1. GitLab Dedicated may offer additional features if there are technical or other limitiations that don't allow us to release them for self-managed customers.

## Go-to-market plans

### Guidelines for Engaging Customers at GA

#### Qualify the customer:

1. Review the [target customer profile](#target-customer) to ensure it is a good fit
1. Ensure that the customer meets the minimum seat count of 1000
1. Review the [Technical Qualification guidelines](https://internal.gitlab.com/handbook/engineering/horse/technical-qualification-evaluation-questionnaire/) to ensure there is a technical fit.
1. Review [pricing](#pricing), as this will cost more than our other offerings


#### Create the opportunity in Salesforce:

1. In your SFDC opportunity, set the Intended Product Tier to Dedicated Ultimate OR include Dedicated in the Opportunity name. This is the most important step to ensure we have visibility into the Dedicated pipeline.
1. Include number of Ultimate seats somewhere easily referenceable in your SFDC opportunity (such as the opportunity title) to make it clear that the deal is [qualified](#qualify-the-customer).

#### When to engage the Dedicated team

_Account teams (Sales leads and SAs) should give the initial pitch of Dedicated to their customers using the materials on the [Dedicated Page in Highspot](https://gitlab.highspot.com/items/636ea5092603d0ca437fcae1). This allows the Product team to spend more time supporting Dedicated deals that are further along in the sales cycle._

1. Technical questions and unique customer requirements
    * After the account team gives the initial pitch, if the opportunity progresses and the customer has technical questions or requirements for the service that cannot be answered by [the documentation](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/) or the [technical qualification guidelines](https://internal.gitlab.com/handbook/engineering/horse/technical-qualification-evaluation-questionnaire/), please reach out to the Dedicated team in the `#f_gitlab_dedicated` channel so that they can help answer these questions. After that, if the questions are still not resolved and a sync meeting is needed, please open an issue in the [Dedicated issue tracker](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues/) using the [Customer Meeting Template](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/blob/main/.gitlab/issue_templates/customer_meeting_request.md) to request a call with the Dedicated team.
1. Pricing Calculator Review
    * Once the customer has been [qualified](#qualify-the-customer) and they have expressed interest in moving forward with pricing, please use the [pricing calculator](https://internal.gitlab.com/handbook/engineering/horse/field-enablement/index.html#pricing) (internal only) to come up with a pricing estimate for the customer. Once you have completed the steps in the pricing calculator, reach out to the Dedicated Product team in the `#f_gitlab_dedicated` channel requesting a review. Also provide the [SFDC link](#create-the-opportunity-in-salesforce) for this opportunity.

Note: _you must receive approval from the Dedicated Product team before sharing any pricing numbers with the customer and before creating a formal quote via Salesforce_
{: .alert .alert-warning}

#### Additional public-facing GitLab Dedicated materials:

We have the following public facing pages available for those interested in learning more:
1. Documentation: [https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/)
2. Blog post: [https://about.gitlab.com/blog/2022/11/30/introducing-gitlab-dedicated/](/blog/2022/11/30/introducing-gitlab-dedicated/)
3. GitLab Dedicated webpage (and waitlist signup): [https://about.gitlab.com/dedicated/](/dedicated/)

### Channel Partner Role in GitLab Dedicated

GitLab Dedicated creates a business opportunity for both GitLab and GitLab channel partners who offer hosted GitLab services. We are creating this offering to meet the needs of customers who want to consume hosted solutions directly from the DevOps vendor (in this case GitLab, Inc.) to more closely align operational and DevOps application needs. Customers who are interested in purchasing hosting services that include value-add managed services (for example, helping meet industry-specific specific requirements like HIPAA) would benefit from working with a Managed Service Provider (MSP) [Partner](https://partners.gitlab.com/English/directory/) Additionally, many customers have existing relationships with Channel Partners. Per the [services ROE](https://handbook.gitlab.com/handbook/sales/selling-professional-services/), these customers should continue consuming GitLab through their Channel Partner. By following the segmentation laid out above, we can minimize any disruption to existing [channel-sourced ARR](https://gitlab.my.salesforce.com/00O4M000004aqhB)(GitLab internal).

With this effort, we also see an opportunity to grow the overall market for GitLab-hosted services through collaboration with partners. In the short-term we plan to enable MSP partners with [design guidance and certifications](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/1) (GitLab Internal) so that they can offer better hosted GitLab solutions for their customers. We will work with the GitLab Channel Partner team to create a partner certification that will provide MSP partners with technical certifications, training, deployment and maintenance guidelines, and access to some of the same underlying tooling that powers GitLab Dedicated (e.g. GitLab Environment Toolkit and official Reference Architectures). We plan to keep the other underlying services (e.g. Switchboard and Amp) as well as the `GitLab Dedicated` branding proprietary to GitLab, Inc. Longer-term opportunities for consideration include enabling partners [to resell GitLab Dedicated](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues/499)(GitLab internal). These partners would provide customers value-added services or integrated vendor stacks while the GitLab Dedicated team would still host the GitLab instance on behalf of the partner.

### Pricing

The pricing for GitLab Dedicated is comprised of the following components:

- Ultimate licenses (1000 seat minimum)
- Infrastructure & Management fee (which covers our costs of operating and hosting the service)
  - Fixed fee that varies based on the Infrastructure Size (e.g. S, M, L, XL, XXL, XXXL)
  - The Infrastructure & Management fee covers the following costs:
    - The cloud provider costs incurred when deploying the selected Infrastructure Size to two sites (the primary and secondary regions)
    - Engineering costs needed to operate the environment (e.g. perform ongoing tasks such as upgrading the instance, applying security patches, and achieving the stated SLAs)
    - Customer Support costs
    - Annual pentests, audits, and security software costs

- Storage
  - Amount of GB the customer wants to buy for their projects. [Free storage quota](https://docs.gitlab.com/ee/user/usage_quotas.html) applies.
  - The storage fee covers the following costs:
    - Cloud provider storage costs for all data stored in object storage and on disk
    - Networking costs
    - Cost of the data stored in the Geo secondary

#### More details on pricing
We've priced GitLab Dedicated to align with likely buyers based on minimums and the complexities of their deployments. As mentioned above, the pricing for GitLab Dedicated is comprised of the following components: the [cost for Ultimate Licenses](/pricing/), plus additional fees for instance infrastructure & management, the amount of storage needed, and the customer's infrastructure size (e.g. S, M, L, XL, XXL). As we scale and introduce GitLab Dedicated to more and more customer cohorts we'll share further details on pricing options.

## User success metrics
<!--
- What specific user behaviors are indicate that users are trying these features, and solving their problems?
- How will users discover these features?
-->

- Primary Performance Indicator
  - Paid GMAU
- Secondary Indicators
  - Customer Satisfaction
  - Uplift revenue: defined as revenue the offerings contributes beyond licenses. This includes the infra+management fee plus revenue from consumption pricing.
  - Gross Margin

## Competitive Landscape
<!-- The top two or three competitors, and what the next one or two items we should
work on to displace the competitor at customers, ideally discovered through
[customer meetings](https://handbook.gitlab.com/handbook/product/product-processes/#customer-meetings). We’re not aiming for feature parity with competitors, and we’re not just looking at the features competitors talk
about, but we’re talking with customers about what they actually use, and
ultimately what they need.-->

The main competitor to GitLab Dedicated is [GitHub AE](https://docs.github.com/en/github-ae@latest/admin/overview/about-github-ae), which offers a fully-managed GitHub Enterprise instance in the customer's desired region on Azure. Other competitors offering single-tenant, fully-managed devops solutions include AWS CodeCommit, Azure Devops, and GitLab Host.

#### Footnotes

1. IDC, Worldwide DevOps Software Tools Forecast, 2022–2026, Doc # US48599322, July 2022
