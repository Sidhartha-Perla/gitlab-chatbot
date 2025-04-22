---
layout: sec_direction
title: "Category Direction - Static Application Security Testing (SAST)"
description: "Static Application Security Testing (SAST) checks source code to find possible security vulnerabilities."
---

- TOC
{:toc}

## SAST - Market context

This context informs our [SAST direction](index.html).

### Context: Know our customers

The ideal/typical customer profile for GitLab SAST is affected by our pricing, our packaging (as part of Ultimate), and the market that our company addresses overall.
Customers approach SAST and other GitLab security products in a way that's somewhat different from other areas of the product.

#### Customer journey

There are at least a few big-picture aspects to mention:

- Our customers are generally trying to **bring developers into their security program**. They're often doing this because there are so many more developers than security engineers. For our customers, security testing is not a "once in a release" task.
  - This applies at any organization size—we have customers with 50 developers and 1 security engineer, or thousands of developers and a team of dozens of security engineers. Notice how, in both cases, each security engineer has to scale their impact to many, many developers!
  - In many cases, these organizations are trying to get wide scanning coverage because their business has scaled faster than their security program.
  - As a result of these factors, our customers tend not to tolerate many false-positive (incorrect) results. They are (sometimes implicitly, sometimes explicitly) willing to accept some false-negative results (missed detections) so that they can avoid the false positives.
- Our customers generally tend to have **more modern technology stacks**. That's because using GitLab is itself an indication that they're at least _attempting_ something like DevOps, DevSecOps, or “digital transformation”.
  - This doesn't mean that every customer is writing web applications and deploying them on Kubernetes or something like that—far from it. For example, we have a lot of hardware companies doing firmware development on C/C++ and banks or other entities building on what you could call “legacy” technologies.
  - However, this does mean that we can largely stick to more-modern languages and ecosystems as we develop features. This is part of why we currently are prioritizing improving result quality rather than expanding the set of languages scanned.
- Because of how GitLab is priced and packaged, our customers typically are **uptiering from Premium to Ultimate** when they have their first experience of GitLab SAST. It is comparatively rare for customers to purchase Ultimate right off the bat, though we want this to happen too.
  - Either way, during their evaluation, they are often in the midst of a time-limited Ultimate trial (typically 30 days).
  - If a customer is upgrading from Premium, they experience a list-price increase of roughly 3x. (The price difference an individual customer sees will vary depending on the terms of their existing contract.)
  - Customers often want to consolidate other products onto GitLab. These are often security tools because of the number of GitLab security features that are Ultimate-only.

#### Big-picture constraints

These large factors have led us to a few foundational design goals and constraints:

- **Developer-oriented:** Our customers are using GitLab SAST to scale up their AppSec programs. They need their developers to contribute to security improvements—or at least avoid making new security mistakes.
- **Fast:** Everyone's busy, and a security tool that doesn't deliver timely results is a security tool that's ignored. Results and guidance need to be available before the developer or security engineer switches to another task.
- **Deeply integrated:** GitLab is a unified DevSecOps platform, and our customers build their SDLC and processes around it. We can deliver uniquely convenient and "sticky" workflows as part of a platform.

#### Next-level details

Those foundational goals are helpful, but not specific enough to guide all decisions. Going one level deeper, we can use beliefs like the following:

- **False positives are disfavored:** Our customers tend to prefer fewer false-positive (incorrect) results. They are willing to tolerate some false-negative results (missed detections) so that they can avoid false positives.
- **We need to explain ourselves:** Our product serves a broad audience, from expert security engineers to junior developers. This means that we must explain potential vulnerabilities clearly—even if we raise a true-positive result, if the user is confused by it result and doesn't believe it's true, we don't get any credit for that!
- **Some results is better than none:** When a scan runs into an error, it's better to provide whatever insights we can correctly produce. We should still make the error visible in an appropriate way, but imagine a customer rolling out SAST to all their projects—it should "just work" and, if it doesn't work, this should not cause noisy pipeline failures or disrupt developer workflows.
- **Design as if scan results will be enforced automatically:** Development teams often do not take action unless they are required to, so our security customers often want to implement automated enforcement. They can't do this unless we are careful to design our findings to be enforceable—for example by giving enough metadata that a policy can target the most-reliable and highest-impact findings while not causing workflows to be disrupted for minor nitpicks or guesses.

