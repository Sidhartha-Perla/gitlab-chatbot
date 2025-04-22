---
layout: markdown_page
title: "Category Direction - Utilization - Seat Cost Management"
description: "The Utilization group aims to ensure customers have access to seat usage data, so that they can make the optimal decisions for their business needs."
---

- TOC
{:toc}


## Fulfillment: Utilization - Seat Cost Management Overview

The Utilization group aims to ensure customers have access to seat usage data, so that they can make the optimal decisions for their business needs.

## Vision

_What is our long-term solution concept? Analogy: what will it look like at the top of the mountain?_

Today, seat assignment, management, and overages are broken. Examples of how customers are impacted by these:
- **Overages result in unexpected bills** – “I didn’t know that I could add additional users without first purchasing seats. I was not expecting a bill this large.”
- **Role promotion can have billable implications** – "Our Ultimate guests can easily become non-guests which ends up costing us more money."
- **EAP users can change roles** -- "Our EAP users no longer occupy Planner roles. Why is that and how do we know how many EAP users we have?"
- **Consolidated users view lacking in GitLab.com** – “I am confused by what user information is shown on the Member’s page and the Usage Quotas pages. In SM, we had a consolidated users view, why don’t we have that on GitLab.com?”
- **Role elevation can make compliance hard** – "Our minimal access users can easily become developers and that violates our corporate compliance workflows and who is allowed to do what."

To solve these problems we are going to:
1. **Develop a seat assignment model (SAM).** We’ll move away from users immediately consuming a subscription seat when being added to a group or project based on their role. With SAM, group owners and admins will be able to assign users to a seat type which in turn determines what roles they can have when being added to groups and projects.
    1. For example, you could have a namespace with an Ultimate Subscription and 20 users. 15 of those 20 users could have a Seat Type = Base where available roles are Reporter, Developer, Maintainer, Owner, Admin, or a billable custom role. 5 of 20 users could be on Seat Type = Free where the roles available are Guest, Minimal Access, or a non-billable custom role. You'll be able to assign a Seat Type to a user, which determines what roles they can then have.
2. **Establish controls to allow for promotions between seat types.** We’ll move away from users being able to easily transition between roles, which can have billable and compliance consequences. Instead, admins/group owners will be given controls to manage seat type promotions.
    1. For example, let's say you have a user in an Seat Type = Free with Role = Guest that is free. However, the user has now changed roles and needs access to a Developer role. As part of that transition, they will need to be promoted to a Seat Type = Base, which has increased cost implications. We will need to give customers controls to make that transition from Seat Type = Free to Seat Type = Base given both the compliance and cost implications of such changes.
3. **Prevent unintended overages.** Today, all customers are charged for seat overages. In the future, the majority default for customers will be that they will need to purchase seats before seats can be assigned to users. However, enterprise customers will be able to continue to have overages via contract negotiations.

These changes will not be universally felt by customers:
- For our enterprise customers that are optimizing for frictionless addition of new users will largely be able to continue to interact with GitLab as they do today while also appreciating enhancements like a consolidated users view in GitLab.com and optimized billable calculations. If they want more controls for cost, they can opt-in to those.
- However, for the large majority of customers, who are optimizing for controlling costs, we will be giving them more controls and visibility to manage their costs.

## Feature Overview and Maturity

_What features are the Utilization group responsible for and how mature are they?_

**Legend**:

- 🙂 **Minimal**: Available and works for a small number of use cases. Some transparency for internal teams.
- 😊 **Viable**: Available and works for the majority of use cases. Some transparency for internal teams.
- 😁 **Complete**: Fully functional for all eligible use cases. Full transparency for internal teams.
- 😍 **Lovable**: Glowing reviews from external and internal users.

| Category | Feature | Maturity | Description |
|---------|---------|:--------:|-------------|
|Seat Cost Management (non-add-on products) | Seat Usage Visibility | 😊 Viable | Customers understand how many seats are being used and by whom |
|Seat Cost Management (non-add-on products)| Billable Users Calculation | 🙂 Minimal | Customers understand how many billable seats are being used, by whom, and when they are being used |
|Seat Cost Management (non-add-on products)| Seat Limits | 😊 Viable | Customers understand if they are within the user limits threshold and how to take action (remove, add more, set seat limits) |

