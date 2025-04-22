---
layout: markdown_page
title: "Category Direction - Portfolio Management"
description: GitLab supports enterprise Agile portfolio and project management frameworks, including Scaled Agile Framework (SAFe), Scrum, and Kanban. Learn more!
canonical_path: "/direction/plan/portfolio_management/"
---

- TOC
{:toc}

## Portfolio Management

|                       |                               |
| -                     | -                             |
| Stage                 | [Plan](/direction/plan/)      |
| Maturity              | [Viable](/direction/#maturity) |
| Content Last Reviewed | `2025-02-12`

### Introduction and how you can help

Thanks for visiting this category direction page on Portforlio Management in GitLab. This page belongs to the [Product Planning](https://handbook.gitlab.com/handbook/product/categories/#product-planning-group) group of the Plan stage and is maintained by Amanda Rueda [E-Mail](mailto:<arueda@gitlab.com>).

This direction page is a work in progress, and everyone can contribute:

 - Please comment and contribute in the linked [issues](https://gitlab.com/groups/gitlab-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=Category%3APortfolio%20Management&first_page_size=100) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=Category:Portfolio+Management). Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
 - If you're a GitLab user and want to discuss how GitLab can improve Portfolio Management tools, we'd especially love to hear from you!


## Strategy and Themes
Our Portfolio Management strategy focuses on delivering a comprehensive, integrated solution for tracking strategic initiatives, aligning cross-functional work, and providing actionable insights to drive project outcomes. By enhancing tools for planning, tracking, and reporting, we enable organizations to manage complex project portfolios within GitLab’s single application framework, seamlessly connecting product and engineering teams.

GitLab supports popular [enterprise Agile portfolio and project management frameworks](https://about.gitlab.com/solutions/agile-delivery/), including Scaled Agile Framework (SAFe), [Scrum, and Kanban](https://about.gitlab.com/solutions/agile-delivery/).


|  Multi-level planning        |      Roadmaps    |    Kanban      |
| ---      | ---      | ---      |
| ![epicstree-direction.png](/direction/plan/portfolio_management/new_epic_tree.png)  | ![roadmap_2023.png](/direction/plan/portfolio_management/roadmap_2023.png)   |![epic_board_2023.gif](/direction/plan/portfolio_management/epic_board_2023.gif)|


### 1 Year Roadmap
We’re committed to enabling workflows that bring clarity to complex project landscapes, giving teams the insights they need to coordinate effectively, stay agile, and adapt to change with confidence. By investing in enhancements to visibility, reporting, and inter-team workflows, we aim to empower users at every level to contribute toward organizational goals, track meaningful progress, and make informed decisions.

Over the next several quarters we'll improve the core Jobs to Be Done (JTBD) for our users across varied workflows. We plan to enable users to maintain focus on their primary tasks while minimizing context switching, bolstering productivity. For example, improvements to dependency mapping, timebox tools, and visualization options empower users to make informed, data-driven decisions in real-time. Our enhancements to epics, issues, and roadmaps are designed to bring greater consistency, aligning the entire planning experience with how users think and work, rather than forcing adaptation to separate systems.

Ultimately, our vision is to make GitLab a comprehensive, intuitive hub for all project management needs, eliminating the need for external tools and creating a seamless experience for project managers, product owners, and developers alike.




#### What we are currently working on


1. [Enhance workflow efficiency with contextual drawer view for quick work item access](https://gitlab.com/groups/gitlab-org/-/epics/10501). You'll now be able to access and manage your work items more efficiently with our new contextual drawer view, accessible from listing pages, boards, detail pages, and roadmaps. This feature allows you to quickly view and edit work item details without navigating away from your current page, significantly reducing context-switching and boosting your productivity throughout your workflow.
1. [Streamline dependency management with consistent blocked and blocking iconography](https://gitlab.com/groups/gitlab-org/-/epics/10623). You'll now have a more consistent and intuitive experience when working with blocked work items (issues and epics) across GitLab's Plan features. We've unified the visual indicators for blocked and blocking items throughout epic boards, issue boards, lists, and roadmaps, making it easier for you to identify and manage dependencies in your projects.
1. [Epic milestones](https://gitlab.com/groups/gitlab-org/-/epics/329). Easily track long-term initiatives by assigning epics, capabilities, and features to milestones.
1. [Consolidated listing page](https://gitlab.com/groups/gitlab-org/-/epics/11918). Refine your backlog and plan with ease. The consolidated listing page offers a streamlined experience that puts all your work at your fingertips.
1. [Epic weight](https://gitlab.com/groups/gitlab-org/-/epics/12273). You can now assign weights to epics, allowing you to estimate and prioritize large-scale initiatives more effectively. This new feature not only helps you with initial planning but also automatically updates the epic's weight as you break it down into smaller issues, giving you real-time insights into the scope and progress of your projects.






#### Next up


1. [Consolidated boards](https://gitlab.com/groups/gitlab-org/-/epics/16800) - One Board for all of your workflows. Power every stage of development from planning to delivery in a single, flexible view.
1. [Saved views](https://gitlab.com/groups/gitlab-org/-/epics/13364). Save and share your preferred views and filters across teams to standardize planning workflows.
1. [Design management for epics](https://gitlab.com/groups/gitlab-org/-/epics/15122) - You can now manage designs across work items at both project and group levels, giving you more flexibility in your workflow. This enhancement supports various team structures and methodologies, allowing you to seamlessly integrate design management into your GitLab experience regardless of how your organization is set up.
1. [Assignees on Epics](https://gitlab.com/groups/gitlab-org/-/epics/4231) - You can now assign epics to individuals, making it clear who is responsible for overseeing the progress. This allows for better visibility into work ownership, streamlined communication, and easier tracking of project status.
1. [Tasks on boards MVC](https://gitlab.com/gitlab-org/gitlab/-/issues/469544) - You can now manage your tasks more efficiently with the new Tasks on Boards feature. This enhancement allows you to view and interact with tasks alongside issues on your boards, giving you a more comprehensive overview of your project's workflow and improving your ability to track and prioritize work items.
1. Improvements to increase the maturity of [Roadmaps](https://gitlab.com/groups/gitlab-org/-/epics/2649) - Roadmaps are an industry standard way in which plans are visualized, and are key to an experience that is lovable by product and project managers. Key functionality like drag and drop editing are missing from our current implementation.


#### What we recently completed


1. [New epic experience](https://gitlab.com/groups/gitlab-org/-/epics/6033) - We launched a new epic experience that improves the structure and usability of epics within Portfolio Management. Delivered in version 17.6 for SaaS users, and 17.7 for self-managed and dedicated users. The update provides an intuitive way to organize and track epics, improving clarity and enabling more effective cross-team collaboration.gn epics to individuals, making it clear who is responsible for overseeing the progress. This allows for better visibility into work ownership, streamlined communication, and easier tracking of project status. With this new experience, we've also shipped the following new epic features:
     1. Customizable Color Options: Color options have been expanded. You can now choose from a larger set of pre-existing values or add custom RGB or hex value. This helps in categorizing and prioritizing tasks visually. Color is a flexible tool to categorize epics. Use cases include creating associations to squads, company initiatives, or levels in the epic hierarchy. Epic color can be viewed on the Roadmap and Epic Boards.
     1. Parent Epics & Ancestry: The new Parent feature allows you to add a parent directly from the epic, just like adding a parent epic from an issue. Ancestry has been moved to the top in a breadcrumb-like manner, displaying the immediate and ultimate parents. This makes it easier to navigate and understand the hierarchy of your epics.
     1. Time Tracking: Time tracking is now available at the epic level. You can log time spent on different parts of the project, ensuring accurate time management. For instance, if a feature is estimated to take 10 weeks, you can log time for each sprint and monitor progress, helping you stay on schedule and within budget.
     1. View on Roadmap: We've replaced the embedded roadmap tab with a 'View on Roadmap' option in the more actions menu. This takes you to the full roadmap page with all its settings and sorting options, filtered by the selected epic. This change offers a more detailed and customizable view of your project's roadmap.
     1. Linking Different Types of Records: You can now link dependencies between different types of records, such as tasks, issues, and epics. This creates a connected view, enhancing traceability and providing a comprehensive overview of related work items. This helps ensure that all related tasks are managed together, improving overall project coherence.
     1. Webhooks for Epics: Users can automate and streamline their workflows by sending real-time updates from GitLab to their preferred tools and services whenever changes occur in epics, enhancing efficiency and collaboration.
     1. Resolve threads: You can now resolve threads in work item discussions, making it easier to manage and track important conversations. This feature allows you to collapse resolved threads by default, helping you focus on active discussions and streamline your workflow within GitLab's work item interface.
     1. Update relationship types on the fly: You'll now be able to change issue relationships directly from the linked item widget, saving you time and reducing frustration. No more deleting and recreating relationships when you need to update them – simply use the new option to switch between 'relates to', 'blocks', and 'is blocked by' with ease, making your issue management more flexible and efficient.
     1. Convert task list to child items: Quickly convert task lists from the description into individual child issues. This update streamlines the process, letting you fill in details as you go, making child item creation faster and more efficient for your workflow.






#### What is Not Planned Right Now

In the next two years:
- We plan to build a flexible planning tool that can be configured to implement SAFe. We do not plan to implement a system that is optimized for SAFe only.
- In order to meet the Portfolio Management vision described in this page, we have decreased investment in our Requirements Management, Test Management and Design Management categories. We will continue to address defects and support community contributions but we are not planning to make significant improvements.

### UX Themes

These UX Themes represent the JTBD we've decided are the most important for our users. We're working on features that improve on the ability to accomplish these goals.

|Theme|[Persona](https://handbook.gitlab.com/handbook/product/personas/)|[JTBD](https://handbook.gitlab.com/handbook/product/ux/jobs-to-be-done/deep-dive/)|
|---|---|---|
|Support product managers in configuring and sharing hierarchy of work items to increase alignment in how planned work is driving larger goals|[Parker](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)|When visualizing the plan of how my strategy will be implemented, I want to display how prioritized items cascade up toward larger vision and business objectives, so I can increase alignment on the overall impact and importance of even the most granular items within my plan. |
|Allow teams to group or relate work items to increase alignment on dependencies or related work.|[Parker](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager) <br><br> [Delaney](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead) |When splitting prioritized initiatives or features into requirements, I want to group related slices of value and surface dependencies, so I can maximize alignment on the scope of a business goal and efficiently plan its incremental delivery.|
|Decrease effort and time it takes for teams to identify and monitor impediments so that they may be better mitigated. |[Delaney](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)  |When reviewing a plan, I want to identify and enable continual monitoring of high risk items, so I can maintain effectiveness of mitigation plans, even as they evolve.|
| Allow product managers to visualize and share progress and completion of goals in order to increase trust with stakeholders|[Parker](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)  |When implementing to a plan, I need to monitor progress (velocity) so I can demonstrate that the team is efficiently capturing value for our stakeholders. |
|Increase alignment of teams by allowing them to visualize status of work within a workflow |[Parker](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager) <br><br> [Delaney](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead) | When collaborating with a team or stakeholders, I want to communicate the current status of work continuously, so I can increase alignment on progress and any impediments that need to be addressed.|
|Support teams in managing their capacity to increase predictability | [Delaney](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead) | When planning a release, I want to prioritize and sequence estimated work based on feasibly, capacity, and ROI, so I can incrementally deliver toward business objectives.|
|Empower users to prioritize work that best drives value|[Parker](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)  | When reviewing proposed initiatives, I want to categorize opportunities based on how efficiently they drive the success of business objectives, so I can increase confidence in items I have prioritized, and feel empowered to say no to less impactful ideas. |
|Increase alignment of teams by allowing teammates to easily update others on progress or status either manually or automatically |[Sasha](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer) | When collaborating with a team or stakeholders, I want to maintain transparency to the status of work, to enable others to self-serve that information, and so I can increase alignment on progress and any impediments that need to be addressed.|
| Support product teams in crafting a SSOT with well-documented requirements|[Parker](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager) |When planning a release, I want to prioritize and sequence estimated work based on feasibly, capacity, and ROI, so I can incrementally deliver toward business objectives. |


## Best in Class Landscape
<!-- Blanket description consistent across all pages that clarifies what GitLab means when we say "best in class" -->

BIC (Best In Class) is an indicator of forecated near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.

### Key Capabilities

| Feature |Description |
| ------ |------|
| Portfolio financial management  |Visibility and insight into funding capacity rather than projects. Instead of determining how much it will cost to achieve the next two milestones, managers determine how much capacity is required to deliver a consistent flow of value. |
|Portfolio level planning |  Identifying which programs to invest in, and how much. Portfolios are largely trying to figure out what initiative to fund, based on when the previous one is scheduled to finish.    |
| Program level planning  |  Breaking large deliverables into chunks that make sense for each team and coordinating the teams' work. Programs need to worry about dependencies and coordination.   |
| Enterprise agile framework (including SAFe) |SAFe support includes the processes, roles, and artifacts that enable scaling across teams, and the ability to plan and track work and assess economic benefits using at a minimum Portfolio SAFe in SAFe v. 5.0. EAP tools may support multiple enterprise agile frameworks commonly used in the industry.|
| Forecasting |[A forecast is a calculation about the future completion of an item or items that includes both a date range and a probability.](https://www.scrum.org/resources/blog/agile-forecasting-techniques-next-decade#:~:text=A%20forecast%20is%20a%20calculation%20about%20the%20future%20completion%20of%20an%20item%20or%20items%20that%20includes%20both%20a%20date%20range%20and%20a%20probability.) Forecasts take the progress to date of all of the programs, then make forward-looking predictions.  |
|Dependency management|Dependencies are the relationships between work that determine the order in which the work items (features, stories, tasks) must be completed by Agile teams. Dependency management is the process of actively analyzing, measuring, and working to minimize the disruption caused by intra-team and / or cross-team dependencies. |
| Roadmapping |  [Roadmaps are the glue that link strategy to tactics. They provide all stakeholders with a view of the current, near-term, and longer-term deliverables that realize some portion of the Portfolio Vision and Strategic Themes.](https://www.scaledagileframework.com/roadmap/#:~:text=Roadmaps%20are%20the%20glue%20that%20link%20strategy%20to%20tactics.%20They%20provide%20all%20stakeholders%20with%20a%20view%20of%20the%20current%2C%20near%2Dterm%2C%20and%20longer%2Dterm%20deliverables%20that%20realize%20some%20portion%20of%20the%20Portfolio%20Vision%20and%20Strategic%20Themes.)  _© Scaled Agile, Inc._  |
| End-to-end visibility to the value stream  | This capability indicates the tool’s ability to show the progress of software throughout the value stream from ideation through to production realization of the customer and business value.|
| Collaboration  |  Collaboration tools have the highest value for distributed organizations. These tools can range from virtual boards and team rooms to threaded conversations or advanced, work-item-context chat tools.  |


### Top Competitive Solutions


1. [Jira Align](https://www.atlassian.com/software/jira/align/solutions). Jira Align (formerly known as AgileCraft) was acquired by Atlassian in early 2019. It's a cloud-based product that connects securely to one or more instances of Jira (of any flavour: Cloud, Server, or Data Center) to give insight into the state of play for all of the teams in an enterprise-level organisation. ([reference](https://www.adaptavist.com/blog/introduction-to-jira-align#:~:text=Jira%20Align%20(formerly,enterprise%2Dlevel%20organisation.)))
     - Based on strong reviews from Gartner, Forrester, Peer Insights, and my own user review, Jira Align is the **top competitor** in the Enterprise Agile Planning space due to its full support for enterprise agile frameworks such as SAFe, excellent roadmapping, forecasting, dependency management, and collaboration capabilities. While Planview and Digital.ai also scored high with analysts, I found their UX heavy and dated. Jira Align scores well in portfolio management functionality and usability.
1. [Planview AgilePlace](https://www.planview.com/products-solutions/products/agileplace/). Planview's solutions enable organizations to connect the business from ideas to impact, empowering companies to accelerate the achievement of what matters most. Planview’s full spectrum of Portfolio Management and Work Management solutions create an organizational focus on the strategic outcomes that matter and empower teams to deliver their best work, no matter how they work. The comprehensive Planview platform and enterprise success model enables customers to deliver innovative, competitive products, services, and customer experiences. Headquartered in Austin, Texas, with locations around the world, Planview has more than 1,000 employees supporting 4,000 customers and 2.4 million users worldwide. For more information, visit www.planview.com. ([reference](https://www.linkedin.com/company/planview/))
1. [Digital.ai](https://digital.ai/). Based out of Boston, Massachusetts, Digital.ai is an industry-leading technology company dedicated to helping Global 5000 enterprises achieve digital transformation goals. The company's AI-powered DevOps platform unifies, secures, and generates predictive insights across the software lifecycle. Digital.ai empowers organizations to scale software development teams, continuously deliver software with greater quality and security while uncovering new market opportunities and enhancing business value through smarter software investments. ([reference](https://www.linkedin.com/company/digitaldotai/about/#:~:text=Digital.ai%20is,smarter%20software%20investments.))

### GitLab opportunities

|Area of focus|GitLab|[Digital.ai](https://gitlab.com/gitlab-org/plan-stage/product-planning/competitive-research/-/issues/2#gitlab-vs-digitalai-agility-user-rating)|[Planview](https://gitlab.com/gitlab-org/plan-stage/product-planning/competitive-research/-/issues/3#gitlab-vs-planview-user-rating)|[Jira Align](https://gitlab.com/gitlab-org/plan-stage/product-planning/competitive-research/-/issues/4#gitlab-vs-jira-user-rating)|
|---|:---:|:---:|:---:|:---:|
| Portfolio financial management|⬜️ | 🟨|🟩 |🟨 |
| Portfolio level planning|⬜️ |🟩 |🟨 |🟨 |
| Program level planning| ⬜️|🟩 | 🟨| 🟩|
| Enterprise agile framework (including SAFe)| 🟨 |🟩 |🟩 |🟩 |
| Forecasting|⬜️ |🟨 |🟨 |🟩 |
| Dependency management| ⬜️ |🟨 |🟨 |🟩 |
| Roadmapping| 🟨 |🟩 |🟨 |🟩 |
| End to end visibility to the value stream|🟨 |🟩 |🟨 |🟩 |
| Collaboration|🟩 |🟨 |🟨 |🟩 |

- ⬜️  lacking
- 🟨  needs improvement
- 🟩  excels


### Target Audience

- [Cameron, Compliance Manager](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager)
- [Parker, Product Manager](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)
- [Delaney, Development Team Lead](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
- [Presley, Product Designer](https://handbook.gitlab.com/handbook/product/personas/#presley-product-designer)
- [Sasha, Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)







