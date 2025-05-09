---
title: Working with Sales
category: General
description: This page is about working with sales.
---

## General workflow

### 1. Respond to the customer on Zendesk

1. Assign the ticket to yourself.
1. Select the appropriate specific workflow to follow (see below).
1. Check the `Escalated to sales` box and set the ticket status to `Open`.
1. Set the ticket status to `Pending`.

#### If the account is owned by `AMER|EMEA|APAC SMB Sales User`

Inform the customer that they may email `smallbusiness@gitlab.com` directly to reach the account management team if they choose to.  See below for more information on contacting the SMB team internally when necessary.

Alternatively, if the ticket requestor is listed as a contact already in SFDC on the correct account, they can use the [Contact Sales form](https://about.gitlab.com/sales/) on the marketing website to contact the team directly as well

Using either the email address or the form will result in the creation of a Salesforce case.
***NB:** A Zendesk trigger will prevent a ticket from being set to `Pending` when an agent made an internal note instead of a public comment. It will set the ticket back to `Open` when that happens. So if you check the `Escalated to sales` box and set the ticket status to `Pending`, it will be reverted to status `Open`. Saving a second time as `Pending` will also work.*

### 2. Leave a message for the Salesforce `Account Owner` on Chatter with the relevant details

#### If the Salesforce account has a named `Account Owner`

1. Consider adding the following note in the Chatter message:

 > Please note that according to the "Working with Sales workflow" (<https://handbook.gitlab.com/handbook/support/license-and-renewals/workflows/working_with_sales/>) we expect a reply from you on this chatter within 24 hours (excluding weekend, Family and Friends Day & global holidays) stating when/if you will contact the customer.

1. Share the link to the Chatter message (right-click on timestamp) in an internal note on the ticket.

- Note that you can only link to the original Chatter message, not to any of its comments.

1. You may want to check the account owner's Slack status to see if they're
 currently taking time off work.
1. If reaching out to the account owner on Slack (always on `#support_to_sales_escalation`
 and always *as a courtesy*), link them the Chatter message and ask them to
 respond there.

***NB:** Support should be able to rely on the Salesforce `Account Owner` field to determine who is responsible for the account. If that is incorrect, escalate it **immediately**.*

#### If the Salesforce `Account Owner` is `AMER|EMEA|APJ SMB Sales User`

- Follow this [process](/handbook/sales/commercial/high_velocity_sales_first_orders/#working-with-the-global-digital-smb-account-team) to create a case, OR
Slack message the #hvs_public channel.
  - Once a case is created, it will be picked up by an SMB Advocate.  Once picked up, the SMB Adovate will drop a note in the Zendesk ticket advising that the request is being actioned.
  - The case can then be tracked by viewing the `Case Status` field, and `Case Next Steps` field.
  - Support Cases, and their current status, can be viewed on the SFDC account, or via this [SFDC Report](https://gitlab.my.salesforce.com/00OPL000000toc5).

- If the Support Engineer does not have Salesforce access, post a message in the [**#global-digital-smb_public**](https://gitlab.enterprise.slack.com/archives/C06H72XGQUD) slack channel.
- In your post, include:
  - details of the request
  - the Zendesk ticket link
- Note: Chattering the group or creating a slack post, instead of creating a Salesforce case, will result in a delayed response.  Chatters and slack messages can also not be tracked.

##### If the Salesforce `Account Owner` is not a person and is not `<@AMER|@EMEA|@APAC> SMB Sales` User

1. Find the person in charge of the [sales segment](/handbook/sales/field-operations/gtm-resources/#segmentation)
  and [sales territory](https://internal.gitlab.com/handbook/sales/sales-operations/#territory-management) and mention them in a Chatter comment. In your post, include:
    - details of the request
    - the Zendesk ticket link
1. If anyone you reach out to does not respond within 24 hours (excluding weekend, Family and Friends Day & global holidays):

### 3. When someone from Sales confirms that they'll be in touch with the customer

1. Post an update to the ticket, mentioning:
    - The name of the person who will be in touch
    - That we will follow up in 2 business days to check with the customer as to whether they've been contacted by Sales, and that we will escalate at that time if necessary
1. Set the ticket status to `Pending`.

*(Pro tip: create a personal ticket view where "Escalated to Sales" = checked, to pull these out into their own queue)*

### 4. Escalation procedure

**Before escalating consider checking the "Activity" section of the account's Salesforce page to see if someone has reached out to the customer. If you see activity since your first chatter, consider confirming status with the customer or the sales rep instead of escalating.** To confirm with Sales, just reply to the original chatter asking them whether they reached out. If you see no activity since you started the chatter, escalate as described below.

### If the Salesforce `Account Owner` is incorrect or unable/unwilling to assist

- Examples of being unable/unwilling to assist:
  - Account owner no longer works at GitLab.
  - Account owner says the account is not theirs any more.
  - Account owner says they have no time to help.
  - A reasonable amount of time has passed (> 24hrs) with no response

#### If the Salesforce account has a named `Account Owner`

- Mention the person's direct manager in a Chatter comment.
  - Suggested message text:
      > Following the "Working with Sales workflow" (<https://handbook.gitlab.com/handbook/support/license-and-renewals/workflows/working_with_sales/>) I'm escalating this, as we haven't heard from <account owner\> within the agreed upon time.
      >
1. From VP level onwards, mention them in a Slack message in `#support_to_sales_escalation` in addition to a Chatter comment.
    - Suggested message text in Chatter:
      > Following the "Working with Sales workflow" (<https://handbook.gitlab.com/handbook/support/license-and-renewals/workflows/working_with_sales/>) I'm escalating this, as we haven't heard from <account owner\> nor <account owner's manager\> within the agreed upon time.
    - Suggested message text in Slack:
      > Following the "Working with Sales workflow" I'm escalating support ticket <https://gitlab.zendesk.com/agent/tickets/><ticket number\> as we haven't heard from <account owner\> nor <account owner's manager\> within the agreed upon time.
1. Repeat as necessary every 24 hours and go one step up the reporting line, going all the way up to CEO if necessary.
    - It is helpful to refer to the [company organization chart](https://comp-calculator.gitlab.net/org_chart)
   to see who to escalate to.

#### If the Salesforce `Account Owner` is `AMER|EMEA|APAC SMB Sales User`

- If you have SFDC access to the case, and the case has an assigned owner
  - Ping the case owner in chatter on the case
  - Include the applicable Regional manager:
    - EMEA: @Miguel Nunes
    - AMER/ APAC: @Taylor Lund
  - notify your regional [L&R DRI](/handbook/support/license-and-renewals/#support-management-contacts) in [#support_licensing-subscription](https://gitlab.enterprise.slack.com/archives/C018C623KBJ) for awareness.
- If you do not have SFDC access, or the case is not owned
  - Post a message in the [**#global-digital-smb_public**](https://gitlab.enterprise.slack.com/archives/C06H72XGQUD) slack channel.
  - In your post, include:
    - details of the request
    - the Zendesk ticket link
    - cc: your regional [L&R DRI](/handbook/support/license-and-renewals/#support-management-contacts) in your post for awareness.
- If you are unable to make contact with the Regional manager within a reasonable amount of time, escalate to: @Mike Smith via chatter on the case and notify your regional [L&R DRI](/handbook/support/license-and-renewals/#support-management-contacts) in [#support_licensing-subscription](https://gitlab.enterprise.slack.com/archives/C018C623KBJ) for awareness.

## Determining whether **to pass** or **to NOT pass** to Sales

Please see specific workflows below:

Pass to Sales:

- The customer wants to pay via a method that isn't credit card
- The customer had a sales-assisted purchase last year and wants to purchase on an order form (company requires a quote or purchase order)
- The purchase needs to happen via a reseller (reseller or end user contacts us)

DO NOT pass to Sales:

- The customer wants to upgrade their SaaS or self-managed plan - they can use the upgrade button in the customers portal.
- Don't escalate until you understand what the customer needs
- The customer is trying to reach sales person to renew, but haven't received a response - Instead ask customer what they need assistance with and see if we can assist.
- The customer asks a product or process question (we can answer this or put in another Support queue most of the time)
- The customer has renewed, but they didn't add enough users - ask the customer to use the Add more seats button in customers portal.
- The customer wants to renew for less seats than their current subscription. The customer can renew for a minimum of their current usage or more. If they want to renew for less seats, they have to bring their seat usage down before the renewal, [disable automatic renewal](https://docs.gitlab.com/subscriptions/gitlab_com/#enable-or-disable-automatic-subscription-renewal) and manually renew the subscription (for [SaaS](https://docs.gitlab.com/subscriptions/gitlab_com/#renew-or-change-a-gitlab-saas-subscription) and [Self-Managed](https://docs.gitlab.com/subscriptions/self_managed/#renew-a-subscription)).

NB, Sales does not simply waive trueups, there is an approval process for exceptional cases. Please don't set the expectation that any fees will be waived. When in doubt, ask in Slack for a second opinion.

## Support responsibilities regarding True-Up waiver requests

In situations involving True-Up waiver requests, L&R Support can:

- Help customers and/or sales identify if a True-Up overage has occurred.
- Generate a requested license based on what the subscription allows.
- Generate a temporary license or subscription until a True-Up waiver request is resolved.

L&R Support cannot:

- Provide an in-depth explanation as why an overage has occurred, support can only collate the data that proves whether an overage has occurred or not.
- Provide detailed analysis on the nature of the overage (e.g. confirm if overage accounts were logged into or not, confirm how and when accounts were created or provide a timeline of the duration of any overages, etc.)
- Be the arbiter for whether a True-Up can be waived or not; this is the responsibility of Sales as detailed in [waived true-ups policy and approval requirements](/handbook/sales/field-operations/order-processing/#waived-true-ups-policy-and-approval-requirements).

## Specific workflows to pass to Sales

Many of the following workflows advise you to `Chatter Sales`.  How to do this
is described in the [expired license](/handbook/support/workflows/sla_and_views#handling-customers-with-incorrect-expired-support)
process.

The following workflows use the [Pass to Sales Zendesk macro](https://gitlab.zendesk.com/agent/admin/macros/360025924680)
unless otherwise stated.

### Customer wishes to use alternative payment method

A customer wishes to pay via method other than credit card

Workflow:

- Confirm the paymemt method the customer wishes to use (wire, ACH or check)
- Chatter Sales and summarise the customer's request, ask for them to reach out
- Respond to the customer with the appropriate macro

### Purchase Orders and Quotes

A customer wants to pay and has a PO or requires a paper quote or invoice

Workflow:

- Find the existing opportunity or subscription (if renewal)
- Chatter Sales and summarise the customer's request, ask for them to reach out
- Respond to the customer with the appropriate macro

### A reseller (or reseller customer) wants to change their subscription or ask a question

A reseller or reseller customer wants to make changes to their subscription or follow up on an order

Workflow:

- Confirm the end-user and the reseller, by finding the account in Zuora
- Chatter Sales and summarise the customer's request, provide the reseller and end-user information, ask for them to reach out
- Respond to the customer with the appropriate macro

### Customer seeking a discount

A customer is seeking a discount and their subscription is above the Starter tier

Workflow:

- Confirm their tier and the details of the discount requested, if they are not above Starter or the discount request is unreasonable (use your discretion), explain that a discount is not available
- If you are unsure whether a discount should be given, consult with the Account Owner first
- Chatter Sales and summarise the customer's request, ask for them to reach out if they confirm a discount is possible
- Respond to the customer with the appropriate macro, set the expectation that a discount is not guaranteed and is at the discretion of the relevant approvers

### Product transfer between SaaS and Self-Managed

A customer wishes to transfer from SaaS to Self-managed or vice versa

Workflow:

- If the current subscription is close to its end date, advise the customer to let it expire and purchase a new subscription
- If the current subscription is close to its start date, ask billing if a refund would be possible. If they say yes, seek confirmation from the customer that we can cancel and refund their current subscription so that they can purchase a new subscription with the correct product type
- If neither of the above is an option, Chatter Sales and summarise the customer's request, specifying how many seats are needed for the new product, ask for them to reach out with a quote for the transfer
- Respond to the customer with the appropriate macro

**DOWNGRADE PLAN** - a customer wishes to downgrade from their current tier to a different tier (same product)

Workflow: Ask in Slack for advice on the best solution for the situation you are dealing with.

**SaaS - DOWNGRADE PLAN TO FREE**

Follow the workflow in the `Downgrading to a free plan` section of the [Handling trials, extensions, and plan changes on GitLab.com](/handbook/support/license-and-renewals/workflows/saas/trials_and_plan_change) page.