### Strategy and themes
<!-- Capture the main problems to be solved in market (themes). Describe how you intend to solve these with GitLab (strategy). Provide enough context that someone unfamiliar with the details of the category can understand what is being discussed. -->

The [customer context described above](#context-know-our-customers) informs our strategy.

#### Meet table-stakes requirements

We need to meet "table stakes" requirements because we aren't creating the market or introducing customers to the concept of a SAST product for the first time.
Nearly all of our customers have used a SAST product, or at least a related product like a linter or quality tool, before.

And, most organizations adopting Ultimate are going to compare us to other tools. Typically, they are either:

1. Trying to use GitLab SAST to **replace another product** they already use (usually paid, but sometimes open-source or free).
    - In this case they often know the incumbent product well. This can be good or bad, since customers will know both the benefits and the frustrations related to that tool!
    - The social/organizational dynamics are most interesting when one team (often Security) wants to keep the incumbent tool, but the other team (often Development) wants to adopt Ultimate. These head-to-heads can be particularly detailed and exacting.
    - Customers differ in how intensively they evaluate GitLab against their incumbent tools. They also differ in how quickly they expect to consolidate their other tools onto GitLab. Some do detailed evaluations as part of the initial evaluation, while others postpone this until closer to a renewal decision.
1. Evaluating which SAST tool they should **adopt for the first time**.
   - In this case we are usually compared against newer-generation, easier-to-purchase tools.

In both cases, customers will design some kind of evaluation or testing process, ideally in collaboration with their account team.
These can be very quantitative, comparing results and FP/FN rates, or they can be more qualitative.
Sometimes the evaluation is on a benchmark app like [DVWA](https://github.com/digininja/DVWA), [JuiceShop](https://github.com/juice-shop/juice-shop), or [OWASP Benchmark](https://owasp.org/www-project-benchmark/); evaluators often view these as "simple tests" so they expect GitLab SAST to perform well on them, even if they are unrepresentative of the organization's typical code.
Other times the evaluation is based on the organization's real code.

The upshot is that we need to perform _well enough_ in these evaluations to get through to the next stage of the evaluation.
In other words, our platform value proposition, or other features like security policies, don't get a chance to compete if we aren't at least _close_ in terms of result quality and clarity.

Similarly, we need to avoid being eliminated for lacking common "checklist" buyer features, like offering cross-file analysis, IDE integration, or ability to implement policies.

#### Lean into unique advantages

Often, the best products rely on some kind of "unfair advantage" against competitors. (For some companies, that's access to a brand-new technology; for others, it's the opportunity to start fresh without a legacy stack and customer base; for others, it's an uncommonly powerful sales and marketing motion; for others it's pricing or packaging.)

We will "punch above our weight" if we leverage GitLab's unique advantages. Those advantages include:

- Our product is a key part of user workflows throughout the SDLC: viewing source code, doing code review in merge requests, using the IDE, building artifacts, running tests, searching, planning, etc. We can build native integrations where other companies would not be able to.
- As a result, we have real-time access to data and events across the SDLC, such as commit history, builds, other information; many other tools do not have this data natively and must connect to it over APIs or other integrations.
- We are part of a unified platform that's prepaid annually, so we can lead customers and users on a gradual adoption or activation journey, progressively increasing the amount of insight and value we provide without requiring them to first buy a new product or pay a bill.

#### Focus on Ultimate, but support Free

GitLab SAST must exist in certain tiers based on our business model.

- **Ultimate:** We focus on Ultimate. Our main focus should be making Ultimate as valuable as we can. That's because security and compliance is a key driver of Ultimate revenue, and this is our role in GitLab's business.
- **All tiers:** "Basic scans" are currently available in all tiers.
  - This is partly due to our historical use of open-source technology and our desire to provide basic security hygiene to all. Today, the Free offering does not play a major part in our business strategy.
  - However, GitLab disfavors removing or uptiering features, so some basic GitLab SAST functionality must be available in Free/Premium.
  - This does not mean that some part of _every aspect of SAST_ is available in Free. For example, features like vulnerability management, vuln tracking, and UI flows are (and should remain) 100% Ultimate-only.
  - Similarly, proprietary technology in which we've invested significant resources will almost always remain Ultimate-only.

#### Don't invest uniformly

Not all features or languages are equal-value.

Our customers expect the features we have previously released to continue to exist, so we disfavor removing capabilities entirely.
This means that we should assume that we need to continue to maintain the support matrix and features we current have. For example, if we have declared support for scanning a particular language, we cannot easily remove it.

However, this _doesn't_ mean that we need to invest the same amount of effort or achieve the same sophistication for every language or feature.
For example, it is completely appropriate to continue to use open-source scanners to power less-commonly-used languages like Apex or Elixir until the appropriate customer demand shows us that we need to invest more resources in developing improved technology for those languages.

#### Operate everywhere

Our technology stack going forward must:

- Support operating in different contexts, including classic "shift left" contexts like the IDE and merge request (code review).
  - The biggest thing to remember is that we need to provide a _consistent_ experience across these contexts.
    - "Consistent" _does not_ mean "identical". For example, in the IDE we are subject to short time deadlines and our goal is to get easy-to-understand fixes in front of developers very quickly. In such cases we can make limitations like only scanning for simpler-to-detect issues (e.g. bad/risky functions) and reserve taint analysis for operational environments where longer-running scans are acceptable.
    - "Consistent" _does_ mean that the product feels like it's actually one product. So, for example, if you dismiss a finding in Vulnerability Management, that same finding should not reappear in the IDE. Or, if you disable a rule in a project, that preference should be applied everywhere that scanning happens.
- We also must support operating in all three types of GitLab Ultimate offerings: GitLab.com (multi-tenant SaaS), GitLab Dedicated (single-tenant SaaS), and self-managed.
  - Self-managed includes operating completely offline (not connected to GitLab cloud services in any way). A significant number of customers do this—often the most security-conscious ones, who also want to use SAST and other security tools.

#### Allow customization, but still be opinionated

Some customers want a product that "just works"—more of a black box than anything.
Others will want to customize scan behavior to detect custom problems, for example insecure use of an internal library, that would not be appropriate to ship in a global ruleset to all customers.
Roughly speaking, most customers are closer to the "black box" mentality; a smaller proportion of security teams prefer the customization approach—typically those who have a Security Engineering approach and build significant hands-on expertise within their teams.

One strength of GitLab as a product is that we offer many basic "primitives" that customers can use in creative ways to achieve their goals.
But, it is easy to allow a product to become very complicated and hard-to-use in the service of endless customization. GitLab's [configuration principles](https://handbook.gitlab.com/handbook/product/product-principles/#configuration-principles) include:

- Ensure a great experience by default.
- Encourage favorable behaviors by limiting configuration.
- Avoid configuration completely when possible.

We should be opinionated about the interfaces we offer, including the types of customizations we support, so that we can give customers simplicity and maintain our own technical flexibility.
For example, customers sometimes want to ban calls to particular libraries or functions.

- One way to offer this is to allow injection of fully custom rules.
- But another would be to accept, as a specific configuration option, a list of function names that should never be called.

The two options here differ greatly in:

- the amount of complexity surfaced to the user—learning a pattern language and a YAML format, for example, versus entering a function name into a form.
- how much the customization dictates other technology choices. While a generic list of banned functions could be consulted by many different scanning systems, a more generic pattern is unlikely to losslessly translate to systems other than the one it was originally designed for.
