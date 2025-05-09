---
title: "HVS-FO Data and Ops Team at GitLab"
description: "The HVS-FO Data and Ops Team is responsible for leveraging data to optimize for the self-service customer experience and drive nARR growth via sales efficiency. Data insights from this team feed: sales visibility, self-service fulfillment features, and growth/marketing experiments. The HVS-FO Data and Ops Team also aims to create data tools to help with efficiency, prioritization, and decision making."
---

<link rel="stylesheet" type="text/css" href="/stylesheets/biztech.css" />

## Welcome to the HVS-FO Data and Ops Team Handbook

{{% alert color="success" %}}
The HVS-FO Data and Ops Team is responsible for leveraging data to optimize for the self-service customer experience and drive nARR growth via sales efficiency. Data insights from this team feed: sales visibility, self-service fulfillment features, and growth/marketing experiments. The HVS-FO Data and Ops Team also aims to create data tools to help with efficiency, prioritization, and decision making.
{{% /alert %}}

## Team

|  **Name** | **GitLab Handle** | **Title** |
| :--------------- | :----------------- | :----------------- |
| Max Fleisher | @mfleisher | Sr. Mgr, HVS Data and Operations |
| Sara Gladchun | @sglad | Sr. Analyst, HVS Data |
| Ed Lu | @eclu94 | Sr. Analyst, HVS Operations |

## Who We Work With

**HVS-FO Team** - We partner with the overall HVS-FO team to provide data insight and operational support to drive nARR and growth through sales efficiency and strategy.

**Central Data Team** - We work with the central data team by staying involved in cross functional data initiatives, collaborating where possible, and providing feedback on data models and the data that live in Snowflake. We also work with the data science team by staying up to date on their projects and models and incorporate many of their predictive outputs into our analyses and triggers,

**Product Analytics** - We work with product analytics by staying up to date on what major projects they are working on and by leveraging many of their models in our own data work.

**Fulfillment** - We work with fulfillment to provide data around self service fulfillment features and feature requests.

**Marketing Analytics** - We partner with Marketing Analytics to provide data around FO Funnels as well as targeted digital outreach to the Pooled Account customers.

## Resources

### General

|  **Resource** | **About** |
| :--------------- | :----------------- |
| [Data Request Issue Template](https://gitlab.com/gitlab-com/sales-team/hvs/-/issues/new?description_template=Data_Question_Intake) | Template that should be used for ad-hoc data questions and requests |
| [Data Hub](https://docs.google.com/document/d/10p86n7f5vt4UmhHM4ZGRZm4OSa5k5g-LKQ0uBAKnvSc/edit?usp=sharing) | All of our data assets and resources in one place |

### OKRs

- [FY26](https://docs.google.com/spreadsheets/d/1i9yYZKZVJ-OimjoF-Ip_SbA2hlqqhYfoag2m71wqs1M/edit?gid=1461447719#gid=1461447719)

<!-- ### Quarterly Prioritization List

- [FY23-Q4](https://gitlab.com/groups/gitlab-com/sales-team/-/epics/61)
- [FY24-Q1](https://gitlab.com/groups/gitlab-com/sales-team/-/epics/66)
- [FY24-Q2](https://gitlab.com/groups/gitlab-com/sales-team/-/epics/66)
- [FY24-Q3](https://gitlab.com/groups/gitlab-com/sales-team/-/epics/66) -->

## Working with us

**Purpose**: Outline how the broader Self-Service team can engage the Self-Service Data Squad (Max, Sara)

**Goal**: Minimize dependencies/blockers to insights while providing transparent engagement model

**Disclaimer**: Not all data questions will be able to be answered. Ultimately, taking time to answer ad-hoc questions means less time on projects (aka the zero-sum capacity problem). That is not to say that ad-hoc questions are not important; however, we do have "boulder" level projects in flight have been prioritized via the OKR process, which we also need to make progress on.

**How to submit your ad-hoc data request or question**:

1. Have you tried to answer this question leveraging existing resources (e.g. data hub, SFDC)?

   - If no, please try to answer your question using these existing resources.
   - If yes, but you're still unable to answer your question, go to question 2.

2. Using the Data Question Intake issue template in [our project](https://gitlab.com/gitlab-com/sales-team/hvs/-/issues/new?description_template=Data_Question_Intake), please:

- Fill out all items under the "Filled out by Requestor" section
- Add the "Self-Service Data" and "Self-Service Data Ad Hoc" labels
- If business stopping: tag Max in Slack (ideally in #hvs) with link to issue.

<!-- ## How we prioritize ad hoc requests
The more points the better!

1. Can this question be incorporated into existing OKR? If yes, +3
2. Ease of ability to answer question (+0 = 8+ hours; +1 = 4-8 hours; +2 = 2-3 hours; +3 = 1 hour or less)
3. Priority (High = +3, Medium = +2, Low = +1)
4. Is an c-suite member asking for this? If yes, +2

If an ad-hoc request scores north of 7 points, we will re-consider prioritizing it above existing OKR work. -->

## SSOT Queries

SSOT data is necessary in order to have confidence in our metrics, have repeatable and replicable reporting, and for our data team to work more efficiently. We have created a [GitLab repo](https://gitlab.com/gitlab-com/sales-team/self-service/-/tree/main/SSOT%20Queries) to house our SSOT SQL queries for both our foundational [base queries](https://gitlab.com/gitlab-com/sales-team/self-service/-/tree/main/SSOT%20Queries/Base_Queries) and for [ad hoc analyses](https://gitlab.com/gitlab-com/sales-team/self-service/-/tree/main/SSOT%20Queries/Ad_Hoc_Analyses).

This allows us to keep a record of queries used for foundational projects like our dashboards and for one off analyses that may need to be repeated, tweaked, or modified in the future.
Dashboard queries are also housed in Sisense as snippets in order for the data team to work more efficiently within the BI tool. We are currently updating these queries to work within Tableau as well.

**The current workflow for creating or updating snippets and SSOT queries is the following**:

1. Create or update the query and ensure it produces the desired results and accurate data
2. Update the query in the SSOT Queries directory and commit to a new branch
3. Create an MR and tag another Data Team member as a reviewer
4. The reviewer will review the code and merge the MR to update the query
5. Once MR is approved and merged, the original author will either update the snippet in Sisense (original author must also update the date in the comments with the most recent date updated)

**Tableau Data Source Workflow (WIP - New Data Source)**:

1. Create query using Snowflake worksheet to produce desired output
2. Create new Data Source in Tableau Desktop from Snowflake
3. Copy query into SSOT Repo to save work and track changes
4. Copy query as Custom SQL into Tableau and set to Extract
5. Run Extract and check data integrity and accuracy
6. Commit any necessary changes to the Repo
7. Once the query is finalized:
        - Publish Data Source to Server
        - CRITICAL - Data Source must be published to the Development -> Sales -> SAFE folder
        - Embed Snowflake credentials to allow for refresh

**Updating a published Tableau Data Source**:

1. Log into Tableau Server
2. Locate the Data Source in My Content or in the folder above
3. Select Edit Data Source
4. Use Snowflake worksheet to test any changes to the stored query
5. Commit changes to the Repo
6. Copy new query into the Data Source Custom SQL
7. Run the extract
8. Publish the updated Data Source
