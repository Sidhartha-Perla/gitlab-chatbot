---
layout: markdown_page
title: "Category Direction - AI Research"
description: "Identify and explore AI/ML models to support DevSecOps use cases"
---

## On this page
{:.no_toc}

- TOC
{:toc}

## AI Research 

| | |
| --- | --- |
| Stage | [AI-powered](/direction/ai-powered/) |
| Group | [AI Model Validation](/direction/ai-powered/ai_model_validation) |
| Maturity | [Available](/direction/#maturity) |
| Content Last Reviewed | `2024-10-05` |


## Overview
The AI Research category aims to identify and explore AI/ML models to support use cases other GitLab sections, stages, groups are developing to enrich the DevSecOps experience for GitLab users. 

We continuously evaluate AI/ML model vendors, open source models, and generative AI foundation models. Models that show promising results from our initial research and exploration will be further tested via the [AI Evaluation](../ai_evaluation/) platform to be compared against models already supported in our [AI Framework](../../ai_framework/) and that are actively powering [GitLab Duo](https://about.gitlab.com/gitlab-duo/) features including [self-hosted models](../../custom_models/). 

### Evaluation Criteria 
We evaluate models with a wide range of criteria to support our enterprise customer's needs including: 

- Model capabilities 
- Model interface 
- Data Governance policies 
- Security
- Deployment options 
- Track record of organization offering the model 
- And more

## Evaluation Techniques 
GitLab has built an advanced model evaluation platform that we call our prompt library. This contains thousands of human and synthetic generated prompts that we use to evaluate various AI models and different versions of AI models. 

We use this suite of evals to run large scale testing of AI model quality output against both human and synthetic generated benchmarks to evaluate model output quality. We leverage techniques like cosign similarity, embedding similarity, and LLM evaluators (LLMs evaluating other LLM outputs). While no one technique is perfect, we leverage a blend of these techniques to compare quality of different models and versions.

This system allows GitLab to evaluate both new model versions but also updated model versions. We've already leveraged this system to catch issues with model updates pushed by our AI vendors. In some cases it has even detected model drift in models that our vendors did not anticipate or communicate with GitLab. 

While our AI Evaluation suite provides a point in time comparison, we are working to automate testing to run the entire suite against models regularly to detect drift and model regressions continuously. 