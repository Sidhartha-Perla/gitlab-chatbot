---
layout: markdown_page
title: "Group Direction - Custom Models"
description: "Focused on grounding and enriching AI models with Customer data to produce higher quality model outputs"
canonical_path: "/direction/ai-powered/custom_models/"
---

## On this page
{:.no_toc}

- TOC
{:toc}

## Custom Models

| | |
| --- | --- |
| Stage | [AI-powered](/direction/ai-powered/) |
| Group | [Custom Models](/direction/ai-powered/custom_models) |
| Maturity | [Available](/direction/#maturity) |
| Content Last Reviewed | `2024-10-05` |

# *** Self-Hosted GitLab Code Suggestions and GitLab Duo Chat in Now in Beta ***

GitLab Duo Self-Hosted is now generally available for Gitlab Duo Chat and Code Suggestions. With GitLab Duo Self-Hosted, customers can now enable self-hosted models on their self-managed Gitlab environment using supported model platforms and models.

With GitLab Duo Self-Hosted, you can use models hosted either on-premise or in a private cloud. We currently support open-source Mistral models on vLLM or AWS Bedrock, Claude 3.5 Sonnet on AWS Bedrock, and OpenAI models on Azure OpenAI.

For more information on how to set-up your self-hosted model, see [GitLab Duo Self-Hosted documentation] (https://docs.gitlab.com/administration/gitlab_duo_self_hosted/). For information on how to trial GitLab Enterprise, see [Get Started with GitLab Duo] (https://about.gitlab.com/solutions/gitlab-duo-pro/sales/?toggle=gitlab-duo-pro).

## Overview

The [Custom Models group ](https://gitlab.com/groups/gitlab-org/-/epics/13068) is dedicated to empowering GitLab users with the flexibility to deploy and customize GitLab Duo Features within their local environments. We also aim to allow customers to adapt Duo Features with their own data, based on their own code, needs, requirements and styles. Our goal is to give customers a more tailored Duo experience.

We will leverage a variety of open source and private-cloud hosted AI models to enable GitLab Duo functionality on all GitLab surfaces, to include Air-Gapped, Self-Managed, Dedicated, and Gitlab.com. We will ensure that supported features are of the highest possible quality using GitLab’s [validation process](https://about.gitlab.com/blog/2024/05/09/developing-gitlab-duo-how-we-validate-and-test-ai-models-at-scale/), and support customers in tailoring GitLab Duo features with their own source code and data. We will also work with other teams within GitLab to explore opportunities for customizing AI models across the platform. 

# What Drives The Need For Custom Models? 

Regardless of how customers access GitLab, they deserve the chance to leverage Duo features. Customers have a wide variety of security and compliance requirements, some of which may preclude them from utilizing our existing Duo features that are enabled through GitLab.com. Providing customers with a self-hosted deployment option for Duo features will allow them to reap the benefits of AI while meeting their security and compliance requirements.

Customers may also want to adapt their Duo experience more directly to their own organization. For example, a customer may want the ability to adapt Code Suggestions to be based on their own code base so that any suggestions match their unique coding styles, standards, and programming language of preference. In addition, customers may want to be able to orient Duo Chat to their internal knowledge bases to answer questions on their own documentation. 

## Strategy 

The Custom Models team has dual focus of 1) enabling GitLab Duo features by leveraging customer-hosted open source (OS) models and 2) enabling customization of Duo features grounded in customer data. 

### [Self-Hosted Models ](https://gitlab.com/groups/gitlab-org/-/epics/13069)

The Custom Models team is currently primarily focused on delivering self-hosted versions of existing [Gitlab Duo features](https://docs.gitlab.com/ee/user/gitlab_duo/index.html). We are actively iterating on self-hosted support to Code Suggestions and Gitlab Duo Chat. Self-hosted Code Suggestions [moved from experimental to beta](https://about.gitlab.com/releases/2024/10/17/gitlab-17-5-released/#use-self-hosted-model-for-gitlab-duo-code-suggestions) in 17.5, and General Availability (GA) for both self-hosted Code Suggestions and Chat are coming soon. GA for self-hosted Code Suggestions and Chat will include support for Mistral models on both vLLM and Amazon Bedrock, as well as Claude models on Amazon Bedrock. GA of these features will be closely followed by additional support for GPT models on AzureOpenAI, as well as Llama 3 models on AWS GovCloud, AWS Bedrock, and vLLM.

Up-to-date information on our feature support and expected delivery milestones can be found on our [Self-Hosted Model Deployment epic](https://gitlab.com/groups/gitlab-org/-/epics/13069), as well as on the [Custom Models roadmap](https://gitlab.com/groups/gitlab-org/-/epics/14665).

Our aspirational goal is to support a self-hosted (open-source based) version of each Gitlab Duo feature in line with the GA release of that feature. Due to the complexities of building a self-hosted version of a feature, this may not always be possible. This is predicated upon pre-GA validation of the feature, and an understanding of a feature as reaching a “mature” stage. Both validation and feature maturity creates a standard upon which to build and compare self-hosted feature variants. While self-hosted Duo features may not necessarily be as performant as features based on large, provider-hosted, 3rd party models, each feature should be validated as generally correct, useful, and reliable. Custom Models will also factor in customer demand, feasibility, and other relevant factors when determining support.

Support for self-hosted versions of a Duo feature will be predicated upon following a data-centric approach. An understanding of the domain for each feature, as well as the performance of available open source models within that domain, are essential to this approach. Models chosen for self-hosted model support will be based on both customer demand and optimal models for a feature. 

Prior to developing self-hostable Duo features, the Custom Models team will first identify potential OS foundation models within the required domain space. Once Custom Models has identified the optimal OS model for a feature, we will baseline the performance of that model or models to understand its strengths and weaknesses. Custom Models will then develop prompts specific to that model, and determine the appropriate architecture. To the extent that it is possible and sensical, we will attempt to leverage existing elements of the feature that we are seeking to adapt to self-hosting (i.e. pre- and post-processing, applicable data flows, etc). 

### [Customization](https://gitlab.com/groups/gitlab-org/-/epics/13070)

Customization is currently a secondary focus of the Custom Models group. Not all Duo features will benefit from a customized approach and we are assessing the added value of customization for several of the Duo features. Our first approach to customization of Duo features is grounded in a Retrieval Augmented Generation (RAG) approach. Our first customization approaches with RAG consider leveraging customer data to inform Code Suggestions Additional information on our considerations for customization can be found on our [Model Personalization epic](https://gitlab.com/groups/gitlab-org/-/epics/13070), with additional details on our [RAG for Model Personalization epic](https://gitlab.com/groups/gitlab-org/-/epics/13391). 

### Logging 

As we advance support for self-hosted models and customization approaches, we need to allow customers visibility into their own LLM flows for debugging, auditing, validation, and potentially accumulating data sets for supervised fine tuning. To that end, Custom Models will enable customer-facing logging (not visible to GitLab) on self-managed instances. Additional information can be found on the [Logging epic](https://gitlab.com/groups/gitlab-org/-/epics/14718). 

### Validation 

As we offer additional configuration options, either in the form of enabling model choice for GitLab Duo features or in customizations, GitLab will not necessarily have insight into the performance of Duo features. Customers will want to assess the performance and functionality of their selected models and customizations. While GitLab has an internally facing validation process via the Centralized Evaluation Framework (CEF), configurations made within a self-managed customer space will not be visible to GitLab. Customers will require the ability to assess the performance of their chosen implementations. We are exploring a UI for validation that is fully integrated into the GitLab platform, allowing users to leverage prompt libraries to establish baselines performances for different models and RAG configurations.This will allow customers to deploy self-hosted models and leverage customization with confidence. Additional information on our plans can be found on the [Customer-Facing Validation epic](https://gitlab.com/groups/gitlab-org/-/epics/14719).

## Focus 

#### Identify and validate models that can be customized using the following criteria:

* open source or available via private-cloud hosting
* minimal computing requirements
* well suited for Duo feature use cases
* high quality output

#### Deeply understand customer privacy and security concerns associated with AI/ML use cases

#### Develop Blueprints For Configuring Self Hosted Models

* Perform customer research to Inventory which GitLab deployments customers are using (Gitlab.com, Dedicated, Self-Managed) and how they would like to deploy self-hosted models.
* Determine architectures for enabling Enterprise users to leverage customized models.
* Assess what security and compliance requirements will we need to consider based on our customer platforms and specifications.

#### Research techniques to enable customer customization of models.

* How can we allow customization without sacrificing the quality of Duo features?
* Techniques under consideration include:
  * RAG
  * Fine-Tuning

#### Validate Customer Modification

Develop or identify a lightweight validation framework that can give customers assurances that customized product is performing at a high level of quality output and haven’t degraded performance of the model

#### What We Are Not Doing

* Bring your own model - we are not currently supporting any and all model; we need to ensure the quality of the features and so will be starting with a set of pre-defined model options.
* We are not supporting personalization at an individual user level, but rather Enterprise-level customization.