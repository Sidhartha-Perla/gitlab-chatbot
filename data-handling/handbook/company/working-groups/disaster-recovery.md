---
title: "Disaster Recovery Working Group"
description: "The Disaster Recovery Working Group improves the disaster recovery mechanism for GitLab SaaS and Self-Hosted Products."
status: active
---

## Attributes

| Property       | Value                                                        |
| -------------- | ------------------------------------------------------------ |
| Date Restarted | August 1, 2022                                               |
| Date Created   | November 11, 2020                                            |
| End Date       | January 6, 2025 |
| Slack          | [#wg_disaster-recovery](https://gitlab.slack.com/archives/C01D6Q0DHAL) (only accessible from within the company) |
| Google Doc     | [Working Group Agenda](https://docs.google.com/document/d/1dLgmLlvET5WyWF0CpX5JUxiyQKyDzctocs7unwLueY8) (only accessible from within the company) |
| Overview & Status | [Internal Handbook](https://internal.gitlab.com/handbook/engineering/disaster-recovery/) |

### Scope and Definitions

In the context of this working group:

1. **Recovery Point Objective (RPO)**: maximum duration of time in which data might be lost due to an incident.
1. **Recovery Time Objective (RTO)**: maximum duration of time that a service is unavailable due to an incident.

### Goals

The working group exists to coordinate the delivery of cross-team efforts that improve both the values and the confidence in our RTO and RPO targets.

The exit criteria and target goals for the working group are defined [here](https://internal.gitlab.com/handbook/engineering/disaster-recovery/) in the internal handbook.

## Roles and Responsibilities

| Working Group Role     | Person                  | Title                                          |
|------------------------|-------------------------|------------------------------------------------|
| Facilitator/DRI        | Andras Horvath          | Engineering Manager, Gitaly                    |
| Product Management DRI | Mark Wood               | Senior Product Manager, Gitaly                 |
| Member                 | Gerardo Lopez-Fernandez | Engineering Fellow, Infrastructure             |
| Member                 | Chun Du                 | Director of Engineering, Enablement            |
| Member                 | Lucie Zhao              | Engineering Manager, Geo             |
| Member                 | Sampath Ranasinghe      | Senior Product Manager, Geo                    |
| Member                 | John Jarvis             | Staff SRE, Infrastructure                      |
| Member                 | Michele Bursi           | Engineering Manager, Delivery                  |
| Member                 | Sami Hiltunen           | Senior Backend Engineer, Gitaly                |
| Member                 | Joshua Lambert          | Director of Product Management, Enablement     |
| Member                 | Ahmad Sherif            | Senior SRE, Infrastructure                     |
| Member                 | Fabian Zimmer           | Director of Product Management, SaaS Platforms |
| Member                 | Nick Westbury           | Senior Software Engineer in Test, Geo          |

## Related Links

- [Backup and recovery of gitlab.com](/handbook/engineering/gitlab-com/policies/backup/)
- (internal handbook) [gitlab.com Disaster Recovery](https://internal.gitlab.com/handbook/engineering/disaster-recovery/) including RTO/RPO targets
- [GitLab Dedicated Disaster Recovery Plan](/handbook/engineering/infrastructure/team/gitlab-dedicated/slas/#disaster-recovery-plan)
- Followup: [Align on the Performance Indicator for Disaster Recovery capabilities for GitLab.com and GitLab Dedicated](https://gitlab.com/gitlab-com/gl-infra/mstaff/-/issues/397)
