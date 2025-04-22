---
layout: markdown_page
title: "Category Direction - AI Evaluation"
description: "An automated and scalable AI/ML model evaluation tool"
---

## On this page
{:.no_toc}

- TOC
{:toc}

## AI Evaluation 

| | |
| --- | --- |
| Stage | [AI-powered](/direction/ai-powered/) |
| Group | [AI Model Validation](/direction/ai-powered/ai_model_validation) |
| Content Last Reviewed | `2024-10-05` |

## Overview

AI Validation is a critical cornerstone for successfully implementing Generative AI solutions. AI Validation provides a mechanism by which to empirically measure the output of Generative AI solutions at scale, enabling data-driven decisions. It empowers methodical iteration on AI features, creating greater efficiency in the creation and implementation of AI-enabled workflows across the platform. AI Validation also ensures the reliability and the quality of AI outputs, mitigating the risks associated with Generative AI.

The AI Validation Team’s Centralized Evaluation Framework supports the entire end-to-end process of AI feature creation, from selecting the appropriate model for a use case to evaluating the AI features’ output. AI Validation works in concert with other types of evaluation, such as SET Quality testing and diagnostic testing, but is specifically focused on the interaction with Generative AI.

The foundation of the Centralized Evaluation Framework is based upon three main elements: a prompt library, [validation metrics](https://about.gitlab.com/direction/ai-powered/ai_model_validation/ai_evaluation/metrics/), and comparative [foundational models](https://about.gitlab.com/direction/ai-powered/ai_model_validation/ai_evaluation/foundation_models/). The prompt library is composed of diverse benchmark datasets tailored to serve as a proxy to various use cases, including code completion, code generation, and natural language questions. Validation metrics provide a basis upon which to assess the accuracy and usefulness of Generative AI outputs against industry benchmarks. The Centralized Evaluation Framework incorporates various validation metrics, to include but not limited to LLM consensus filtering, LLM judges, and cosine similarities. Foundational models provide a baseline for understanding the performance of GitLab AI features against industry standards. Additional information on our validation process can be found [here](https://about.gitlab.com/direction/ai-powered/ai_model_validation/ai_evaluation/procedures/).

The Evaluation Framework enables large-scale tests that are designed to be composable via CLI and API, enabling feature teams to assess the impact of code changes on specific AI-generated content. (For example, if a team is focused on improving output for a specific use case, they can choose to test only on that use case rather than the entire corpus of tests.) Test results may be accessed locally, on BigQuery, or via a feature-specific dashboard. The AI Validation team began with providing support to Code Suggestions, and is now actively supporting Duo Chat. 

## Quick Links

- [validation metrics](https://about.gitlab.com/direction/ai-powered/ai_model_validation/ai_evaluation/metrics/)
- [foundational models](https://about.gitlab.com/direction/ai-powered/ai_model_validation/ai_evaluation/foundation_models/)
- [validation process](https://about.gitlab.com/direction/ai-powered/ai_model_validation/ai_evaluation/procedures/)

## Goal

The AI Validation team continues to iterate on and build the Centralized Evaluation Framework with the goal of expanding support to future AI-powered features, enhancing developer productivity, and instilling confidence in the reliability and value of AI-powered processes for tasks across the software development lifecycle.

The AI Validation category focuses on assessing the performance, tuning parameters, prompt engineering techniques, and quality of algorithms for various AI models. The Centralized Evaluation Framework incorporates numerous open source, as well as industry models from Google, Anthropic, and others.

Current work supports the Duo Chat team’s assessment of chat responses based on correctness, readability, and comprehensiveness. The AI Validation team has leveraged industry models as a benchmark, and both open source and custom datasets have been curated for specific use cases identified by the Duo Chat team. Validation methods appropriate to the chat use case have been employed, including LLM consensus filtering, LLM judges, and cosine similarity scores. The AI Validation team is working hand in glove with the Duo Chat team to enable efficient, data-driven iteration on Chat tool engineering and the production of high-quality responses.

## What's Next & Why

[AI Validation Group Direction](https://gitlab.com/groups/gitlab-org/-/epics/11290 "AI Model Validation Group Direction")

[Our OKRs](https://gitlab.com/gitlab-com/gitlab-OKRs/-/issues/?sort=title_asc&state=opened&label_name%5B%5D=group%3A%3Aai%20model%20validation&first_page_size=20)

FY25 R&D Investment Themes: [Enable AI/ML Efficiencies Across DevSecOps](https://about.gitlab.com/direction/#enable-aiml-efficiencies-across-devsecops)

 Our goal for AI Validation is to enable data-driven decisions in the creation and implementation of GenAI features across the GitLab platform. We have provided support to Code Suggestions and Duo Chat, and will continue to enable efficient iteration on GenAI features. As a long-term initiative, we want to expand our Centralized Evaluation Framework to evaluate various models based on Quality, Cost, and Latency. 

As we move towards that long-term goal, our short-term goals support the scaling of the Centralized Evaluation Framework and include:

* Publishing the centralized blueprint for the end-to-end architecture of the Centralized Evaluation Framework and algorithmic basis for AI evaluation methods.
* Providing ongoing support to Duo Chat, by augmenting Centralized Evaluation Framework datasets with prompt libraries supporting Code Generation, Code Explanation, and Search. We will further add two additional metrics for evaluation.
* Solution validating an API access point for the Centralized Evaluation Framework, providing more uniform access to the prompt library and versioning of inputs (to include models, prompt engineering, and other inputs).
* Solution validating a dynamic dashboard that would provide metrics, updated on a weekly basis, that track model drift and other potential issues. This dashboard would include all production models and previously tested industry benchmark models.

Primary Decision Factors, inspired by this [paper](https://arxiv.org/pdf/2203.02155.pdf):

1. Will the code be honest? (consistent with the facts)?
1. Will the code be harmless (not including completions that might offend)?
1. Will the code be helpful (accomplishing the goal of the coder)? 

