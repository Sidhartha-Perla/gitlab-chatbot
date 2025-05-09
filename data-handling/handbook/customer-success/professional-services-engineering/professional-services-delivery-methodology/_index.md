---
title: "Professional Services Delivery Methodology"
description: "Learn the processes and methodology that GitLab Professional Services uses to help ensure Customer Success."
---

- [What is the Professional Services Delivery Methodology (PSDM)](#what-is-the-professional-services-delivery-methodology-psdm)
- [Managing a Project in GitLab](#managing-a-project-in-gitlab)
- [Project Velocity and Iteration Scheduling](#project-velocity-and-iteration-scheduling)
- [Status Planning](#status-planning)
- [Status and Burndown Reporting](#status-and-burndown-reporting)
- [Mitigating Risk via RAID Board](#mitigating-risk-via-raid-board)
- [Internal Retrospective Guidelines](#internal-retrospective-guidelines)
- [Customer Retrospective Guidelines](#customer-retrospective-guidelines)
- [Guidelines for Iteration based PSDM](#guidelines-for-iteration-based-psdm)

## What is the Professional Services Delivery Methodology (PSDM)

The Professional Services Delivery Methodology (PSDM) is the guiding framework for Program and Project Delivery within GitLab. The goal is to ensure the PS Delivery team operates within a predictable timeframe against the Project scope while prioritizing Customer Success. This is achieved through:

- Using GitLab.com as the Single Source of Truth (SSOT)
- Following label guidelines for managing and reporting progress
- Identifying and mitigating risks
- Actioning/tracking improvements internally
- Implementing iterations based for Sprint/Iteration-based SOWs
- Utilizing enablement materials
- Applying fundamental Agile best practices

## Managing a Project in GitLab

GitLab serves as both a project management and collaboration platform for all Professional Services engagements. We utilize the following features/terminology within GitLab for project management:

Please reference the [GitLab best practices](./gitlab-best-practices/_index.md) when navigating GitLab.

For initial configuration of GitLab as a Project Management tool, see [the configuration guide](./cp/_index.md).

> **NOTE:** Any issues marked as "internal" are still visible to anyone who has "developer" access into the GitLab Collaboration project. This includes people outside of GitLab. It is recommended to use the Project's "Internal Epic" for confidential communications.

### Project Management Mapping in GitLab

| PM Term    | GitLab Definition |
| -------- | ------- |
| Group  | This is the landing page for the Customer project and serves as the single source of truth for Project Governance.    |
| Projects | If an engagement has more than one Workstream (or SOW), we will track these using multiple Projects. Change Order activities will be tracked against the original project (SOW).   |
| Boards    | Typically organized by labels or scoped labels to keep the team on track together. In some cases, the GitLab/Customer team may utilize multiple Boards across Projects.    |
| Epics    | Generally derived from Workstreams or "Activities" outlined in the SOW.    |
| Issues    | These are the atomic units of work that roll up into an Epic.    |
| Iterations    | Time-boxed (generally two-week) events that are reviewed during Agile ceremonies.      |
| Milestones    | Used to track progress against Project Phases    |
| Labels    | Used in various ways, with the most important applications being: </br> <ul><li>Managing progress during delivery using a left-to-right workflow</li><li>Managing prioritization</li><li>Organizing specific sub-categories of work</li><li>Tracking and mitigating risks</li></ul> |
| Weight | Indicates the size or level of effort of an issue. See [Good Estimation Techniques](./good-estimation-techniques/_index.md) for guidance on assigning weight    |

For additional clarity on mapping Agile terminology to GitLab, reference [this guide](./agile-to-gitlab-terminology/_index.md).

### Label Guidelines

Labels are the most effective way to generate reports around Projects and organize information according to the Project team's needs. While teams have flexibility to create labels that meet their specific project reporting requirements, there are established guidelines for label generation for internal use.

Our [CP (Customer Project) automation](./cp/_index.md) includes the following default labels:

- SOW-# or PO# - helps the GitLab team search for Projects within the Professional service Group
- PM name - helps the GitLab team sort by PM name
- PSD workflow (for issue board management)

Labels used for *Internal retrospectives & RAID tracking/reporting* can be found in the "Reporting throughout the Iteration" section below.

## Project Velocity and Iteration Scheduling

The [iteration schedule and cadence](./iteration-scheduling/_index.md) is first introduced in Iteration 0 and becomes part of the Engagement Charter within the GitLab Customer Project (Group). It is crucial that the Customer agrees to an Iteration Schedule as an output of the Customer Kickoff. However, this should be initially introduced and collaboratively developed with the Customer during the Stakeholder Planning meeting.

When working within an Iteration/Sprint schedule, there are five key components:

1. **Iteration Planning** - Setting goals and selecting work items for the iteration
2. **Daily Standup** - Brief synchronization meetings to share progress and identify blockers
3. **Backlog Refinement** - Clarifying, estimating, and prioritizing upcoming work
4. **Iteration Review** - Demonstrating completed work and collecting feedback
5. **Retrospective** - Reflecting on the process and identifying improvements

When not working within Iterations, it's still important to clearly communicate the project velocity to ensure consistent resource alignment. For example: "We anticipate working 40 hours/week for 5 weeks to perform a successful upgrade and seamless migration of 1000 users and 2000 projects from GitLab SaaS to Self-Managed for FedRAMP compliance." This is validated during the Stakeholder Planning meeting and Customer Kickoff.

## Status Planning

For Agile SOWs, the Program Manager / Project Manager provides strategic direction for the project, including the vision, product roadmap, release goals, and iteration objectives. The Program Manager / Project Manager is responsible for managing the product backlog by inserting, re-prioritizing, refining, or removing items as needed. This can occur at any time until the iteration scope is defined and committed to by the development team.

Please reference [Backlog Management](./backlog-management/_index.md) for guidance on estimation, backlog grooming, and preparation for Iteration Planning.

If the scope of work is more strictly defined within the SOW, the PM is expected to assess the impact of any changes and work with the Customer to either reprioritize or initiate the Change Order process.

## Status and Burndown Reporting 

### Who Updates What?

While the PM is responsible for preparing ceremonies, reporting status, and managing Issues, the GitLab PSE (Professional Services Engineer), TA (Technical Architect), and Customer team members are all expected to contribute to and update their assigned issues (tasks) within the Project board. This highlights the importance of establishing effective Working Agreements during Iteration 0.

Working asynchronously and remotely presents unique challenges. Ensuring that the Directly Responsible Individual (DRI) actively contributes to their assigned issues is vital to maintaining project velocity. This approach allows the PM to shield technical teams from distractions while enabling effective status roll-up.

Not every Project will follow a Sprint or Iteration cadence. However, status updates should be documented within GitLab and reported to the Customer on a weekly basis. It is recommended to use an Engagement Charter to direct stakeholders to weekly status updates, RAID logs, and other relevant project documentation.

**Status Report Examples:**

- [Engagement Charter Example](https://gitlab.com/gitlab-com/customer-success/professional-services-group/professional-services-delivery/gitlab-partner-collaboration/Ingram-Barge/SOW-3184/-/blob/main/engagement-charter.md?ref_type=heads)
- [Status Update Example 1](https://gitlab.com/groups/gitlab-com/customer-success/professional-services-group/professional-services-delivery/gitlab-professional-services/Delta/-/epics/1)
- [Status Update Example 2](https://gitlab.com/gitlab-com/customer-success/professional-services-group/professional-services-delivery/gitlab-professional-services/smartsheet/SOW-2163/-/issues/2)
- While the GitLab CP is the recommended platform for status reporting, if the Customer prefers a presentation format, please reference this [template](https://docs.google.com/presentation/d/1jSc5vAID3DMMwojyZnAnOT0aKY2UwDfH2Si-XxEHjLU/edit#slide=id.g2e5808acdbf_0_252).

### Project Burndown

While Kantata is the single source of truth for our Financial Management, we recommend PMs track the hourly and finanical burn seperately for additional auditing and progress against the progression of the Project. Templates can be found [here](https://drive.google.com/drive/folders/1SKUu-nVP8c1rt0VKv8-7U5Yfk_6CWBYe). It is required to track hourly/financial progress within the weekly status report

## Mitigating Risk via RAID Board

The RAID (Risks, Actions, Issues, and Decisions) framework serves as our single source of truth for project risk identification, management, and resolution. It provides several key benefits:

- Creates transparency for project stakeholders and leadership
- Enables proactive monitoring of projects with Yellow/Red health status
- Centralizes risk documentation and mitigation strategies

### Setting Up RAID

- The RAID board is automatically created when the PM initializes the CP template
- Rename the template to "RAID - [Customer Name] - [SOW/PO#]"
- While the PM is responsible for creating and managing the RAID, both internal team members and Customer representatives are encouraged to update it as challenges and mitigations evolve
- View an [Example RAID Log](https://gitlab.com/gitlab-com/customer-success/professional-services-group/professional-services-delivery/gitlab-professional-services/autozone/SOW-2464/-/boards/7689705?label_name[]=PS%20RAID%20Log)

### Reporting on Risk via RAID

When documenting a risk, follow these guidelines:

1. **Apply appropriate labels:**
   - "PS RAID Log" 
   - "PS Risk" 
   - "PSD Workflow::Not Started"

2. **Define severity using priority labels:**
   - "PS:: Priority High"
   - "PS:: Priority Medium" 
   - "PS:: Priority Low"

3. **Quantify impact in terms of:**
   - Timeline effects
   - Scope changes
   - Quality implications
   - Budget consequences

4. **Assign ownership:**
   - Designate a person responsible for accepting, mitigating, or resolving the Risk

5. **Detail mitigation plan:**
   - Document specific actions to lessen or eliminate the Risk

6. **Escalation process:**
   - Use the "Escalated" label for risks requiring immediate attention that impact project progress
   - Escalated items should be surfaced in the Professional Services Portfolio report

## Internal Retrospective Guidelines

The Internal Retrospective issue serves as an ongoing reflection mechanism throughout the project lifecycle, focusing on:

- Capturing team accomplishments and celebrations
- Documenting technical challenges and solutions
- Identifying process improvements
- Recording business development opportunities
- Building institutional knowledge for future engagements

Unlike the Customer Retrospective which occurs at project milestones and reviewed with the Customer, the Internal Retrospective serves as a way to capture improvements needed to improve our proceses and celebrate team wins

### Setting Up the Internal Retrospective

The Internal Retrospective is automatically created when the Customer EPIC is established:

1. **Location:**
   - The issue lives within the internal Customer EPIC
   - It should be linked in the internal Project Slack channel for easy access

2. **Template:**
   - Use the [latest template](https://gitlab.com/gitlab-com/customer-success/professional-services-group/ww-consulting/ps-plan/-/blob/master/.gitlab/issue_templates/project_retrospective.md?ref_type=heads) to ensure standardization
   - The PM should ensure the template is properly populated with project information

3. **Access:**
   - This is an internal-only issue - no customer access should be granted
   - All GitLab team members working on the project should have access

### Contributing to the Internal Retrospective

Team members should contribute to the Internal Retrospective throughout the project:

### What to Document

1. **Project Wins and Celebrations:**
   - Technical achievements
   - Customer praise and positive feedback
   - Team collaboration successes
   - Innovative solutions

2. **Lessons Learned:**
   - Technical challenges and how they were overcome
   - Process gaps and workarounds
   - Communication improvements
   - Tools and techniques that proved effective

3. **Opportunities for Improvement:**
   - Areas where processes could be streamlined
   - Documentation gaps
   - Training needs identified
   - Tool limitations

4. **Assets Created:**
   - Scripts and code snippets
   - Documentation templates
   - Configuration guidelines
   - Customer-specific solutions with reuse potential
   - Any Delivery Kit related updates

### How to Contribute

- **Ongoing Basis:** Team members should add comments to the issue as noteworthy events occur
- **Weekly Check:** The PM should encourage updates during weekly team meetings
- **Phase Transitions:** Special attention should be given to capturing learnings at the end of each project phase

### Finalizing the Internal Retrospective

At project completion, the PM should:

1. **Conduct a Final Session:**
   - Schedule a 30-60 minute Gitlab team retrospective call, inviting PS Practice team members
   - Review contributions and synthesize key learnings
   - Identify patterns and major takeaways

2. **Categorize Learnings:**
   - Apply appropriate labels to facilitate future searching:

3. **Create Follow-up Issues:**
   - Generate specific issues for action items
   - Assign owners for implementation
   - Set realistic timelines for completion

An example Internal Retrospective can be found [here](https://gitlab.com/gitlab-com/customer-success/professional-services-group/ww-consulting/ps-plan/-/issues/18060)]. The list of inflight and completed internal retros can be found in the "PS-Plan" Gitlab Project by searching within "Titles" and the text "Internal Retro".

### Knowledge Sharing

PS leadership regularly reviews retrospective data to:

- Identify common challenges across projects
- Recognize exceptional team performance
- Inform training and enablement priorities
- Update delivery kits and methodologies
- Shape future service offerings

### Best Practices

- Keep entries objective and solution-focused
- Include specific examples rather than generalizations
- Maintain a balance of positive observations and improvement opportunities
- Focus on systems and processes rather than individuals
- Quantify impact where possible (time saved, problems avoided, etc.)
- Suggest specific, actionable improvements

## Customer Retrospective Guidelines

The Customer Retrospective is a critical component of the Professional Services Delivery Methodology that provides structured feedback on the engagement alondside our Customers. It serves to:

- Capture the customer's perspective on the engagement
- Identify what went well and areas for improvement
- Document successes and challenges for future reference
- Strengthen the customer relationship through collaborative reflection
- Generate insights that can inform future engagements
- Encourage CSAT particpiation

### Setting Up the Customer Retrospective

The Customer Retrospective issue is automatically created when setting up the collaboration project:

1. **Initial Setup:**
   - Rename the template to "[Customer Name], [SOW/PO#]" when setting up the project CPR
   - The issue serves as a living document that both GitLab and Customer teams can contribute to throughout the engagement

2. **Ongoing Documentation:**
   - Much like the internal retrospective, encourage Customers to document feedback throughout the engagement
   - Regular updates help capture insights while they're fresh and relevant

### Conducting the Customer Retrospective

### Preparation

1. **Schedule the session:**
   - Plan a closure/retrospective meeting with the customer at the end of the PS engagement
   - Share the retrospective issue in the meeting agenda for team members to pre-fill before the session

2. **Encourage participation:**
   - Ask team members to add their initials before their feedback under each main section
   - If someone agrees with existing feedback, they should add their initials alongside the original contributor

### During the Session

The retrospective meeting should cover these key sections which are found in the issue template:

1. Attendees and Date
2. Summary of Services & Value Delivered
3. Final Burn Down Report
4. Retrospective Discussion
   - What went well
   - What could be improved
   - Lessons Learned
5. Feedback on PS processes or Methodology
6. Voice of the Customer

### Documenting and Following Up

After the retrospective session:

1. Finalize the document
2. Apply appropriate labels
3. Create action items
4. Share insights within #ps-internal

### Best Practices for Customer Retrospectives

- Keep the tone collaborative and constructive
- Focus on specific, actionable feedback
- Balance discussion of challenges with celebration of accomplishments
- Capture both technical and process-related insights
- Ensure customer's voice is prominently featured
- Document quotes and testimonials (with appropriate permissions)
- Use the retrospective to strengthen the customer relationship

### Additional Resources

- [Retrospective Facilitation Issue/Guide](https://gitlab.com/gitlab-com/customer-success/professional-services-group/professional-services-delivery/cpr_gitops/-/blob/main/cpr_gitops/issue_templates/retrospective.md)
- [Customer Survey Template](https://gitlab.gainsightcloud.com/v1/sites/survey/SurveyResponse?at=1I0025DXE6KKG8JCV1GWLAUNW5DYWBNMUL90)

## Guidelines for Iteration based PSDM

The full PSDM implementation with a complete Iteration schedule is required only when the Agile-specific SOW

- Exceeds 5 Iterations, or
- The engagement is planned to exceed two months

Please review the [archetype definitions](./archetype-definition/_index.md) to understand what constitutes a "large" Customer engagement.

Use the following guide when planning for Iteration 0:

|    | Projects > 5 Iterations (~9 weeks, incl. iteration 0) | Projects < 5 Iterations |
| -------- | ------- | ------- |
| Managed in GitLab as SSOT | Required | Required |
| Iteration 0 | Required | Required |
| Internal Retrospective tracking | Required | Required |
| RAID tracking | Required | Required |
| Backlog Refinement | Required | Only as needed |
| Daily Standup | Required (with customer-determined cadence) | Only if needed |
| Communication Plan | Required | Required |
| Iteration Planning | Required | Only as needed |
| Iteration Review (status report) | Required | Weekly Status at minimum |
| In-project Retrospectives | Required | Only if needed |

<!--
##### What Kind of Engagements is PSDM Suited For?

PSDM is intended to be used on the large, complex, customers ([see archetype definition](professional-services-delivery-methodology/archetype-definition/_index.md)) that are falling into one of two use case scenarios:

1. **_Large Scale Tool Adoption -_** scaling usage of GitLab across the organization (tool adoption use case), or are
2. **_DevSecOps Transformation -_** assisting customers with transformational activities (transformational use case)

Some characteristics for both use cases include:

* Large customers (Fortune 500)
* Committed to substantial investments in new technologies and personnel, as well as a deep commitment to change at all levels of the organization
* Considering tools adoption and digital transformation a strategic overhaul that seeks to maximize digital tools to improve performance, meet customer expectations, and innovate
* Trying to shorten cycle time, and increase time to market velocity
* Involving changes that **impact people, process, and technology**
* Have been sold on GitLab benefits
  * One platform
  * Simplification of the DIY toolchain and saving on license costs
  * Shift-left security
  * Enhanced developer experience

The difference between the _tool adoption use case_ and the _transformational use case_ lies in the complexity and breadth of the approach.

**Tool adoption** is frequently limited to a set number of users, departments, and work streams, making the application of the methodology more predictable. Tool adoption frequently are multi-workstream engagements that manage parallel efforts of SCM migration, CI/CD transition, Security tool consolidation and workforce enablement and training. This use case is _similar to traditional IT system rollouts_:

1. Install GitLab SM / configure SasS / configure Dedicated
2. Migrate source repositories and user data - in waves
3. Train user in groups
4. CI/CD transition - [DevSecOps Workshop](https://drive.google.com/file/d/1mZm_DiwPdtssFqBolrDqPooaH6kA5Y5u/view?usp=share_link), [CI/CD Workshop](https://drive.google.com/file/d/10RzC-e0fhvgKBRaoZlxEgUQc90Z_0IVR/view?usp=sharing), [DevSecOps App Transformation](https://drive.google.com/file/d/1TDJSVO9uvy4NqC6uksQsSc_sSgEcpacV/view?usp=drive_link), [CI/CD App Modernization](https://drive.google.com/file/d/1ib6-xhja3WJbV_46rU2iDF9I-4I8xo8M/view)
5. Security tool consolidation
6. [Training and Education](https://university.gitlab.com/)

**Transformational** activities frequently involve cross departmental analysis of cycle times, processes, technical architectures and _tying specific technical activities to desired business outcomes_ (see a simple definition for Digital Transformation [here](professional-services-delivery-methodology/digital-transformation/_index.md)). Transformations frequently _address business goals **and** technology adoption **and** adopting new ways of working in order to achieve step change improvements in **business performance**_. This necessitates transformational activities to be focused on:

1. People
2. Process
3. Technology
4. Continuous Improvement, and
5. Key Performance Indicators - [DORA metrics](https://docs.gitlab.com/ee/user/analytics/dora_metrics.html)

#### Key Principles

##### A Word about Terminology

Just like GitLab in general, Professional Services follows a light-weight, iterative, process. The goal is to be efficient and effective while minimizing administrative burden.

Most agile, iterative, process methodologies (such as Scrum, SAFe, or PMI-DA), define a set of terms and conventions. So does GitLab, and there is a [simple mapping of agile to GitLab terminology](professional-services-delivery-methodology/agile-to-gitlab-terminology/_index.md) that documents the differences while acknowledging that essentially their meaning is the same.

Because industry parlance and GitLab terminology only differ slightly (for example, the common industry standard term for a time-boxed development cycle is "sprint" or "iteration", whereas GitLab uses the term "milestone") PSDM uses some of the terminology interchangeably.

##### Principles

There are eight (8) key principles to make any GitLab engagement successful. These are generally acknowledged to be industry best practice, and customers that understand and fully embrace these principles are more likely to succeed. This is important for PS to stress with customers before and during engagements.

The key principles are:

1. [Optimize communication](professional-services-delivery-methodology/optimize-communication/_index.md) – especially focused on executive, buyer, and stakeholder alignment and addressing progress towards business outcomes
2. We iterate and work in Small Batches - with [work conducted according to a cadence and organized in backlogs and iterations / sprints](professional-services-delivery-methodology/cadence-backlog-sprints/_index.md)
3. Enable ownership and personal accountability
4. [Small Teams](professional-services-delivery-methodology/small-teams/_index.md) equal better and faster communication
5. Localized decision making – not in terms of geography but team organization
6. Allow for [continuous improvement / continuous learning](professional-services-delivery-methodology/retrospectives/_index.md)
7. Understand the customers' products, value streams and associated lead (wait) times - critical to optimizing cycle times and achieving business goals
8. Embrace a new way of thinking, planning, and budgeting - instead of waterfall upfront scheduling and budgeting, work through iterative, prioritized deliverables, against a fixed project budget

These principles underly a disciplined 11 step implementation approach.

#### 11 Steps to Success

It is important to point out that GitLab’s PSDM is agnostic to popular implementation and process methodologies and can seamlessly be applied regardless of what the specific customer circumstances are.The steps are:

 1. Identify, document, and conduct an engagement strategy based on the specific customer situation
 2. Build awareness and excitement at all levels - regularly communicate status to all relevant parties: executives, buyers, stakeholders
 3. Identify MVP pilot project(s) - [we always utilize one or more MVPs to prove out our engagement strategy](professional-services-delivery-methodology/mvp/_index.md)
 4. Train the customer development team(s)
 5. [Develop product backlog and estimates for the engagement](professional-services-delivery-methodology/cadence-backlog-sprints/_index.md)
 6. [Run iterations / sprints producing incremental value](professional-services-delivery-methodology/good-user-stories/_index.md)
 7. [Identify metrics - make data centric decisions](https://about.gitlab.com/solutions/value-stream-management/dora/)
 8. [Gather feedback and improve](professional-services-delivery-methodology/retrospectives/_index.md) – adjust the process
 9. Mature
10. Scale across other teams, programs, portfolios - scale in waves
11. Regularly Assess and Refine

It is recommended to encourage the customer to follow [GitLab Best Practices](professional-services-delivery-methodology/gitlab-best-practices/_index.md).

##### Iterative Basics

##### 1. Harden Implementation Success in MVP Pilot(s)

Each engagement will successfully deliver one or several [MVP pilot(s)](professional-services-delivery-methodology/mvp/_index.md) - depending on the size and complexity of the engagement.

MVP Pilot Phases of an engagement consist of:

1. [Discovery](professional-services-delivery-methodology/discovery/_index.md) - The initial phase to assess capabilities  and validate assumptions to ensure we’re **building the right thing and meeting customer needs**
2. [Team Readiness](professional-services-delivery-methodology/team-readiness/_index.md) - The process to define people, process and structures to **prepare teams operating in an iterative way**
3. [Sprint 0](professional-services-delivery-methodology/sprint0/_index.md) - The initial sprint where the **team aligns on norms and objectives, and key technology choices**
4. [Sprinting](professional-services-delivery-methodology/cadence-backlog-sprints/_index.md) - The execution and delivery process for teams to **deliver the GitLab engagement**

[Scaling](professional-services-delivery-methodology/scaling/_index.md) up across the organization is achieved by breaking down the overall implementation effort into waves that will be delivered successively - after successful delivery of one or several MVP pilot(s).

##### 2. Integrate Business and IT

Integrating business and IT needs is accomplished through a disciplined decomposition of higher level Vision and Goals into Epics and User Stories, which in turn drive the technical implementation of the customer engagement.Depending on the size and complexity of the engagement, one or several Program Managers are closely coordinating with executive level stakeholders and business sponsors in order to ensure that key business goals are achieved.Lower level technical coordination and tasking is done by one or several projects managers, working with the GitLab TA/PSE Team and the customer sourced Dev Team.

![IntegrateBizAndIT.jpg](/images/customer-success/professional-services-engineering/processes/IntegrateBizAndIT.jpg)

##### 3. Adopt GitLab's Consistent Tools

Helping customers adopt the GitLab platform across the entire software development life cycle delivery on two key promises:

1. Achieving significant license savings by replacing a complex DIY tool chain
2. Enabling productivity improvements due to an enhanced developer experience, streamlined collaboration, and reduced context switching

![GitLabPlatformOptimizesValueStream.jpg](/images/customer-success/professional-services-engineering/processes/GitLabPlatformOptimizesValueStream.jpg)

##### 4. Optimize Internal Controls

By optimizing and automating internal controls (sign-offs / approvals), cycle times are significantly reduced and Time to Market windows are shortened. Collaboration is streamlined, context switching is eliminated, and velocity is increased. Overall productivity increases.

 ![ValueStreamOptimization.jpg](/images/customer-success/professional-services-engineering/processes/ValueStreamOptimization.jpg)

##### 5. Establish Thought Leadership through Continuous Value Delivery and Cost Savings

* GitLab consultants are “catalysts” who show direction and provide coaching
* Focus is on setting up systems for people to work effectively
* Small, autonomous cross-functional teams deliver value constantly using GitLab, we live our values
* Teams are empowered to make decisions and are responsible for end-to-end outcomes
* Our engagements enable customers to conduct production deployments automatically without lengthy approval processes
* Cycle times are greatly reduced and value streams are more optimized
* Cost savings are achieved due to a simplified tool chain using the GitLab platform -->

<!-- ## PS Process & Methodology Mapped to the Customer Journey

The Professional Services process and methodology fits within the Customer journey that is supported by Customer Success.Professional Services contributes to the customer journey from the point of **SOW Close** through the **Project Closee** phase.

![!\[''\](/images/customer-success/professional-services-engineering/processes/customer-journey-mapped-ps-process.png)](<PS Delivery Customer Journey Flow - Page 1 (11).jpg>)

 [Source, GitLab Team Members Only](https://docs.google.com/presentation/d/1eC_ocJkzNkH4Vw3v4Vkd3S58a0NALYxXtnb6BZ7pJdc/edit?usp=sharing)

## PS Process Methodology Stages

The above diagram (slide 4) is meant to describe the Directly Responsible Individuals (DRIs), Activities, Outcomes, and Tools/Collateral for each stage of the methodology. We can also see clear categorization of stages in pre-sales and post-sales phases.

In the linked pages below, you can see a detailed drill down into the steps within each stage that individuals use to perform activities to deliver desired outcomes per each stage. These pages are split by the Phase of the selling process (Pre-sales vs Post-sales).

### Scoping (Pre-Sales)

For a more detailed explanation of the steps that comprise each stage of the scoping phase, check out the [Scoping (Pre-Sales)](pre-sales-methodology) page. In this page, we drill down into- and describe- specific steps in each phase of the pre-sales scoping process.

![Pre-Sales Stages & Steps](/images/customer-success/professional-services-engineering/processes/scoping-workflow.png)

### Delivery (Post-Sales)

For a more detailed explanation of the steps that comprise each stage of the delivery phase, check out the [Delivery (Post-Sales)](post-sales-methodology) page. In this page, we drill down into- and describe- specific steps in each phase of the post-sales delivery process.

![Post-Sales Stages & Steps](/images/customer-success/professional-services-engineering/processes/PS-delivery-workflow.png) -->

<!-- ---

title: "Go To Market (Pre-Sales)"
description: “Discover how GitLab Scopes Professional Services for customers who have requirements that fall outside the scope of the packaged services.”
---

## Overview

The purpose of this page is to document the sales-assisted selling motion used by Professional Services Engagement Managers and Regional Delivery Managers. If you're on a GitLab sales account team looking for information, try these pages on [positioning professional services](/handbook/customer-success/professional-services-engineering/positioning) or [selling professional services](/handbook/customer-success/professional-services-engineering/selling/#custom-scoped-services).

This page will help outline the when and how to get involved with positioning and scoping services, how to estimate, how to use SOW generation software, and the processes to gain approval.

> *Note: Services engagements can take [two forms](/handbook/customer-success/professional-services-engineering/selling). This will focus on the **custom SOW scoping** process, not the Standard SKU process.*

For custom SOWs, the [workflow for SOW creation](/handbook/customer-success/professional-services-engineering/selling/#custom-scoped-services) involves a partnership between the Account Team and the Professional Services Team.

![''](/images/customer-success/professional-services-engineering/processes/scoping-workflow.png)
[Source](https://docs.google.com/presentation/d/1TOI2aoseBoyWYQC6-xpJVMknEncCNreSFfMvOHO7EBA/edit#slide=id.gbfb62d0c00_0_58) (GitLab Team Members Only)

## 1. Positioning

- **DRI**: Account Team (SAE/AE, SA, CSM)
- **Supported By**: Engagement Manager

### MEDDPICC

Professional services can be positioned when a prospect becomes a customer (e.g. the Land of a new deal) or when an already existing customer is growing their staff or interesting in adopting new features of GitLab (e.g. expansion). The SA, SAE, AE, or CSM (e.g. "Account Team") is primarily responsible for this process, following the [Command of the Message](/handbook/sales/command-of-the-message/) and [MEDDPICC](/handbook/sales/meddppicc/) messaging frameworks.

For the larger, more strategic customers PS Engagement Managers tend to get involved earlier in the selling process to help with discovery and provide lessons learned on rollout from past engagements. For the medium sized customers, Engagement managers tend to get involved with account teams when the SFDC stage 4 (Proposal) is achieved.

### Customer Success Discovery

The Account team should be encouraged to use the [Customer Terrain Mapping templates](/handbook/customer-success/customer-terrain-mapping/#catalog-of-customer-terrain-mapping-engagements) to help the customer to start thinking about *how* they will achieve their longer term success. This typically results in conversations about services to aide them in their journey.

### Services Needed

Once its identified that the customer will likely want to engage with professional services, its the responsibility of the Account Team to [get in touch with the Engagement Manager](/handbook/customer-success/professional-services-engineering/engagement-mgmt/#how-to-contact-or-collaborate-with-us).

## 2. Scoping

- **DRI**: Engagement Manager
- **Supported By**: PS Practice, Account Team (SAE/AE, SA, CSM)

### Gather Data

After the [services calculator](https://services-calculator.gitlab.io/) is run by the Account Team, scoping issues and Project Scheduling Intake issues are automatically created and land in the [PS Plan](https://gitlab.com/gitlab-com/customer-success/professional-services-group/ps-plan/-/issues) Project. Using this customer scoping issue and Project Scheduling Intake issue, the engagement manager gathers data asynchronously from the account team. Questions about the potential engagement can sometimes be answered by the Account Team from the discovery that was done already. We want to make sure we avoid asking duplicate questions to the customer. In some cases when the account team cannot provide the level of detail to create an egagement, the EM will meet with the Account team and Customer to ask additional discovery questions to get to a level of detail needed. Once the data has been gathered, the EM will populate the answers to the Project Scheduling Intake issue.

### Create Engagement Estimate

A PS Engagement Estimate spreadsheet used for scoping services. The Engagement Manager uses the [PS engagement estimate spreadsheet](https://docs.google.com/spreadsheets/d/1wkmKhhGyLoxqWCXFtiI99tNgVaEJ-hTQJRwTOsU0j_Y/edit#gid=1815139260) to define the services in scope and estimate the amount of time for each activity. There is a catalog of activities in the [SOW generation automation](https://gitlab.com/services-calculator/services-calculator.gitlab.io) project or a list of services can be found at our [offerings framework](/handbook/customer-success/professional-services-engineering/framework) page.

### Iterate / Review Engagement Estimate

After the first iteration of building detail into the straw-man, the Engagement manager posts a request for review in the [professional services slack channel](/handbook/customer-success/professional-services-engineering/working-with/#slack) to the Account team. Often the Engagement Manager will get on a zoom call with the customer and provide context and gather feedback from the customer.

### Generate SOW

Once the Engagement Manager can get buy in from the account team and/or customer on the size and activities included in the services engagement, the [SOW generation automation](https://gitlab.com/services-calculator/services-calculator.gitlab.io) can be run using the straw-man as an input.  The engagement manager is responsible for running this automation which can be done by following the instructions on the readme in the above project.

### Iterate/Review SOW Data

Once the SOW is generated, it is ready for review by the account team. Iteration can occur here but should be minimized if the proper iteration was done on the Straw-man Steps.

### SOW Review/Approval

After one or more rounds of iteration on feedback from the account team, the SOW will be ready for Review and Approval by Sr. Director of Professional Services. The review processes are signaled in the [professional services slack channel](/handbook/customer-success/professional-services-engineering/working-with/#slack) and **at-mention** the GitLab engagement stakeholders.

## 3. Delivery Prep

- **DRI**: Project Manager
- **Supported By**: EM, PM, PSE, TA, Account Team

Once the engagement moves to stage 6, `awaiting signature` in salesforce, the engagement manager schedules an intro meeting between the PM and the customer stakeholder to discuss "how we manage projects at GitLab".  During this call, the PM will also discuss resource assignment, and scheduling details. Simultaneously, the PM will schedule an internal transition meeting with the EM, PM, PSE, TA, and Account Team to review the technical discussions that occurred during the customer scoping meetings.  This is a opportunity for the entire team to discuss and disclose the inner workings and dynamics of the customer project team.

### PM Introduction

Engagement managers introduce the PS Project Manager as they are in contract with the customer during the scoping exercise and are perfectly positioned to do so.

### Resource Identification

The PS Proejct Coodinator, working closely with the Regional Delivery Manager, will identify the best resource to deliver the project based on skillset, timezone, personality, tenure, and availability.

### Project Prep call

This is a call between the customer stakeholder and the PS Project Manager to discuss HOW we work.  Where we track project progress, what status report will look like, what the meeting cadence might be, a review of the contract terms that affect how we work such as minimum hours per week, expiration dates, delay language, and most importantly, how to achieve mutual agreement with the customer on a preliminary project schedule, prior to the kick-off call which includes the entire project team.

Check out the PS Delivery methodology to understand the details around pre-sales handoff to the delivery team, to ensure a successful relationship and productive engagement.

### 4. SOW Execution/Close

- **DRI** Engagement Manager
- **Supported By**: PS Leader, Sr. PSE, SAE/AE, Legal, Finance, Deal Desk

Finance Approval
The engagement manager can kick off the finance approval process in Salesforce. TODO: Add more details.

### Legal Approval

The Engagement Manager is responsible for creating a Legal Approval Case in Salesforce from the associated opportunity. This process often involves reviewing and accepting redlines from the customer and from our legal team. The source of truth for the latest SOW is managed in the SFDC legal case. The EM should coordinate who "holds the pen" to ensure we maintain version control of the SOW with the latest redlines.

### Customer Signature

Once the SOW has been approved by PS leadership, Legal and Revenue, the account team is owns the process of executing the SOW. They should take the approved SOW from the legal case and route it for signature with the customer.

### Deal Desk updates SFDC

Once the SOW is fully executed, the deal desk team updates the Salesforce PS-Only opportunity to `closed-won`.

### Journal Epic (Delivery Kit)

TODO: update this with documents and delivery kits that are organized to help the delivery team be successful with the engagement.

![''](/images/customer-success/professional-services-engineering/processes/PS-delivery-workflow.png) -->

<!--This page provides scoping questions designed to collect details and uncover the customer's required capabilities. This ensures alignment of the SOW and PS delivery with the positive business outcomes the customer is looking for.  While not an exhaustive list, these questions and suggestions will help spark the discovery conversations.

## Migration scoping questions
Migrations are one of the most complex types of services in any technical field.  Systems store data in a variety of ways that evolves.  Also, customers and users often use the same data model and system to represent completely different logical units to their teams.  To ensure a transition that meets the customer's needs, we want to make sure we understand their usage of their current systems.

### GitLab to GitLab scoping questions
The following questions are about bringing multiple GitLab instances together into a single "parent" instance:

1. How many instances need to be migrated together?
1. Breakdown of repositories per instance (and total git storage space)
1. Breakdown of users per instance
1. Breakdown of groups per instance
1. Breakdown of disk space per instance
1. Do any of the users use SSO (LDAP, SAML, etc.) to log in users?
1. What is the version of every GitLab instance involved?
1. What integrations are used on each instance?
1. For each instance, how is artifact, upload, container registry and Git LFS storage handled?

### SVN to Git scoping questions

SVN to Git Questions:

1. What is the structure of the SVN repos and subprojects? Do they follow the "standard" of:
    ```html
        Repository
            Project 1
                branches/trunks/tags
            Project 2
                branches/trunks/tags
    ```
    1. Any other variations? Example:
        ```html
            Trunk
                Project 1
                Project 2
            Tags
                tag name
                    Project 1
                    Project 2
            Branches
                Branch name
                    Project 1
                    Project 2
        ```
1. How many SVN repositories are there? How are they broken up?
1. What is the overall size of the SVN repos?
1. How much history (e.g. tags, branches, etc.) should be migrated?
1. Are any binary files stored in SVN?
1. How are you currently using SVN externals? Do you have some example use cases?
1. Which migration/conversion environment (local, VM, cloud) and OS (Windows, Linux, macOS) is preferred?

### GitLab self-managed to GitLab.com scoping questions

Self-Manged to GitLab.com questions:

1. How many repositories are there?
1. What is the average size of the repositories? What is the size of the largest repositories?
1. How many groups are there?
1. How many users?
1. Do we want the same structure of groups/projects/user access? Do we want it to be restructured?
1. Do you use other tools with GitLab. If so, which ones?
1. How are the runners currently set up?
  1. Where are they hosted?
  1. How many specific runners do you have and what are the details of these runners?
  1. Are you looking to make any changes to the runner strategy at your organization or will it stay the same?
1. GitLab.com uses SAML for authorization. What SAML tool would your organization be using?

## Implementation scoping questions
For scoping infrastructure implementation, we have several questions that can help us understand the scope. To get started, make a copy of the spreadsheet below and fill in the answers. If there are questions you want to add, ping the `@ps-team` in Slack channel #[professional-services](https://gitlab.slack.com/archives/CFRLYG77X). Then you can attach this document to the issue created by the [GitLab Services (SoW) Calculator](https://services-calculator.gitlab.io/).

[Implementation Infrastructure Scoping Questions](https://docs.google.com/spreadsheets/d/1TsCUNLuWdpX1V_dTn5MMXIUqnAYKm9Megu5MO9S8eGM/edit?usp=sharing)

**Note:** This document contains tabs for various public and private cloud providers - AWS, GCP, Azure, OpenShift and other on-prem deployments - you should only have to fill out the tab(s) relative to your customer.-->

<!--
title: "Post-Sales"
description: "Describes the workflow governing delivery of GitLab professional service projects."
---

## Overview

The purpose of this page is to describe the workflow governing delivery of professional service projects. We will start by outlining the general workflow that is common across all service delivery categories. Then we will describe the differences for engagements that do not fit the general workflow shown below.

![ps-delivery-workflow](/images/customer-success/professional-services-engineering/processes/PS-delivery-workflow.png)

[Source](https://docs.google.com/presentation/d/1TOI2aoseBoyWYQC6-xpJVMknEncCNreSFfMvOHO7EBA/edit?usp=sharing),  internal only

Update this below
GitLab professional services employs three different workflows that control projects for the following categories:  standard professional services, education, and dedicated engineers.  Each of these categories have unique attributes that warrant a different approach.

## 1. Pre-sales

_Note: for presales scoping and SOW signature, see the [pre-sales methodology page](/handbook/customer-success/professional-services-engineering/processes/pre-sales-methodology)*

### PS/EM Assessment

**TODO: Add content about what happens in this step**

## 2. PS Project Planning

### Resource Assignment

Resource assignment happens only after the SOW is received with Customer signature. The Sr. PS Operations team identifies delivery resources based on the needs of the engagement.

### Sales to PS Handoff

The Project Coordinator will schedule a handoff call with the account team (SAE/AE, SA, CSM), the EM who scoped the engagement, and the delivery team (PM, PSE, Trainer, Training Coordinator). The meeting will start with the EM and account team describing the customers high-level goals, current state, and desired business outcomes. The Account team should note what the growth potential is for this customer and their strategic plan to drive that growth. These topics give the context about the customer to the delivery team to understand where there might be follow on opportunities.

The EM will discuss in more detail the details of the engagement. The Delivery team will ask clarifying questions for what is in scope and what is out of scope. The PMs will review where the project definition document is stored, which is usually in the [Active Projects](https://drive.google.com/drive/u/0/folders/1ozPKiAlUzbKwpkscaYVTp9PVoi9hWm4U) folder under the Customer project.

**TODO: Add or link to content about what happens in this step. E.g. List link to the skills matrix,  Show example of skills requirements breakdown that come from a scoping issue, Link to the appropriate PS Operations handbook page to show the process in mavenlink**.

### Scheduling

The Professional Services (PS) team scheduling is processed through the Sr. PS Project Coordinator (PC).  Our PSA sytem calendar is our single source of truth for scheduing our customer and internal projects.

Follow these steps to schedule a customer engagement.

Submit a Resource Request through Mavenlink with the following details:

- Role
- Dates to be worked
- Hours requested
- Soft or Hard allocation

The PC will review the master planning for availability and procecss the resource request.  If there is a schedule conflict the PC will provide another set of project dates.

Scheduling updates and changes follow this same process with a resource request in Mavenlink.

If a customer project has not booked, but planning/scheduling discussions need to take place, reach out to the PC to review.

#### How to schedule internal time

There are 2 project that track internal time, Creditable and Non Creditable.  If hours need to be scheduled for the projects, a comment in the project activity and mention the PC:

- Requested Dates
- Hours requested
- Task assignment
- Soft or Hard allocation

## 3. Engagement Execution

#### Kickoff

See the details in the Project workflow section of the [PS Project Management](/handbook/customer-success/professional-services-engineering/project-mgmt/) page.

### Plan

**TODO: Add content about what happens in this step**

### Discovery

During discovery or fact finding sessions with the customer, PSEs will often have a predefined list of questions that need to be answered to ensure we're designing and building the appropriate solution given customer constraints and requirements. It is good practice to send these question to the customer prior to the discovery call so they can be prepared for the discussion.

During the call, take notes to ensure that things that have validated or invalidated your initial assumptions have been captured. At the end of the meeting, review the things you've learned to memorialize what will be designed and built. Reiterating back your understanding of the details of the agreement instills confidence in the customer representative that we understand their requirements and can deliver what was reviewed.

After the meeting, based on meeting notes, create issues in the gitlab.com customer collaboration project outlining the work. Include Consider using a simple template with `Overview`, `Open Questions`, `Tasks`, and `Acceptance Criteria`. These can be helpful in further memorializing the scope of work with the customer and getting asynchronous feedback to open questions. Make sure the `overview` is as detailed as possible, and the `tasks` section has build-to level tasks (e.g. update congregate list() function to include data from CI sources).

### Build/Validate

The build validation step is a bit vague on purpose because it depends on what was included in the scope of the engagement. The PSE can use the [delivery kits mapped to our service offerings](/handbook/customer-success/professional-services-engineering/framework/#service-offering-framework) which include templatized discovery documents, automation software to facilitate service delivery, and templatized deliverable documents. Most of the collateral will be modified and updated right from the delivery kits so this section is intentionally light on detail.

### Train

PSEs or Technical Instructors who deliver GitLab Education Services instructor-led courses can use the following workflow to ensure smooth interactions with customers. In addition, PSEs and Technical Instructors should complete these [GitLab Certified Trainer](/handbook/customer-success/professional-services-engineering/gitlab-certified-trainer-process/) steps for each course they are scheduled to deliver.

#### Preparation steps

1. The Project Coordinator will contact the customer with a "Welcome to Education Services Email" to initiate the training scheduling.  After the training dates and times are confirmed, the Project Coordinator will schedule a training session planning meeting. Trainer participation in this meeting is recommended -- please let the Project Coordinator know if you need the meeting to be rescheduled to ensure your attendance.

1. The Project Coordinator will use these [email communication templates](https://docs.google.com/document/d/1rJ9q9gEzsumRxDhoWEe45u70efmKA0eWNg69WONuCYs/edit?usp=sharing) to ensure communication of the key details with the customer and training participants.

1. During the training planning meeting, be sure to discuss and document all of the event logistics listed in the [Training Event Plan Template](https://docs.google.com/document/d/1huNauyfhFPvLCuo-9T7Ol3FtBDYowYxiP_T5ItP2FN4/edit?usp=sharing). The Project Coordinator will create a draft of the Training Event Plan prior to the meeting and update the document during the training planning meeting.
   - During the training planning meeting, the course outline and system requirements pages below are useful to use to review training logistics, topics, teleconferencing, and system requirements.
      - [GitLab with Git Fundamentals course outline](https://university.gitlab.com/pages/gitlab-fundamentals-training)
      - [GitLab CI/CD course outline](https://university.gitlab.com/pages/ci-cd-training)
      - [GitLab Agile Portfolio Management course outline](https://university.gitlab.com/pages/agile-training)
      - [GitLab Security Essentials course outline](https://university.gitlab.com/pages/security-training)
      - [GitLab System Administration course outline](https://university.gitlab.com/pages/system-admin-training)
      - [GitLab Duo Principles course outline](https://university.gitlab.com/pages/duo-training)
      - [System Requirements](https://university.gitlab.com/pages/gitlab-ilt-sysreq)

1. The Project Coordinator will set up a Zoom Meeting or Webinar session for each session using [these set up instructions](/handbook/customer-success/professional-services-engineering/remote-training-session-setup/) and add the registration link(s) to the issue. You will receive an email message with your unique link to join the Zoom Meeting or Webinar session. Make sure to locate the Zoom information within the email message and familiarize yourself with the Zoom functionality. Here is a useful Zoom article for [Managing Attendees and Panelists in a Webinar](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0063276). Depending on your Zoom set up, you may want to log into https://zoom.us, go to Join a Meeting, and enter the meeting ID/webinar ID to start the Zoom session.

1. At least 2 weeks prior to the training session, the Project Coordinator will email the session registration link(s) to the customer, asking them to send the link(s) to each of the employees whom they want to attend the session(s). When each person registers, they will receive an automated confirmation email with a Zoom Meeting or Webinar join link unique to each person, along with a link to add the session to their calendar.

1. The Project Coordinator will advise if a different teleconferencing system is being used for the training and provide additional details for accessing the teleconferencing meeting.

1. Contact the GitLab Education Services team to confirm you have the latest versions of course slides and other materials.

1. Review the train-the-trainer (T3) video for the course you are delivering.

1. Review and follow the [Instructor Pre-Training Checklist](/handbook/customer-success/professional-services-engineering/processes/delivery-checklists/) to ensure that you are properly prepared for your delivery.

1. Review, practice, and use these [PS Remote Training Tips and Tricks](/handbook/customer-success/professional-services-engineering/remote-training-tips/).

1. Complete the GitLab Training Lab set up steps below. Make sure that you review the lab exercises and ensure that the labs are working properly prior to the first day of class.

1. When it's time to join the teleconferencing as a presenter, use the provided information to join the session.

##### Training lab pre-course instructor workflow

PS uses the [GitLab Lab Environment](https://gitlabdemo.com/) as the standard environment for hands-on course lab activities and hands-on certification assessments. Follow these steps to set up your course attendees for lab access.

**1. GitLab Demo System invitation codes**

1. The Project Coordinator will generate the invitation code for your class and provide the invitation code information approximately a week prior to your class start date as part of the instructor friendly reminders post within your Kantata project.
1. Follow the instructions on the [GitLab Lab Environment Invitation Code Redemption handbook page](/handbook/customer-success/demo-systems/#invitation-code-redemption) to redeem the invitation code and access the lab environment.
1. For any edits/extensions/etc or any custom redemption rules (different durations than our standards), contact the GitLab Professional Services Operations team for assistance.

**2. Share the invitation code and access instructions with attendees**:

1. On the first day of class, share the invitation code and review the login process with the attendees. Also let them know the expiration date (which is 30 days from the date they generate the login).

#### Training Closeout

1. Review the [Instructor Post-Training Checklist](/handbook/customer-success/professional-services-engineering/processes/delivery-checklists/) to ensure that you have followed all of the steps to close out your training class.
1. The Project Coordinator will download the attendance report and send a close out email to the customer using an email template located in the [email communication templates](https://docs.google.com/document/d/1rJ9q9gEzsumRxDhoWEe45u70efmKA0eWNg69WONuCYs/edit?usp=sharing).

### Complete

For blended engagements, see the `Deploy & Close` section of our [project management page])(/handbook/customer-success/professional-services-engineering/project-mgmt/#project-workflow)

### Financial Closeout

**TODO: Add or link to content about what happens in this step**

## 4. Customer Success

### Retrospective

The project manager should schedule a retrospective at the end of the project. Invite the accout team (SAE, AE, CSM, SA), the delivery team (PSEs, trainers, Project Coordinators), Engagement Manager who scoped the engagement, and PS Leadership team.

The [Retrospective TEMPLATE](https://docs.google.com/document/d/1CXfnCzjF_hwapy0R-89txiFUmSmvX7jvlEqWn48zN8A/edit#heading=h.yqd5ghhhm2lh) can be used to capture notes during the meeting.

The Retrospective meeting should be run by someone that is not intimately familiar with the execution of the project (typically PS Practice Manager or Engagement Manager). During the meeting, encourage contributions into the notes doc in real time and offer for participants to verbalize their feedback.

Toward the end of the call, gather actions and assign owners to complete those actions.

### Project Go-live/Recap Document

At the end of a project the Project leader should document the customer value drives/positive business outcomes they were looking to accomplish, what PS delivered to help them accelerate their journey, and special thanks to the project team. A [template of this write up](https://docs.google.com/document/d/1U0rOXcSEsBFRITQzIKopIspkrldl804PK08cU4onoUU/edit#) be found in the PMO templates Google Drive folder. An example can be found [here](https://docs.google.com/document/d/1ltSU_2UBKovVE6y6MxG2aKImsnIwicbYjCBS385Zx0A/edit#heading=h.huf1p7y95gl9).

### Success Plan (CSM)

**TODO: Add or link to content about what happens in this step**

### Handoff (Support)

At the end of a small/medium sized projects or after the initial implementation phase of a large engagement, open a [support ops issue](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/organizations/-/issues/new) and add a link to the collaboration project architecture diagram that was deployed. The Support team will load it into a field in Zendesk to help them have context for customer support requests. -->
