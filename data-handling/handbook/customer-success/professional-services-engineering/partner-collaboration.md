---
title: "Partner Collaboration"
description: "Learn how the GitLab Professional Services organization collaborates with Partners."
---

## Why Partners?

As the sales of GitLab increase, the demand for professional services will follow suit. To meet this demand we need to have an **elastic and on-demand bench of delivery resources**. Partner collaboration will also help to **prevent PSE Burnout** by allowing **PSEs to take lead roles** (e.g.architect, technical oversight, etc.). Finally, building relationships with partners allows the delivery team to **add Subject Matter Experts** as needed.

From a sales perspective, channel partners can help facilitate the initial licence deal and up-selling opportunities with customers whom they have an ongoing relationship.

## Partner Disambiguation

There are different types of relationships we can have with partners and its important to outline the distinctions :point_down:. Direct vs indirect is a reference to the way the services are sold - Direct means the partner sells direct to the customer, Indirect means GitLab sells services and the partner helps with execution.

|   | Partner Indirect (Staff Augmentation)  | Partner Indirect (Project Based)  | Partner Direct |
|---|---|---|---|
| Subcontracted to GitLab?  | Yes | Yes | No |
| Access  | Slack, www-gitlab-com, GDrive  | Slack, www-gitlab-com, GDrive | Partner Portal |
| Communication w. GitLab PS | Organic (see above row)  | Organic (see above row)  | Partner Help Desk  |
| Allowed to know of other Customers of GitLab PS?  | Yes | No | No |
| Can contribute back to practice automation?  | Yes | Yes | TBD  |

### Partner Direct

GitLab PS can and should help our partners be successful in delivering services for their (and by extension, our) customers. We can **provide guidance, examples and strategic advice**, including references to public documentation or blog posts that could help "un-stick" a partner in an engagement. If the partner needs **hands-on help**, however, we will need to **engage with the partner via an SOW** to ensure we have appropriate liability protections in place.

*Note: GitLab professional services is building out a means to field and respond to help desk questions from the channel partners who are not subcontracted with us (Jan/Feb 2021). More details to come as this process gets created.*

## Partner Indirect Collaboration Guidelines

