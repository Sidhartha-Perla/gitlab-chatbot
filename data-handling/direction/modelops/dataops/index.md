---
layout: sec_direction
title: "Group Direction - DataOps"
description: "Enabling customers to build data engineering toolchains to enable ELT of enterprise data for ML/AI use cases"
canonical_path: "/direction/modelops/dataops/"
---

# DataOps

## On this page
{:.no_toc}

- TOC
{:toc}

## Overview

Today businesses are creating, moving, storing and more recently, deleting data faster than ever before. They are building applications that leverage this data. Organizations commonly have data teams to help manage the lifecycle of data and to help find value in it. Data doesn't just sit in datastores anymore, [it moves and changes](https://about.gitlab.com/direction/modelops/#data-in-motion). This is a common challenge with data science. The insights and models you built on data today, won't necessarily be accurate or useful in the future as data changes or drifts from your initial modeling. This challenge commonly leads to the dreaded "messy data" problem that makes it difficult for organizations to gain value from their data. Solving this challenge will make it easier for organizations and data science teams to find value in data and allow it to power the applications of the future. That is the focus of this group.

### Goal

This group goes beyond enhancing our existing stages and offering. DataOps will help organizations turn disparate data sources into data-driven decisions and useful workloads. This will enable new efficiencies within organizations using GitLab, and these new capabilities will be particularly attractive to a CTO, CIO, and data teams.

### Categories
- *Extract* → Collecting data from across organizations, applications, and data stores. Meltano today uses Singer.
- *Load* → Aggregating data engineering from disparate sources into a unified data lake. Compare to various data manipulation libraries and tools: Snowflake, Stitch Data, Oracle Data Integrator
- *Transform* → Manipulate data into standardized, cleaned, shaped, and verified data to be used for data science. Run DBT better, compare to DBT Cloud.

### Meltano

Previously GitLab was focused on an internally developed product called [Meltano](https://meltano.com/), an [open-source platform](https://gitlab.com/meltano/meltano) for building, running & orchestrating ELT pipelines leveraging [Singer taps](https://www.singer.io/) and targets and [dbt models](https://www.getdbt.com/), that you can run locally or easily deploy in production. As of mid 2021, [Meltano was spun out of GitLab into its own startup](https://meltano.com/blog/meltano-spins-out-of-gitlab-raises-seed-round/). While we are pursuing alternative routes forward with our DataOps group, Meltano still provides a useful open source ELT platform that connects with GitLab.

## Analyst Research

* [Forrester: Feature Stores Take On The Data In Data Science](https://www.forrester.com/fn/78nWuvBkhTNOFjZC9m1z6g)

*Last Reviewed: 2024-10-05  
Last Updated: 2024-10-05*
</p>