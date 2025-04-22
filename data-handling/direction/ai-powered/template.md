---
layout: markdown_page
title: "Stage Direction - AI-powered"
description: "AI-powered workflows boost efficiency and reduce cycle times with the help of AI."
canonical_path: "/direction/ai-powered/"
---

## On this page
{:.no_toc}

- TOC
{:toc}

## Overview

GitLab is embracing AI/ML technologies within the software development lifecycle, as the most comprehensive AI-powered DevSecOps platform. Since mid 2021,  We've been leveraging AI/ML technologies to enrich features on our platform. We're calling these AI-powered capabilities, [GitLab Duo](https://about.gitlab.com/gitlab-duo/).

The name GitLab Duo is rooted in You + GitLab AI = the AI dynamic duo. GitLab Duo goes beyond just being an AI pair programmer: It is an expanding toolbox of features integrated into the DevSecOps Platform to help teams across the entire software development environment become more efficient.

Duo improves team collaboration and reduces the security and compliance risks of AI adoption by bringing the entire software development lifecycle into a single AI-powered application. At GitLab, we believe everyone can contribute. By bringing GitLab Duo capabilities to every persona who uses GitLab, everyone can benefit from AI-powered workflows and organizations can ship secure software faster.


### Goal
As we continue building GitLab Duo, there are some high level goals that drive our development process.
\*\*AI-powered workflows\*\*
\* Harness the power of AI to enhance and boost efficiency to reduce cycle times in [every phase of the software development lifecycle](https://about.gitlab.com/platform/).
Privacy-first
\* GitLab [we ensures AI model vendors don't use customer data to train their models](https://docs.gitlab.com/ee/user/gitlab\_duo/data\_usage.html#training-data).
Transparent
\* Our [publicly available documentation](https://docs.gitlab.com/ee/user/gitlab\_duo/index.html) describes all AI models used by GitLab Duo and understand exactly how your code base is utilized.
Best AI Model powering each capability
\* We aren't in exclusive agreements with any one AI vendor. We use the best AI model for each task.
AI in all distributions
\* While we innovate with AI first on GitLab.com, our multitenant SaaS platform; we're committed to bringing Duo capabilities to [all GitLab distributions](https://about.gitlab.com/install/) including self-managed, Dedicated instances, and even air-gapped environments.
#### Omniscient
We want GitLab Duo to be as knowledgeable as your most seasoned and tenured employee. That person who you can ask anything to and they are an encyclopedia of knowledge. We don't want to replace that person, but instead help scale them, to every employee in your organization. GitLab Duo will help everyone answer their own questions, learn on the fly, and become more efficient.
GitLab can't do this on our own. While we are working to allow Duo to access data and information across the software development lifecycle, we also rely on our third-party AI model vendors to provide widely knowledgeable foundation models. Together general knowledge and GitLab specific data about your software creates an AI-assistant that truly knows all.
#### Ever Present
What's an assistant, if not always at your side, ready to help at a moments notice. We're building GitLab Duo to meet you wherever you work: the GitLab web UI, the WebIDE, your local IDE, and even your CLI. Infusing the software development lifecycle with AI-powered features means Duo is primed and ready to help, from summarizing content, generating code, reviewing your code, troubleshooting failed CI jobs, or even resolving vulnerabilities. You can do more, faster, with Duo at your side wherever your software development journey takes you.
#### Private & Secure
It's amazing to have a helpful assistant, but not if they are going to tell everyone all your deep dark secrets. GitLab Duo is designed to be private by default and secure. Leveraging modern security techniques, all data in encrypted in transit and at rest with GitLab Duo. Further we have worked with our third-party AI vendors to ensure [they do not retain your data nor use it to train AI models](#). Your data is yours. Period.
We take Duo a step further than most other AI assistant solutions, Duo can function in an offline/air-gapped environment with Duo Enterprise, allowing organizations to host their own models within their own networks to power Duo functionality. Learn more about [self-hosted models]().
Learn more about [Duo data privacy]()
## Groups
The AI-powered stage consists of the following product led groups:
- [Duo Workflow](/direction/ai-powered/duo\_workflow): GitLab's autonomous AI agent .
- [Duo Chat](/direction/ai-powered/duo\_chat/): GitLab's AI-powered DevSecOps assistant.
- [Custom Models](/direction/ai-powered/custom\_models/): Dedicated to empowering GitLab users with the flexibility to deploy and customize GitLab Duo Features within their local networks.
- [AI Framework](/direction/ai-powered/ai\_framework/): Building common tools to support GitLab teams integrating AI/ML technologies into GitLab features.
- [AI Model Validation](/direction/ai-powered/ai\_model\_validation/): Research and Evaluate AI/ML models for use to enrich the GitLab product with Generative AI.
## What's Next & Why
We're actively building many AI-powered features into GitLab Duo, some of our upcoming milestones include:
- \*\*Maturing Duo Enterprise features\*\* ensuring that all our AI-powered features across the software development lifecycle are available to all our customers regardless of their deployment type.
- \*\*Duo Workflow experiment\*\* introducing our vision for the future of software development with automonous AI Agents
- \*\*Expanded and Additional context\*\* to enrich the data that Duo can access and improve it's holistic knowledge of your software projects.
- \*\*Self Hosted Models\*\* to power GitLab Duo in the most restrictive and controlled environments like airgaps and private networks.
- \*\*Inline-chat\*\* for improved user experience while using Duo Chat in code files.
## What we've recently completed
The wider AI industry is moving at light speed, and so are we. We are quickly building to keep up with the rapid innovations in the wider AI/ML market improving our existing Duo capabilities but also introducing new ones.
You can keep up with our latest releases by following our [AI Features documentation](https://docs.gitlab.com/ee/user/gitlab\_duo/index.html)
### 2024
Major achievements include:
- [Duo Pro GA](#)
- [Duo Chat GA](#)
- [Duo Enterprise GA](#)
- [Self-hosted Models Beta](#)
- [Announced GitLab Workflow](#)
### 2023
Major achievements include:
- [Code Suggestions Experimental, Beta, and GA release](/direction/create/code\_creation/code\_suggestions/#short-term-3-6-months-strategy)
- Experimental and Beta release of [Duo Chat](https://docs.gitlab.com/ee/user/gitlab\_duo\_chat/index.html)
- Experimental and Beta release of 15 Generative AI capabilities that we're calling [GitLab Duo](https://about.gitlab.com/gitlab-duo/). Read about these capabilities in our [April AI Fireside chat](https://about.gitlab.com/blog/2023/05/03/gitlab-ai-assisted-features/)
- Initial design and implementation of our [AI Architecture](https://docs.gitlab.com/ee/user/gitlab\_duo/index.html) to support Generative AI use cases.
### 2022
- GA of Suggested Reviewers
- Experimental Code Suggestions
### 2021
- Established the ModelOps stage (later split to create the AI-powered stage)
- [Acquisition of UnReview](#smarter-code-reviewer-suggestions)
- Internal beta of [Automatic Issue Labeling](#automatic-issue-labeling)
#### Smarter Code Reviewer suggestions
> [GitLab acquires UnReview as it looks to bring more ML tools to its platform](https://techcrunch.com/2021/06/02/gitlab-acquires-unreview-as-it-looks-to-bring-more-ml-tools-to-its-platform/)
Integrating [UnReview’s technology](https://about.gitlab.com/press/releases/2021-06-02-gitlab-acquires-unreview-machine-learning-capabilities/) into the GitLab platform marks our first step in building GitLab’s AI Assisted features for DevOps.
#### Automatic Issue Labeling
We are currently actively working on an ML model that automatically labels GitLab internal issues based on issue content. [You'll see GitLab issues](https://gitlab.com/gitlab-org/gitlab/-/issues?label\_name[]=automation%3Aml) with the `automation:ml` label that have been automatically labeled by our model. You can also provide training feedback to the model if it is incorrect by applying the `automation:ml wrong` label. GitLab team members can view a feed of these issues with probability data in Slack in the [#feed-tanuki-stan](https://gitlab.slack.com/archives/C01HM3RA2RE) channel.
We pursued this feature first as a way to get a data science workload working within GitLab's existing CI/CD as well as running on top of production GitLab data and interacting with the GitLab data model. This will set the foundation for work in our MLOps group and our other AI Assisted categories listed above.
## Analyst Landscape
Based on [GitLab’s 2023 What's Next in DevSecOps survey,](https://about.gitlab.com/developer-survey/#ai)
\* AI is becoming more and more embedded in software development.
\* The vast majority (83%) of respondents agreed that it is essential to implement AI in their software development processes to avoid falling behind, and this was consistent across development, operations, and security
\* Organizations are using AI across the software development lifecycle — and that means more than code generation.
\* Developers spend 25% of their time writing new code. That means three quarters of developers’ time is taken up with other tasks beyond code generation.
\* Respondents expressed concerns around data privacy, intellectual property, and security.
\* There is concern around introducing AI into the software development lifecycle, but it’s not extreme: 32% of respondents were “very” or “extremely” concerned about AI being introduced into the software development lifecycle, while 23% were “not very” or “not at all” concerned. The largest proportion, 45%, were “somewhat concerned”
These statistics validate the importance of GitLab’s AI Assisted features for DevOps, and integrating automation and machine learning technology like UnReview into the GitLab platform.
Industry analyst research into successful operationalization of machine learning outlines the many challenges organizations face by adopting point solution technologies. This is contrasted with the business value provided by integrating AI Assisted features, DataOps, MLOps, and ModelOps into existing DevOps processes.
> "With the rapid increase in cloud adoption, spurred by the COVID-19 pandemic, we’re seeing increased demand for cloud-enabled DevOps solutions," said Jim Mercer, research director DevOps and DevSecOps at IDC. "DevOps teams who can capitalize on cloud solutions that provide innovative technologies, such as machine learning, to remove friction from the DevOps pipeline while optimizing developer productivity are better positioned to improve code quality and security driving improved business outcomes."
\* Forrester - [State of TuringBots, 2023](https://www.forrester.com/report/the-state-of-turingbots-2023/RES179746
\* Accompanying blog post: []"AI And Generative AI For The Software Development Lifecycle"](https://www.forrester.com/blogs/ai-and-generative-ai-in-the-software-development-lifecycle/)
\* Forrester - [Future of TuringBots, 2023](https://www.forrester.com/report/the-future-of-turingbots/RES179600)
\* Gartner - [What is Generative AI](https://www.gartner.com/en/topics/generative-ai)
\* Gartner - [Tackling Trust, Risk and Security in AI Models](https://www.gartner.com/en/articles/what-it-takes-to-make-ai-safe-and-effective)
\* McKinsey - [The economic potential of generative AI: The next productivity frontier](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier#introduction)
\* [Retool's 2023 State of AI in Production](https://retool.com/reports/state-of-ai-2023)
### Internal resources
GitLab team members can learn more in our internal handbook:
\* Slack: #ai\_strategy
\* [AI Strategy](https://internal.gitlab.com/handbook/product/ai-strategy/)

*Last Reviewed: 2024-10-05  
Last Updated: 2024-10-05*
</p>
