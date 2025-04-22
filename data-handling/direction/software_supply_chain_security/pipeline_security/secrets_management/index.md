---
layout: markdown_page
title: "Category Direction - Secrets Management"
description: "Stay secure with GitLab’s secrets management, protecting sensitive data in pipelines by ensuring proper handling and storage of credentials."
---

- TOC
{:toc}

## Secrets Management

| | |
| --- | --- |
| Stage | [Software Supply Chain Security](/direction/software_supply_chain_security/) |
| Maturity | [Minimal](/direction/#maturity) |
| Content Last Reviewed | `2025-01-18` |

### Introduction and how you can help

Thanks for visiting this category direction page on Secrets Management in GitLab. This page belongs to the [Pipeline Security](https://handbook.gitlab.com/handbook/product/categories/#pipeline-security-group) group of the Software Supply Chain Security stage and is maintained by Jocelyn Eillis ([E-Mail](mailto:jeillis@gitlab.com)).

This category covers the experiences related to secrets management and CI job token. For more information, check out the [features page](https://about.gitlab.com/features/?stage=govern#secrets_management).

This direction page is a work in progress, and everyone can contribute:

 - Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=Category%3ASecrets%20Management&label_name%5B%5D=group%3A%3Apipeline%20security&first_page_size=100) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=Category:Secrets+Management) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
 - Please share feedback directly via [email](mailto:jeillis@gitlab.com) or schedule a [video call](https://calendly.com/jeillis). If you're a GitLab user and have direct knowledge of your need for secrets management and CI job token, we'd especially love to hear from you.

### Overview
<!-- Describe your category so that someone who is not familar with the market space can understand what the product does.
-->

_Everybody has a secret._

Secrets Management can have a broad meaning. For the Secrets Management product category at GitLab, we have a very specific scope.
Secrets Management is specifically about **enabling GitLab, or a component built within GitLab to connect to other systems.**

The Secrets Management product category does **not** include the various access tokens created within GitLab that allow other systems to access GitLab or GitLab to access itself. In order to provide an aligned vision and strategy around access to GitLab, these features typically fall under [the Authentication and Authorization category](/direction/software_supply_chain_security/authentication/).

As Secrets Management focuses primarily on how GitLab can access 3rd party systems, it is tightly coupled [to the Environment Management product category](/direction/delivery/environment_management/).

There are 3 classifications of secrets within the scope of Secret Management:

- static secrets
- dynamic secrets
- application secrets

Ideally, application secrets would never reach GitLab as they are used only within the user's infrastructure and enable one service to access another service, i.e. the database URI deployed into a web application's configuration. The best approach around application secrets would be to retrieve them within the user's infrastructure, without the secret ever leaving the internal network.

In our categorization, static and dynamic secrets are the secrets used to access a 3rd party system by GitLab itself, let it be for a deployment, reporting or any other integration reason. The difference between dynamic and static secrets is their lifespan. Static secrets are ... static. They either exist permanently or are revoked or rotated in a separate process. Dynamic secrets are short-lived and their lifespan is often managed by a tool. Examples of these tools include HashiCorp's Vault, Azure Key Vault, AWS Secrets Manager, and Google Cloud Secret Manager.

### Strategy and Themes
<!-- Capture the main problems to be solved in market (themes). Describe how you intend to solve these with GitLab (strategy). Provide enough context that someone unfamiliar with the details of the category can understand what is being discussed. -->

### 1 year plan
For information regarding our 1 year plan, please reference our roadmap in [this deck](https://docs.google.com/presentation/d/1-QUDo9j3NHZC2hOrv0P5tRyWouTdM2QFFToYunZ0Bv4/edit#slide=id.g2fb3251c6dc_5_666) [INTERNAL ONLY] and [priorities](https://about.gitlab.com/direction/software_supply_chain_security/pipeline_security/#priorities) for the team.

### Best in Class Landscape
<!-- Blanket description consistent across all pages that clarifies what GitLab means when we say "best in class" -->

BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

#### Key Capabilities
<!-- For this product area, these are the capabilities a best-in-class solution should provide -->
We envision GitLab providing an industry-leading solution for managing static secrets, has loveable integrations with selected third-party secret managers, and provides advanced features (i.e. key management) to ensure best secrutiy practices to fully mitigate the risk of moving application secrets outside customer infrastructure.

The driving principles around static secrets managements are that secrets should be

- restricted
- write only
- encrypted at rest and in transit
- versioned
- auditable
- revokable

Every IT project requires secrets. As a result, by not providing a strong offering in this space, we force all security-minded users to have to search for an alternative solution. Without Secret Management out-of-the-box, we fail to fulfill our vision of being a complete single DevSecOps platform.

We also know that a large majority (80%) of customers only require support for static secrets and removing the pain around application secrets, so our investment does not have to be massive. Nor do we have to complete directly with the market leaders in this space.

#### Roadmap
<!-- Key deliverables we're focusing on to build a BIC solution. List the epics by title and link to the epic in GitLab. Minimize additional description here so that the epics can remain the SSOT. This may be duplicative to the 1 year section however for some categories the key deliverables required to become the BIC solution will extend beyond one year and we want to capture all of the gaps. Moreover, the 1 year section may contain work that is not directly related to closing gaps if we are already the BIC or if we are differentiating ourselves.-->
To become the best-in-class solution for secrets management, we are focusing on the following key deliverables:

1. [Implement GitLab native secrets manager](https://gitlab.com/groups/gitlab-org/-/epics/10723) - This will provide a built-in solution for managing static secrets within GitLab, offering core functionality such as encryption, versioning, and access control.

2. [Enhance CI job token permissions](https://gitlab.com/groups/gitlab-org/-/epics/6310) - Implementing more granular permissions for CI job tokens will improve security and flexibility for users managing access to resources.

3. [Improve JWT token support for OpenID Connect](https://gitlab.com/groups/gitlab-org/-/epics/7335) - Enhancing our JWT token support will enable better integration with third-party services and improve overall security.

4. [Integrate with AWS Secrets Manager](https://gitlab.com/gitlab-org/gitlab/-/issues/29047) - Adding native integration for AWS Secrets Manager will expand our offering to support users in AWS environments.

6. [Implement secrets management instrumentation](https://gitlab.com/groups/gitlab-org/-/epics/9725) - Adding comprehensive instrumentation will provide valuable insights into usage patterns and help inform future feature prioritization.

These deliverables aim to address key capabilities required in a best-in-class secrets management solution, including secure storage, integration with popular third-party services, improved user experience, and enhanced security controls.

#### Top Competitive Solutions
<!-- PMs can choose to highlight a primary BIC competitor--or more, if no single clear winner in the category exists; in this section we should indicate: 1. name of competitive product, 2. links to marketing website and documentation, 3. why we view them as the primary BIC competitor -->

The biggest question with respect to Secrets Management integrations is to choose the right partners. The Secrets Management market is a fast moving target with a few, well known providers offering their solutions, and a huge number of users not using any of these. Beside HashiCorp Vault, notable offerings are at least [CyberAkr Conjur](https://www.conjur.org/) and the Secrets Management offering of [AWS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), [Google](https://cloud.google.com/secret-manager), and [Azure](https://azure.microsoft.com/en-us/services/key-vault/).

Additionally, [Vault Enterprise](https://www.vaultproject.io/docs/enterprise/) offers
additional sets of capabilities that will _not_ be part of the open source version
of Vault bundled with GitLab. This includes
[replication across datacenters](https://www.vaultproject.io/docs/enterprise/replication/index.html),
[hardware security modules (HSMs)](https://www.vaultproject.io/docs/enterprise/hsm/index.html),
[seals](https://www.vaultproject.io/docs/enterprise/sealwrap/index.html),
[namespaces](https://www.vaultproject.io/docs/enterprise/namespaces/index.html),
[servicing read-only requests on HA nodes](https://www.vaultproject.io/docs/enterprise/performance-standby/index.html)
(though, the open source version does support [high-availability](https://www.vaultproject.io/docs/concepts/ha.html)),
[enterprise control groups](https://www.vaultproject.io/docs/enterprise/control-groups/index.html),
[multi-factor auth](https://www.vaultproject.io/docs/enterprise/mfa/index.html),
and [sentinel](https://www.vaultproject.io/docs/enterprise/sentinel/index.html).

For customers who want to use GitLab with the enterprise version of Vault, we need to ensure that this is easy to switch to/use as well.

In the CICD variables space, GitHub [variables](https://docs.github.com/en/actions/configuring-and-managing-workflows/using-environment-variables), offer comparable flexibility and power. They also offer a differentiation between variables and GitHub [secrets](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets), which has set an expectation in the market for a distinct treatment of those objects. We are beginning to investigate this for GitLab in [gitlab#217355](https://gitlab.com/gitlab-org/gitlab/-/issues/217355). GitHub Actions supports [injection of HashiCorp Vault Secrets into CICD pipelines](https://www.hashicorp.com/blog/vault-github-action), which is directly competing with GitLab's first-to market offering of HashiCorp Vault [Secrets in GitLab](https://docs.gitlab.com/ee/ci/secrets/).

### Target Audience
<!--
List the personas (https://handbook.gitlab.com/handbook/marketing/strategic-marketing/roles-personas#user-personas) involved in this category.

Look for differences in user's goals or uses that would affect their use of the product. Separate users and customers into different types based on those differences that make a difference.
-->
Operations, compliance, security, and audit teams will derive immense value from being able to manage secrets within GitLab. In the motion of shifting security left, developers will also be empowered with the comprehensive treatment of variables and keys as a secrets in GitLab. By prioritizing external key store integrations, we will expand GitLab's security by offering an extra layer for tokens, keys, and other confidential data. This combination of tools will further establish GitLab's presence as an enterprise-grade, corporate solution for Release Management.

<!-- commenting this out while I figure out the broken link issue
### Jobs


-->

### Pricing and Packaging
As secret handling is a core requirement of every IT project, basic static secret management should be part of GitLab Free. Enterprise Secrets Management (including permission management, versioning, and advanced audit capabilities) are likely to be paid features.

#### Current Position

Today GitLab supports environment variables. Environment variables do not meet the need for secure storage of sensitive information. Given our security first positioning, we are building our native secrets solution to address this gap within our existing product.

GitLab has native integrations with Hashicorp Vault, Azure Key Vault, and Google Secret Manager. These are basic integrations, and do not provide full coverage for all enterprise use cases.

Lastly, GitLab provides a JSON Web Token (JWT) that enables access to various 3rd party systems. This option requires additional development effort from the user to set up properly.

### Analyst Landscape
- In March 2023 Gartner had publish a research name [Managing Machine Identities, Secrets, Keys and Certificates](https://drive.google.com/file/d/1lYQGoAzDo1OcyhUc5F2a4XAk9RHiUmV7/view?usp=sharing) (internal link)
- Internal research [Enterprise SaaS User Base Survey: Secrets + SaaS](https://docs.google.com/presentation/d/1m4PiVVg7eTLRMXv4C6MThs2ZFV5kWoPAjuIDKV3cHA0/edit#slide=id.g1337c2a03f8_0_264)
