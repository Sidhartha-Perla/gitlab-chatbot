---
title: "Terminus Email Experiences"
description: "Terminus Email Experiences is a marketing tool used as an advertising channel inside the inbox."
---

## Uses

Terminus Email Experiences is a marketing tool used as an advertising channel inside the inbox (formerly known as Sigster).

## Training & Help

1. [Knowledge base](https://resources.terminus.com/l/resources)
1. [Admin role training pt. 1 - Overview, features and integrations](https://drive.google.com/file/d/1boIfDvPnwXlBAxlLUupvnlHzNaP_Eru_/view?usp=sharing)
1. [Admin role training pt. 2 - Setting up a Terminus campaign](https://drive.google.com/file/d/1cy1jMwAUPvvGrEkajIN5JbtfZ1rdOF3t/view?usp=sharing)

## Employee preference center

If you would like to update the information in your signature, [simply login to Terminus Email Experiences](https://email2.terminusplatform.com/users/sign_in/) using your credentials. If you have any difficulty with this method, please post in `#mktgops` and we will send you an email to update your information.

## Account Settings

### Roles

Only `admin` users can create campaigns. Only the `acccount owner` can add `admin` users to the platform.

### Admin

From this tab you can view the account owners and admins, set company signature field defaults, set default UTM parameters, and change the default account time zone.

### Recipients

On this tab, you can define the email recipient domains who will receive any campaign designated as internal. This is currently set as `gitlab.com`.

### Transfer ownership

To transfer account ownership, the owner must login and navigate to `Account Settings` > `Ownership`. From this page, click the `Pick New Owner` drop down, select the person whom you will be transferring ownership to, then select `Transfer`.

### Security

Change password or view API keys for third-party integrations.

### Integrations

#### Salesforce

The [integration between Terminus Email Experiences and Salesforce](https://support.terminus.com/hc/en-us/articles/360051666254-Salesforce-Integration-for-Email-Experiences-Overview) allows marketers to:

1. Sync campaigns lists from Salesforce into Terminus Email Experiences for use in targeted campaigns
1. See which open and closed opportunities have been influenced and generated by campaigns
1. Track which email recipients click on a campaign and how often on an account and contact level

#### Outreach

Terminus Email Experiences appends campaign banners to Outreach signatures every 24 hours. If they are changed from Terminus, campaign banners in Outreach update in real-time. There must be an employee in Sigstr with an email address that matches the user or mailbox in Outreach in order for a campaign banner to be appended.

#### Gmail

##### Terminus Chrome Extension

1. Target individual accounts and contacts with personalized campaign content through targeted campaigns
1. Provides insight into who is engaging with your email campaigns and how often
1. Offers alternative campaign options for employees looking for more control of the content they share

**Instructions for install:**

1. Click this [link](https://chrome.google.com/webstore/detail/terminus-chrome-extension/ihgbenpajiikgfimgecpdloilhaolijd?hl=en)
1. Click `Add to Chrome`
1. Click `Add extension`
1. Ensure the extension is visible in your Chrome browser by clicking the puzzle icon in the top-right corner, navigate to `Terminus Chrome Extension`, and click the pin icon to pin it.
1. Once pinned in your browser, navigate to Gmail and do a hard refresh (Hold ⇧ Shift and click the Reload button. Or, hold down ⌘ Cmd and ⇧ Shift key and then press R.)
1. Compose a message then click the Terminus icon. Here you will see a list of available campaigns that you can switch out within Gmail for your purposes.

**Please note:** The campaigns you will see or not see depend on which employee group you are a part of and the settings of those particular campaigns. If a campaign has not been set up as an `Alternate` campaign, you will not see it in this view. Likewise, if you are part of a specific employee group or you are targeting an account or prospect that is part of a `Targeted` or `Sender` based campaign, your default banner would likely fall under those respective settings. **This extension applies to emails sent from Gmail only.**

#### PathFactory

Each campaign banner only points to one link. With PathFactory, you can use one link while providing additional content for the receipient to consume.

You can identify who clicks on your email signature banners and track content consumption using PathFactory. Using these insights you can optimize your email signature campaigns and content tracks, while simultaneously identifying highly engaged prospects.

To take the most advantage of this integration, pair your banner campaign with an equally targeted content track. This v1 integration allows Terminus to pass a visitor's email address to PathFactory whenever someone clicks on a banner. This means that anyone entering a content track from a banner will be identified in PathFactory analytics. When using this integration and sending an email with a banner to one recipient, when that recipient clicks on the banner Terminus will pass the recipient's email address to PathFactory. This allows PathFactory track the resulting session of the known individual. When there are multiple recipients of a single email Terminus handles identifying visitors differently depending on the scenario.

Here are three different possible scenarios:

- Scenario 1: You send an email to multiple people within one organization (all with the same @domain.com)
  - The visitor sessions will be listed as unique events, but the email address "somebody@domain.com" will be associated with each visitor session
  - The email address will actually say "somebody", and the @domain.com will be the domain you sent the email to
- Scenario 2: You send an email to one external person, and one or more internal people
  - The external recipient's email address will be associated with their session data
  - The internal recipients' email address will be listed in PathFactory as unique events from unknown traffic
- Scenario 3: You send an email to multiple people with different domains
  - Eg. tim@example.com, sarah@demo.com, and lisa@xyz.com
  - No email address will be passed to PathFactory, so the visitors' sessions will be listed as unknown traffic and will not have an associated email address

Read more about the partnership between PathFactory and Terminus [here](https://www.pathfactory.com/blog/sigstr-integration/).

##### Adding a PathFactory track to a banner

The demand generation and account-based marketing teams are primarily responsible for the campaigns that are created and used within Terimnus Email Experiences. In an effort to stay aligned with our go-to-market plan, please work with your approriate campaign manager to request a PathFactory track and/or Terminus campaign.

1. Follow the [normal procedure](#create-a-campaign) for creating a campaign.
1. Once you are at the step for adding a link to your banner, select the URL dropdown and choose `PathFactory Experience`.
1. From the pop-up window, select or search for your PathFactory track. Your PathFactory track should be fully QA'd and finalized before using in a Terminus campaign.

### Notifications

Select the type and frequency of system notifications from Terminus Email Experiences. Daily emails are sent every morning. Weekly emails are sent every Monday morning.

- **Engagement reports** - Emailed daily or weekly and show who has recently clicked a campaign banner. To opt in/out of your individual engagement report email, visit the employee preference center.
- **Install Reminders** - Send reminders to all employees who have yet to install their Terminus email signature. These reminders will be sent automatically based on the selected frequency until the user has successfully installed their signature.
- **Campaign Clicks** - Send real-time notifications to employees anytime someone clicks their Terminus campaign banners. These notifications include the date, time, and contact who clicked on the Campaign banner. Employees can opt out of these notifications by editing their profile. This will automatically enable Campaign Click Notifications for new employees added to Terminus Email Experiences in the future.
  - **Campaign Click Notification Blocklist** - Ignore clicks from some domains (for example, clicks from email security clients). Currently set up to ignore clicks in analytics from GitLab employees.

### Privacy & Data

#### Export Data Archive

Create an archive of a recipient's data from Terminus. The archive will be emailed within 1-2 business days.

#### Delete Individual Recipient Data

Request to delete a specific email recipient's data. This will delete the click and views recipient data and records if they are on a list. A confirmation email will be sent within 1-2 business days.

#### Data Retention

Configure your account to clear out Terminus' store of recipient data on regular intervals. This will delete the clicks and views of all affected recipients.

### Verify

Using [Verify](https://support.terminus.com/hc/en-us/articles/360051982014-Email-Experiences-Verify), you can troubleshoot the timing and personalization of Terminus campaigns.

1. Click the account avatar in the bottom right-hand corner and choose `Verify`.
1. Input the `Sender`, `Recipient`, and `Date of Send` to preview the matching campaign. For `Sender`, select a group or specific email address. For `Recipient`, select a recipient list or specific email address. Please note that the `Recipient` section only pertains to `Targeted` and `Internal Campaigns` while the `Date of Send` only pertains to `Scheduled Campaigns`.
1. The `Results` section details why the campaign was chosen.

## Best practices

1. [Campaign design guidelines](https://support.terminus.com/hc/en-us/articles/360052083613-Campaign-Design-Guidelines-for-Email-Experiences)
1. [Campaign use cases](https://support.terminus.com/hc/en-us/articles/360051319614-Campaign-Use-Cases-for-Email-Experiences)
1. [Campaign best practices](https://support.terminus.com/hc/en-us/articles/360052083593-Campaign-Best-Practices-for-Email-Experiences)
1. [GIF best practices](https://support.terminus.com/hc/en-us/articles/360052083633-GIF-Best-Practices-for-Email-Experiences)
1. [Internal use cases](https://support.terminus.com/hc/en-us/articles/360052083653-Internal-Use-Cases-for-Email-Experiences)
1. [Signature design guidelines](https://support.terminus.com/hc/en-us/articles/360052083413-Signature-Design-Guidelines-for-Email-Experiences)
1. [Signature best practices](https://support.terminus.com/hc/en-us/articles/360052083453-Signature-Best-Practices-for-Email-Experiences)

### Banner ad image dimensions

The image will be constrained to half the size to ensure high density of pixels. Use the same banner ad size for all campaigns.

- 900 wide x 240 pixels tall
- 8px radius corners
- `.png` or `.gif`

## Signatures

### Resources

1. [Signature management](https://support.terminus.com/hc/en-us/sections/360008737653-Signature-Management)

### Default fields

1. First name
1. Last name
1. Job title
1. Schedule a meeting URL
1. Mobile phone
1. Company URL
1. GitLab, Inc. physical address

## Campaigns

Campaigns created in Terminus Email Experiences should align to GTM motions and our current marketing plan. Anything outside of the plan including ad hoc campaigns or activities will need prior approval to ensure there are proper resources to support.

### Resources

1. [Campaign management](https://support.terminus.com/hc/en-us/sections/360008482073-Campaign-Management)

### Use cases

**Content**

1. Whitepapers and eBooks
1. Events & conferences
1. Case studies
1. Product Releases
1. Promotional video & teaser

**Targeted**

1. Region
1. Customer status
1. Persona
1. Industry
1. Past engagement
1. Opportunity stage

### Types

1. **Default** - Display a banner ad as a fallback if no other rules apply
1. **Sender** - Assign banner ads to one or more employee groups
1. **Targeted** - Target banner ads to lists of contacts or accounts
1. **Internal** - Promote internal initiatives and content to GitLab employees
1. **A/B test** - Test two different banner ads to determine a leading variant
1. **Alternate** - Provide employees with a banner ad they can subtitute on compose
1. **Shuffle** - Promote up to five banner ads each with their own unique URLs

### Create a campaign

Before creating a Terminus email campaign, you need to [request a banner ad](/handbook/marketing/inbound-marketing/#brand-and-design-issue-templates) from the brand and design team. All Terminus email banner ads should use the same dimensions (900 wide x 240 pixels tall; 8px radius corners) and be delivered in a `.png` or `.gif` format.

1. Select `Campaigns` from the side menu (flag icon).
1. Click the `Create Campaign` button in the top right.
1. Select your desired [campaign type](/handbook/marketing/marketing-operations/terminus-email-experiences/#types), name your campaign, and click `Get Started`. You are redirected to edit the campaign details.
1. Name your banner ad, enter alt text for the image, and upload the banner ad. All banner ads uploaded to Sigstr must have consistent dimensions to all other banners in our instance for consistency of output. Please follow [best practices](/handbook/marketing/marketing-operations/terminus-email-experiences/#best-practices).
1. Under `Clickthrough URL`, choose your desired link type (manual clickthrough URL, mailto, or PathFactory experience). Note that you must already have a finalized PathFactory URL before selecting `PathFactory Experience`.
1. Select the `UTM Parameters` drop down to add additional parameters for your campaign. If you do not enter additional parameters, the default parameters will be applied: `source=email_signature&medium=terminus&content=employee_email` Note that your campaign name became the default parameter for campaign. You also have the option of adding custom UTM parameters if desired. It is highly recommended that you apply UTM parameters to your campaigns to properly report success.

### Review and activate a campaign

1. On the left side of the campaign edit page, click `Review`. You can also select the `Next` button to accomplish this same action.
1. Verify the look of your campaign. Ensure that the banner image does not appear blurry. If it appears blurry, try reuploading the banner image. If you still experience issues, please create an issue in the marketing operations project.
1. Confirm the banner ad properties including the name, alt text, and clickthrough URL. Please test the URL to ensure it's working and that it leads to your desired location.
1. Choose your desired schedule for this campaign from the `Schedule` pane. You can choose to start the campaign immediately or at a later date/time. You can also set your campaign end date/time or let it run indefinitely.
1. If there is anything missing from your campaign, Terminus will show you in the `Activate` pane below `Verify` pane. Before you can activate a campaign, you must enter all required campaign attributes (banner ad, clickthrough URL).
1. Once finalized, click `Activate this Campaign`. You can also choose `Save Campaign & Exit` to save the campaign as a draft and activate at a later date.
