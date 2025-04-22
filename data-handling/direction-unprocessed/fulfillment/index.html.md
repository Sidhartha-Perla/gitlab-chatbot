---
layout: markdown_page
title: "Product Section Direction - Fulfillment"
description: "The Fulfillment section at GitLab focuses on supporting our customers to purchase, upgrade, downgrade, and renew paid subscriptions."
canonical_path: "/direction/fulfillment/"
---

## On this page
{:.no_toc}

- TOC
{:toc}

Last reviewed: 2024-11

## Fulfillment Section Overview

Fulfillment at GitLab aims to provide a seamless buying experience for customers. We invest in [quote-to-cash](https://handbook.gitlab.com/handbook/company/quote-to-cash/) systems to make purchasing, activating, and managing GitLab subscriptions as easy as possible. This improves customer satisfaction and streamlines our go-to-market (GTM) processes, helping accelerate revenue growth for the company.

## Get Involved

We welcome feedback and contributions to help improve our fulfillment processes:

- For customers and community members: Share your experiences and suggestions through our [public issue tracker](https://gitlab.com/gitlab-org/gitlab/-/issues) or by contacting your GitLab representative.
- For everyone: Create a merge request to this page and assign it to `@courtmeddaugh` for review, or [open a Fulfillment Meta issue](https://gitlab.com/gitlab-org/fulfillment-meta/-/issues/new) with your ideas.
- For GitLab team members: provide input on our [internal OKRs](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/8268) to help us ensure we are prioritizing the most important work.

Your insights help us continually improve and align our efforts with user needs.

### Mission

> Provide customers with an excellent experience by making it easy for them to purchase GitLab paid subscriptions and add-ons, provision their purchase, and manage subscription changes such as increasing seat count or renewing.

GitLab paid plans offer rich feature sets that enable customers to build software faster and more securely. For the Fulfillment section, success is to make it as easy as we can for a customer to transact with GitLab and unlock the value of these rich feature sets in our paid offerings.

We add new product offerings, make our subscription management process simpler, and work to support our customers' preferred purchasing channels and payment methods. This requires investments across all interfaces where customers conduct business with GitLab. Given the breadth of countries, organization sizes, and industries that benefit from the GitLab product, we strive to be excellent at both direct transactions via our web commerce portal or our sales team, as well as sales via [Channels and Alliances](https://handbook.gitlab.com/handbook/sales/#channels--alliances).

## Future Outlook

Looking beyond our [1-year plan](#1-year-plan), the Fulfillment section looks for opportunities to:

- Achieve near-complete automation of standard subscription management processes
- Expand our global payment and billing capabilities to support GitLab's growth in new segments and markets
- Develop more flexible and customizable subscription models to meet the diverse needs of our expanding customer base
- Integrate advanced analytics and AI to provide predictive insights for customer renewal and expansion opportunities

### Impact on GitLab's addressable market

We expand our addressable market by launching new product offerings, including the recent addition of GitLab Duo Pro add-on and Enterprise Agile Planning. We also improve operational efficiency by providing a seamless end-to-end subscription management experience. This enables our Sales teams to spend more of their time on strategic discussions with customers. It also allows our Support and Finance teams to be more efficient.

Recent accomplishments that have expanded our addressable market include:

- The introduction of GitLab Duo Enterprise and Duo Pro add-ons, which open up new revenue streams and address evolving customer needs in AI-assisted development.
- Enabling Ultimate trials on existing GitLab.com Premium namespaces, which has facilitated upgrades and increased adoption of our most comprehensive offering.
- Improvements in self-service capabilities, which have made GitLab more accessible to a broader range of customers, particularly in the SMB segment.


## Recent Accomplishments

We continue to balance delivering new business opportunities while improving our technical systems foundations.

### Recent Pricing & Packaging Highlights

1. 2024-08 [GitLab Duo Enterprise add-on](/blog/2024/08/14/gitlab-duo-enterprise-launch/)
2. 2024-01 [GitLab Duo Pro add-on](/blog/2024/01/17/gitlab-duo-pro/)
3. 2023-11 [Enterprise Agile Planning add-on](/blog/2023/11/16/gitlab-enterprise-agile-planning-add-on-for-all-roles/) for GitLab Ultimate subscriptions

### Recent Customer Experience Improvements

1. FY25-Q3 Launched GitLab Duo Enterprise trials
5. FY25-Q3 Improved Duo seat assignment with sorting, filtering, and expanded bulk UI assignments for up to 100 users at a time
6. FY25-Q3 Launched [Manage Non-billable to Billable Promotions feature](https://docs.gitlab.com/ee/administration/settings/sign_up_restrictions.html#enable-role-promotion-approval)
4. FY25-Q3 Expanded self-service renewal and auto-renewal for subscriptions with multiple rate plans
1. FY25-Q3 Enabled self-service Ultimate trials on exisitng gitlab.com Premium namespaces (previously required internal GitLab team member intervention)
2. FY25-Q3 Rolled out [Beta GitLab.com Opt-in Block Seat Overages](https://docs.gitlab.com/ee/administration/settings/sign_up_restrictions.html#turn-on-restricted-access)
3. FY25-Q3 Completed Duo Offline Licensing for Offline customers running Custom Models
7. FY25-Q2 Launched self-service purchase capabilities for Duo Pro via the [Customers Portal](https://customers.gitlab.com/customers/sign_in)

## Customer Feedback

We've seen improvements in customer satisfaction and reductions in customers needing assistance, which we can attribute to improvements such as: 

- The introduction of Block Seat Overages and Manage Non-billable to billable promotions helping customers looking for more predictable billing
- Our enhanced Duo seat assignment features improving the user management experience for larger organizations
- The ability to self-service renew subscriptions with multiple rate plans has reduced friction in the renewal process for many customers

We continuously incorporate this feedback into our product development process to ensure we're meeting our customers' evolving needs.

## 1-year Plan

Our focus themes align with our key priorities:

1. Enable Revenue Growth and Market Expansion
2. Enhance Customer Experience and Self-Service
3. Simplify Subscription Model and Management
4. Improve System Reliability and Performance
5. Enhance Platform Scalability and Technical Foundation

Within these themes, our top priorities across all Fulfillment groups are outlined below. For more details on specific initiatives, please refer to our category direction pages linked in the Key Links section below.

### 1. Enable Revenue Growth and Market Expansion

- Implement self-service discount flow for SMB customers to increase conversion rates
- Increase sales efficiency by enabling auto-renewal for a significant number of subscriptions
- Continue optimizing trials and ease of purchase for our new product offerings, including GitLab Duo Enterprise and Duo Pro

### 2. Enhance Customer Experience and Self-Service

- Enable Duo provisioning via LDAP to improve adoption and reduce support tickets
- Implement SCIM user account provisioning in .com for better user management in large organizations
- Introduce self-service Billing Account Manager management
- Improve renewal email accuracy to improve customer clarity around renewals
- Implement self-service support contact management
- Further enhance the Customers Portal user experience, including improvements to purchase flows and subscription management

### 3. Simplify Subscription Model and Management

- Complete designs for a new Seat Assignment Model to simplify license management
- Expand the rollout of Block Seat Overages to prevent unexpected billing surprises
- Enhance Automatic Dormant Members Removal for gitlab.com groups to optimize license utilization
- Continue refining our subscription models to reduce complexity and improve customer satisfaction

### 4. Improve System Reliability and Performance

- Implement comprehensive customers.gitlab.com error monitoring to identify and resolve issues faster
- Enhance Customers Portal performance to improve user experience

### 5. Enhance Platform Scalability and Technical Foundation

- Unify Usage Quotas Pages to simplify the codebase and improve developer productivity
- Update technical documentation to improve developer onboarding and speed up implementation
- Improve support engineering tooling for subscription management
- Invest in Fulfillment developer productivity through code refactors and new tooling deployment

## Challenges and Opportunities

As we continue to evolve our fulfillment processes and offerings, we face several challenges and opportunities:

Challenges:
- Balancing the needs of diverse customer segments, from SMBs to large enterprises
- Maintaining system performance and reliability as we scale and add new features
- Ensuring seamless subscription management for an increasing number of products and add-ons

Opportunities:
- Leveraging automation to further streamline fulfillment processes
- Expanding our presence in cloud marketplaces to reach new customer segments

## Roadmap

Due to the [not public](https://handbook.gitlab.com/handbook/communication/confidentiality-levels/#not-public) nature of most of our projects, our product roadmap is internal. 

We have [Fulfillment FY25 Plans and Prioritization](https://gitlab.com/gitlab-com/Product/-/issues/12843) (also Not Public), that GitLab team members can reference to track all planned initiatives by theme.

### Roadmap Prioritization

To learn more about our roadmap prioritization principles and process, please see [Fulfillment Roadmap Prioritization](https://handbook.gitlab.com/handbook/product/fulfillment-guide/#fulfillment-roadmap-prioritization)

## Groups and categories

The Fulfillment section encompasses four groups and [nine categories](https://handbook.gitlab.com/handbook/product/categories/). See [GitLab categories](https://handbook.gitlab.com/handbook/product/categories/#fulfillment-section) for details on the section, stage, and groups organization, including a list of team members. 

A list of Stable Counterparts can be found in the [Engineering Fulfillment Sub-Department page](https://handbook.gitlab.com/handbook/engineering/development/fulfillment/#stable-counterparts)

## OKRs

Team members can reference our [Fulfillment FY25 Q3 OKRs](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/8268) (Internal). 

We follow the [OKR (Objective and Key Results)](https://handbook.gitlab.com/handbook/company/okrs/) framework to set and track quarterly goals.

## Key Metrics

While we don't publicly share specific numbers, we monitor key metrics across support, self-service adoption, and revenue impact to ensure alignment with GitLab’s growth objectives.

- Support ticket reduction related to subscription management
- Self-service subscription management adoption rates
- Seat utilization rates across different subscription types
- Trial conversion rates for new products and add-ons
- Revenue impact of new product offerings and pricing changes
- System uptime and performance metrics for critical fulfillment services


## Recent Accomplishments and Learnings

See [Fulfillment Recap issues](https://gitlab.com/gitlab-com/Product/-/issues/?sort=updated_desc&state=closed&label_name%5B%5D=Fulfillment%20Recap&first_page_size=20) for recaps of other recent milestone accomplishments and learnings (internal when needed).

## Key Links

1. [Fulfillment Guide](https://handbook.gitlab.com/handbook/product/fulfillment-guide/): documentation around CustomersDot Admin tools and process documentation that is not part of the [core product documentation](https://docs.gitlab.com/).
2. [Dev - Fulfillment Sub Department](https://handbook.gitlab.com/handbook/engineering/development/fulfillment/): R&D team, priorities, prioritization processes, and more.
3. [Internal Handbook - Fulfillment](https://internal.gitlab.com/handbook/product/fulfillment/): documentation that can't be in the public handbook. Minimize this to only [Not Public](https://handbook.gitlab.com/handbook/communication/confidentiality-levels/#not-public) information, such as revenue-based KPIs or sensitive project documentation.
4. [GitLab Docs Subscription Documentation](https://docs.gitlab.com/ee/subscriptions/)