- Partners (Indirect) (both flavors) should have access to any subgroup or project under [global practice development](https://gitlab.com/gitlab-com/customer-success/professional-services-group/global-practice-development)
- PSEs should be maintainers responsible for MR approval and Merging new code from other PSEs and Partners (Indirect)
- Code reviews should happen on all merge requests
- Access to customer and PS specific Slack channels
- **Partner Indirect can have access to AWS, Azure, GitLab Demo, etc.**
- For delivery work on a customer engagement:
  - Partner Indirect (Staff aug)
    - Access to all of the delivery journal issues in [PS Plan](https://gitlab.com/gitlab-com/customer-success/professional-services-group/ps-plan/-/issues_)
    - Access to the [global practice development](https://gitlab.com/gitlab-com/customer-success/professional-services-group/global-practice-development)  group with all automation collateral
  - Partner Indirect (project based)
    - Specific access to the customer delivery (? need to check with Melani)
    - Access at the lowest level under [global practice development](https://gitlab.com/gitlab-com/customer-success/professional-services-group/global-practice-development) to complete the customer project (as appropriate)

## Collaboration by Type of Service

### Implementation Services

- These services almost always involve actually building the infrastructure and configuring the GitLab components so maintaining a customer-free reference for IaC of configuration Automation tends to be harder
- [Evaluate](https://gitlab.com/gitlab-org/professional-services-automation/tools/utilities/evaluate) can be used by Partners (Indirect) (project based and staff aug).
- Partners (Direct) TBD
- As Partners (Indirect) deliver implementation services projects, they can use the [Implementation delivery kit](https://gitlab.com/gitlab-org/professional-services-automation/delivery-kits/implementation-delivery-kits/implementation-delivery-kit)
Make sure as you (and/or the partner) is delivering the implementation services, you contribute back to the delivery kit.

### Migration Services

- Any migration to gitlab.com requires PSE involvement due to needing admin tokens to create users on gitlab.com
- Partners (Indirect) (project based and staff aug) can use [Congregate](https://gitlab.com/gitlab-org/professional-services-automation/tools/migration/congregate) and supporting automation utilities.
- As partners start migration projects, they can use the [Migration Plan](https://docs.google.com/document/d/1w3srV4CZQbNMqqMymH0l1CJhY2g33-p2rkmNm8Be3Bk/template/preview) or the  [Migration Delivery Kit](https://gitlab.com/gitlab-org/professional-services-automation/delivery-kits/migration-delivery-kits) to help facilitate delivery discussions.
- When using [Congregate](https://gitlab.com/gitlab-org/professional-services-automation/tools/migration/congregate), you will need to deploy it somewhere. If you need to deploy it within the customer firewall, make sure any hot-fixes you make to migration services source code you port back to the migration services projects.

### Consulting Services

- Require discovery sessions to further define the problem space that customer is trying to solve
- Deliverable(s) for these services is
  - typically a written recommendation on how to solve the problem
  - *sometimes* proof of concept code customers can apply to their environment.
- All code developed for these services must NOT contain any customer information so we can reuse the project for future customers without reinventing the wheel.

## Employing Partner/Consultants

If the project requirements exceed the current capacity of the available resources then the professional services team may employ a Consultant to help deliver the project.  The following provides a checklist of items to process before and during the use of a subcontracted resource:

1. Partner Search
    - Share "sample PS Projects" with viable partners
        - [Advisory Project](https://docs.google.com/document/d/1KhADjTUOndaAev3dSLlRgyEJtBIT6wv_rr3aH5hsKKQ/edit?usp=sharing)
        - [Implementation Project](https://docs.google.com/document/d/13Mw-7uSSclfwm6JWcs8UrXM9SunX8ebIeIk-n9q9b6Y/edit?usp=sharing)
        - [Migration Project](https://docs.google.com/document/d/1OuCZqxZvjiPx2S0bFnX8tGgfBFWeg_gdifQWhdtTlAg/edit?usp=sharing)
        - Project Management Project (coming soon)
        - Training Project (coming soon)
    - Share "PSE Profiles" with viable partners
        - Advisory (Profile coming soon)
        - Implementation (Profile coming soon)
        - Migration (Profile coming soon)
        - Project Management (Profile coming soon)
        - Training (Profile coming soon)
    - Sr. Channel Solutions Mgr Creates Establish PS Partnership Issue where we track completion of all necessary paperwork. We also track creation & completion of company profiles in required systems & tools. Please see list below:
        - Review & Signing of Master Subcontracting & Training Agreement
        - Review & Signing of Data Privacy Addendum & SCCs
        - Partner Company Profile Creation in Procurement Tool (Coupa)
        - Partner Folder Created in Google Drive
        - Partner Profile Created in Partner Tracking Tool
        - Partner Channel Created in Slack

1. Partner Vetting
    - Sr. Channel Solutions Manager sends [Skills Matrix Form](https://docs.google.com/forms/d/e/1FAIpQLScxgCHtbuLl53HrzH55hTpXxCSCXeUDRo6uyM2YKxy9QHMI0w/viewform?usp=sf_link) for Consultant to complete prior to meetings with PS Team Members.
    - Sr. Channel Solutions Manager goes over with Partner Principal how consultants can record a 2-3 minute video demonstrating their soft skills & consultative skills.
    - Consultants must complete Soft Skills Course (upload their video to a google drive and share the link)
    - Sr. Channel Solutions Mgr / Director of PS reviews/approves Soft Skills Course submission
    - Sr. Channel Solutions Mgr confirms that consultants have completed the [PSE Certificaton](https://levelup.gitlab.com/learn/learning-path/gitlab-certified-services-engineer-professional-learning-path) (at minimum the Migration & PM certs)

1. Partner Onboarding
    - Partner principals requests consultants to register on [GitLab's Partner Portal](https://partners.gitlab.com).
        - GitLab Learn (Thought Industries)
            - [Migration](https://gitlab.edcast.com/pathways/gitlab-migration-services-engineer-pathway)
            - [Implementation](https://gitlab.edcast.com/pathways/gitlab-implementation-engineer-specialist-pathway)
            - Training
                - [GitLab Certified Security Speialist](https://gitlab.edcast.com/pathways/gitlab-certified-security-specialist-pathway-for-gitlab-part)
                - [GitLab Certified CI/CD Specialist](https://gitlab.edcast.com/pathways/gitlab-certified-ci-cd-specialist-pathway-for-gitlab-partner)
                - [GitLab Certified Associate Pathway](https://gitlab.edcast.com/pathways/gitlab-certified-associate-pathway-for-gitlab-partners)
                - [GitLab Certfied Project Management Specialist](https://gitlab.edcast.com/pathways/gitlab-certified-project-management-specialist-pathway-for-g-this)
        - PSE Consultant Onboarding
            - Project Coordinator to schedule 30-45 min technical deep-dive with a Senior PSE to ensure consultant right match for project.
            - Interview results captured in partner tracking sheet
            - Sr. PSE approval needed to move forward with onboarding
            - Sr. Channel Solutions Mgr. creates an Access Request for consultant to gain access to necessary systems & tools for them to complete their project.
            - Sr. Channel Solutions Mgr creates & assigns an Onboarding Issue to consultant. They also schedule a call with PS Ops Team to go over operaional tasks (including submitting project expenses (please see end of page for process)) & timesheet submission process.
            - Project Coordinator introduces Consultant to Project PM & kicks off Project.

        - Project Manager Onboarding
            - Consultant PM completes GitLab Certfied Project Management Specialist
            - Sr. Channel Solutions Mgr schedules 30 minute call with Director of PS or Sr. PM to ensure consultant is right fit for project. Approval is required to move forward with onboarding.
            - Sr. Channel Solutions Mgr. creates an Access Request for consultant to gain access to necessary systems & tools for them to complete their project.
            - Sr. Channel Solutions Mgr creates & assigns an Onboarding Issue to consultant. They also schedule a call with PS Ops Team to go over operaional tasks (including submitting project expenses (please see end of page for process)) & timesheet submission process.
            - Consultant must complete onboarding issue and mark onboarding issue as completed
            - Project Coordinator introduces Consultant to Project Team & kicks off Project.
    - Professional Services Operations Team Tasks
        - PS Ops Teams assigns an Onboarding Buddy
        - Onboarding Buddy will follow the Consultant throughout the project
        - PS Ops Team manages the Consultant onboarding journey.
            - Review all necessary operational tasks including timesheet submission.

### Partner Onboarding

- PS Ops Team sets Consultant up in Kantata
- PS Ops Team meets with Consultant to [review how to log time](/handbook/customer-success/professional-services-engineering/professional-services-operations), etc.
- PS Ops Team submits Access Request Issues
  - Requesting access to appropriate technical tools (hardware & software)
  - Requesting to add Consultant to appropriate slack channel(s)
  - PS GitLab Project Manager starts the project with the Consultant
- PS GitLab Project Manager tracks Consultant hours against SOW
- PS GitLab Project Manager keeps tabs on total burn vs. project burn to ensure Consultant can complete the project as per the terms of the SOW
- PS GitLab Project Manager raises risk of Change Order to PS Ops as appropriate
- Consultant holds weekly check-in outside of customer meetings, including with their onboarding buddy. *Consultant and PS Onboarding Buddy ensure clear communication (as Consultant have less access to slack).*

### Consulting Subcontractor Prime Partner Statement of Work (SOW) Process

Consulting subcontracting Prime SOWs include the terms and conditions, such as rates and dollar amount for a partner to deliver Consulting on GitLab's behalf. Each partner has a dollar amount specified on the Prime Partner SOW. After the funds are exhausted, a new Prime Partner SOW is generated. Each Prime Partner SOW has corresponding Coupa requisition and Work Authorization assignments.

The Consulting Subcontracting Prime Partner SOW references the Master Professional Services Agreement, so this agreement, along with a Data Processing Agreement, must also be fully executed.

Sr. Channel Solutions Manager is responsible for managing the relationship with our subcontracting partners.

**Process**

- Sr. Channel Solutions Manager and Project Coordinator verify that there is a fully executed Master Professional Services and Data Processing Agreements in place with the customer. Follow up with the PS Sr. Channel Solutions Manager if necessary.
- After a mutual agreement has been achieved for the partnership, the  Sr. Channel Solutions Manager sends an initial version of the Consulting Subcontracting Prime Partner SOW to the partner for review.
- If the partner makes redlines to the SOW, then the  Sr. Channel Solutions Manager works with GitLab's Legal team and the partner to receive a mutually agreed SOW.
- The  Sr. Channel Solutions Manager notifies the Project Coordinator of the partner Consulting subcontracting Prime Partner SOW initiation. The Project Coordinator will create a new checklist issue to be added to the PC Partner SOW Tracker board for tracking purposes.
- Upon receiving SOW mutual agreement between GitLab and the partner, the Sr. Channel Solutions Manager submits a legal case to add a legal stamp to the Prime Partner SOW.
- After receiving the legal stamped version of the Prime Partner SOW, the Sr Channel Solutions Manager sends it for GitLab and partner signature via DocuSign. Refer to this video for DocuSign basics.
- After receiving the fully executed SOW, the Project Coordinator follows the Zip process steps to submit a request and PO for the Prime Partner SOW.
- As the Prime Partner SOW is undergoing the signature and approval processes, the Project Coordinator will monitor the status and update the checklist issue on the PC Partner SOW Tracker board accordingly.
- After the SOW, Coupa req and PO are approved:
  - Project Coordinator saves a copy of the fully executed Prime Partner SOW in the partner SFDC account and the applicable partner Google drive folder.
  - Project Coordinator creates a partner and SOW-specific version of the Partner Invoicing SOW Consulting Funds Tracker within the applicable partner G-Drive folder.
  - Sr. Channel Solutions Manager sends a copy of the fully executed Prime Partner SOW to the partner.

### Partner Scheduling Process

The Partner Scheduling Process is as follows:

1. The Project Coordinator reviews the internal capacity first prior to outsourcing to our partners for project delivery.
2. Once it is determined that we need to have a partner staff a project, the Project Coordinator will tag the partner lead in the partner slack channel with the project information.
3. After the Project Coordinator works with the partner lead on an agreed project assignment, the Project Coordinator will send the work authorization form for the partner to review and execute via Docusign.
4. If the Partner Engineer is not vetted, the Project Coordinator will go through the partner vetting process outlined earlier.
5. If the Partner Engineer is vetted, the Project Coordinator will proceed and send the work authorization form.
6. The Project Coordinator will track the Work Authorizations against the funding on the Prime Partner SOW.

### Consulting Work Authorization Form

The Consulting subcontracting Prime Partner SOW includes a work authorization form. The work authorization form is used to contractually secure a partner engineers and trainers for a Consulting and Training delivery. One Consulting or Training project should be listed on the Consulting or Training Work Authorization form. The PS Operations Team will initiate the work authorization form for the partner.

- Work Authorization include, but not limited to:
        - Scope
        - Technical requirements
        - Background check/security clearance requirements
        - Hourly rate
        - Billing terms as determined in MSA, MPA or Sub-contracting Agreement
        - Dates of work completed
        - Travel and expenses (if on site required)

### Delivery Kits

Delivery kits are comprehensive packages of resources, tools, and documentation that partners can use to streamline the delivery of GitLab professional services. These kits include:

1. Project templates and checklists
2. Best practices and guidelines
3. Technical documentation

Partners have access to [Delivery Kits](https://gitlab.com/gitlab-org/professional-services-automation/delivery-kits). They are encouraged to use these kits as a starting point for their engagements.

Each kit is regularly updated by the GitLab Professional Services team to ensure partners have access to the latest methodologies and tools for successful service delivery.

### Time Sheet Submissions

Each week, the Partner will submit their timesheets into our PSA tool by the end of their business day.
Timesheets are due on the Friday of each week. It is imparative that all timesheets are submitted into the PSA tool weekly by the deadline!
Month end deadlines for timesheet submissions are posted in the partner slack channels at month end. Reminders are submitted mid-month as we lead up to the month-end deadline. If there are further questions, please reivew with Project Managers or the Operations team.

### Partner Monthly Invoicing

After each month end, our partners will submit their invoices for time spent on our projects into the Coupa Procurement System. The PC assigned will receive an email notification that there is an invoice waiting for approval.
Invoies should be submitted in Coupa on the first week each month for the previos month. For example, work performed between May 1-31 would be submitted in Coupa on the first week of June. If invoices are not submitted by the 15th of each month, the PS Operations Team will follow up with the Partner lead to ensure the invoices are submitted on time.

Invoices should be submitted in Coupa with the following details:

- Partner Name
- PO Number
- Dates of work performed
- Name of Consultant
- Name of Project
- Hours worked
- Hourly Rate
- Total

[See Example](/handbook/customer-success/professional-services-engineering/examples/partner_invoice_mockup.md)

There should be 1 invoice submitted each month for each partner, then have a line broken out for each project.
If there is a need to have multiple invoices submitted each month, then approval would need to be obtain from the Operations Manager

If additional support is needed, please, be sure to reach out in your partner slack channel.

Coupa Helpful Resources:

[Coupa Supplier Portal](/handbook/finance/procurement/coupa-faq/#where-can-i-find-more-information-on-the-coupa-supplier-portal)

[Coupa End Users Guide](/handbook/finance/procurement/coupa-faq/)

### Customer Project Onsite Travel

When a GitLab Partner Travels:

Before making a purchase of any type or booking travel for a customer project, be sure to obtain approval from your Project Manager or Project Coordinator. The Project Manager or Project Coordinator will provide the travel budget to the partner. Once the travel has incurred, the expenses should be submitted for invoicing through Coupa and include the following details:

- Expense report per this [template](https://docs.google.com/spreadsheets/d/1fSn1G4opUDpnmGlcd35Zi_Mks5zTFoeg03FP__Xghes/edit?usp=sharing) that includes a separate line item for each expense
- One PDF document to include receipts for each expense
- Guidelines for [Traveling](/handbook/finance/travel/#expenses-while-traveling)
- Expense [Guidelines](/handbook/finance/expenses/)

Expenses are to be invoiced in the month in which they have incurred

### Partner Offboarding

- PS Project Manager invites Consultant to Project Retrospective meeting (as appropriate)
- PS Project Manager submits an Access Request to:
- Remove the Consultant from the customer project slack channel
- Remove access to any project specific GitLab tools or development work spaced
- Ensure Consultant is not working on any other ongoing projects
