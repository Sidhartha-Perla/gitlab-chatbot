---
layout: markdown_page
title: "Competitive Landscape - Monitor:Observability"
description: "Compare GitLab's observability tools with competitors, providing insights into how GitLab delivers superior monitoring and performance analysis capabilities."
---

- TOC
{:toc}

## Market Definition

> _“Gartner defines the application performance monitoring (APM) and observability market as software that enables the observation and analysis of **application health, performance and user experience**. The targeted roles are IT operations, site reliability engineers, cloud and platform teams, application developers, and product owners. These solutions may be offered for self-hosted deployment, as a vendor-managed hosted environment, or via SaaS.”_

Source: [Gartner 2023 MQ: APM & Observability](https://www.gartner.com/en/documents/4877531) ([internal link](https://drive.google.com/file/d/1O7Ccf_R_XaaUTSD_imWON-mTOIaxS_1Y/view?usp=sharing))

**Key Categories:** Application Performance Monitoring, Infrastructure monitoring, Logs Management ([more](https://medium.com/investment-thesis/observability-n-0-cfb2e52c6324#:\~:text=Key%20components%20of%20the%20Observability%20stack))

## Competitive landscape

**In-house solutions:**

* Based on open-source tools like [Grafana](https://github.com/grafana/grafana), [Prometheus](https://github.com/prometheus/prometheus), [ELK](https://www.elastic.co/elastic-stack/), or custom-built tools
* Usually for small or very large companies ([costs \> 2-5M$ / year](https://blog.pragmaticengineer.com/datadog-65m-year-customer-mystery/#:\~:text=Above%20%242%2D5M,run%20that%20infra.))
* High TCO (Total Cost of Ownership): requires a team to maintain the system, including data storage.
* [Grafana Cloud](https://grafana.com/products/cloud/), [Elastic Cloud], [AWS Managed Services for Prometheus](https://aws.amazon.com/prometheus/) offer managed cloud solutions that makes it easy for companies to migrate to cloud, to reduce internal team’s maintenance and TCO.

**Observability Platforms:**

* [Datadog](https://www.datadoghq.com/), [Dynatrace](https://www.dynatrace.com/), [New Relic](https://newrelic.com/), [Elastic](https://www.elastic.co/observability), Cisco [AppDynamics](https://www.appdynamics.com/) and [Splunk](https://www.splunk.com/)
* Enterprise-focused
* Full-stack platforms covering all use cases and personas (development, infrastructure, network…), modern and legacy systems.
* Can be expensive for large companies (100K$ - XM$+ ARR)

**Point solutions:**

* [HoneyComb](https://www.honeycomb.io/) or [Sentry](https://sentry.io/), focusing on APM for developers; [Komodor](https://komodor.com/) or [Lens](https://k8slens.dev/) for Kubernetes monitoring
* More cost effective, more breadth of features, modern-first;
* More limited use cases covered

**Cloud-providers solutions:**

* [AWS Cloudwatch](https://catalog.workshops.aws/observability/en-US/intro), [Azure Monitoring](https://learn.microsoft.com/en-us/azure/azure-monitor/), [GCP Stackdriver](https://cloud.google.com/products/operations?hl=en)
* Limited capabilities; work only on one cloud vendor
* Easier to configure
* More cost-effective

**Legacy solutions:**

* Solarwinds, [VMWare](https://cloudsolutions.vmware.com/services/aria-operations-for-applications.html), [IBM Instana](https://www.ibm.com/products/instana/cloud-monitoring#:\~:text=IBM%C2%AE%20Instana%C2%AE%20Observability,Azure%20and%20Google%20Cloud%20Platform.)...
* Primarily for legacy use cases - on-premise with older infrastructure types

**Newcomers:**

* [Signoz](https://signoz.io/), [Coroot](https://coroot.com/)
* Leveraging the latest technologies - OpenTelemetry, eBPF, columnar databases
* None seem to have attained a significant market share yet.

## Market Trends

**Shift to Cloud:**

* Enterprise software is massively migrating from on-prem to cloud, which require new, cloud-based monitoring tools.

**Tool consolidation:**

* Customers increasingly want a single observability platform instead of multiple point solutions to reduce the integration challenges associated with assembling different tools
* Customers want to centralize multiple sources of data into one single place as a source of truth where they can query any data - and avoid having to switch between tools.
* It’s also more cost effective for large companies’ procurement department

**Expansion into other categories:**

* Monitoring vendors are expanding into Security, Developer tools, IT Service management, Business Intelligence & Analytics - and vice versa.
* Monitoring tools will look more and more like BI analytics tools (ie. Sisense/Tableau), probably with additional market consolidation in the future.

**DevOps / Shift-left**

* Traditionally, monitoring was the role of specialized Operations teams, focusing on Infrastructure Management. DevOps methodologies (“you build it you run it”) changed the way monitoring is done, with the ascent of SRE teams & Developers sharing on-call duties.
* Performance issues and errors (aka. “defects”) caught before production are easier to fix than after. Embedding performance testing into development workflows help minimize issues going into production, reduce downtimes and reduce time spent fixing them.

source: [Gartner](https://drive.google.com/a/gitlab.com/open?id=1HQCrRW4Y18nSEYCjDzAbxsn_XbvgGFJk) (internal only)