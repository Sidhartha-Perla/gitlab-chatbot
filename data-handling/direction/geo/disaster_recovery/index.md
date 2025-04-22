---
layout: markdown_page
title: "Category Strategy - Disaster Recovery"
description: "GitLab wants disaster recovery to be robust and easy to use for systems administrators - especially in a potentially stressful recovery situation. Learn more!"
canonical_path: "/direction/geo/disaster_recovery/"
---

- TOC
{:toc}

## 🚨 Disaster Recovery

|Section | Group | Maturity | Last updated|
|--------|-------|------|------|
|[Enablement](https://about.gitlab.com/direction/enablement/) | [Geo](https://about.gitlab.com/direction/geo/)|  [](/direction/#maturity)  | 2024-07-02   |

Thanks for visiting this category strategy page for GitLab Geo Disaster Recovery. This page belongs to the [Geo group](https://handbook.gitlab.com/handbook/product/categories/#geo-group).

### Overview

GitLab is part of the business critical infrastructure for many of our customers. As such, it is important our customers are able to rapidly and safely recover their GitLab instance from a disaster. We built Geo Disaster Recovery for exactly this purpose.

Geo Disaster Recovery (DR) helps our customers fulfill their business continuity plans by creating processes that allow the recovery of a GitLab instance following a natural or human-created disaster.

It all starts with a well-designed, well-tested, and well-practiced DR plan that will minimize the business impact of a catastrophic event. Two key metrics for disaster recovery are Recovery Time Objective (RTO) and Recovery Point Objective (RPO). These two metrics determine the maximum acceptable time your application can be offline and the maximum length of time data might be lost from your application respectively. Companies strive for both of these metrics to be small as possible. Geo Disaster Recovery was built to help customers minimize both of these metrics by providing an easily configurable warm standby (Geo site) in an additional region, which can quickly take over in the event the services at the primary site are interrupted.

It is important that customers can recover all of their core GitLab data in the event of a disaster. Therefore, Geo replication and verification support for GitLab-generated data is part of the [definition of done](https://docs.gitlab.com/ee/development/contributing/merge_request_workflow.html#definition-of-done). This ensures that new features ship with Geo support and our customers are not exposed to data loss. Today Geo replicates and verifies 100% GitLab core data.

You can read more about how we started this journey in our blog post, [How we built GitLab Geo](https://about.gitlab.com/blog/2018/09/14/how-we-built-gitlab-geo/)

The Geo team will be splitting our time between DR and backup restore feature development during calendar year 2025. While we will be working on new DR features, we will be operating at lower capacity during this period.


#### How you can help

Please reach out to Sampath Ranasinghe, Product Manager for the Geo group ([Email](mailto:sranasinghe@gitlab.com)) if you'd like to provide feedback or ask any questions related to this product category.

This strategy is a work in progress, and everyone can contribute. Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=group%3A%3Ageo&label_name[]=Category%3ADisaster%20Recovery) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=group%3A%3Ageo&label_name[]=Category%3ADisaster%20Recovery) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.

#### Useful resources

- [Roadmap for Disaster Recovery](https://gitlab.com/groups/gitlab-org/-/roadmap?state=all&sort=start_date_asc&layout=MONTHS&timeframe_range_type=CURRENT_YEAR&label_name%5B%5D=group%3A%3Ageo&label_name%5B%5D=Category%3ADisaster+Recovery&progress=COUNT&show_progress=true&show_milestones=false&milestones_type=ALL)
- [Maturity: ](/direction/#maturity)
- [Documentation](https://docs.gitlab.com/ee/administration/geo/disaster_recovery/)
- [Lovable Maturity epic](https://gitlab.com/groups/gitlab-org/-/epics/4988)
- [All Epics](https://gitlab.com/groups/gitlab-org/-/epics?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=group%3A%3Ageo&label_name[]=Category%3ADisaster%20Recovery)

### Vision

We envision a disaster recovery solution that our customers can rely on to restore the full operational capability of GitLab in the event of a catastrophe and one that they can repeatedly exercise without fear of losing their data. A solution that makes the actual experience of failing over to warm standby sites seamless and uneventful both for the systems administrator and the end users.

A robust disaster recovery plan needs to be regularly tested and adjusted as necessary. Testing both the process and the infrastructure is essential to ensuring a successful recovery in the event of a disaster. Regular testing will expose weaknesses that can be addressed under controlled circumstances. Geo Disaster Recovery will allow customers to perform routine controlled failovers without data loss.

The solution will perform an autonomous failover to a designated secondary site under limited circumstances, relying on specific trigger events that indicate a problem with the primary site. The failover will be seamless and transparent to the end users. CI runners will automatically register with the new primary and restore a fully operational GitLab instance. This will reduce the monitoring burden on the system administrators by allowing the GitLab solution to self-heal.

System administrators will be notified of irregularities in the replication and verification processes asynchronously via push notifications such as email and Slack messages alerting them to potential data loss if a failover were to happen. System administrators can follow the information in the notifications to investigate and remediate the issues.

The solution will support all current and future GitLab [reference architectures](https://docs.gitlab.com/ee/administration/reference_architectures/).

GitLab customers will be able to scale and tailor the Geo Disaster Recovery solution to best fit their business continuity plans. They will be able to configure the disaster recovery solution to meet a defined RTO and RPO.

All GitLab SaaS services such as GitLab Dedicated and GitLab.com will be protected by Geo Disaster Recovery to ensure that all best practices are followed and that we dogfood our own solutions.

### Target audience and experience

#### [Sidney - (Systems Administrator)](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)

- 🙂 **Minimal** - Sidney can manually configure a DR solution using Geo sites.
  More complex configurations, such as HA, are supported but are highly manual
  to set up. Some data may not be replicated. Failovers are manual.
- 😊 **Viable** - Sidney can follow a set of clearly defined procedures for
  planned failovers. DR is available for all reference architectures; some data
  may not be replicated yet.
- 😁 **Complete** - All Git and File data is replicated and verified. A dashboard informs users
  of the current data replication and verification status. A recovery process is less than <10 steps.
- 😍 **Lovable** - Automatic failovers are supported and it's possible to initiate a planned failover using the UI.

For more information on how we use personas and roles at GitLab, please
[click here](https://handbook.gitlab.com/handbook/product/personas/).

### In a year

#### Simplifying Promotion of Secondary Sites

It is possible to promote a secondary site to a primary site, either during a planned failover or in a genuine disaster recovery situation. Geo supports promotion for a single node installation and for a high-availability (HA) configuration. The current promotion process consists of a large number of manual preflight checks, followed by the actual promotion. The promotion is only possible in the command line; no UI flow is possible and for high-availability configurations modifications to the `gitlab.rb` file are required on almost all nodes. Given the critical nature of this process, Geo should make it [simple to promote a secondary](https://gitlab.com/groups/gitlab-org/-/epics/3131), especially for more complex high-availability configurations.

#### Simplify Demotion of Primary Sites

After a failover, an administrator may want to re-attach the demoted primary site back as a secondary site in order to failback to the original primary at some point. This is currently possible. However, the process is highly manual and not well-documented. After we have simplified the promotion process, we want to [simplify demoting a secondary site](https://gitlab.com/groups/gitlab-org/-/epics/2153) site of any size by reducing the steps required and making the process easily automatable.


#### Improve observability

[Improving observability](https://gitlab.com/groups/gitlab-org/-/epics/8240) of replication and verification operations will allow systems administrators to monitor the health of the warm standby secondary sites. It will help identify any fault conditions in the replication and verification process and aid in the remediation of these faults. By surfacing the underlying errors in the UI, it will provide easy access to this information and speed up recovery actions needed on the part of the systems administrators.

#### Enable Geo on GitLab.com for Disaster Recovery

GitLab.com is by far the largest GitLab instance and is used by GitLab to [dogfood GitLab itself](https://handbook.gitlab.com/handbook/engineering/index.html#dogfooding). GitLab.com does not use GitLab Geo for DR purposes. This has many disadvantages and the Geo Team is [working with Infrastructure to enable Geo on GitLab.com](https://about.gitlab.com/company/team/structure/working-groups/disaster-recovery/).

### What's Next & Why

#### Publish metrics dashboard

The Geo admin dashboard provides a basic overview of the status of the Geo sites. This is helpful when setting up Geo and for confirming Geo status at a glance. However, it does not show long term trends and historical statistics. A [Grafana](https://docs.gitlab.com/ee/administration/monitoring/performance/grafana_configuration.html) dashboard together with [Prometheus](https://docs.gitlab.com/ee/administration/monitoring/prometheus/) metrics serves this purpose well.

Geo publishes an extensive list of [prometheus metrics](https://docs.gitlab.com/ee/administration/monitoring/prometheus/gitlab_metrics.html). [Publishing a Grafana dashboard](https://gitlab.com/gitlab-org/gitlab/-/issues/197147) would make these metrics more accessible and useful for systems administrators.

### What is not planned right now

We currently don't plan to replace PostgreSQL with a different database e.g. CockroachDB.

We currently don't plan to support an Active/Active configuration.

### Maturity plan

This category is currently at the 
maturity level, and our next maturity target is lovable (see our [definitions of maturity levels](/direction/#maturity)).

In order to move this category from  
to lovable we are working on all items in the [lovable maturity epic](https://gitlab.com/groups/gitlab-org/-/epics/4988).

### Metrics

We currently track:

- [The total number of replication events(Internal link)](https://app.periscopedata.com/app/gitlab/500159/Enablement::Geo-Metrics?widget=10278011&udv=0), which scales with the overall amount of data and our ability to replicate more data types.

### Competitive landscape

GitHub Enterprise Server 2.22 supports a [passive replica server](https://docs.github.com/en/enterprise-server@2.22/admin/enterprise-management/configuring-high-availability-replication-for-a-cluster) that can be used for disaster recovery purposes.

### Top customer success/sales issue(s)

- [Geo: Create a single command that can be run on any node to promote a secondary to primary](https://gitlab.com/groups/gitlab-org/-/epics/3341)
- [GitLab Environment Toolkit: Add ability to perform Geo failover for Hybrid architectures](https://gitlab.com/gitlab-org/gitlab-environment-toolkit/-/issues/133)

### Top user issues

- [Category issues listed by popularity](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=group%3A%3Ageo&label_name[]=Category%3ADisaster%20Recovery)

### Top internal customer issues/epics

- [Geo for DR on GitLab.com](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/12)

### Top strategy item(s)

- [Verify all blob replicators](https://gitlab.com/groups/gitlab-org/-/epics/5285)
- [Geo: Promoting a secondary should be simple](https://gitlab.com/groups/gitlab-org/-/epics/3131)
- [Geo: Simplify the demotion process](https://gitlab.com/groups/gitlab-org/-/epics/2153)
