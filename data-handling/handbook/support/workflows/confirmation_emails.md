---
title: Confirmation Emails
category: GitLab.com
subcategory: Accounts
description: "Workflow for cases when a customer reports they are not receiving their confirmation email"
---

## Overview

This workflow covers cases when a user says they are not receiving their confirmation email. The activation token in a confirmation email will only be valid for 24 hours. Thereafter, the user will need a new confirmation email.

## **Stage 0:** Ticket Triage

Before working the ticket ensure that it's correctly triaged with the `SaaS Account` form and `Did not receive confirmation email` problem type so that
the [SaaS Account Ticket Helper](/handbook/security/customer-support-operations/docs/zendesk/apps#gitlab-super-app) application can activate.

If the user has already correctly chosen the problem type, the automation will activate when an agent opens the ticket for the first time. If the SaaS Account Ticket Helper application fails to solve the issue for any reason, proceed to manually resolve it by going through the steps in the following sections.

## **Stage 1:** Locate Account

Before the issue can be resolved we first need to locate the account in question. This can be done by either checking the [GitLab User Lookup App](#method-1-check-gitlab-user-lookup-app) or by checking [GitLab Admin](#method-2-check-gitlab-admin).

### Method 1: Check GitLab User Lookup App

1. Click the `Apps` button located in the top right of the Zendesk interface, while viewing the ticket.
1. Scroll down to the `GitLab User Lookup` app.
1. Observe the results. Check if the app found an account associated with the username or email address provided by the user. If a result was returned for the username lookup only, go to the provided `Admin Link` and check what email address is listed on the account.
1. Proceed to Step 2 under Check GitLab Admin.

**If no account was found** use the Zendesk macro [`Support::SaaS::Gitlab.com::Account does not exist`](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/Account%20does%20not%20exist.md?ref_type=heads) or, if you believe it's applicable, use [`General::Verify account self-managed or .com`](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/macros/-/blob/master/macros/active/General/Verify%20account%20self-managed%20or%20.com.yaml) and then wait for a followup from the user.

### Method 2: Check GitLab Admin

1. In the GitLab.com Admin Area, [search for the user](https://gitlab.com/admin/users) by username to confirm the account exists. Alternatively, search in your browser using [the API](https://gitlab.com/api/v4/users?search=email@email.test) or [ChatOps](/handbook/support/workflows/chatops#user).
1. Check the email address against what the user has reported and then perform one of the following fixes:
    - They likely are not receiving their confirmation email due to a suppression. See 👉 [Stage 2: Fix](#stage-2-fix).

## **Stage 2:** Fix

Ensure the ticket has the correct:

- Form `SaaS Account`
- Category, such as `Cannot receive emails`
- Subcategory, such as `Cannot get confirmation emails`
- Impacted email address

Zendesk should automatically check for and remove a suppression if found.

The automation will send out an email to the customer letting them know whether there was a suppresion on their account or not and what next steps they can take.

### Typo Fix

As of 2023-08-07, unconfirmed users are [deleted after a set number of days](https://docs.gitlab.com/user/gitlab_com/#email-confirmation) on GitLab.com.

#### Free Users

Free users are required to wait for GitLab to automatically delete the account.

#### Paid Users

Paid users are recommended to wait for GitLab to automatically delete the account, however it is possible for Support to update the email address with manager approval if required.

### Manually remove a Suppression in Zendesk

1. Click the `Apps` button located in the top right of the Zendesk interface.
1. Scroll down to the `SaaS Account Ticket Helper` app located below the tag locker app.
1. Click the button for `Email Suppressions`.
1. Search for the email address using the search field.
1. If a suppression is found you may optionally click the `copy` button to save the log from Mailgun to your clipboard that you can then paste into an internal comment on the ticket.
1. Click the `Remove the suppression?` button.
1. Send the user a new confirmation email.

If this process doesn't work you'll need to remove the suppression in Mailgun. See 👉 [Removing a Suppression in Mailgun](#manually-remove-a-suppression-in-mailgun).

### Manually remove a Suppression in Mailgun

If the `SaaS Account Ticket Helper` doesn't work for any reason, we can remove suppressions in Mailgun directly:

1. Click on `Suppressions` along the left-hand side navigation bar.
1. Wait a moment for results to load before searching.
1. Ensure that `mg.gitlab.com` is set as the domain at the top of the page.
1. Enter the email address to be checked into the `Search for recipients` search bar and perform a search.
1. Click the `Delete` button next to an entry and then confirm your selection to remove the suppression.
1. Send the user a new confirmation email. See 👉 [Resend Confirmation Email](#stage-3-resend-confirmation-email).

## **Stage 3:** Resend Confirmation Email

### Primary email

Once the problem has been fixed, if the email is the primary email on the account, you can send the user a [new confirmation email](https://gitlab.com/users/confirmation/new). Afterwards, let the user know you've sent them a new confirmation email and ask them to check their inbox and spam folders.

>**Note:** If a user changes their primary email this will not work. See 👉 [Secondary Email](#secondary-email).

### Secondary email

Instruct the user to sign in and trigger a new confirmation email through their profile by visiting [https://gitlab.com/-/profile/emails](https://gitlab.com/-/profile/emails).

### Wacky State

If the user is unconfirmed, but their primary email address does not match the unconfirmed email address (see [this internal example](https://gitlab.com/gitlab-org/gitlab/-/issues/239098#note_399726260)), then there are two options to resolve:

1. Impersonate the user and click on the "Resend confirmation email" under Email on their Settings > Profile page.
1. File a [console escalation internal request](https://gitlab.com/gitlab-com/support/internal-requests/-/issues/new?issuable_template=GitLab.com%20Console%20Escalation) to set the `unconfirmed_email` to `nil`.

## Customers Portal account email

If the problem is with the customers portal account email, you can send the user a [new Customers Portal confirmation email](https://customers.gitlab.com/customers/confirmation/new). Afterwards, let the user know you've sent them a new confirmation email and ask them to check their inbox and spam folders.

## Extras

### Checking Mailgun logs

NOTE:
The `mg.gitlab.com` domain contains relevant data for Support troubleshooting. You will not see this list as a domain option in the drop-down on any pages. You must select the domain under Send > Sending > Domains. There is an email.mg.gitlab.com domain which appears by default, but will not work.

On the first attempt, if our email system could not get through (usually server says it's non-existent or similar), then our mail server will put a suppression on sending further emails.

This is useful to check if emails have been delivered successfully from our end, which could mean that the error is with the users' email provider.

1. Utilize the Mailgun SSO tile on your Okta dashboard to log in to [Mailgun](https://app.mailgun.com/app/dashboard).
1. Click on `Send` on the left-hand side navigation bar.
1. Click on `Sending` along the left-hand side navigation bar.
1. Click on `Logs`.
1. Ensure that `mg.gitlab.com` is set as the domain above the activity graph.
1. Enter the email address to be checked into the search bar, search, and then scan the results to see if mail is being delivered to that address.
    - If email is delayed, respond to the user and ask them to wait.
    - If email is bouncing due to a suppression (evidenced by the message `Not delivering to previously bounced address` in the log) proceed to [Removing a Suppression in Zendesk](#manually-remove-a-suppression-in-zendesk) or [Removing a Suppression in Mailgun](#manually-remove-a-suppression-in-mailgun).
    - If email is marked as `Delivered` and the response code under `delivery-status` is `"code": 250`, this indicates that the user's mail server acknowledged the receipt, and the email delivery was successful.

#### Using Mailgun's new log search

Mailgun has introduced a new search page, which they've announced [here](https://www.mailgun.com/blog/product/mailgun-announces-improvements-to-logs-feature-to-increase-visibility-into-deliverability-problems/). One can choose to use this new search by clicking the link in the info box labeled "Check out our new reporting logs experience with updated functionality here" at the top of the old search page, or one can find it here: https://app.mailgun.com/mg/reporting/logs. Note: this new search functionality may become the default search in the future.

Mailgun's new search functionality allows a support engineer to use filters to narrow down the search results. Usage of this new search will change the steps above slightly. Support engineers can also use the new search to perform more in-depth searches if needed - including searching for all messages sent to a specific domain. Here are the steps:

1. Utilize the Mailgun SSO tile on your Okta dashboard to log in to [Mailgun](https://app.mailgun.com/app/dashboard).
1. Click on `Send` on the left-hand side navigation bar.
1. Click on `Reporting`.
1. Click on `Logs`.
1. Choose a date range using the date range picker at the top of the `Controls` box.
1. Click the `Filters` button to the right of the date range picker.
1. Choose the filters you wish to use. To search for suppressions, use **To** and **Contains** as the source, then input the user's email address in the `Enter text` field and click the `Add` button. Then, click `Apply` at the bottom right.
    - If email is delayed, respond to the user and ask them to wait.
    - If email is bouncing due to a suppression (evidenced by the message `Not delivering to previously bounced address` in the log) proceed to [Removing a Suppression in Zendesk](#manually-remove-a-suppression-in-zendesk) or [Removing a Suppression in Mailgun](#manually-remove-a-suppression-in-mailgun).
    - If email is marked as `Delivered` and the response code under `delivery-status` is `"code": 250`, this indicates that the user's mail server acknowledged the receipt, and the email delivery was successful.

Support engineers can also choose to filter on **Status message**, **Status code**, and more. For example, a support engineer can choose to filter on **Status code** **Equals** "550" and **To** **Contains** "gmail.com" to find all undelivered messages to `@gmail.com` addresses that were rejected because the user's inbox doesn't exist.

### How to see or resend emails in Mailgun

This is to check the content of an email sent:

1. Follow the steps from the section [Checking Mailgun logs](#checking-mailgun-logs) to locate an email in Mailgun - The email subject must be "Verify your identity".
1. Access the log details by clicking on the dented wheel icon at the right end of the log entry.
1. In the log details, go to the third tab named "quick view" to display the full email.
![Mailgun email body](/images/support/workflows/assets/Mailgun_email_body.png)

To resend an email:

**Important note**: Any email resend to a **different** email address must be approved by a manager and performed after an ownership verification. *No approval or ownership verification is needed if you resend to the same email address.*

1. On the dented wheel icon at the right end of the log entry, click on the "Resend message" button.
1. From there you can enter an email address and press "Send".
![Mailgun resend email](/images/support/workflows/assets/Mailgun_resend_email.png)

### Identifying Multiple Suppressions on a Single Domain

Mailgun does not allow us to check for multiple suppressions on the same domain within it's `Suppressions` section, but we can use another method to find them without asking the customer for a list of email addresses that they suspect are being suppressed. To do so:

1. Utilize the Mailgun SSO app on your Okta dashboard to log in to [Mailgun](https://app.mailgun.com/app/dashboard).
1. Click on `Sending` along the left-hand side navigation bar.
1. Click on `Logs`.
1. Ensure that `mg.gitlab.com` is set as the domain above the activity graph.
1. In the search bar enter the customer's domain using `*` as a wildcard for the username.
1. Add a filter for `Event is Permanent Fail`.
1. Scan the results, any email address listed with a `Delivery Status Message` of  `Not delivering to previously bounced address` has been suppressed at one point in time.
1. Navigate to the `Suppressions` tab and enter in an email address from your previous search to confirm whether or not it's currently suppressed.

### Password reset on behalf of a user

When a user (free or paid) forgot the primary email of their account we are not able to disclose this information but we can send a password reset email on their behalf:

1. Take note of the primary email address of the account.
1. Open an incognito window.
1. Go to https://gitlab.com/users/password/new
1. Trigger the password reset with the user primary email address.
1. Optional - Go to Mailgun and check the email is delivered before going back to the user with the following:

> Due to our privacy policies I am unable to reveal what the primary email address is. That being said we have triggered a password reset for the account <username> just now, if you have access to the primary email address for this account you should see an email and be able to perform the password reset steps.
