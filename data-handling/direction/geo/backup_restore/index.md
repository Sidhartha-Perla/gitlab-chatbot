---
layout: markdown_page
title: "Category Strategy - Backup and Restore"
description: "GitLab supports backup and restore procedures that rely
on standard unix tools."
canonical_path: "/direction/geo/backup_restore/"
---

- TOC
{:toc}

## 🗄 Backup and Restore

|Section | Group | Maturity | Last updated|
|--------|-------|------|------|
|[Enablement](https://about.gitlab.com/direction/enablement/) | [Geo](https://about.gitlab.com/direction/geo/)|  [](/direction/#maturity)  | 2023-12-15   |

Thanks for visiting this category strategy page for GitLab Geo Disaster Recovery. This page belongs to the [Geo group](https://handbook.gitlab.com/handbook/product/categories/#geo-group).

### Overview

GitLab is part of the critical infrastructure for many of our self-managed customers. It is important that GitLab is resilient in the face of various types of disasters that might impact the availability of its services.

A robust disaster recovery strategy needs to be able to recover quickly from hardware and power failures, and data centre outages. This is where [Geo Disaster Recovery](https://about.gitlab.com/direction/geo/disaster_recovery/) can help. Geo allows the creation of one or more warm standby sites that can be rapidly promoted to take over in the event of a disaster.

A comprehensive disaster recovery strategy also needs to defend against malicious and unintentional corruption of data. This is where [backup and restore](https://docs.gitlab.com/ee/raketasks/backup_restore.html) plays an important role. Being able to restore your data from a point in time in the past before the occurrence of such corruption will ensure you can successfully recover from such events.

The existing backup and restore solution from GitLab relies on standard Unix tools, such as `rsync` and `tar`. By default, backups cover most data but not GitLab’s configuration. For GitLab instances that contain several hundred gigabytes or even terabytes, the current solution does not scale well. This means that backing up or restoring such a GitLab instance can take many hours.

Cloud-hosted customers can leverage the cloud vendor's backup tools in conjunction with `gitlab-backup` to achieve scalable backups. We have [updated guidance and documentation](https://docs.gitlab.com/ee/administration/backup_restore/backup_large_reference_architectures.html) on how to perform backups in AWS. We will be adding [content for GCP](https://gitlab.com/gitlab-org/gitlab/-/issues/418163) soon.

File system snapshots are an alternative fast and scalable option for installations that do not run Gitaly cluster. For larger [GitLab reference architectures](https://docs.gitlab.com/ee/administration/reference_architectures/) that choose to run Gitaly cluster, snapshot backups can lead to the Praefect database going out of sync with the disk storage and create backups that are not viable.

We have started working on a [new backup solution](https://gitlab.com/groups/gitlab-org/-/epics/11577). A single tool that works across all the different GitLab installation types (Linux packages, Cloud Native Hybrid, Docker and GDK). It will have a strong emphasis on scalability from the start and a focus on cloud-hosted installations initially. The existing backup tool will continue to be supported while we build out the new tool.

#### How you can help

Please reach out to Sampath Ranasinghe, Product Manager for the Geo group ([Email](mailto:sranasinghe@gitlab.com)) if you'd like to provide feedback or ask any questions related to this product category.

This strategy is a work in progress, and everyone can contribute. Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Ageo&label_name%5B%5D=Category%3ABackup%2FRestore%20of%20GitLab%20instances&first_page_size=50) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=group::geo&label_name[]=Category:Backup/Restore+of+GitLab+instances) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.

#### Useful resources

- [Roadmap for Backup and Restore](https://gitlab.com/groups/gitlab-org/-/roadmap?state=all&sort=start_date_asc&layout=MONTHS&timeframe_range_type=CURRENT_YEAR&label_name[]=group::geo&label_name[]=Category:Backup/Restore+of+GitLab+instances&progress=COUNT&show_progress=true&show_milestones=false&milestones_type=ALL&show_labels=false)
- [Maturity: ](/direction/#maturity)
- [Documentation](https://docs.gitlab.com/ee/raketasks/backup_restore.html)
- [Viable Maturity epic](https://gitlab.com/groups/gitlab-org/-/epics/6079)
- [All Epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=group::geo&label_name[]=Category:Backup/Restore+of+GitLab+instances)

### Vision & Strategy

GitLab and the data held within is business critical for the majority of our customers. As such, this data must be protected against malicious and unintentional corruption. Such corruption can lead to loss in productivity, financial losses and loss of customer confidence. In the event of such corruption, it must be possible to rapidly restore the data to a good state and resume normal operations. Backups are an essential part of protecting against these events.

We envision a backup solution that is easy to use, secure, fast, cost-effective and reliable to back up your GitLab data. A solution that works across all GitLab reference architectures, deployment types and GitLab offerings such as self-managed, GitLab Dedicated and GitLab.com. One with a low Recovery Point Objective (RPO), integrates with native cloud vendor services, based on a scalable and extensible architecture that evolves with GitLab. A solution that compliments our [Disaster Recovery (DR) solution based on Geo](https://about.gitlab.com/direction/geo/disaster_recovery/).

In pursuit of this vision, we are taking a two-pronged approach; make impactful, quick-win improvements to the existing solution to extend its utility while we build out the next-generation solution.

#### Quick win improvements to the existing solution

We are making high-impact, quick-win improvements to our existing tools. This will provide immediate relief to customers who are struggling with long backup times and reliability issues while we work on our next-gen solution. Notable improvements we are making include adding support for [parallel compression](#parallel-compression) and switching to a more [performant and reliable S3 tool](#faster-more-reliable-s3-tool-for-cloud-native-backups).

#### Building next-generation solution

We are building a new backup solution from the ground up. The new backup solution will work across all GitLab reference architectures, installation types and offerings. We will initially focus on cloud-hosted deployments with support for the major cloud vendors such AWS, Google and Azure. There are three major pillars to our strategy for building the new solution.

Systems administrators will be able to invoke a backup on demand as well as schedule routine backups daily. It will cover 100% of all core GitLab data and can be easily extendable to cover new data components as GitLab evolves; ensuring our customers are protected from data loss in the event they need to recover their GitLab instance from a backup. We will strive for a low RPO and data consistency in the backups. It will scale to hundreds of terabytes of GitLab data. 

Backups will run to completion in the face of non-critical errors thus ensuring all possible data is backed up and highlight non-critical failures such that systems administrators can take the appropriate actions to remedy them. Notifications of success or failure of backup jobs together with non-critical errors encountered during backup runs will be available to systems administrators. 

Systems administrators will be able to see a list of their recent backups and easily restore a GitLab instance based on a selected backup. They will be able to test the integrity of the backup and their recovery processes. 

##### Scalability and reliability

Scalability has been one of the major pain points for our customers with the existing backup solution. We will reduce the need for intermediary storage and processing, and embrace the tools and capabilities available from the major cloud vendors to build a solution that works in synergy with these systems. Some of the efforts in this space include [incremental server-side repository backups](#server-side-incremental-repository-backups), [faster more reliable S3 tool](#faster-more-reliable-s3-tool-for-cloud-native-backups) and [incorporation of transaction logs into backups](#lower-rpo-and-more-consistent-backups) to provide granular Point-In-Time-Recovery(PITR).

##### Simplification and usability
Another major challenge with the existing solution is the need for different tools and different approaches based on the architecture and installation type. For example, Linux packaged, Docker and self-compiled GitLab backup is based on a [rake task](https://docs.gitlab.com/ee/administration/backup_restore/backup_gitlab.html?tab=Self-compiled#backup-command) and Cloud Native Hybrid backups are based on the [backup-utlity](https://docs.gitlab.com/charts/architecture/backup-restore.html#backup-utility). We will have a single solution that works across all reference architectures (1K - 25K) and installation types (Linux packaged, Docker, Cloud Native Hybrid, GDK) with a [single unified [Command-Line Interface](CLI)](#next-gen-backup-solution---mvc). This will vastly simplify the backup experience and allow us to streamline our guidance and documentation. We will have an updated, more opinionated guidance for larger deployments](#update-guidance-and-documentation-for-larger-deployments) which describes how to successfully use the backup solution in combination with the cloud vendor's backup services. This will be followed by [cloud vendor integration](#cloud-vendor-api-integration) to create a single interface for driving the backup. 

We will add support for [non-cloud hosted and air-gapped customers](#support-non-cloud-hosted-environments) completing the coverage for all deployments.

##### Long-term sustainability and internal adoption
We want to build a sustainable and extendable solution that can evolve with GitLab to ensure our customers are protected against data loss. We will achieve this with a [self-service framework for adding new components](#self-service-framework). It will be easy for internal teams as well as 3rd parties to add new data components to the backup, maximizing code reuse and reducing maintenance costs.

[Deployment to GitLab Dedicated](#deploy-to-gitlab-dedicated) and [integration with Cells architecture to provide backup services for GitLab.com](#deploy-to-gitlabcom) will allow GitLab SaaS offerings to benefit from the solution. They will no longer have to maintain their own custom solution for backup and restore. This will ensure we dogfood our own solution and build and share best practices with our self-managed customers.

### Target audience and experience

#### [Sidney - (SystemsAdministrator)](https://handbook.gitlab.com/handbook/product/personas/#sidney-systems-administrator)
 * Backups should contain all GitLab core data, and be easy to create, automate, and restore. They also
need to complete as fast as possible and make efficient use of storage.

#### Jobs To be Done (JTBD)

Jobs To be Done (JTBD) is a framework for viewing the product in terms of the process customers trying to achieve. [Learn more about the JTBD](https://handbook.gitlab.com/handbook/product/ux/jobs-to-be-done/).

- Category JTBD: When my organization has critical data, I want to have a reliable backup and restore procedure, so that we can recover from any planned or unplanned data loss event.
  - **Backup**: When my organization is building software on a DevOps platform, I want to back up my data regularly so that it is protected from corruption. I also want to have my most recent data backed up on demand so that it is protected during events such as upgrades, infrastructure and configuration changes.
  - **Restore**: When my organization experiences an outage, data loss or corruption event, I want to be able to restore the data as quickly as possible from a selected backup so that my customers experience minimal downtime with my service.

### In a Year

#### Support non-cloud hosted environments

The initial development of our new backup solution is focused on cloud-hosted deployments. We will evolve this to add support for non-cloud-hosted deployments such as those hosting GitLab on their own hardware and air-gapped customers. Typically such customers either store files in local storage or use object storage appliances including MinIO and run Linux packaged Postgresql.  

#### Deploy to GitLab.com

GitLab.com has a vast dataset and it is challenging to stretch a self-managed solution to the required scale. Today, GitLab.com operates its own [custom backup solution](https://handbook.gitlab.com/handbook/engineering/infrastructure/production/#backups). GitLab.com will migrate to the new [cells architecture](https://about.gitlab.com/direction/core_platform/tenant-scale/cell/) thus splitting the large dataset into manageable cells. The new unified backup solution will provide the backup and restore capability to cells. This has several benefits including having a single backup solution that caters to all flavors of GitLab offerings - self-managed, Dedicated and GitLab.com. It is another opportunity for GitLab to dogfood its own backup solution. Opportunities to share our learnings and best practices with self-managed customers. Feature improvements will benefit all GitLab offerings by sharing a single solution.

#### Usage metrics

Build anonymized usage metrics into the new backup solution. Usage metrics will allow GitLab to learn about how our customers use the solution, ensure we are on track to meet our customers' needs and help us understand the impact of new features we develop. It will also inform where we focus our efforts and how we evolve the product. 

### What's Next & Why

#### Update guidance and documentation for larger deployments

The evolution of the GitLab backup and restore solution over the years has resulted in several tools and multiple pages of documentation. Customers have found it challenging to identify the right solution for their needs and successfully implement it. Therefore, together with the [Gitaly](https://about.gitlab.com/direction/gitaly/) and [Distribution](https://about.gitlab.com/direction/distribution/) teams the Geo team is working on [simplifying and enhancing our guidance and improving our backup and restore documentation](https://gitlab.com/groups/gitlab-org/-/epics/10047). We are also working on providing a runbook for customers who are on large reference architectures or have large data sets that find the current solutions are either taking too long or don't work at all. Our approach will focus on consolidating and levering the existing solutions together with storage and database vendor backup solutions to create a multi-part complete backup that can be used to fully restore a GitLab instance.

#### Parallel compression 

The current GitLab backup tool compresses the contents of the backup using gzip which is a single-threaded compression library. Modern processors have multiple powerful compute cores that can be taken advantage of to speed up the compression stage of the backup. Therefore, we will be allowing the default gzip compression command to be overridden by compatible [parallel compression](https://gitlab.com/gitlab-org/gitlab/-/issues/322914) library of your choice with associated parameters passed as an option to the backup command.

#### Faster, more reliable S3 tool for Cloud Native backups

The default S3 tool used to upload and download files from AWS S3 or S3-compatible object storage services by the [backup-utility](https://docs.gitlab.com/charts/architecture/backup-restore.html#backup-utility) is [s3cmd](https://s3tools.org/s3cmd). There are faster and more reliable alternatives such as [s5cmd](https://github.com/peak/s5cmd) and [AWS native CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3.html) that support multipart concurrent operations. We already support AWS CLI as an optional override. We will replace s3cmd as the default with one of the alternatives for a faster and more reliable experience.

#### Server-side incremental repository backups

The Gitaly team is working on [server-side incremental repository backups](https://gitlab.com/gitlab-org/gitaly/-/issues/5461). This is an enhancement to [server-side backups](https://docs.gitlab.com/ee/administration/backup_restore/backup_gitlab.html#create-server-side-repository-backups) that will allow you to backup only the changes since the last full backup, saving space and time. 

#### Next-gen backup solution MVC 

We have started work on a [new backup tool](https://gitlab.com/groups/gitlab-org/-/epics/11577). A single tool that works across all GitLab installation types (Linux packaged, Docker, Cloud Native Hybrid and GDK) using a unified CLI. There will be a strong emphasis on scalability - support for large datasets and architectures. Initial iterations will focus on cloud-hosted deployments, working in synergy with the cloud vendor's native backup offerings for each data type such as managed Postgresql and object storage. 

The [MVC](https://gitlab.com/groups/gitlab-org/-/epics/11908) will build the foundations for the unified CLI

Starting with support for 1K reference architecture for [Docker](https://docs.gitlab.com/ee/install/docker.html) and [Linux packaged](https://docs.gitlab.com/omnibus/) installation types.

#### Scaling up next-generation backup

Building upon the MVC, we will add support for Cloud Native Hybrid architectures and scale up to [10K reference architectures](https://gitlab.com/groups/gitlab-org/-/epics/11911) followed by [25K+ reference architectures](https://gitlab.com/groups/gitlab-org/-/epics/12042).

#### Self-service framework

As GitLab evolves, new data components will be created. It is expensive and unproductive to need to write new code from scratch each time a new component is introduced. A [self-service framework](https://gitlab.com/groups/gitlab-org/-/epics/12045) will enable code reuse and reduce the overall maintenance overhead as we have seen with the [Geo self-service framework](https://docs.gitlab.com/ee/development/geo/framework.html). It will also make it easier and faster for 3rd parties to contribute new data components to backups.

Eventually, we want to encourage GitLab teams to ensure that any new data components they add are included in the backup thus protecting GitLab customers against data loss in the event they need to restore their data from a backup.

#### Lower RPO and more consistent backups

The Gitaly team will implement [write-ahead logs(WAL) for repositories](https://gitlab.com/groups/gitlab-org/-/epics/8911). Combining this with Postgresql WAL which is offered by all major cloud vendors for their managed Postgresql databases, we can reduce the RPO for backups on cloud-hosted deployments. The [WAL transaction logs will be incorporated into the backups](https://gitlab.com/groups/gitlab-org/-/epics/12043) such that they can be played back after restoring the main backup thus reducing the RPO.

Reducing the RPO leads to more consistent backups. While each data component backup will have a different completion the inclusion of the transaction logs compensates for the difference. The transaction logs can be used to align the different data types to a much narrower point in time when restoring thus reducing the inconsistencies in the restored instance.

#### Cloud vendor API integration

All major cloud vendors have API integrations for their services - managed Postgresql, object storage, backup vaults, etc. The new unified backup solution will have [API integrations](https://gitlab.com/groups/gitlab-org/-/epics/12059) into the required services on the main three cloud vendors (AWS, Google and Azure). The integrations allow the solution to orchestrate the different services to produce a complete backup without requiring the systems administrator to drive the cloud vendor's interfaces separately. This will result in less cognitive load on the systems administrator and reduce the chances of ending up with an unviable backup as a result of having to drive multiple interfaces and collate disparate pieces of data across different services to form a complete backup. 

Similarly, the backup restore experience will be improved through these integrations enabling sequencing and unpacking of the backup to the appropriate locations through a single CLI.

#### Deploy to GitLab Dedicated

The [GitLab Dedicated](https://about.gitlab.com/dedicated/) team has a custom backup solution for backing up their customers' data. The new backup solution can replace this custom solution with a standard solution that is used by our self-managed customers. This will have several benefits for GitLab, GitLab Dedicated team and our customers: 
- Do not have to maintain multiple backup solutions across the GitLab organization
- We dogfood our own solution
- Share our learnings and best practices with self-managed customers

### What is not planned right now

We currently don't plan to implement application-consistent backups (i.e. temporarily quiesce the application and flush data in memory to disk). 

### Maturity plan

This category is currently at the  maturity level, and our next maturity target is viable (see our
[definitions of maturity levels](/direction/#maturity)).

### User success metrics

- Time to backup/time to restore
- Number of manual steps required to be performed by a systems administrator to
  backup and restore.
- Number of backup/restore operations performed via Web UI

To measure these success metrics, we also need to enable GitLab's usage ping
and gather data specific to the backup and restore process. For example, the
time it took for a backup to complete.

### Competitive landscape

All major competitors offer backup solutions for their products. GitHub, for
example, offers a [more robust and scalable backup/restore solution](https://github.com/github/backup-utils#github-enterprise-server-backup-utilities) that allows for [incremental backups](https://gitlab.com/gitlab-org/gitlab/-/issues/19256) done on a separate host. There are also standalone solutions such as [GitProtect](https://gitprotect.io/gitlab.html).


### Top customer success/sales issue(s)

- [Most popular backup and restore issues with customer label](https://gitlab.com/gitlab-org/gitlab/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=Category%3ABackup%2FRestore%20of%20GitLab%20instances&label_name[]=customer)

### Top user issues

- [Most popular backup and restore issues](https://gitlab.com/gitlab-org/gitlab/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=Category%3ABackup%2FRestore%20of%20GitLab%20instances)

### Top internal customer issues/epics

- [Backups support Pool Repositories](https://gitlab.com/groups/gitlab-org/-/epics/6080)

### Top strategy item(s)

- [Backups should be performant at any scale](https://gitlab.com/gitlab-org/gitlab/-/issues/28780)
- [Backups should support incremental backups](https://gitlab.com/gitlab-org/gitlab/-/issues/19256)
- [Backups should be a part of the administrator UI](https://gitlab.com/gitlab-org/gitlab/-/issues/13965)
