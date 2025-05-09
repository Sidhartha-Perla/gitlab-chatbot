---
layout: markdown_page
title: "GitLab Direction"
description: "Our vision is to replace disparate DevSecOps toolchains with a single application that is pre-configured to work by default across the entire DevSecOps lifecycle."
canonical_path: "/direction/"
extra_css:
  - maturity.css
  - direction.css
---

## On this page
{:.no_toc}

- TOC
{:toc}

# 3-year strategy

## Situation
GitLab competes in a large market space, with a [CSM](https://internal.gitlab.com/handbook/product/investment/) estimated at ~$18B in 2024. GitLab has recently surpassed the $150M ARR milestone, with unusually high revenue growth and retention rates. GitLab is uniquely positioned in the market with a vision to offer a single application for the entire DevSecOps lifecycle. GitLab competes across numerous market segments and aims to deliver value in [80+ market categories](https://handbook.gitlab.com/handbook/product/categories/). GitLab’s product vision is uniquely ambitious, as we were the first DevSecOps player to take a [single application approach](/topics/single-application/). From idea to production, GitLab helps teams improve cycle time from weeks to minutes, reduce development process costs, and enable a faster time to market while increasing developer productivity. With software “eating the world,” this is widely viewed as a mission-critical value proposition for customers. We also have a number of [tailwinds](https://handbook.gitlab.com/handbook/leadership/biggest-tailwinds/) in the form of cloud adoption, Kubernetes adoption, and DevSecOps tool consolidation, which are helping fuel our rapid growth. Finally, GitLab has an open source community and distribution model, which has exposed the value of GitLab to millions of developers and has sped up the maturation of our product through [more than 200 monthly improvements](https://gitlab.biterg.io/goto/937475d38035f496df3501c9b30af5ef) to the GitLab codebase from our users.

## Strategic challenges
1. **Tension between Breadth and Depth:** Our ambitious single-application product vision means we need to build out feature function value across a very large surface area. With so much to deliver in a single application, it is a big UX challenge to keep the experience simple, consistent, and seamless between DevSecOps phases. Our challenge is to drive the right balance between breadth and depth by retaining a [seed then nurture](https://handbook.gitlab.com/handbook/company/strategy/) approach in new product areas while simultaneously improving existing product areas that generate usage and revenue. Shifting more focus to product depth will allow us to win and retain sophisticated enterprise customers.
1. **GitLab.com and Self-Managed:** Another challenge we face is the balance between our self-managed and GitLab.com offerings. GitLab's early paying customers were more interested in self-managed, and the majority of our customers use this offering today. As a result, we focused heavily on delivering a great self-managed customer experience. However, as the market shifts toward cloud adoption, we are seeing an increasing demand for our GitLab.com offering. We now need to rapidly meet the same enterprise-grade security, reliability, and performance expectations our paying customers have come to expect from self-managed in our SaaS (.com offering).
1. **Wide Customer Profile:** We also serve a wide range of customers, from individual contributor developers to large enterprises, across all vertical markets. This range of deployment options and customer sizes makes our business complex and makes it hard to optimize the customer experience for all customer sizes. Over the past few years, we have prioritized enabling our direct sales channel, but in the process have not focused enough on great customer experiences around self-service purchase workflows, onboarding, and cross-stage adoption.
1. **Competition:** Finally, we have formidable competition from much larger companies, including Microsoft, Atlassian, and Synopsys to name a few. Microsoft is starting to mimic our single application positioning, and while behind us in the journey, have substantial resources to dedicate to competing with GitLab.

## Product Strategy
* **Focus on increasing Stages per Organization [(SpO)](https://handbook.gitlab.com/handbook/product/performance-indicators/#stages-per-organization-spo):** There is a strong correlation between the number of stages customers use and their propensity to upgrade to a paid package. In fact, **adding a stage triples conversion!** Each product group should be laser-focused on driving adoption and regular usage of their respective stages, as it should lead to higher [Net ARR](https://handbook.gitlab.com/handbook/sales/sales-term-glossary/arr-in-practice/#net-arr), reduced churn, and higher customer satisfaction. As outlined in this [user journey](https://handbook.gitlab.com/handbook/product/product-principles/#multi-feature-usage-adoption-journey), the most important additional stages for customers to adopt are Create to Verify and Verify to Release, as each of these adoption steps open up three additional stages to users.
* **Harness the unique power of a single application:** GitLab’s primary point of differentiation is our single application approach. As we continue to drive value in any given stage or category, our first instinct should be to connect that feature or product experience to other parts of the GitLab product. These [cross-stage connections](#cross-stage-efforts) will drive differentiated customer value and will be impossible for point product competitors to imitate. Recognizing this opportunity, we have grown our R&D organization significantly over the past two years, and plan to invest an outsized amount on R&D for the next 2-3 years to extend our lead in executing against the single application product vision.
* **Increase wider-community contributions:** To achieve this ambitious vision more quickly, we will leverage our powerful open source community. Each stage should have a clear strategy for tiering the value of the stage. When stages are early in maturity, we will bias toward including as much functionality in our Core open source version as possible, to drive more rapid adoption and greater community contributions, which will help us mature new stages faster. Once stage adoption is achieved, we can then layer on additional value in paid tiers to encourage upgrades.
* **Make our core journey categories complete:**  We want to ensure the core product usage experience is great, which will lead to more paying customers and improved customer retention.  We intend to maintain our market-leading depth in stages with complete categories, which currently are Verify (Continuous Integration) and Create (Source Code Management and Code Review).  Beyond that, we will endeavor to rapidly mature our offering to complete in Plan (3rd most used stage), Release (4th most used stage), and Secure (important element of our Ultimate tier).
* **GitLab-hosted first:** Most customers don't want to run GitLab themselves (self-managed), so we should build out the offerings where we do it for them (GitLab-hosted). GitLab-hosted includes our SaaS (GitLab.com), any single-tenant offerings, and other GitLab hosted services that self-managed installations can use. Our customer and revenue growth rate for our SaaS offering is faster than our self-managed offering. To meet growing customer demand, our SaaS offering needs to have enterprise-grade security, availability, and performance. We must also ensure [feature parity between self-managed and SaaS](/features/) and that customers have an easy migration path from self-managed to SaaS. Going forward, all new features should be available on SaaS when they are available on self-managed, if not before. We will also begin offering GitLab-hosted services to self-managed customers to provide additional value that may not be feasible to deliver in a self-managed environment, e.g. automated cloud backups. Finally, we expect to offer different GitLab-hosted deployment options for single tenant customers and specific geographic regions to meet the regulatory, security, and data residency requirements of various customer segments.

# Fiscal year product investment themes

Every year at GitLab, we choose some specific areas of emphasis to help guide the teams on the areas of our product that we want to accentuate. This section is used to highlight that emphasis. It is not a comprehensive list of everything we plan to do this year. Direction for each stage and category can be found at the respective [direction pages](https://handbook.gitlab.com/handbook/product/categories/). We are not asking the teams to deviate from their core mission.

Many teams will see themselves contributing to these areas of emphasis directly. The other teams will continue to execute on their mission - that is also important.

The themes are to help facilitate cross-team collaboration when invariably teams working on the 1-year themes may need to collaborate with others. Our guidance is: if any team approaches you to prioritize something that is thematic for this year, consider that as a higher priority than you would normally - as it is in service of the broader product-wide goal that we, as a company, have deemed important to accomplish this year.

See [Product Investment](https://internal.gitlab.com/handbook/product/investment/) (_internal handbook page_) for how we allocate our R&D investment across our [product hierarchy](https://handbook.gitlab.com/handbook/product/categories/#hierarchy).

## FY26

### Key Principles Driving Themes

1. Usability: Users are telling us that we need to better meet their expectations and make the experience more intuitive.
1. Depth: We need to stop doing some of the things we are doing today. Customers are asking us to improve core functionality through usability improvements and remove half-completed features.
1. Data Quality: Without more visibility, we cannot make as many data-driven decisions. And neither can our customers. We need to complete our data unification effort to make this easier.
1. Deployment Parity: All three deployments (GitLab.com, GitLab Dedicated, Self-Managed) will have feature parity (with the exception of “admin area” topics on .com and Dedicated).

### R&D Investment Themes

For FY26, the four key R&D investment themes we are focused on are:

1. [Win with DevSecOps platform completeness](#win-with-devsecops-platform-completeness)
1. [Differentiate with AI across the Software Development Life Cycle (SDLC)](#differentiate-with-ai-across-the-sdlc)
1. [Lead with SDLC insights and reporting](#lead-with-sdlc-insights-and-reporting)
1. [Elevate customer-centricity to customer obsession](#elevate-customer-centricity-to-customer-obsession)

#### Win with DevSecOps platform completeness

We will focus primarily on core DevSecOps platform capabilities across SCM, CI, CD, security, compliance, and enterprise agile planning with the goal to achieve a leadership position or extend our existing leadership position. We will drive Premium and Ultimate value by helping propel free-to-paid conversion through product-led growth / feature discovery moments.

#### Differentiate with AI across the SDLC

We will introduce new as well as improve existing GitLab Duo AI capabilities within our core DevSecOps platform capabilities. We will also bring ModelOps features to general availability, including a focus on enabling customers to work with native data science workloads within GitLab.

#### Lead with SDLC insights and reporting

We will focus on deepening the types, and quality of metrics, as well as pulling metrics from third party integrations, with the goal of making GitLab the central component to understanding SDLC insights. We will also provide reporting of feature usage enabling customers to understand what features and capabilities are being used by their teams as well as what usage is connected to Premium and Ultimate tiers, or are features and capabilities included in add-ons.

#### Elevate customer-centricity to customer obsession

We will focus on addressing use case adoption issues as well as improving user experience within onboarding to improve our customer's time-to-value for core DevSecOps platform capabilities. We will improve customer experience improve ease-of-use for SMB/commercial customers with license management and self-service workflows. Based upon and informed by the pricing research completed in FY25, we will also implement an updated pricing strategy.

## FY25

### Key Principles Driving Themes

1. Depth over Breadth: For the past several years we have focused on breadth over depth. This has allowed us to show our direction as a company and define the DevOps Platform market. In FY24, we pivoted to depth over breadth as product depth allows us to win and retain sophisticated enterprise customers. We will continue our focus on depth throughout FY25.
1. Drive Adoption of Ultimate: Due to the increasing demands for security and compliance in software development, GitLab Ultimate continues to gain popularity with our customers. We will focus on increasing the value of Ultimate by not only improving security and compliance functionality but also adding value from other key areas within our platform like Plan, Verify, and Data Science.
1. Differentiate: Our primary point of differentiation is our [single application](https://handbook.gitlab.com/handbook/product/categories/gitlab-the-product/single-application/) approach: all aspects of our [DevSecOps platform](/platform/) work seamlessly together, right out of the box, and can be tailored to the specific needs of each organization.

### R&D Investment Themes

For FY25, the four key R&D investment themes we are focused on are:

1. [Enable AI/ML Efficiencies Across DevSecOps](#enable-aiml-efficiencies-across-devsecops)
1. [Drive Use Case Adoption to Fully Realize Value](#drive-use-case-adoption-to-fully-realize-value)
1. [Differentiate on DevSecOps Platform](#differentiate-on-devsecops-platform)
1. [Strengthen Our SaaS Deployments & Capabilities](#strengthen-our-saas-deployments--capabilities)

#### Enable AI/ML Efficiencies Across DevSecOps

AI as part of software development has continued to mature and has become the number one topic in our customer discussions. To meet our customers’ needs and the evolving market landscape, we will take a three pronged approach to AI (GitLab Duo, ModelOps, AI agents) as part of our DevSecOps platform providing us differentiation in the market.

#### Drive Use Case Adoption to Fully Realize Value

CI and CD are critical to the success of Premium, while security and governance drives value in Ultimate. We will increase our focus on adoption of these areas - ensuring that customers realize the value of the capabilities they have paid for. This will continue to reduce churn, drive free-to-paid conversion, and increase up-tiering from Premium to Ultimate.

#### Differentiate on DevSecOps Platform

Toolchain consolidation continues to come up with customers as well as in our annual DevSecOps survey. We will capitalize on our position as the enterprise DevSecOps platform by continuing to expand our planning capabilities, continuing to mature our metrics and reporting, and bring new SCM capabilities to general availability.

#### Strengthen Our SaaS Deployments & Capabilities

GitLab.com and GitLab Dedicated continue to grow in popularity as more organizations need to undergo digital transformations however do not want the overhead of self-hosting their DevSecOps platform. We expect this trend to continue in FY25 and will invest in our SaaS deployments to ensure they meet our customers’ expectations.


## DevSecOps stages



DevSecOps is a broad space with a lot of complexity. To manage this within GitLab,
we break down the [DevSecOps lifecycle](/solutions/devops-platform/)
into a few different [sections](https://handbook.gitlab.com/handbook/product/categories/#hierarchy), each with its own direction page you can review.


  
    
  
    
  
  
  
  
  
    
      
      
    
  



### Your contributions

In addition to addressing the [DevSecOps lifecycle](/solutions/devops-platform/) internally through the above sections, [contributions from the community](/community/contribute/) also help increase our rate of innovation, which [helps mature](https://handbook.gitlab.com/handbook/company/strategy/#seed-then-nurture) the stages of our [DevSecOps platform](/platform/). These community contributions are an important part our [company mission](https://handbook.gitlab.com/handbook/company/mission/#contribute-to-gitlab-application) and [strategy](https://handbook.gitlab.com/handbook/company/strategy/#assumptions).

[Our issue tracker](https://gitlab.com/gitlab-org/gitlab/issues) contains requests made for features and changes to GitLab. Contributing is the best way to
get a feature you want included as we continually merge code to be released in the next version. Please see our [Contribute to GitLab page](/community/contribute/) for more details such as guides to get started contributing, areas looking for contributions, and contribution
acceptance criteria.

## Personas

[Personas](https://handbook.gitlab.com/handbook/product/personas/) are the people we design for. Developers, security professionals, and operations professionals are currently the primary personas we focus on, and we tailor our user experience to their needs. We want GitLab to be the main interface for people in these roles, so they can show up at work, start their day, and load up GitLab. And that’s already happening.

But there are a lot of other roles involved with the development and delivery of software. That is the ultimate GitLab goal - where everyone involved with software development and delivery uses a single application so they are on the same page with the rest of their team. We are rapidly expanding our user experience for [Designers](https://handbook.gitlab.com/handbook/product/personas/#presley-product-designer), [Compliance Managers](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager), [Product Managers](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager), and [Release Managers](https://handbook.gitlab.com/handbook/product/personas/#rachel-release-manager). We’ll also be expanding to the business side, with Executive visibility and reporting. While we’re still calling it DevSecOps, we’re really expanding the definition of DevSecOps and delivering it all as a single application.

## Mitigating low-end disruption

GitLab is not immune to disruption. In some ways, it is a sign of success that GitLab is now at a scale where we have to think about low-end disruption. Arguably, a few years ago, GitLab was a low-end disruptor.

Clayton Christensen defines [low-end-disruption](https://online.hbs.edu/blog/post/4-keys-to-understanding-clayton-christensens-theory-of-disruptive-innovation) as follows:

_Low-end disruption refers to businesses that come in at the bottom of the market and serve customers in a way that is "good enough." These are generally the lower profit markets for the incumbent and thus, when these new businesses enter, the incumbents move further "upstream." In other words, they put their focus on where the greater profit margins are._

Our perspective is that low-end disruption is an additional and critical sensing mechanism. This is especially true for the DevSecOps market. We look at the following attributes to figure out if a low-end disruption has anything close to potential product-market resonance. This list is an adaptation of the [Product Zeitgeist Fit](https://a16z.com/2019/12/09/product-zeitgeist-fit/).

   - **Builder Enthusiasm**: Are the most talented, hardest working, or most-in-demand people - the engineers, the developers - so intrigued by the approach that they are working on it, excited by it, and trying to make it a thing?  If that is the case, then there is a good chance that they will eventually make it happen, moving beyond the fringes to the mainstream. Number of stars, forks, and contributions in the repo are some metrics to look for here.
   - **Despite Test**:  When people are using a product despite the fact that it’s not the best thing out there, or, in some cases, that it’s straight-up terrible, it’s a great sign. It shows that the product has a line into something emotional, not solely functional. Wanted, not just needed. In the early days, these products can often feel misunderstood or controversial. At first blush, the conceit may even raise a few eyebrows. But to the people who have been working on those products, they’re so clearly elegant, if temporarily imperfect, solutions to big and important problems that they seem almost obvious once they recognize it. Google Trends and posts on Hacker News are some things to monitor here.
   - **T-shirt Test**:  If people with no connection to the company are wearing their t-shirts or putting their stickers on their laptops or wearing their socks, that  desire to associate with the idea indicates as much a movement as a product.

A reason low-end disruptors are able to enter the market is that the feature-absorption by users is lower than the feature-velocity of the established vendor. To address this we  are focused on a [working-by-default configuration principle](https://handbook.gitlab.com/handbook/product/product-principles/#configuration-principles).

## Maturity

As we add new categories and stages to GitLab, some areas of the product will be deeper and more mature than others. We publish a
list of the categories, what we think their maturity levels are, and our plans to improve on our [categories page](https://handbook.gitlab.com/handbook/product/categories/).

We strive to be the best product in the market and to be complete. As the market, customer needs, competitive landscape, and technology change, we should expect our maturities to also change, including changing to a lower maturity rating. By embracing a [focus on improvement](https://handbook.gitlab.com/handbook/values/#focus-on-improvement) and [low level of shame](https://handbook.gitlab.com/handbook/values/#low-level-of-shame), we encourage moving a maturity down. This is a strong indicator that we are realists about our product with an eye on achieving the best results for our customers.

## Scope

We try to prevent maintaining functionality that is language or platform
specific, because they slow down our ability to get results. Examples of how we
handle it instead are:

1. We don't make native mobile clients. Instead, we make sure our mobile web pages are great.
1. We don't make native clients for desktop operating systems. We make our web application great—for example, GitLab was the first to have merge conflict resolution in our web application. People can also use [Tower](https://www.git-tower.com/) or other clients.
1. For language translations, we [rely on the wider community](https://docs.gitlab.com/ee/development/i18n/translation.html).
1. For code navigation, we're hesitant to introduce navigation improvements that only work for a subset of languages.
1. For building and testing with [Auto DevOps](https://docs.gitlab.com/ee/topics/autodevops/), we use Heroku Buildpacks.

Outside our scope are Kubernetes and everything it depends on:

1. **Network** (fabric) [Flannel](https://github.com/coreos/flannel/), Openflow, VMware NSX, Cisco ACI
1. **Proxy** (layer 7) [Envoy](https://www.envoyproxy.io/), [nginx](https://nginx.org/en/), [HAProxy](http://www.haproxy.org/), [traefik](https://traefik.io/)
1. **Ingress** [(north/south)](https://networkengineering.stackexchange.com/a/18877) [Contour](https://github.com/heptio/contour), [Ambassador](https://www.getambassador.io/),
1. **Service mesh** [(east/west)](https://networkengineering.stackexchange.com/a/18877) [Istio](https://istio.io/), [Linkerd](https://linkerd.io/)
1. **Container Scheduler** we mainly focus on Kubernetes, other container schedulers are: CloudFoundry, OpenStack, OpenShift, Mesos DCOS, Docker Swarm, Atlas/Terraform, [Nomad](https://nomadproject.io/), [Deis](http://deis.io/), [Convox](http://www.convox.com/), [Flynn](https://flynn.io/), [Tutum](https://www.tutum.co/), [GiantSwarm](https://giantswarm.io/), [Rancher](https://github.com/rancher/rancher/blob/master/README.md)
1. **Package manager** [Helm](https://github.com/kubernetes/helm), [ksonnet](https://ksonnet.io/)
1. **Operating System** Ubuntu, CentOS, [RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux), [CoreOS](https://coreos.com/), [Alpine Linux](https://alpinelinux.org/about/)

During a presentation of Kubernetes, Brendan Burns talks about the four Ops layers
at [the 2:00 mark](https://youtu.be/WwBdNXt6wO4?t=120):

1. Application Ops
1. Cluster Ops
1. Kernel/OS Ops
1. Hardware Ops

GitLab helps you mainly with application ops. And where needed, we also allow you
to monitor clusters and link them to application environments. But we intend to
use vanilla Kubernetes, instead of something specific to GitLab.

Also outside our scope are products that are not specific to developing,
securing, or operating applications and digital products.

1. Identity management: Okta and Duo, you use this mainly with SaaS applications
   you don't develop, secure, or operate.
1. SaaS integration: Zapier and IFTTT
1. Ecommerce: Shopify

In scope are things that are not mainly for SaaS applications:

1. Network security, since it overlaps with application security to some extent.
1. Security information and event management (SIEM), since that measures
   applications and network.
1. Office productivity applications, since
   ["We believe that all digital products should be open to contributions, from legal documents to movie scripts and from websites to chip designs"](https://handbook.gitlab.com/handbook/company/strategy/#why)

We expect GitLab to continue to grow, and we have several ideas for [possible future stages](https://handbook.gitlab.com/handbook/product/categories/#possible-future-stages)

## Quarterly Objectives and Key Results (OKRs)

To make sure our goals are clearly defined and aligned throughout the
organization, we make use of OKRs (Objectives and Key Results). Our [quarterly Objectives and Key Results](/company/okrs/)
are publicly viewable.

## How we plan releases

At GitLab, we strive to be [ambitious](https://handbook.gitlab.com/handbook/product/product-principles/#how-this-impacts-planning),
maintain a strong sense of urgency, and set aspirational targets with every
release. The direction items we highlight in our [kickoff](https://handbook.gitlab.com/handbook/product/product-processes/#kickoff-meetings)
are a reflection of this ambitious planning. When it comes to execution, we aim
for
[velocity over predictability](https://handbook.gitlab.com/handbook/engineering/development/principles/#velocity-over-predictability).
This way, we optimize our planning time to focus on the top of the queue and
deliver things fast. We schedule 100% of what we can accomplish based on past [Development Department merge request rate](https://handbook.gitlab.com/handbook/engineering/development/performance-indicators/#development-department-mr-rate)
and availability factors (vacation, contribute, etc.).

See our [product handbook on how we prioritize](https://handbook.gitlab.com/handbook/product/product-processes/#how-we-prioritize-work).

## Previous releases

On our [releases page](/releases/), you can find an overview of the most
important features of recent releases and links to the blog posts for each
release.

## Upcoming releases

GitLab releases a new version [every single month](/blog/why-we-shift-objectives-and-not-release-dates-at-gitlab/). You can find the
major planned features for upcoming releases on our [upcoming releases page](/upcoming-releases/) or see the [upcoming features for paid tiers](/direction/paid_tiers/).

Note that we often move things around, do things that are not listed, and cancel
things that _are_ listed.

## ML/AI at GitLab

With Gitlab 15.4, Suggested Reviewers was released as our first customer-facing ML/AI technology in production features. We have additional ambitions [in the near future](/direction/modelops/ai_assisted/) for several types of problems. This is the focus of our new [ModelOps stage](/direction/modelops/).

## Cross-Stage efforts

GitLab consistently strives to deliver a cohesive experience that enables workflows that span the DevSecOps loop. We have a number of existing capabilities and planned improvements that do just that:

- TBA

#### Footnotes

1. IDC, Worldwide DevOps Software Tools Forecast, 2020–2024, Doc # US45188520, July 2020
