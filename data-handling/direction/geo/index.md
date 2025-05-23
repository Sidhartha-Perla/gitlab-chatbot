---
layout: markdown_page
title: "Product Direction - Geo"
description: "The Geo group enables users to distribute GitLab to different locations and use those Geo nodes for disaster recovery purposes. Learn more!"
canonical_path: "/direction/geo/"
---

- TOC
{:toc}

 
Last updated: 2022-11-05

## Overview

![Geo](images/geo-direction.png)
 
The Geo group provides features that extend GitLab installations to different geographic locations. This is achieved by replicating the entire GitLab data set to new locations in a coordinated, verifiable and coherent manner. Data can be accessed from any of the locations whilst intelligent proxying techniques guarantee users have access to the most recent data.

This architecture addresses a number of customer problems that includes proximity based data acceleration and disaster recovery.

The Geo group is responsible for three distinct product categories:

- **[Geo replication](/direction/geo/geo_replication/) - ([Maturity: ](/direction/#maturity))**

  Help remote teams work more effectively with faster access to GitLab data by serving data from Geo sites closer in proximity to their geographic location. This solution is built on top of the Geo replication and verification framework to replicate data to the remote sites.
  
- **[Disaster Recovery](/direction/geo/disaster_recovery) - ([Maturity: ](/direction/#maturity))**

  Replicate all critical GitLab data to a secondary site that can be promoted to an active instance in the event of a natural or human-caused disaster. This solution is built on top of the Geo replication and verification framework to replicate data to the secondary disaster recovery site.

- **[Backup and Restore](/direction/geo/backup_restore/) - ([Maturity: ](/direction/#maturity))**

  Backup and restore all critical GitLab data.

If you'd like to discuss this strategy directly with the product manager for
[Geo](https://handbook.gitlab.com/handbook/product/categories/#geo-group), please
feel free to reach out to Sampath Ranasinghe via [e-mail](mailto:sranasinghe@gitlab.com)

## Upcoming

The Geo group works using epics to plan larger efforts. For a visual overview of
the epics for both
[Geo-replication](/direction/geo/geo_replication/) and [Disaster
Recovery](/direction/geo/disaster_recovery/), please have a look at [our
roadmap](https://gitlab.com/groups/gitlab-org/-/roadmap?state=all&sort=start_date_asc&layout=MONTHS&timeframe_range_type=CURRENT_YEAR&label_name%5B%5D=group%3A%3Ageo&progress=COUNT&show_progress=true&show_milestones=false&milestones_type=ALL).
Backup and restore epics will be included at a later stage.
