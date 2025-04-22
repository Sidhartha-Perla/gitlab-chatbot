---
layout: markdown_page
title: "Product Direction - Global Search"
description: "GitLab supports Advanced Search for GitLab.com and Self-Managed instances. This provides users with a faster and more complete search."
canonical_path: "/direction/global-search/"
---

- TOC
{:toc}

# Global Search


| | |
| --- | --- |
| Stage | [Core Platform](/direction/core_platform/plans) |
| Maturity | [Viable](/direction/#maturity) |
| Content Last Reviewed | `2024-08-04` |
| Content Last Updated | `2024-08-04` |

Global Search is managed by the [Global Search Group](https://handbook.gitlab.com/handbook/product/categories/#global-search-group) of the [Data Stores stage](https://about.gitlab.com/direction/core_platform/#data-stores) as part of the [Core Platform Section](https://about.gitlab.com/direction/core_platform/). 

We encourage you to share feedback via [scheduling a call](https://calendly.com/bvenker-gitlab/30m-meeting-ben-venker).

You can view our current and future work at the below links:
- Our high-level [roadmap](https://gitlab.com/groups/gitlab-org/-/epic_boards/1056673?label_name%5B%5D=group::global%20search&label_name%5B%5D=Roadmap) shows what we're working on now, next, and later
- Our [Epics by workstream board](https://gitlab.com/groups/gitlab-org/-/epic_boards/1056733?label_name%5B%5D=Roadmap&label_name%5B%5D=group::global%20search) shows the work we're doing or have planned in each of our active workstreams
- You can also view our [Issues by workstream board](https://gitlab.com/gitlab-org/gitlab/-/boards/7434592?label_name%5B%5D=group::global%20search) if you want a more granular view
- Finally, you can always see what is actively being worked on by looking at our [current milestone board](https://gitlab.com/groups/gitlab-org/-/boards/4440461?milestone_title=Started&label_name%5B%5D=group::global%20search).

### Useful terms

| Term | Definition |
|------|------------|
| **Context** | Data that can be used to enhance the quality of LLM responses and was not in the model's training data. This allows LLMs to draw a wider body on knowledge than their training corpus. |
| **Local Context** | Refers to context that is stored on an end-user's machine, such as local files or code in their IDE. |
| **Server-side Context** | Refers to context that is outside the scope of an end-user's machine, such as remote code repositories or issues. Server-side context is accessible via a customer's GitLab instance. |
| **RAG** | Stands for Retrieval-Augmented Generation, a technique that combines information retrieval from a knowledge base with language generation to produce more accurate and contextually relevant AI responses. [Read more about RAG](https://github.blog/ai-and-ml/generative-ai/what-is-retrieval-augmented-generation-and-what-does-it-do-for-generative-ai/). |
| **Relevance** | In search and information retrieval, relevance refers to the degree to which a returned result matches the user's query intent and satisfies their information need. |


## Overview

Global Search is the foundation for intelligent information retrieval across GitLab, unifying diverse data sources to provide rich search features for users and context for AI-powered features. It enables users to quickly find relevant information, while empowering internal teams with a scalable framework for accessing context to build and enhance AI capabilities throughout the platform. This centralized approach to search and context accelerates development, improves decision-making, and enhances the overall GitLab experience.

Global Search caters to two distinct personas, end-users of GitLab and GitLab developers:

### For End-users

- **[Advanced search](https://docs.gitlab.com/ee/user/search/advanced_search.html)**, available for GitLab Premium self-managed, GitLab Premium SaaS, and higher tiers, expands the scope of searchable content, provides advanced filtering options, and enables cross-project and cross-group code search. It will also be the source for similarity search backed by vector embeddings. For self-managed instances, Advanced search requires integration with either [Elasticsearch](https://docs.gitlab.com/ee/integration/elasticsearch.html) or [OpenSearch](https://opensearch.org/docs/latest/), to enable these more powerful and flexible search capabilities. Advanced search enables us to provide many benefits:

    - **Global GitLab search**, allowing search across your entire GitLab instance for code, MRs, issues, epics, and more
    - **Significantly improved performance**, in the form of significantly lower latency and increased result relevance
    - **Horizontal scalability**, maintaining high performance even as the size of your GitLab instance grows.

- **[Basic search](https://docs.gitlab.com/ee/user/search/#basic-search)** is the default mode for GitLab, requiring no additional setup. While it offers a seamless setup experience, its feature set is limited compared to its more advanced counterpart. For example, global code search is not available, nor is cross-group or cross-project searching of code. Basic search uses Postgres text search, which can be slower for medium-large and larger datasets. It also doesn't support advanced text analysis features like relevance scoring, and as such will have lower qualtiy results.


### For GitLab developers

Global Search provides a centralized framework and interface for accessing, indexing, and retrieving context and traditional search results across GitLab. This enables teams to build context- or search-powered features that leverage GitLab's rich data ecosystem. Key benefits include:

- **Unified context access**: A single layer for retrieving relevant context and search results from various GitLab data sources, such as code, merge requests, issues, epics, and comments.
- **Scalability**: Built to handle large volumes of data and concurrent requests efficiently, so developers don't need to worry about how to scale the architecture
- **Ease of integration**: Easily index, embed, and search data from new and existing sources to meet customer needs.
- **Continuous improvement**: Ongoing enhancements to context relevance and retrieval interfaces.


## What we recently completed

- [Hybrid search for GitLab issues](https://gitlab.com/gitlab-org/gitlab/-/issues/440424), including foundational infrastructure work allowing embeddings to be generated and kept up to date via the AI Gateway
- [PoC with Code Creation team](https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp/-/issues/263) to provide server-side context to Code Suggestions
- Rolling out Zoekt code search Beta to ≥ 80% of .com customers, including completing Zoekt [sharding and replication](https://gitlab.com/groups/gitlab-org/-/epics/11382)
- Supporting the [Work Items migration of epics to the issue table](https://gitlab.com/groups/gitlab-org/-/epics/12903)


## What we are currently working on

While we will adjust our investment allocation based on the [new strategy laid out below](#vision--fy25-h2-and-fy26), the below represents what we're actively working on today.

### Investment allocation

| Category   | Allocation   |
| ---------- | ------------ |
| Context | 60% |
| Advanced search framework | 10% |
| Performance optimization | 20% |
| Usability and feature depth | 5% |
| Work Items migration support | 5% |

### Context

As we continue to develop our Advanced search capabilities, we're increasingly leveraging search to enhance AI functionality. Our goal is to implement [hybrid search capabilities](https://gitlab.com/groups/gitlab-org/-/epics/11748) across GitLab, combining traditional keyword-based search with AI-powered methods like semantic search. Combining the methods allows us to broaden our query with the semantic understanding of vector search, while maintaining the accuracy of exact term matches.

We're continuing to develop more vector embedding pipelines for [vector embeddings](https://docs.gitlab.com/ee/development/ai_features/embeddings.html), currently focusing on code embeddings for Code Suggestions. This infrastructure will allow us to generate, store, retrieve, and update vector representations of content across GitLab. These embeddings are crucial for enabling semantic search and other advanced AI-powered features, allowing us to capture and compare the meaning and context of both queries and content.

Finally, we continue our work to [scale Zoekt code search to our largest customers](https://gitlab.com/groups/gitlab-org/-/epics/13923). The addition of Zoekt to our hybrid search will offer increased relevance for features like Code Suggestions.

### Advanced search interfaces

For our development teams, we're focusing on [simplifying the integration of Advanced search across GitLab](https://gitlab.com/groups/gitlab-org/-/epics/13873). Our goal is to make it as easy as possible for feature teams to incorporate powerful search capabilities into their work. This involves creating intuitive APIs, providing clear documentation, and offering support to teams as they implement search features.

We'll also [update our abstraction layer for Elasticsearch and OpenSearch to support embeddings](https://gitlab.com/gitlab-org/gitlab/-/issues/454764) in OpenSearch, so self-managed customers running OpenSearch can utilize features reliant on vector search.

### Performance optimization

For our SaaS deployments, performance optimization is a key focus. We're working on [migrating inefficient searches to Elasticsearch](https://gitlab.com/groups/gitlab-org/-/epics/13112), which offers superior speed and accuracy for large-scale search operations. Once complete, this migration will help improve database scalability by allowing us to move heavy production queries onto Elasticsearch, for example, merge request text searches.

Beyond this migration, we're committed to maintaining high performance and reliability standards across all our search functions. This involves ongoing monitoring and proactive optimizations to ensure that our search capabilities can scale with our users' needs.

### Usability and feature depth

The user interface and overall user experience of our search functionality are critical to its success. We're continuously working to [improve the command palette](https://gitlab.com/groups/gitlab-org/-/epics/12031), making it more intuitive and powerful. The command palette serves as the primary access point for search and other actions, and its refinement will help users navigate GitLab more efficiently.

We're also collaborating closely with feature teams across GitLab to [improve search UX consistency across the product](https://gitlab.com/gitlab-org/ux-research/-/issues/2656). This will involve creating and implementing design guidelines, gathering and acting on user feedback, and ensuring that search behaves predictably and effectively no matter where in GitLab a user encounters it.

### Work Items migration support
As noted [above](#what-we-recently-completed), we recently completed the [Work Items migration of epics to the issue table](https://gitlab.com/groups/gitlab-org/-/epics/12903), however the Plan team is continuing it's migration to Work Items, and we continue to be downstream of that work and will have ongoing migration efforts required to support it.



## Vision : FY25-H2 and FY26

The search landscape is currently being transformed rapidly by developments in AI, making the future impossible to predict. Even as LLMs with million-token context windows are being built for research, we believe a real and significant gap exists between them and what is commercially viable in the medium-term. The foreseeable future is barely so, and constantly changing. But certain patterns, such as RAG, have emerged as relatively stable because they address real limitations of LLMs today. As such, 18 months seems a reasonable maximum duration to plan for, during which Global Search will strive to execute on lasting, high impact initiatives to improve GitLab's competitive market position.

Global Search aims to create and support transformative experiences within GitLab by intelligently connecting users to the information they need, whether through search directly, or by providing context to other features.

Our vision extends beyond traditional search capabilities; we see search as the foundation for enabling relevance-driven experiences that power AI-assisted features and empower users to take meaningful action on the information they discover.

We recognize an opportunity to reinvent the retrieval layer that underpins user experiences. This aligns with the broader industry trend towards more sophisticated, context-aware information systems. As the volume of data within GitLab instances continues to grow, the ability to quickly find and leverage relevant information becomes increasingly crucial for user productivity and satisfaction. Global Search is uniquely positioned within GitLab to lead this transformation.


### Objectives

Our objectives for Global Search are ambitious and forward-looking, designed to enable the revolutionizing of user interactions with GitLab data, empower internal teams, and ensure continuous improvement in our search capabilities. As the depth and breadth of GitLab data grow over time, search becomes increasingly vital for users to efficiently navigate, discover, and utilize the wealth of information across the platform. These objectives align with our overall vision of creating an innovative and intelligent search experience within GitLab and serve as the foundation for our strategic decisions:

- Build differentiated platform capabilities by enabling intelligent, context-rich search and chat experiences
- Enable any GitLab feature to leverage server-side contextual AI, making advanced capabilities accessible throughout the entire platform
- Position search as a cornerstone of the GitLab platform, evolving its relevance, intelligence, and cross-platform integration to keep pace with and leverage our rapidly expanding content ecosystem. 

### Goals

Our goals for the coming fiscal year reflect our commitment to driving adoption, fostering collaboration, demonstrating value, and showcasing innovation in Global Search. They are designed to support our strategic objectives and measure our progress in key areas: growing our user base, enabling internal teams, providing evidence of successful implementations, and establishing thought leadership in the field of search and AI.

- ≥ 90% adoption of Advanced search among GitLab Duo trial participants in FY25-Q4 and FY26
- 5% month-on-month increase in self-managed Advanced search seat count over FY25 H2 and FY26
- Collaborate with 3 teams to ship one new feature each, using server-side context in FY25-H2 and FY26-H1
  | Team | Feature | Timeline |
  | --- | --- | --- |
  | Threat Insights | Vulnerabilities searching | FY25-Q4 start |
  | TBD | TBD | TBD |
  | TBD | TBD | TBD |
- Develop 2 case studies showcasing successful Advanced Search implementations during FY25-H2 and FY26
- Publish 1 blog post highlighting GitLab's innovative use of search and context in AI applications in FY26 Q1

### Product strategy

#### Where to play

The "Where to play" choices define our strategic focus areas - the specific arenas where we'll concentrate our efforts to achieve our objectives. These choices involve carefully selecting which user segments, product features, and adoption channels we'll prioritize. Our selections are designed to be mutually reinforcing, addressing real user needs while leveraging our unique strengths.
  
1. **Win with internal teams needing context-powered AI features:** This is crucial for promoting consistency across the platform and enabling other teams to easily incorporate powerful search capabilities into their features. It also increases the leverage of the Global Search team, allowing us to have greater impact.

2. **Win with self-managed Duo trial prospects:** By making Advanced search a seamless part of the Duo experience, we increase the likelihood of long-term adoption and showcase the synergy between AI features and powerful search capabilities.

3. **Win with new large self-managed customers:** Focusing on new, large self-managed customers presents the greatest opportunity for impact. These customers often have complex needs that Advanced search can address, such as searching across large codebases or large numbers of groups and projects. We hypothesize that focusing on new customers increases the odss they will be willing to add a step to enable Advanced search as part of their GitLab setup. By driving adoption in this segment, we not only increase our use case adoption but also gain valuable insights from new sophisticated use cases, which can inform future product development.


#### How to win

Our "How to Win" strategies are intrinsically linked to our "Where to Play" choices, taking a cohesive and mutually reinforcing approach. These strategies outline the specific actions we'll take within our chosen arenas to achieve success. They define our unique value proposition, detailing how we'll excel in each focus area.

1. **Be collaborative:**
	- [Build a rich context layer](https://gitlab.com/groups/gitlab-org/-/epics/14911) with a high relevance baseline for GitLab teams to leverage, starting with server-side context for Code Suggestions and Duo Chat
	- Conduct bi-quarterly training sessions for internal teams on leveraging Advanced Search capabilities
	- Continuously improve the Advanced Search framework based on internal feedback

2. **Be the choice of customers:**
	- Create a simple, easy Advanced Search onboarding experience
	- Build awareness and excitement around Advanced Search and server-side context with CSMs and SAs, focusing on Code Suggestions and Duo use cases
	- Establish stronger customer feedback mechanisms to drive adoption, feature development, and performance improvements
 
3. **Be a thought leader within GitLab:**
	- Implement and showcase novel applications of search and context that increase GitLab's platform differentiation and drive customer and internal team interest
	- Leverage cutting edge context storage and retrieval techniques, such as product quantization, reranking, and hybrid retrieval


### Infrastructure strategy

Our Global Search infrastructure strategy centers on creating a powerful, flexible search foundation that can handle the diverse data types and vast scale of modern DevSecOps workflows. By leveraging Elasticsearch's robust capabilities alongside specialized tools like Zoekt, we're building a search ecosystem that not only delivers fast, relevant results across any GitLab data, but also supports advanced features like Code Suggestions and semantic search. This approach allows us to continuously enhance our search experience, enabling users to find and act on information more efficiently throughout the entire DevSecOps lifecycle, reinforcing GitLab's position as a comprehensive, integrated platform.

Global Seaarch currently utilizes the following data stores:

- **Elasticsearch** for Advanced search and Context (OpenSearch is also supported for self-managed customers)
- **Zoekt** for code search
- **PostgreSQL** for Basic search
- **Gitaly** for code search when uesrs don't have Advanced search enabled


#### Strategic pillars

##### Advanced Search framework

- Leverage our Advanced search framework to abstract complexities, providing a consistent interface for users and developers.
- Enable seamless integration of new data types and search technologies without disrupting the user experience.

##### Platform diversity

- Utilize a multi-engine approach (Elasticsearch, Zoekt, Gitaly) to optimize performance for different data types and use cases.
- Implement intelligent query routing and graceful performance degradation to ensure a bug-free experience across deployment types.

##### Leverage vendors (but remain flexible)

- Support multiple search engines (Elasticsearch, OpenSearch) to avoid vendor lock-in and provide options for self-managed customers.
- Maintain abstraction layers to facilitate potential future migrations or integrations of new technologies.

##### Continuous relevance improvement

- Develop a feedback loop system to continuously refine relevance ranking based on user behavior.


#### Key infrastructure initiatives

- **Vector Quantization:** Leverage Elasticsearch's native, automatic product quantization to optimize storage and query performance of embeddings, reducing costs up to 4x and improving AI-powered search performance.
- **Advanced Relevance Tuning:** Deploy Learning to Rank (LTR) and develop GitLab-specific ranking features to significantly improve search relevance across all data types.


#### Addressing challenges

- **Search Latency:** Continuously optimize query performance and explore caching strategies to minimize latency, especially for frequently accessed data.
- **Infrastructure Costs:** Balance performance needs with cost-efficiency through smart resource allocation and potential use of serverless technologies.


## What's next for us

### Continue Server-side Context work

We will continue to develop and refine our server-side context capabilities to enhance AI-powered features across GitLab. Key focus areas include:

1. **Expanding context types:** [Implement additional context types beyond issues, such as code, merge requests, and CI/CD pipelines](https://gitlab.com/groups/gitlab-org/-/epics/14911).

2. **Improving context and search relevance:** Develop and implement text chunking and ranking approaches for search, to better determine the most relevant context for each query, ensuring that AI-powered features receive relevant context even without tuning.

3. **Implementing feedback loops:** Establish mechanisms to gather and analyze usage data and user feedback, allowing us to continuously improve the relevance and effectiveness of our server-side context.


### Create a simple and easy Advanced Search onboarding experience

1. **Streamlined setup process:** Develop a guided, step-by-step setup for self-managed instances to easily configure Advanced search.

2. **Improved setup documentation:** Create comprehensive, user-friendly documentation that explains the setup process of Advanced Search.

3. **Reference architecture recommendations:** Offer pre-configured templates for common Advanced search configurations to help users get started quickly.


### Collaborate with teams on context-powered features

To foster collaboration and drive adoption of our server-side context capabilities, we will:

1. **Create an Advanced search integration toolkit:** Develop a comprehensive toolkit including APIs, documentation, and code samples to simplify the integration of server-side context into new features.

2. **Implement a context feature request process:** Create a streamlined process for teams to request new context types or improvements to existing ones.

3. **Develop showcase projects:** Build and highlight successful implementations of context-powered features to inspire and guide other teams.

4. **Provide ongoing support and consultation:** Offer dedicated support channels and regular consultation sessions for teams working on context-powered features.

5. **Implement a feedback loop:** Establish mechanisms to gather and act on feedback from teams using server-side context, ensuring continuous improvement of our offerings.


### Risks and mitigations

As we pursue our strategy for Global Search, it's crucial to identify and plan for potential risks. The ordering reflects a balance between immediate market pressures, core technical challenges, and longer-term growth considerations.


| Risk | Description | Mitigation |
|------|-------------|------------|
| Rapid AI Innovation Outpacing Development | The field of AI is evolving at an unprecedented rate. There's a risk that our development cycle might not keep pace with new AI advancements, potentially leading to our solutions becoming outdated quickly. | Maintain flexibility in our architecture to quickly incorporate new AI models and techniques. Establish strong partnerships with AI teams and vendors to stay at the forefront of innovations. |
| Competitive Pressure | Other DevOps platforms may accelerate their AI and context-aware capabilities, potentially eroding GitLab's differentiation. | Stay attuned to market developments, focus on GitLab's unique strengths (like our single application approach), and maintain a rapid iteration cycle to quickly address competitive challenges. |
| Integration Complexity | The development of a high-quality context layer that works seamlessly across various GitLab features could prove more complex than anticipated. | Start with a minimum valuable product (MVP) approach, focusing on key use cases for Code Suggestions and Duo Chat. Gradually expand based on lessons learned. |
| Resource Constraints | With a small team and limited resources, there's a risk of overextension, potentially leading to delays or quality issues. | Carefully prioritize initiatives, focus on high-impact areas, and leverage cross-functional collaborations within GitLab. Consider a phased approach to major features to manage our workload. |
| Adoption Challenges | There may be resistance or slow adoption of Advanced search, particularly among large self-managed customers who may have established workflows. | Invest in user education, provide clear documentation, and work closely with CSMs and SAs to demonstrate value. Develop compelling case studies to showcase benefits. |
| Scalability Challenges | As we grow adoption, especially among large self-managed customers, there may be unforeseen scalability issues with our search infrastructure. | Conduct thorough performance testing, design with scalability in mind from the outset, and have a clear plan for addressing performance bottlenecks as they arise. |


### Measures

Our measurement framework is designed to provide a comprehensive view of Global Search's performance, adoption, and impact across three key dimensions: user experience, internal adoption, and customer adoption. They groups are listed below in priority order: we believe the ability to enable great user experiences will drive internal adoption, and that the creation of those experiences will drive customer adoption, which will in turn drive more internal adoption as more internal teams adopt server-side context or enhance their existing context-based features.

#### User experience measures

These metrics focus on the quality and efficiency of the search experience from the user's perspective. They are crucial for ensuring that our advanced search capabilities translate into tangible benefits for end-users.

| Metric | Description |
|--------|-------------|
| Customer satisfaction with Duo responses | Measures user satisfaction with AI-generated responses that utilize server-side context. This metric is not maintained by Global Search, but is nonetheless critical to measuring the quality of our context. |
| Average click depth by search type | Tracks how far users typically navigate through search results for different types of searches. |
| Average dwell time by search type | Measures how long users spend on pages reached through different types of searches. |
| Average time to click result by search type | Tracks how quickly users select a search result for different types of searches. |
| Duo response acceptance rate | Measures the frequency with which users accept or act on Duo responses that use server-side context. |

#### Customer adoption measures

This set of metrics helps us understand how widely and effectively our Advanced search capabilities are being adopted by customers. By tracking cross-namespace searches, integration times, and overall adoption rates, we can assess the real-world impact of our search improvements and identify any barriers to adoption. They are vital for measuring the success of our go-to-market strategies and informing our product development priorities.

| Metric | Description |
|--------|-------------|
| Number of cross-namespace and cross-project searches | Tracks usage of Advanced Search's capability to search across multiple namespaces and projects. |
| Time to complete Advanced search integration | Measures how long it takes customers to fully integrate Advanced Search into their workflow. |
| Total self-managed customers with Advanced search | Counts the number of self-managed customers who have enabled Advanced Search. |
| Percentage of eligible customers using Advanced search | Measures the adoption rate of Advanced Search among customers who are eligible to use it. |
| Self-managed Advanced search seat count | Tracks the total number of user seats with access to Advanced Search in self-managed instances. |
| Month-on-month growth in Advanced search customers | Measures the monthly increase in the number of customers using Advanced Search. |

#### Internal adoption measures

These metrics focus on the uptake and integration of our server-side context capabilities within GitLab itself. By measuring the number of features using server-side context, integration times, and overall usage, we can assess how effectively we're leveraging search across the platform. These metrics aren't very automatable and so will be harder to collect, but are critical to understanding Global Search's impact and penetration.

| Metric | Description |
|--------|-------------|
| Features shipped using server-side context | Counts the number of GitLab features that have been released using the server-side context layer. |
| Features scheduled to use server-side context | Tracks the number of upcoming features that plan to incorporate the server-side context layer. |
| Teams using server-side context | Counts the number of internal GitLab teams leveraging the server-side context in their features. |
| Time to integrate existing context type | Measures how long it takes teams to integrate an already-supported type of context (min, max, mean). |
| Time to integrate new context type | Tracks the time required to integrate a completely new type of context (min, max, mean). |
| Growth in server-side context retrieval requests | Measures the monthly increase in the number of requests made to the server-side context layer. |