## 1-year Plan

_Where are we focused over the next 12 months to make meaningful steps towards achieving our vision and increasing feature maturity?_

### 1-year Roadmap

[Further Details](https://internal.gitlab.com/handbook/product/fulfillment/seat-cost-management/) (Not Public)

| What is the work to do? | Why are we doing this work? |
|---------|--------|
| [Dormant User Management for GitLab.com](https://gitlab.com/groups/gitlab-org/-/epics/7533) | Identifying dormant users and removing them on Gitlab.com is a labor intensive and not very intuitive process for our customers. We should make user management, specifically around dormant users, easier so owners can focus their time on less arduous tasks and budgets overages are avoided. |
| Expansion of seat cost management through [non-billable role promotion management](https://gitlab.com/groups/gitlab-org/-/epics/12141) | - Users' roles are easily adjustable, which can have billable implications in some scenarios. Customers want the ability to manage a user's role to ensure it is not adjusting without the correct approvals. <br>- User caps intends to avoid having billable users > user cap, thus helping GitLab Admins/Owners control the costs of their subscription. Non-billable users don't contribute to billings, so they don't need to be controlled by the user caps feature to accomplish the goal of the feature. |
| Create feature to [block seat overages](https://gitlab.com/groups/gitlab-org/-/epics/12452) | Enables customers to manage their seat usage  |
|Evolve billing model with the [Seat Assignment Model](https://gitlab.com/groups/gitlab-org/-/epics/13684) | In our current billable model, when adding users to a group or project, they immediately consume a license/subscription seat based on the role they have. We are developing a plan for a Seat Assignment Model (SAM), whereby we allow group owners to assign members to a seat type, which in turn determines what roles they can have when being added to groups or projects. |

### Possible Future Opportunities

| What is the work to do? | Why are we considering doing it  |
|---------|--------|
| Make [user counts consistent](https://gitlab.com/groups/gitlab-org/-/epics/6330) | Our GitLab sales and support team members frequently get reports of User counts in self-managed and SaaS behaving in an unexpected manner and our goal is to improve the customer experience and user count visibility. |
| [Seat digest](https://gitlab.com/gitlab-org/fulfillment/meta/-/issues/1630) for users with QSRs | These customers are the ones who already get billed quarterly base on the same usage information we would be sending them in these e-mails. They are the ones who could benefit from seeing the digest in advance of the QSR as a way avoid surprise bills. |

### Prior Work

- [FY'25 Q1 Fulfillment OKRs](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/5573) (Not Public)
- [FY'25 Q2 Fulfillment OKRs](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/6895) (Not Public)
- [FY'25 Q3 Fulfillment OKRs](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/8268) (Not Public)

## Additional Information

### Q&A

| Question | Answer |
|---------|-------------|
| What type of customers does Utilization serve? | - SM & SaaS Self-service customers <br>- SM & SaaS (GitLab.com and Dedicated) Sales assisted customers <br>- SM & SaaS Channel Partners and their customers |
| What customer personas are Utilization solving for? | Our customers fit the [buyer persona](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/roles-personas/buyer-persona/) and may play a different role in the decision-making and purchasing process depending on their company size and their role. |
| What customer segment is Utilization focused on? | - For SMB and mid-market companies: [The application development manager](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/roles-personas/buyer-persona/#app-dev-avery) needs to have visibility into usage across their teams and be able to control usage in a way that fits their company preferences/processes/budget. <br> - For large or enterprise company: [The release and change management director](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/roles-personas/buyer-persona/#release-rory) is concerned with accurate billing and being able to make purchasing decisions based on usage information. |
| What internal teams does Utilization serve? | - [Support](https://handbook.gitlab.com/handbook/support/) <br>- [Customer Success](https://handbook.gitlab.com/handbook/customer-success/) <br>- [Sales](https://handbook.gitlab.com/handbook/sales/) |

### Key Links

- [Internal Handbook Page - Seat Cost Management](https://internal.gitlab.com/handbook/product/fulfillment/seat-cost-management/)
