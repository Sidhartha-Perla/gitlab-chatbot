---
layout: markdown_page
title: "Category Direction - Component Catalog"
description: "Reusable pipeline configuration and definitions"
canonical_path: "/direction/verify/component_catalog/"
---

- TOC
{:toc}

## Component Catalog

|                       |                                 |
|-----------------------|---------------------------------|
| Stage                 | [verify](/direction/verify/)    |
| Maturity              | [Minimal](/direction/#maturity) |
| Content Last Reviewed | `2025-01-25`                    |

### Introduction and how you can help

Thanks for visiting this direction page on the Components catalog category at GitLab. This page belongs to the [Pipeline Authoring Group](https://handbook.gitlab.com/handbook/engineering/development/ops/verify/pipeline-authoring/) in the Verify Stage and is maintained by Dov Hershkovitch. You can submit your feature requests using [GitLab issue tracker](https://gitlab.com/gitlab-org/gitlab/-/issues/new).

## Overview

We aim to foster a collaborative community of developers who can easily share, build, and maintain high-quality CI/CD configurations. By providing a platform that serves as a centralized hub for managing all DevOps-related assets within an organization, we aim to empower developers to focus on true innovation and unlock the full potential of the open-source ecosystem. Through our commitment to inclusivity, transparency, and accessibility, we strive to create a continuous learning and improvement culture where every community member can contribute.

### Strategy and Themes

DevOps is all about speed, it delivers value faster by shortening the software development life cycle. Organizations that want to accelerate their DevOps adoption need to set up a working pipeline so other teams can use it to automate their workflow. During the development of a pipeline configuration, engineers frequently encounter the following challenges:

1. *"Where can I find it?"* - Whenever engineers embark on setting up a new pipeline, they often search for existing pipelines in their organization or externally. This is because someone, at some point, has likely attempted to configure a similar pipeline.
2. *"How do I use it?"* - After engineers locate a suitable pipeline to work with, they require clear instructions on effectively using it. This guidance is crucial for understanding the pipeline's functionalities and ensuring its proper usage.
3. *"Does it always work as expected?"* - Engineers often question whether the pipeline is consistently reliable and delivers the expected results. They also evaluate its reusability and whether it can be shared effectively with other teams within the organization. These aspects are vital for determining the pipeline's suitability for wider adoption and collaboration.

While it is possible to solve each problem separately, GitLab believes that we need to solve those problems holistically by building a framework that contains tools that add functionality and improve your CI/CD workflow. We aspire to provide the best-in-class experience for building and maintaining CI/CD pipelines.

Our strategy is to provide an opinionated framework that:

1. Is the SSoT for users to browse and search for the desired pipeline components.
2. Contains shareable and reusable package components that could be attached to any CI/CD configuration.
3. Has an easy way to document the usage of each component.
4. Fosters a collaborative methodology by allowing users to contribute to the catalog by developing and publishing their own components.

We should adopt a bottom-up approach to construct this solution, starting with the smallest building blocks and gradually progressing upwards. By starting from the foundational elements and gradually building on them, we can create a robust and cohesive solution.

### 1 year plan

**November 2024 to January 2025**

- [Enhancing the Release Process of the catalog](https://gitlab.com/groups/gitlab-org/-/epics/12788) - A crucial step in reaching our goal is refining the release process for adaptability. This adjustment will enable us to efficiently and effectively release any resource to the catalog.

**February to April 2025**

- [Support .com components in Self Manage instance](https://gitlab.com/groups/gitlab-org/-/epics/15224) - We aim to empower our self-managed customers to seamlessly integrate and work with components from GitLab.com, ensuring a unified and efficient experience.

- [Developer security workflows](https://gitlab.com/groups/gitlab-org/-/epics/15112) - When publishing or utilizing CI components, teams require a secure and reliable method to verify that the components are free from vulnerabilities and tampering. This safeguards CI/CD pipelines from potential security risks while preserving trust in both internal and third-party components.

**May to July 2025**

- [Support inputs for pipelines](https://gitlab.com/gitlab-org/gitlab/-/issues/438097) - Today, when creating a pipeline, we rely on CI variables to inject dynamic content into the pipeline. Inputs provide a superior interface for this purpose since only the specified inputs can be passed. Inputs support basic types of validation. The input lifecycle is scoped to the pipeline creation via text interpolation.
- [Component visibility dashboard](https://gitlab.com/groups/gitlab-org/-/epics/14027) - We aim to improve visibility into component usage across project pipelines, addressing the current inability to track where components are used. This will enable users to quickly identify projects using outdated versions, notify teams, ensure required components are included, and support lifecycle management, including deprecation.
- [Integrate CI steps to the CI/CD catalog](https://gitlab.com/groups/gitlab-org/-/epics/13725) - We'll focus on the seamless integration of CI Steps into the CI/CD Catalog, ensuring they become a first-class component alongside our existing offerings. Our goal is to provide users with a curated experience that presents a collection of CI Steps alongside CI components (template type), covering a wide range of use cases and scenarios. To learn more about CI/CD please visit the [pipeline composition direction page](direction/verify/pipeline_composition/#1-year-plan)

**August to October 2025**

- [Restrict who can publish components to the Catalog](https://gitlab.com/groups/gitlab-org/-/epics/14060) - We need to provide users with the ability to restrict specific individuals or groups from publishing components to a catalog. This feature would enable organizations to enforce tighter control over catalog contributions, ensuring that only authorized users or teams can publish components
- [Block users from using unofficial components](https://gitlab.com/gitlab-org/gitlab/-/issues/441102) - We want to allow administrators to restrict component domain usage to specific users or groups, ensuring tighter governance and alignment with organizational policies. This capability reflects our commitment to delivering a refined catalog experience that meets enterprise needs while fostering a secure and well-regulated ecosystem

**November to January 2026**

[Mature the CI/CD catalog to a competitive maturity level](https://gitlab.com/groups/gitlab-org/-/epics/11538) - We aim to advance the CI/CD catalog to a competitive level of maturity, providing robust features, seamless usability, and enterprise-grade governance. This evolution will ensure the catalog meets the diverse needs of users, supports organizational goals, and positions GitLab as a leader in CI/CD pipeline management.

If you are interested in improving the Catalog, please checkout the [feedback issue](https://gitlab.com/gitlab-org/gitlab/-/issues/407556).

### Long term vision

We aim to enhance our CI/CD catalog by introducing paid features tailored for enterprise customers, thereby delivering additional value to their operations.

#### Support Self manage customers

In our effort to support all customer segments we would like to help our Self manage customers and customers in an air-gapped environment to easily consume components that exist today in our [.com catalog](https://gitlab.com/explore/catalog). This approach aligns with our overarching goal of driving use case adoption, where every customer, regardless of their setup, can readily explore and implement additional functionalities from our platform.

#### CI Step as first class object

A CI step is a minimum executable unit that the user configures; CI step runs in the context of a job, which enables the composability of jobs in your CI pipelines. A step is a type of component, which means it needs to be a first-class citizen of the Catalog, this translates to the fact that all the overarching features in the Catalog (Search, release, publish, inputs) need to be applied on CI step
The CI Steps epic can be found [here](https://gitlab.com/groups/gitlab-org/-/epics/11535).

#### Analytics

Our goal is to empower users with seamless control over component management across pipelines, ensuring optimal version control and project alignment. This addresses the challenge of users currently lacking visibility into component usage across various project pipelines. Our objective is to provide users with the capability to swiftly identify outdated versions and take prompt corrective actions as needed. This enhancement will foster an environment where users can efficiently manage and update components, promoting both version control precision and project alignment.

#### Inputs improvments
Inputs are the recommended way to pass any parameter to a component. It has multiple benefits over the usage of variables, and since its launch in 15.11, it has been widely adopted by our users and customers. This is why we decided to continue our investment in inputs and increase its scope and flexibility. More information can be found in [this epic](https://gitlab.com/groups/gitlab-org/-/epics/10603).


#### Expanding catalog resource types
Expanding the GitLab CI/CD catalog to accommodate multiple resource types will broaden its scope, enhance its utility, and cater to a wider range of development and deployment needs:
* Project Templates: Introduce project templates to encapsulate entire project structures, including source code, configuration files, and predefined CI/CD configurations. This streamlines project initiation with standardized setups, reducing setup time and ensuring consistency across projects.
* Container Registry Integration: Integrate the catalog with the container registry to host and manage container images. This empowers teams to store, version, and share container images directly through the catalog. Users can discover and deploy container images to various environments, enhancing application deployment consistency and reliability.
* Integration with 3rd-Party Apps: Integrate the catalog with third-party applications to incorporate external tools and services into the development workflow seamlessly.

#### Service catalog
Introduce a service catalog to provide a centralized repository for all services within the organization. This service catalog will store key attributes, enabling engineers to:

* Swiftly troubleshoot outages
* Automate configurations accurately
* Expedite onboarding for new developers
Additionally, automated fulfillment of these requirements will be ensured upon the creation of new services, enhancing operational efficiency and collaboration across teams.

#### AI improvements

* [Intelligent search powered by generative AI](https://gitlab.com/gitlab-org/gitlab/-/issues/412663) - Unlike traditional keyword-based searches, Intelligent Search understands the intent behind user queries, enabling it to provide more accurate and relevant results. In addition, we can leverage AI to prompt for more information about specific inputs required by the user, which will result in configured and fine-tuned components with the relevant inputs. This could enhance the user experience and streamline the process of selecting, configuring, and using components from the catalog.

#### What is next for us

We aim to empower central administrators to manage component creation, usage, and publication within their organizational catalog. We are committed to ensuring the publishing process seamlessly integrates with the organization's standards and existing workflows. Additionally, we want to enable platform administrators with the capabilities to secure and govern the catalog and component workflows. More information can be found in [this issue](https://gitlab.com/groups/gitlab-org/-/epics/14060).



#### Analyst Discussion

* [Notes](https://docs.google.com/document/d/1ZOEl7ycibtxN6dDGfsQlfoc-09p7GXEqDUgCCrocUFQ/edit) from Gartner discussion (internal)
* Related articles
  * [DevEx, a New Metrics Framework from the Authors of SPACE](https://www.infoq.com/articles/devex-metrics-framework/)
  * [DevEx: What Actually Drives Productivity](https://queue.acm.org/detail.cfm?id=3595878)

#### What we recently completed

* [Track components usage via an API query](https://gitlab.com/gitlab-org/gitlab/-/issues/466575) - Provides our users with the visibility into where their components are been across all projects


### Best in Class Landscape

BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities
1. [Centralized Component Catalog:](https://gitlab.com/groups/gitlab-org/-/epics/12153) Create a centralized component catalog that serves as a single source of truth for users to browse and search for pipeline components. The catalog should be easily accessible and provide comprehensive information about each component, including its purpose, usage, and documentation.
2. Shareable and Reusable Components: Enable users to develop and publish their pipeline components to the catalog. Components should be designed to be shareable and reusable, allowing developers to easily attach them to their CI/CD configurations. This promotes collaboration and reduces duplication of effort within the organization.
3. [Versioning: Implement versioning for components](https://gitlab.com/gitlab-org/gitlab/-/issues/427286) to ensure users can pin their pipelines to a specific component revision. This helps in maintaining stability and allows for controlled updates.
4. [Component Abstraction and Encapsulation:](https://gitlab.com/groups/gitlab-org/-/epics/12464) Encourage the development of components that abstract away complex pipeline configuration units. Components should encapsulate implementation details and provide a clear interface, enabling users to use them without needing to know the underlying details.
5. Documentation: Provide a mechanism for users to document the usage of each component. This should include clear guidelines, examples, and best practices to help users understand how to use the components effectively.
6. Collaborative Contribution: Foster a collaborative community where developers can contribute to the component catalog by developing and publishing their own components. Implement mechanisms for peer review, feedback, and contribution management to ensure the quality and reliability of the catalog assets.
7. Accessibility: Design the platform to be inclusive and accessible to all community members. Provide intuitive interfaces, clear navigation, and comprehensive search capabilities, making it easy for users to find the components they need.
8. [Continuous Improvement and Learning:](https://gitlab.com/gitlab-org/gitlab/-/issues/407556) Establish a culture of continuous learning and improvement within the community. Encourage feedback from users, collect analytics on component usage, and iterate on the catalog based on user needs and preferences. Regularly update and enhance the catalog with new components, improved documentation, and additional features based on community contributions.
9. [Securing users workflow:](https://gitlab.com/groups/gitlab-org/-/epics/12713) - we are committed to providing our users with means to ensure the security and reliability of their workflows and underlying capabilities
## Dogfooding
The best way to understand how GitLab works is to use it for as much of your job as possible, this is why we practice [dogfooding](https://handbook.gitlab.com/handbook/values/#dogfooding). We have recently begun collaborating with these internal teams in GitLab which expressed their desire to dogfood some of our features:
\* Engineering Productivity team - This effort is tracked through this [collaboration issue](https://gitlab.com/gitlab-org/quality/engineering-productivity/team/-/issues/141), and the team is currently identifying commonly used CI/CD templates and attempting to convert them into components. Our goal is to understand our customers' challenges when converting their templates into components.
\* Incubation team - This effort is tracked through this [collaboration issue](https://gitlab.com/gitlab-org/gitlab/-/issues/399480).
\* Secure team - We've converted some of our existing templates such as SAST, Secret detection, and more. This effort is tracked through this [collaboration issue](https://gitlab.com/gitlab-org/gitlab/-/issues/390656).
## Competitive Landscape
Notable competitors in this space are:
- GitHub actions with their [actions marketplace](https://github.com/marketplace?category=&query=&type=actions&verification=).
- [Circle CI orbs](https://circleci.com/developer/orbs).
- CodeFresh also provide their users with a [CI step library](https://codefresh.io/steps/).
Watch this walkthrough video of the different contribution frameworks available by these competitors:
 
</figure>

## Glossary

This section defines the terminology used throughout this project. With these terms we are only identifying abstract concepts, and they are subject to changes as we refine the design by discovering new insights:

* **Component**: A reusable single pipeline configuration unit. Use them to compose an entire pipeline configuration or a small part of a larger pipeline..
* **Component Project**: A component project is a GitLab project with a repository that hosts one or more components..
* **Catalog**: Collaborative platform that presents the collection of CI/CD projects and components.
* **Version**: The release name of a tag in the project, which allows components to be pinned to a specific revision, components of the same project and versioned together.
