---
title: Database Lexicon - terms and definitions relating to our database
description: "This is not a comprehensive list of all of the commonly used terms, but rather it is a list of terms that are commonly confused or conflated with other terms.  In each section we will identify common phrases, define our specific usage and list external references for the term in question."
---

## Commonly Used Terminology

This is not a comprehensive list of all of the commonly used terms, but rather it is a list of terms that are commonly confused or conflated with other terms.  In each section we will identify common phrases, define our specific usage and list external references for the term in question.

### Partitioning

For our purposes, when referring to partitioning we are referring to a local optimization of splitting one large table into many small tables.  Additionally, this is done in a way such that the application accessing this partitioned table is mostly unaware of the changes. Queries benefit from partitioning only if they use the partitioning key as a filter.

Definition - "Partitioning refers to splitting what is logically one large table into smaller physical pieces." Reference: [PostgreSQL: Documentation: 11: 5.10. Table Partitioning](https://www.postgresql.org/docs/11/ddl-partitioning.html)

To learn more about the implementation details and performance improvements of partitioning please read the Database Team handbook entry: [Database Partitioning](/handbook/engineering/infrastructure-platforms/data-access/database-framework/doc/partitioning/)

### Sharding

The simplest definition of sharding is the process of breaking up portions of your database (e.g. large tables) into smaller tables and distributing those smaller tables across multiple servers.  Where sharding can get confusing, especially with PostgreSQL, is that most definitions of sharding use the term `partitioning` to describe how the tables are broken down and distributed.  This can lead to the terms `sharding` and `partitioning` being conflated.

For our purposes, when referring to *sharding* we are referring to horizontally distributing data across multiple database clusters ("shards"). Each shard only contains a subset of the overall data.

#### Application Sharding

Another variant of sharding is `application sharding`  This typically refers to an architecture that implements routing logic to route data requests from the application to the correct data repository.  During our discussions in the [Sharding Working Group](/handbook/company/working-groups/sharding/) we typically referred to the [Shopify Pods Architecture](https://shopify.engineering/a-pods-architecture-to-allow-shopify-to-scale) as an example of application sharding.

### Foreign Data Wrapper (FDW)

Foreign Data Wrappers allow for accessing remote data from multiple data sources. FDW can be used to create an integrated view from your PostgreSQL instance into many [different types of resources](https://wiki.postgresql.org/wiki/Foreign_data_wrappers), but for our purposes we are focusing on integrating multiple PostgreSQL servers.  Foreign Data Wrappers (FDW) are an implementation detail that can change your PostgreSQL partitioning implementation to what is considered a [Built-in Sharding](https://wiki.postgresql.org/wiki/Built-in_Sharding) implementation.

### Partitioning with FDW = Sharding

With PostgreSQL, partitioning is the first implementation step taken on the path to sharding using Foreign Data Wrappers (FDW).  More information and implementation details can be found in the Database Team Handbook Entry: [PostgreSQL 11 sharding with foreign data wrappers and partitioning](/handbook/engineering/infrastructure-platforms/data-access/database-framework/doc/fdw-sharding/)
