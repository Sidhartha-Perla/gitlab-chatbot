---
layout: markdown_page
title: "Product Direction - Fulfillment: Subscription Management"
description: "The Subscription Management team at GitLab is focused on delivering an easy, informed, and reliable experience for customers to purchase GitLab products, manage their subscriptions, and view billing details and contacts."
canonical_path: "/direction/fulfillment/subscription-management/"
---

## On this page
{:.no_toc .hidden-md .hidden-lg}

- TOC
{:toc}

 **Last updated**: 2025-01-23

## Mission

Deliver an easy, informed, and reliable experience for customers to purchase GitLab products, manage their subscriptions, and view billing details and contacts.

## Overview

The Subscription Management team is responsible for providing customers with the self-service tools and features needed to purchase GitLab products and efficiently manage their subscriptions and accounts.

### Key focus areas

1. Empower customers to purchase new products and make changes to their subscriptions without requiring assistance from GitLab support or sales teams.
1. Automate subscription management with features like Quarterly Subscription Reconciliation (QSR) and Auto-Renewal to streamline processes for customers and internal teams.
1. Continuously improve the [Customers Portal](https://customers.gitlab.com/) to ensure a seamless and intuitive experience for all user types, including self-service, sales-assisted, and channel partner customers.
1. Given the global commerce functionality, support compliance, legal, and tax related efforts to safeguard revenue and meet regulations.

By focusing on these areas, the Subscription Management team aims to reduce friction in the subscription lifecycle, improve customer satisfaction, and support GitLab's overall growth and retention goals.

### Target audience and experience

- Self-service customers
- Sales assisted customers
- Channel Partner customers
- Internal teams (Sales, Customer Success, Billing, Legal, Tax, Compliance)

### Feature overview and maturity

| Feature | Maturity | Description | To reach the next Maturity level |
|---------|:--------:|-------------|----------------------------------|
| Purchase subscription | 😊 `Viable` | First time and repeat purchases of Gitlab.com and Self-managed subscriptions, as well as add-ons such as Storage, Compute Minutes and Duo Pro. | |
| View subscriptions | 😊 `Viable` | Gitlab.com, SM, Dedicated subscriptions can be viewed in the Customers Portal. | |
| Renew subscription | 😊 `Viable` | Gitlab.com and SM subscriptions can be renewed with a credit card. | |
| Auto-Renew subscription | 😊 `Viable` | Gitlab.com and SM subscriptions can be auto-renewed, certain exclusion apply. |  |
| Add seats to a subscription | 😊 `Viable` | Gitlab.com and SM subscriptions can have seats added with a credit card. | |
| Remove seats from a subscription | ✖️  | Not Planned  | |
| Upgrade a subscription | 😊 `Viable` | Gitlab.com and SM Premium subscriptions can be upgraded to Ultimate with a credit card. | |
| Downgrade a subscription | ✖️ | Not planned | |
| View invoices | 😊 `Viable` | All customers that purchased directly from GitLab can view their invoices. | |
| Pay for the invoice | 🌱 `Planned` | All customers can pay for the invoice with a credit card. | |
| Manage payment methods | 😊 `Viable` | All customers that purchased directly from GitLab can view and manage their credit cards. | |
| Quarterly Subscription Reconciliation (QSR) process | 🙂 `Minimal` | QSR will process for some use cases of SaaS and SM subscriptions (Self-Service and Sales Assisted) that are opted into QSR.  | |
| Special UX for Channel Partner customers  | 😊 `Viable` | Channel customers are able to login, manage contact information, view subscriptions and licenses. They get directed to the GitLab Partner to make subscription changes.  | |
| Emails/In-app notifications related to subscription management | 🙂 `Minimal` | | |

**Legend:**

- ✖️ **Not Planned**: Not planned right now.
- 🌱 **Planned**: Not yet implemented, but on our roadmap.
- 🙂 **Minimal**: Available and works for a small number of use cases. Some transparency for internal teams.
- 😊 **Viable**: Available and works for majority of use cases. Some transparency for internal teams.
- 😁 **Complete**: Fully functional for all eligible use cases. Full transparency for internal teams.
- 😍 **Lovable**: Glowing review from external and internal users.

## Roadmap and Planning

### Current opportunities

| Opportunity | Solution(s) |
|---------|:--------|
| Customers often struggle to identify the appropriate contact for assistance with purchasing or managing their subscription and billing account. | We plan to [create a "Contact Us" page](https://gitlab.com/groups/gitlab-org/-/epics/14927) where customers can view their Account Executive's contact information and direct links to reach support. |
| Customers would like the ability to add extra subscription contacts to their accounts without contacting Support. | We plan to [enable customers to invite multiple billing account managers to the Billing Account](https://gitlab.com/groups/gitlab-org/-/epics/10495). |
| Customers who purchased GitLab through the sales team would like the option to pay their outstanding invoices using a credit card. | We plan to [build a "Pay for Invoice" page to enable one-time payments](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/10399). |
| Customers in India are unable to make direct purchases from GitLab due to the [Reserve Bank of India (RBI) mandate](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12051&Mode=0). | [We plan to address this problem](https://gitlab.com/groups/gitlab-org/-/epics/16220). |

### Next opportunities

| Opportunity | Solution(s) |
|---------|:--------|
| Customers often find Upcoming Renewal emails confusing, as they tend to be irrelevant, unclear, and lacking actionable information. | [Move subscription renewal emails out of Zuora and into CustomersDot](https://gitlab.com/groups/gitlab-org/-/epics/9303). This will allow us to limit which emails are sent, and customize their contents. |
| Purchase flows in the Customers Portal lack a consistent user experience and scalable technical implementation. The process for buying Premium or Ultimate differs significantly from purchasing products like Storage or Compute, as well as from upgrading or renewing. This inconsistency increases the engineering team's workload in building and maintaining these various flows. | We are working to [unify all purchase flows in the Customers Portal to enhance scalability and improve the user experience](https://gitlab.com/groups/gitlab-org/-/epics/12199). |

### Future opportunities

| Opportunity | Solution(s) |
|---------|:--------|
| A subscription set to auto-renew may fail to renew for several reasons: expired credit card, payment failure, unpaid overages, or issues calculating overages. | Analyze data on the number of subscriptions that failed to auto-renew and develop a tactical plan to increase the success rate of auto-renewals. |
| Approximately 5% of our customers are associated with multiple billing accounts, but the Customers Portal currently does not support this scenario. | [Create an experience](https://gitlab.com/groups/gitlab-org/-/epics/8986) that allows customers to view and switch between multiple billing accounts seamlessly. |

### What we recently completed

Most recently completed projects are shown first.

1. [Enable self-service renewal and auto-renewal of subscriptions with Duo Pro and Duo Enterprise](https://gitlab.com/groups/gitlab-org/-/epics/10977).
1. [Enable self-serice renewal of subscriptions with Storage only](https://gitlab.com/groups/gitlab-org/-/epics/9589).
1. [Update self-service renewal flow to accommodate all renewable products in the subscription](https://gitlab.com/groups/gitlab-org/-/epics/11869).
1. [Combine multiple rate plans for the same product during renewal](https://gitlab.com/groups/gitlab-org/-/epics/11916).
1. [Improve the purchase flows in the Customers Portal following the migration from .com](https://gitlab.com/groups/gitlab-org/-/epics/14096).
1. [Move purchase flows from .com to the Customers Portal](https://gitlab.com/groups/gitlab-org/-/epics/9569).
1. [Support for 3D Secure authentication for credit card payments](https://gitlab.com/groups/gitlab-org/-/epics/7714).
1. [New Navigation for the Customers Portal, which enables BillTo/Sold contact management and displays Billing Account Managers](https://gitlab.com/groups/gitlab-org/-/epics/10367).
1. [Updated subscription display in the Customers Portal so that it's more user friendly and scalable for various product offerings](https://gitlab.com/groups/gitlab-org/-/epics/9746).
1. [Allowing customers that puchased via Reseller to access Customers Portal](https://gitlab.com/groups/gitlab-org/-/epics/8941).
1. Renewal discounting functionality in preparation for the [GitLab Premium Price update](https://about.gitlab.com/blog/2023/03/02/gitlab-premium-update/).
1. [New subscription display in the Customers Portal for ramp subscriptions](https://gitlab.com/groups/gitlab-org/-/epics/8748).
1. [Research on the renewal experience](https://gitlab.com/gitlab-org/ux-research/-/issues/1782) and existing processes, involving both internal teams and GitLab customers, to understand and enhance the overall renewal process.
1. [Subscription auto-renewal](https://handbook.gitlab.com/handbook/product/fulfillment-guide/#subscription-renewal-and-auto-renewal) for all major use cases.
1. Improved transparency into the overages and related billing for SaaS customers [at the time of adding users](https://gitlab.com/groups/gitlab-org/-/epics/7230).

### Reference to OKRs, Epics, Issues and Boards

Some content is confidential and therefore won't be visible.

* Quarterly OKRs
   * FY25-Q2: [Fulfillment section](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/6895), [Subscription Management group](https://gitlab.com/gitlab-com/gitlab-OKRs/-/issues/?sort=updated_asc&state=all&label_name%5B%5D=group%3A%3Asubscription%20management&label_name%5B%5D=FY25-Q2&first_page_size=50)
   * FY25-Q3: [Fulfillment section](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/8268), [Subscription Management group](https://gitlab.com/gitlab-com/gitlab-OKRs/-/issues/?sort=updated_asc&state=all&label_name%5B%5D=group%3A%3Asubscription%20management&label_name%5B%5D=FY25-Q3&first_page_size=50)
   * FY25-Q4: [Fulfillment section](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/9504), [Subscription Management group](https://gitlab.com/gitlab-com/gitlab-OKRs/-/issues/?sort=updated_asc&state=all&label_name%5B%5D=group%3A%3Asubscription%20management&label_name%5B%5D=FY25-Q4&first_page_size=20)
* [Fulfillment Roadmap > Subscription Management](https://gitlab.com/groups/gitlab-org/-/roadmap?state=all&sort=end_date_asc&layout=QUARTERS&timeframe_range_type=THREE_YEARS&label_name%5B%5D=Fulfillment+Roadmap&label_name%5B%5D=group%3A%3Asubscription+management&progress=COUNT&show_progress=true&show_milestones=false&milestones_type=GROUP)
* All Subscription Management epics
   * [List of epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=group::subscription+management)
   * [Organized epics board](https://gitlab.com/groups/gitlab-org/-/epic_boards/31408?label_name[]=group%3A%3Asubscription%20management)
* All Subscription Management issues
   * [List of issues](https://gitlab.com/groups/gitlab-org/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=group%3A%3Asubscription%20management&first_page_size=20)
   * [Organized issues board](https://gitlab.com/groups/gitlab-org/-/boards/4282426?label_name[]=group%3A%3Asubscription%20management)
