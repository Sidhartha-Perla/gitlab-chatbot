---
title: "Database Operations Team  (formerly known as the Database Reliablity Engineering (DBRE) team)"
---

## Mission

The mission of the Database Operations team at GitLab is to Build, Run, Own and Evolve the entire lifecycle of the PostgreSQL database engine for GitLab.com.

The team is focused on owning the reliability, scalability, performance & security of the database engine and its supporting services. The team should be seeking to build their services on top of [Production Engineering::Foundations](/handbook/engineering/infrastructure-platforms/production-engineering/foundations/_index.md) services and cloud vendor managed products, where appropriate, to reduce complexity, improve efficiency and deliver new capabilities quicker.

The team uses [Engineering Principals](/handbook/engineering/development/principles/) to guide the decisions it makes for it's services. The team does not explicitly have any self hosted product responsibilities but we should contribute the lessons we learn running the database engine for GitLab at scale in production  back to the Product, Development & Support teams to improve overall customer experience with GitLab, as well as collaborating with the Support teams when self managed customers encounter complex database engine issues.

## Team Members

{{< team-by-manager-slug "rmar1" >}}

## Ownership

### Services

Systems and services we are primarily responsible for:

- PostgreSQL Core (VM)
- PostgreSQL Core (PGaaS) (coming soon)
- PostgreSQL High Availability and Load Balancing (e.g. Patroni, PGBouncer, consul, PostgreSQL Replication etc.)
- PostgreSQL Disaster Recovery (backup/restore and other techniques)
- Database Observability (Prometheus instrumentation, workload analysis etc.)
- Support & troubleshooting of GitLab applications, specifically related to their use of and interaction with the PostgreSQL ecosystem.

- Self-Hosted Clickhouse (coming soon)

Systems or services explicitly not owned by us:

