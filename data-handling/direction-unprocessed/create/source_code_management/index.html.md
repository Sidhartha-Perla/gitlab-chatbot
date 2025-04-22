---
layout: markdown_page
title: "Category Direction - Source Code Management"
description: "Direction for the Source Code Management group"
canonical_path: "/direction/create/source_code_management/"
---

- TOC
{:toc}

## Source Code Management

| Stage                 | [Create](/direction/create/) |
|-----------------------|------------------------------|
| Maturity              | Loveable                     |
| Content Last Reviewed | `2025-01-28`                 |

## Introduction and how you can help
<!-- Introduce yourself and the category. Use this as an opportunity to point users to the right places for contributing and collaborating with you as the PM -->

Thanks for visiting the category direction page on Source Code Management. The Source Code Management direction page belongs to the [Source Code](https://handbook.gitlab.com/handbook/product/categories/#source-code-group) group of the Create stage, and is maintained by [Marie-Christine Babin](https://gitlab.com/mcbabin).

This direction page is a work in progress, and everyone can contribute:

- Please comment and contribute to issues linked througout this page or contained in our [category epic](https://gitlab.com/groups/gitlab-org/-/epics/12547). Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
- If you would like to share your feedback directly or schedule a video call, please reach out directly to Marie-Christine Babin via [email](mailto:mbabin@gitlab.com).

## Strategy and Themes
<!-- Describe your category. Capture the main problems to be solved in market (themes). Describe how you intend to solve these with GitLab (strategy). Provide enough context that someone unfamiliar with the details of the category can understand what is being discussed. -->
Source Code Management (SCM) is a foundational practice in software development. Building great software depends on teams working well together. Teams can rarely be divided into areas of complete independence.

**GitLab's vision for Source Code Management is the following**: Managing code and data with GitLab is a practice that ultimately sparks collaboration between all team members, by centralizing the sharing and synchronization of both code and data securely, efficiently and intuitively, regardless of the file type or size, making it easy to track, compare and revert changes and understand how code and data evolves over time.

This vision stands in support of [GitLab's mission](https://handbook.gitlab.com/handbook/company/mission/#mission) to make it so everyone can contribute. Teams in industries such as game development, automotive, healthcare, engineering, construction and architecture, and teams working with datasets in machine learning, have dependencies on code and data being tightly coupled to be able to iterate efficiently. As per our [GitLab values](https://handbook.gitlab.com/handbook/values/), we believe iteration enables results and efficiency. Facilitating collaboration for teams iterating with both code and data will help them iterate with less friction, enabling them to achieve results more efficiently.

In support of GitLab's vision for Source Code Management, our strategy is to **enable scale across team management, repository size and file size**. This strategy stands on 3 strategic pillars and one foundational pillar:

### Strategic Pillars

- **Easy administration for large teams**: Scale Source Code Management to large teams efficiently and intuitively.
- **High performance and better collaboration with large binary files**: Handle large binary files effortlessly and collaborate seamlessly between developers and other team contributors, such as artists and designers, to support [GitLab's mission](https://handbook.gitlab.com/handbook/company/mission/#mission) to make it so everyone can contribute.
- **High performance and streamlined workflows with large repositories**: Easily manage and collaborate with large repositories, including monorepos.

### Foundational Pillar

- **Usability at scale**: Manage source code with **confidence** with easy and intuitive workflows.

![Source Code Management Strategy Pillars](../../../images/source_code_management/source_code_direction_pillars.png)

~*Note: SCM is not only the most used function in GitLab but also the one with the longest history as it has been there from the beginning. As a result, we get a lot of feedback and have a long backlog of issues. Therefore, we need to spend a considerable share of our teams’ capacity on issues that are not at the center of this vision but address bugs, stability, security, and scalability to keep our users and customers happy.*~

### Challenges

GitLab's Source Code Management builds on top of Git. [Git](https://git-scm.com/) is the leading Version Control System (VCS). It excels at tracking changes in source code and makes it easy and transparent to merge changes from different developers into one code base. Yet, neither Git nor GitLab SCM are perfect. Here are the current main shortcomings:

- GitLab's SCM UX, has shown to be partly unintuitive. For instance, controls to enforce rules are hard to discover, understand and manage at scale.
- Git is not particularly good at handling binary files. While [Git Large File Storage (LFS)](https://docs.gitlab.com/ee/topics/git/lfs/) aims to address this, it is often deemed not suitable for use cases where teams iterate with a large amount of data such as game development, digital twins development (found in industries such as automotive, healthcare, engineering, construction and architecture) and for teams leveraging machine learning models with large datasets.
- Performance can be impacted when repositories become exceptionally large (even if they do not contain binary files), including for monorepos which are used in several large tech companies. [Partial clone](https://docs.gitlab.com/ee/topics/git/partial_clone.html) addresses some of these issues.

## 1 year plan

<!--1 year plan for what we will be working on linked to up-to-date epics. This section will be most similar to a "road-map". Items in this section should be linked to issues or epics that are up to date. Indicate relative priority of initiatives in this section so that the audience understands the sequence in which you intend to work on them. -->

**Feature Enhancements**

- **In Progress:** [Branch rules for Squash Settings](https://gitlab.com/groups/gitlab-org/-/epics/15526)
- **In Progress:** [Exempt specific files from CODEOWNER rules](https://gitlab.com/gitlab-org/gitlab/-/issues/41914)
- **In Progress:** [Add support for mailmap configurations](https://gitlab.com/gitlab-org/gitlab/-/issues/14909)
- **In Progress:** [Support ignoring commits in blame (`blame.ignoreRevsFile`)](https://gitlab.com/groups/gitlab-org/-/epics/15751)

**UX Improvements**

- **In Progress:** [Directory and single file pages improvements](https://gitlab.com/groups/gitlab-org/-/epics/9913)
- **In Progress:** [Improved validation support for CODEOWNERS](https://gitlab.com/groups/gitlab-org/-/epics/15598)

**Performance & Reliability Improvements**

- **In Progress:** Improve support for Git LFS: [Git LFS performance improvements](https://gitlab.com/groups/gitlab-org/-/epics/10834)
- **In Progress:** [Approvals rule re-architecture](https://gitlab.com/groups/gitlab-org/-/epics/12955)
- **In Progress:** [Reusable Rapid Diffs Architecture](https://gitlab.com/groups/gitlab-org/-/epics/11559)

    Diffs are at the center of the code comparison within GitLab. We're working on a new architecture for diffs that improves performance and allows us to build more features on top of them.

### What is next for us
<!-- This is a 3 month look ahead for the next iteration that you have planned for the category. This section must provide links to issues or
or to [epics](https://handbook.gitlab.com/handbook/product/product-processes/#epics-for-a-single-iteration) that are scoped to a single iteration. Please do not link to epics encompass a vision that is a longer horizon and don't lay out an iteration plan. -->

- [Branch rules for Merge Methods](https://gitlab.com/groups/gitlab-org/-/epics/15327)

   Introducing more flexible merge method options to support a variety of workflows is a critical pillar in source code management. We're evaluating how to introduce more flexible merge method configuration as well as exploring related work to [improve fast-foward merges](https://gitlab.com/gitlab-org/gitlab/-/issues/895) and make [squashed merges more straighforward](https://gitlab.com/gitlab-org/gitlab/-/issues/1822).

- [Commit signing for GitLab UI commits on GitLab.com](https://gitlab.com/gitlab-org/gitlab/-/issues/467692): We are planning for the rollout of commit signing for GitLab UI commits on GitLab.com now that the feature has been delivered for Self-Managed and GitLab Dedicated. Once this is introduced, we will support signing web commits and automated commits made by GitLab for all GitLab.com projects.

- Provide support for internal projects with other teams:
  - [Disaster Recovery Working Group](https://handbook.gitlab.com/handbook/company/working-groups/disaster-recovery/)
  - [GitLab Cells](https://gitlab.com/groups/gitlab-org/-/epics/7582)

### What we are currently working on
<!-- Scoped to the current month. This section can contain the items that you choose to highlight on the kickoff call. Only link to issues, not Epics.  -->

- Providing support for internal projects with other teams:
  - [GitLab Cells](https://gitlab.com/groups/gitlab-org/-/epics/7582)

### What we recently completed
<!-- Lookback limited to 3 months. Link to the relevant issues or release post items. -->

- [Role based CODEOWNER approvals](https://about.gitlab.com/releases/2025/01/16/gitlab-17-8-released/#use-roles-to-define-project-members-as-code-owners)
- [Enhanced branch rules editing capabilities](https://about.gitlab.com/releases/2024/10/17/gitlab-17-5-released/#enhanced-branch-rules-editing-capabilities)

Other important issues recently delivered by the group can be seen in [this list](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=updated_desc&state=closed&label_name%5B%5D=group%3A%3Asource%20code&or%5Blabel_name%5D%5B%5D=direction&or%5Blabel_name%5D%5B%5D=type%3A%3Afeature&first_page_size=20).

### What is Not Planned Right Now
<!--  Often it's just as important to talk about what you're not doing as it is to
discuss what you are. This section should include items that people might hope or think
we are working on as part of the category, but aren't, and it should help them understand why that's the case.
Also, thinking through these items can often help you catch something that you should
in fact do. We should limit this to a few items that are at a high enough level so
someone with not a lot of detailed information about the product can understand -->

The Source Code group is not investing in the following opportunities in the immediate future:

- [Branch read access controls](https://gitlab.com/gitlab-org/gitlab-ee/issues/720)
  - Limiting which branches a user can read in a Git repository is possible in a basic sense, by only advertising a subset of refs, but it is not possible to guarantee that unreachable objects will not be sent to the client. This means that branch read access controls would be very weak, since they could not prevent exfiltration of data they do not have permission to read.

- Path-level read access controls
  - From a commit, Git expects all trees and blobs to be reachable. Although Git supports partial clone and spares checkout, which allow data to be excluded from fetch and checkout, Git expects to be able to fetch missing objects on demand. Deliberately excluding objects by path is likely to cause unexpected failures.

- Report number of lines per contributor
  - [Research](https://gitlab.com/groups/gitlab-org/-/epics/8589#note_1462211450) has shown that reporting the lines of code contributed could hurt individual users as this has a tendency to be misused as a false measure of contribution.

- Improvements to [Project Templates](https://gitlab.com/groups/gitlab-org/-/epics/2767)
  - Due to other priorities, we won't be able to progress [Project templates](https://docs.gitlab.com/ee/user/group/custom_project_templates.html).

## Best in Class Landscape
<!-- Blanket description consistent across all pages that clarifies what GitLab means when we say "best in class" -->
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

### Key Capabilities
<!-- For this product area, these are the capabilities a best-in-class solution should provide -->

This information is maintained on [this internal handbook page](https://internal.gitlab.com/handbook/product/best-in-class/create/#source-code-management)

### Roadmap
<!-- Key deliverables we're focusing on to build a BIC solution. List the epics by title and link to the epic in GitLab. Minimize additional description here so that the epics can remain the SSOT. -->

This information is maintained on [this internal handbook page](https://internal.gitlab.com/handbook/product/best-in-class/create/#source-code-management)

### Top two Competitive Solutions
<!-- PMs can choose to highlight a primary BIC competitor--or more, if no single clear winner in the category exists; in this section we should indicate: 1. name of competitive product, 2. links to marketing website and documentation, 3. why we view them as the primary BIC competitor -->

This information is maintained on [this internal handbook page](https://internal.gitlab.com/handbook/product/best-in-class/create/#source-code-management)

## Maturity Plan
<!-- It's important your users know where you're headed next. The maturity plan section captures this by showing what's required to achieve the next level. The
section should follow this format:

This category is currently at the XXXX maturity level, and our next maturity target is YYYY (see our [definitions of maturity levels](https://about.gitlab.com/direction/#maturity).

- Link to maturity epic if you are using one, otherwise list issues with maturity::YYYY labels)

(For non-marketing categories this section is optional)  -->

This [category is currently of **Loveable** maturity level](https://gitlab.com/gitlab-org/ux-research/-/issues/941) (see our [definitions of maturity levels](https://about.gitlab.com/direction/#maturity).

## Target Audience
<!--
List the personas (https://handbook.gitlab.com/handbook/marketing/strategic-marketing/roles-personas#user-personas) involved in this category.

Look for differences in user's goals or uses that would affect their use of the product. Separate users and customers into different types based on those differences that make a difference.
-->

All GitLab users use the Source Code category. The more intensive users are the following:

1. [Sasha, Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
2. [Priyanka, Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
3. [Delaney, Development Team Lead](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
4. [Cameron, Compliance Manager](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)
