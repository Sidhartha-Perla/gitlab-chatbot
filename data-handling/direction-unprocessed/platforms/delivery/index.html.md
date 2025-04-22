---
layout: markdown_page
title: "Product Direction - Delivery"
description: "GitLab's Delivery Group are responsible for delivering GitLab to our SaaS and Self-Managed Customers"
canonical_path: "/direction/saas-platforms/delivery/"
---

- TOC
{:toc}

## Overview

The [Delivery Group](https://handbook.gitlab.com/handbook/engineering/infrastructure/team/delivery/) enables GitLab Engineering to deliver features in a safe, scalable, and efficient fashion to both GitLab.com and self-managed customers. The Group deploys changes to GitLab.com [continuously](https://handbook.gitlab.com/handbook/engineering/deployments-and-releases/) throughout the day and also ensures that GitLab's monthly, security, and patch releases are made available to our SaaS Platforms and self-managed customers on a [predictable schedule](https://handbook.gitlab.com/handbook/engineering/releases/).

## Challenges
<!-- Optional section. What are our constraints? (team size, product maturity, lack of brand, GTM challenges, etc). What are our market/competitive challenges? -->

### Open Core, Staying Secure

Since GitLab is [public by default](https://handbook.gitlab.com/handbook/values/#public-by-default) and operates both SaaS platforms as well as a self-managed offering, there are some unique challenges as part of day to day operations. GitLab's [business model](https://handbook.gitlab.com/handbook/company/stewardship/#business-model) is based around an open core and we believe in maintaining transparency over the source code that is part of GitLab, even where this introduces additional challenges.

However, as a typical part of business for a software company in recent times, we are required to implement security fixes and remediations on a regular basis. In order to keep both ourselves and our customers safe and secure, we must discuss and implement these security fixes whilst maintaining confidentiality until the fixed release is made available to all of our customers. As a result, we have two streams of code that flow into GitLab and divergence can add complexity.

### Tight Logical Coupling

GitLab is made up of a series of components that have a tight logical coupling and strong forward/backward compatibility requirements. Our GitLab.com deployments and managed versioning release processes span many parts of the organization and are reflective of our organization structure, [see Conway’s Law](https://en.wikipedia.org/wiki/Conway%27s_law). This can make the process highly resistant to change, as there is a significant organizational burden to coordinate and align on the changes that need to be made across a process, where each department has their own metrics and responsibilities. Visibility across processes is low and it has prevented Delivery from truly evolving the process as opposed to iterating on sections over time.

### High Operational Load

Delivery models the [complex subsystem team pattern](https://teamtopologies.com/key-concepts) and is responsible for ensuring that GitLab is delivered to customers, without outages, multiple times a day. The team has deep expertise in the architecture, deployment patterns, and hands-on remediations involved in deploying and releasing GitLab. Onboarding, operating, and maintaining these systems have a high cognitive and operational load. As a consequence, project work that could evolve our deployment capabilities and unlock new business opportunities can be deprioritized over “keep the lights on work” which prevents/mitigates user impact.

## 3-5 Year Strategy

<!-- Where will the product be in 3 years? How will the customer's life/workflow be different in 3 years as a result of our product? -->

### Releases are Fully Automated, on a schedule and published in advance.

To maximize predictability for customers and efficiency for GitLab, releases should be fully automated and manual steps should be eliminated from business as usual work.
We will work towards a system where release manager interventions are driven by actionable notifications that supply the right context to team members.
The release schedule will be published in advance and driven by our SLOs/SLAs and input metrics/PIs.
A regular schedule will provide predictability inside GitLab and therefore stability to Customers of GitLab.

### No release blocks another type of release

Patch releases currently block monthly releases and vice versa.
This is primarily driven by two problems - broken mirroring and potential to leak security fixes.
We want to have the flexibility to perform a patch release in the middle of a monthly release or perform the monthly release without leaking a security vulnerability.
Over time we will work towards overhauling our tools and processes to remove blocking from all releases.
This will enable us to release changes to customers at any time and increase results for customers, particularly in the dimension of delivering bug and security fixes sooner.

### Team Members can understand the state of a release in under a minute

Release managers field a lot of questions on the state of the release and what is happening as part of their shift.
We also use several slack channels as a rolling feed of release information.
This can be hard to use both for release managers and engineers and other team members that don’t use the channels and chatops every day.
Team members at GitLab should be able to quickly understand the state of a release, what they need to do and when they can expect to see updates.
We will work towards pull based and push based systems for team members in order to minimize toil and maximize throughput and results for customers.
The first iteration of our pull based system can be seen in the [Release Dashboard](https://dashboards.gitlab.net/d/delivery-release_info/delivery3a-release-information?orgId=1&from=now-7d&to=now) (Internal).

### Continuous Deployment for the Graduation Ring

Delivery::Deployments is working on the first version of a ring based deployment system as described in the [Cells application deployment blueprint](https://docs.gitlab.com/ee/architecture/blueprints/cells/infrastructure/deployments.html).
The first iterations of this can be viewed in the [Cells Tissue](https://gitlab.com/gitlab-com/gl-infra/cells-tissue) project.
When we have a fully operational series of rings, Delivery::Deployments will focus on automating the promotion of packages into the rings that Delivery are responsible for.
This would mean continuous deployment for all cells in ring 0 up to and including the graduation ring where we graduate packages for release to customers, Dedicated and the higher rings of Cells.

### Finer Grained Control of Deployments

Our unique business situation, offering both a number of SaaS products and a self managed product that are open source, has necessitated a tight coupling between deployments and releases of GitLab.
This has ensured the organization can move at the fastest speed possible whilst sacrificing some flexibility.
Over time we want to enable all teams at GitLab to move at their own pace, getting value to customers sooner.
This will also be essential to support our goal of experimental deployments, enabling our teams to get the best version of features out to customers.

### Enable Experimental Deployments

We want to be able to enable experimental deployments that help teams at GitLab test product functionality, features, core dependencies, and performance all while reducing risk associated with unknowns servicing customers at the scale of GitLab.com.
Experimental deployments will be the basis of different release 'channels' at GitLab, meaning that customers who want the latest and greatest can subscribe to an 'experimental' or 'beta' channel whilst customers that optimise for stability can stick to the GA release channel.
How this will shape up over time will depend on internal and external demand for this kind of release.

This will help us to be more secure and more performant over time which will increase results for customers.

## 1-Year Plus Plan
<!-- Describe key themes, projects, and/or features planned over the next year. Also highlight what we will not be doing in the next year -->

For FY 25, we’re investing in the following capabilities, which are linked to our [group 3-5 year strategy](#3-5-year-strategy):

### Automating Releases

#### Release Environments validate all backported changes

Today when we release a patch of a previous minor version, we are not always able to reliably validate our changes in a reasonable time frame.
We have released the first iterations of 'Release Environments', for the current stable version, which are live installations of GitLab that look like customer installations of GitLab.
With Release Environments, we provide a surface on which to test older versions of GitLab that we are releasing to customers.
We will work toward all releases within the maintenance policy being validated as part of our release process - e.g. omnibus, Kubernetes, GET, etc.
This will provide maximum confidence that the changes we make will not have any negative impact on customers.
Over time, by providing release environments on our stable branches for many flavors of GitLab, we will ensure that there is always a place to test and verify the latest changes, increasing organizational efficiency.

#### Maintenance policy for bug fixes and security fixes is the same

Today the [Maintenance Policy](https://docs.gitlab.com/ee/policy/maintenance.html) for bug fixes and security fixes are asymetrical.
Extending the bug fix policy to be in line with the security fix policy will mean that more customers get more fixes sooner.
We support this unofficially today in delivery thanks to the improvements we’ve made on the security releases last year.
A large piece of work will be aligning this new policy with stage teams and getting them to commit to backporting fixes to two previous minor versions.
We hope to align the maintenance policy in FY25.

### Non-Blocking Releases

#### Internal Releases

Internal releases are an important emerging need now that we are supporting multiple internal GitLab installations (.com & Dedicated) and plan to support even more as Cells are added to production infrastructure.
We need a way to ensure that we can remediate vulnerabilities on GitLab managed systems before those vulnerabilities are disclosed publicly.
Additionally, internal releases will provide the first iterations of the mechanism that evolve to power our non-blocking releases and highly flexible release tools.

#### Non-blocking release branches

We will update our branching strategy around stable branches to enable non-blocking release trains, prevent the leak of security vulnerabilities and resolve the issues around broken mirroring in the security mirrors.
This will help us to maximise customer results in our decision making and lower the impact of any compromise to GitLab.

#### Release trains on branches to unblock different release types

One of the capabilities that we have envisioned is a release train that helps engineers to understand when and where releases are happening as well as what changes a release will contain.
Delivery will provide the tooling and mechanics of the release train, including visuals and notifications of the status.
The release train will start on a fixed timeline toward a release and notify GitLab engineers that a release is happening and any changes that can get on the release train will be deployed with the next release.
This will also feed into our push based system for release information with engineers getting direct feedback about their changes and inclusion in versions of GitLab.

### Better Release Information for Team Members

#### Release Status in a Single Pane of Glass

Centralizing release information in a single place will lower the context required to discover release information, lower the dependency on release managers and decrease toil for all team members.
We have completed our initial iteration, displaying information about the monthly release on the [Release Dashboard](https://dashboards.gitlab.net/d/delivery-release_info/delivery3a-release-information?orgId=1&from=now-7d&to=now). We will iterate here to expand to patch releases as well as other supplementary release information.

#### Greater instrumentation of release states

Having greater understanding and instrumentation of the release states will give us more granular and detailed information that we can display to users.
This will further lower the context required for team-members to understand the release states and increase organizational efficiency across the board for GitLab.
We’re starting with an “announced” state for the monthly release to let team-members know a release candidate has been picked.

#### Push Based Delivery

As well as the pull based self-serve solutions for release information, engineers in particular will benefit from a push based system that allows them to get instant and/or direct feedback about their changes and what release the changes will be included into.
We will build push based notification into our releases, in combination with the delivery of a release train, that enables engineers to get feedback about releases in relation to their changes.
This will help to lower the context around releases and allow engineers to focus on delivering their work, decreasing context switching and improving customer results.

### Ring Based Deployments

#### Zero Downtime, Ring Based Deployment for gitlab.com

Building on the insight we have gathered from running GitLab.com and applying our zero downtime expertise to GitLab Dedicated, we will deliver a zero downtime, ring based deployment system that will enable GitLab to evolve into a cellular architecture.
The first iterations of this can be viewed in the [Cells Tissue](https://gitlab.com/gitlab-com/gl-infra/cells-tissue) project.

#### Z Score / Metric Based deployment Safety Metric for Alerting

We will introduce a deployment safety metric which will allow us to reason about how ‘normal’ any deployment is compared to previous deployments.
Over time, this will allow us to grow confidence in more unattended deployments and promotions and build automation to take action when we observe known problematic behaviors.
This is a key requirement for moving towards continuous deployment and specifically, automatic promotion of packages for gitlab.com.
Once we have a trusted deployment saftey metric, we can begin to increase the level of automation around promotion to production.

### Experimental Releases

### Release Channels on .com

As we mature the tooling that allows us to perform experimental deployments, we expect that we will be able to open specific release 'channels' that customers are able to subscribe to.
These release channels may come with added incentives to participate in our experiments and/or beta programs whilst maintaining stability for a GA channel, for the majority of the fleet.

### What we're not doing

As part of being a [complicated subsystem team](https://teamtopologies.com/key-concepts) with a high operational load, we have to be deliberate about the work that we take on. There are a few things that we’re interested in, but can’t take on right now:

- Supporting Teams with non standard release processes in automating their deployments and implementing the [component requirements](https://gitlab.com/gitlab-org/release/docs/-/blob/master/components/index.md)

## What's Next

For a Look at the work in progress and what's next, you can stay up to date with our in progress epic and our roadmap epics:

- [Current work in progress](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/170)
- [Releases Roadmap](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1276)
- [Deployments Roadmap](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1277)


## Prioritization Framework

Because Delivery are responsible for deploying our multi-tenant SaaS offering (gitlab.com) as well as releasing GitLab packages for Dedicated and Self Managed, we prioritize "Keep the lights on" activities (e.g. deployment failures, incidents, release management) above all else to ensure we provide customers a high level of service that continually meets our reliability and performance SLAs. Aside from this our work assumes the normal [product prioritization process](https://handbook.gitlab.com/handbook/product/product-processes/#how-we-prioritize-work) and the top priority is just a reflection of our operational responsibilities.
