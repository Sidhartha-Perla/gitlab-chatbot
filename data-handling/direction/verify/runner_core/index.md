---
layout: markdown_page
title: "Category Direction - Runner Core"
description: "This is the Product Direction Page for the Runner Core product category."
canonical_path: "/direction/verify/runner_core/"
---

## Navigation & Settings

|                       |                               |
| -                     | -                             |
| Stage                 | [Verify](/direction/verify/)  |
| Maturity              | Lovable |
| Content Last Reviewed | `2025-01-15`                  |

### Introduction and how you can help

Thanks for visiting this direction page on the Runner Core category at GitLab. This page belongs to the [Runner Group](https://handbook.gitlab.com/handbook/product/categories/#runner-group) within the Verify Stage and is maintained by [Darren Eastman](mailto:deastman@gitlab.com).

### Strategy and Themes

**Vision**:

- Our vision is a GitLab CI/CD build agent for any compute architecture and any computing stack. Platform administrators and developers can easily install and configure GitLab Runner to run the CI/CD workloads of any scale on the computing stack specific to their software development needs.

**Context**

- GitLab Runner - the near-ubiquitous build agent that executes CI jobs on a target compute platform is a critical foundational pillar of GitLab's [one DevSecOps platform vision](https://about.gitlab.com/direction/#vision). The fundamental problems customers must solve in this product category include installing, configuring, and scaling CI/CD build agents (runners) on public or private cloud infrastructure and securely executing CI/CD jobs on heterogeneous computing architectures, x86-64, ARM, and s390x.

- For customers that run millions of CI/CD jobs monthly, the primary GitLab Runner autoscaling options for CI/CD builds in ephemeral, isolated environments are Kubernetes and public cloud or on-premise virtual machine environments. Therefore, critical needs for this customer segment include consistently fast start times for builds, fast build times as measured by total wall clock time, low CI build failure rates due to runner or runner host infrastructure issues, and minimal operational overhead. Other customers require seamless support for multi-platform and architecture builds, while others need the flexibility to install a build agent according to their organization's security and compliance policies

### 1 year plan

In the calendar year 2026, our major investment themes for **new features and capbilities** are as follows:

- [GitLab Runner Kubernetes Executor - FY26](https://gitlab.com/groups/gitlab-org/-/epics/12691)

### What is next for us
<!-- This is a 3 month look ahead for the next iteration that you have planned for the category. This section must provide links to issues or
or to [epics](https://handbook.gitlab.com/handbook/product/product-processes/#epics-for-a-single-iteration) that are scoped to a single iteration. Please do not link to epics encompass a vision that is a longer horizon and don't lay out an iteration plan. -->

In the next three months (February to April) we plan to deliver these features or capabilities:

- Add additional metrics to the runner Prometheus metrics endpoint - specifically [exposing a duration histogram for the runner `prepare` stage](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/37471).
- [Add fault tolerance to the Runner K8s executor - attach strategy](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/36951)

### What we are currently working on
<!-- Scoped to the current month. This section can contain the items that you choose to highlight on the kickoff call. Only link to issues, not Epics.  -->

We are working working on [pre-requisite testing](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/38458) of the [fault tolerance feature](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/36951) for the Runner Kubernetes executor.

### What we recently completed
<!-- Lookback limited to 3 months. Link to the relevant issues or release post items. -->

- [GitLab Runner Fleet design and configuration guide for Google Kubernetes Engine](https://gitlab.com/gitlab-org/gitlab/-/issues/412945)
- [Support AWS S3 multipart uploads via scoped temporary credentials](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/26921)

### What is Not Planned Right Now

We are not actively working on the following features:

- [Runner Priority](https://gitlab.com/gitlab-org/gitlab/-/issues/14976) - The problem to solve for this viral feature is routing CI jobs to an available or less busy Runner. One use case that has come up in multiple customer conversations is routing CI/CD jobs to public cloud-hosted runners (cloud bursting) when the capacity of on-premise hosted runner infrastructure is at capacity. Using the public cloud for burst-only workloads is critical as it enables customers to keep their cloud costs for runner infrastructure to a minimum. For FY25, we decided not to prioritize work on a solution to this problem due to the complexity of architectural changes needed for the GitLab CI job queueing mechanism. However, recent customer interviews have highlighted how critical this problem is and the urgency of a solution for their expanded use of GitLab CI. Therefore, the next step is a [small iteration](https://gitlab.com/gitlab-org/gitlab/-/issues/419985), which aims to develop a proof-of-concept solution

- [Sticky Runners](https://gitlab.com/gitlab-org/gitlab/-/issues/17497) - For this feature, the problem to solve is that users need to improve CI job performance in scenarios where each job can generate intermediate build elements with hundreds of GBs in size. In the current GitLab CI model, a significant amount of pipeline execution time is due to the uploading and downloading of intermediate build elements between jobs in a pipeline. Given the current Runner executor implementation, i.e., we support several executor types out of the box (shell, docker, Kubernetes), changing the CI job execution paradigm in GitLab is a significant architectural change. The Sticky Runners MVC feature is not in the near-term roadmap due to higher priority features in the Runner core and the Verify stage.

### Best in Class Landscape
<!-- Blanket description consistent across all pages that clarifies what GitLab means when we say "best in class" -->

BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

#### Key Capabilities

When you run a continuous integration pipeline job or workflow, the code in that pipeline must execute on some computing platform to complete your software's building, testing, and deployment. Terms used to describe the software that handles the pipeline code execution include worker, agent, or runner.

So while the basic functionality of pipeline code execution is table stakes in the industry, the ability to efficiently build software on multiple compute platforms with low operational maintenance overhead are critical features for a best-in-class solution.

#### GitLab Runner Value Proposition

1. Autoscaling on Kubernetes or VM's: GitLab Runner includes a fully mature Kubernetes autoscaling solution where CI builds run in one-time use, runner worker pods or the GitLab Runner autoscaling technology for public cloud virtual machine instances where CI builds by default run in ephemeral, one-time use virtual machine instances.
1. Scalability and Flexibility: GitLab Runner is highly scalable, allowing you to run multiple concurrent jobs across different environments. Whether you have a small personal project or a large-scale enterprise application, GitLab Runner can adapt to your needs, providing flexibility in managing your CI/CD workflows.
1. Multi-platform Support: GitLab Runner can be installed on various operating systems, enabling developers to build and test their projects across different platforms and environments. This versatility ensures consistency and reliability throughout the development and deployment pipeline.
1. Distributed Execution: GitLab Runner allows distributed job execution across multiple machines, enabling faster and more efficient CI/CD pipelines. Jobs can be parallelized, reducing overall execution time and improving developer productivity.
1. Easy Configuration: GitLab Runner is seamlessly integrated with GitLab CI/CD and is straightforward to configure. The `.gitlab-ci.yml` file provides a declarative syntax for defining jobs, stages, and dependencies, making it easy for developers to set up and manage their pipelines.
1. Docker Integration: GitLab Runner has native Docker integration, allowing you to leverage the power of containerization for your CI/CD workflows. Docker images can be used as execution environments for jobs, providing consistency and reproducibility in building and testing applications. Red Hat's daemonless Podman container engine is fully supported as a drop-in replacement.
1. Extensibility: GitLab Runner supports various executors, including Shell, Docker, Kubernetes, and more. This extensibility enables integration with different tools and platforms, empowering developers to leverage their preferred technology stack and infrastructure.
1. Security and Isolation: GitLab Runner ensures secure and isolated execution of jobs. Each job runs in its own environment, preventing interference between different jobs and maintaining data privacy and security.

#### Top [1/2/3] Competitive Solutions

| Solution | CI/CD Agent naming convention/brand |Self-Managed Option Availablity|Notes|
| ------ | ------ |------ |------ |
|GitHub Actions| Runners |Available|At its core, GitHub Action Runners are similar to GitLab Runners in that they communicate to a central server via a REST API, execute jobs, and send the logs and artifacts back to the server when finished. However, multi-platform support, native autoscaling on cloud instances, support for Kubernetes as a build environment, concurrency, and parallel CI/CD job execution are more mature in GitLab Runner. As expected, GitHub has continued to invest in features and capabilities to improve the maturity of GitHub Action Runners. For instance, the recently released [Actions Runner Controller (ARC)](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/quickstart-for-actions-runner-controller) enables GitHub Actions Runners to autoscale on Kubernetes clusters. However, as noted by others, there is operational overhead involved in the setup and configuration of ARC. On the GitHub public roadmap, we also notice similar investment themes regarding multi-platform support as GitHub continues to target market segments requiring a self-managed platform.|
| Harness.io   | Harness Delegate                          |Available| Harness currently provides the following types of Delegate: Kubernetes, Shell Script, AWS ECS, Helm, Docker. Though the Delegates perform a similar essential function as GitLab Runner, i.e., executes tasks provided by the Harness Manager, the Delegates' primary purpose is to deploy software to the target platform. In this regard, the value proposition of the [GitLab Agent for Kubernetes](https://docs.gitlab.com/ee/user/clusters/agent/) is a critical consideration when evaluating capabilities in GitLab for developer frictionless cloud-native deployment.
|Nx Cloud|Nx Agents|Available| [Nx Cloud](https://nx.dev) a build system for optimizing CI performance and scaling for monorepos,includes [Nx agents](https://nx.dev/ci/features/distribute-task-execution) which dynamically distrbutes the CI/CD jobs across multiple buiild machines.|
|Jenkins|Agents|Available|In Jenkins, an agent is a software executable that runs a task under the direction of the Jenkins controller.  Like GitLab Runner, a Jenkins agent can run on different computing environments (bare metal, virtual machines, containers, Kubernetes clusters).  Java must be supported and installed on the host OS to run a Jenkins agent. |