| System name | Description | Owner and supported by | Extra info/Open questions |
|-------------|-------------|------------------------|---------------------------|
| Redis | There are several use cases such as caching, rate-limiting, sidekiq queueing. | [Scalability Group](/handbook/engineering/infrastructure/team/scalability/) | [Redis Architecture](/handbook/engineering/infrastructure/production/architecture/#redis-architecture) |
| Data team systems |          | Data team |                          |
| Self Managed databases|           | Self managed Support |               |

## Useful Links

|   |   |
|---|---|
| Backlog | [DBO Status](https://gitlab.com/groups/gitlab-com/gl-infra/data-access/dbo/-/epics/13) |
| Roadmap Ideas | [Now-Next-Later](https://gitlab.com/groups/gitlab-com/gl-infra/data-access/dbo/-/epic_boards/2066770) |
| Reaching us | [`#g_database_operations`](https://gitlab.enterprise.slack.com/archives/C02K0JTKAHJ) <br> `@gitlab-org/data-access/dbo` |
| Weekly Agenda | [Weekly APAC and EMEA/AMER](https://docs.google.com/document/d/1d8YrRO4Vw_pHXohgwq-lEBM75ihMtkLpcd2_cFa6Yrs/edit#) |

## DBO Escalations

We have a detailed [DBO escalation process](dbre-escalation-process) which provides escalation guidelines for handling database related production incidents.

## OKRs

We use quarterly [Objectives and Key Results](/handbook/company/okrs/) to plan and measure our Key Performance Indicators (KPIs).

## Performance indicators

We measure the value we contribute by using [performance indicator metrics](/handbook/engineering/infrastructure/performance-indicators/#key-performance-indicators).

In addition to the Infrastructure Department's KPIs for [availability](/handbook/engineering/infrastructure/performance-indicators/#gitlabcom-availability)
and [performance](/handbook/engineering/infrastructure/performance-indicators/#gitlab-com-performance) of GitLab.com, the Database Operations team tracks the following:

- Backup and Recovery SLOs
- General database availability(Uptime)

## Key Technical Skills

The team is comprised of Database Operations engineeers with varying levels of expertise in:

- Supporting PostgreSQL in large production environments.
- Infrastucture automation and configuration management, using tools such as Chef, Ansible, Terraform, etc.
- PostgreSQL internals, tuning & optimization, SQL and PL/pgSQL.

## Common Links

To make it easier to find your way around you can find a list of useful or important links below.

### Monitoring & Performance Related Tools

The following tools can be helpful:

- [Postgres Checkup](https://gitlab.com/gitlab-com/gl-infra/infrastructure/issues?label_name%5B%5D=postgres-checkup):Detailed report about the status of the PostgreSQL database.
- [Private Grafana](https://dashboards.gitlab.net/): for both application and system level performance data.
- [Performance Bar](https://docs.gitlab.com/ee/administration/monitoring/performance/performance_bar.html): type `pb` in GitLab and a bar with performance metrics will show up at the top of the page. This tool is especially useful for viewing the queries executed and their timings.

If you have identified a Postgres Performance Problem and want to dive deeper, we reccomend these runbooks and dashboards. They are best used together, with the runbooks explaining how to understand the dashboards.

Dashboards: 

- [Postgres node performance overview (high-level)](https://dashboards.gitlab.net/d/postgres-ai-node-performance-overview)
- [Postgres aggregated query performance analysis](https://dashboards.gitlab.net/d/postgres-ai-NEW_postgres_ai_02)
- [Postgres single query performance analysis](https://dashboards.gitlab.net/d/postgres-ai-NEW_postgres_ai_03)
- [Postgres wait events analysis](https://dashboards.gitlab.net/d/postgres-ai-NEW_postgres_ai_04)

Runbooks:

- [High-level performance analysis and troubleshooting of a Postgres node](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/patroni/single-node-high-level.md?ref_type=heads)
- [Postgres wait events analysis (a.k.a. Active Session History; ASH dashboard)](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/patroni/wait-events-analisys.md)
- [SQL query analysis and optimization for Postgres](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/patroni/query-analysis.md)

### Dashboards

The following (private) Grafana dashboards are important / useful for database specialists:

- [PostgreSQL Overview](https://dashboards.gitlab.net/d/000000144/postgresql-overview?orgId=1&var-prometheus=Global&var-environment=gprd&var-type=patroni)
- [Patroni Overview](https://dashboards.gitlab.net/d/patroni-main/patroni-overview?orgId=1)
- [Patroni CI Overview](https://dashboards.gitlab.net/d/patroni-ci-main/patroni-ci-overview?orgId=1)
- [PgBouncer Overview](https://dashboards.gitlab.net/d/pgbouncer-main/pgbouncer-overview?orgId=1)
- [PgBouncer CI Overview](https://dashboards.gitlab.net/d/pgbouncer-ci-main/pgbouncer-ci-overview?orgId=1)
- [GitLab Triage](https://dashboards.gitlab.net/d/RZmbBr7mk/gitlab-triage?orgId=1)
- [PostgreSQL Bloat](https://dashboards.gitlab.net/d/000000224/postgresql-bloat?orgId=1&refresh=5m)
- [PostgreSQL Disk IO](https://dashboards.gitlab.net/d/pEfSMUhmy/postgresql-disk-io?orgId=1&var-environment=gprd&var-prometheus=Global&var-type=patroni&var-node=patroni-main-2004-01-db-gprd.c.gitlab-production.internal&from=now-7d&to=now)
- [Host stats](https://dashboards.gitlab.net/d/bd2Kl9Imk/host-stats?orgId=1)
- [Tuple Statistics](https://dashboards.gitlab.net/d/000000167/postgresql-tuple-statistics?from=now-3h&to=now&var-prometheus=Global&var-environment=gprd&var-type=patroni&orgId=1&refresh=5m)
- [Postgres node performance overview (high-level)](https://dashboards.gitlab.net/d/postgres-ai-node-performance-overview)
- [Postgres aggregated query performance analysis](https://dashboards.gitlab.net/d/postgres-ai-NEW_postgres_ai_02)
- [Postgres single query performance analysis](https://dashboards.gitlab.net/d/postgres-ai-NEW_postgres_ai_03)
- [Postgres wait events analysis](https://dashboards.gitlab.net/d/postgres-ai-NEW_postgres_ai_04)

### Documentation

- [What requires downtime?](https://docs.gitlab.com/ee/update/with_downtime.html)
- [Adding database indexes](https://docs.gitlab.com/ee/development/database/adding_database_indexes.html)
- [Post Deployment Migrations](https://docs.gitlab.com/ee/development/database/post_deployment_migrations.html)
- [Background Migrations](https://docs.gitlab.com/ee/development/database/batched_background_migrations.html)
- [SQL Migration Style Guide](https://docs.gitlab.com/ee/development/migration_style_guide.html)
- [SQL Query Guidelines](https://docs.gitlab.com/ee/development/sql.html)
- [Infrastructure runbooks and documentation](https://gitlab.com/gitlab-com/runbooks#postgresql)
