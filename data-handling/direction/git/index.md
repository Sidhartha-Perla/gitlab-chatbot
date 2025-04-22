---
layout: markdown_page
title: "Category Direction - Git Contributions"
description: "The Git team makes upstream contributions to the Git open source project, and helps other teams use Git effectively and efficiently."
canonical_path: "/direction/git/"
---

- TOC
{:toc}

## Git

| | |
| --- | --- |
| Section | Data Access |
| Maturity | Non-marketable |
| Content Last Reviewed | 2025-04-01 |

### Introduction

GitLab is built on top of the open source [Git project](https://git-scm.com/), and we feel very strongly that we should be contributing to this project. As users and ambassadors of Git, it is our goal to actively engage in the Git community through bug fixes, feature additions, and mentoring. One of this team's major goals is to ensure we continue to enhance the Git project.

In addition to contributing to upstream Git, the Git team is responsible for providing the knowledge for how to use Git to other groups. This involves optimizing our internal usage of Git, performing housekeeping on repository data and generally ensuring that the repository storage for our customers is performing as well as possible for all shapes and sizes of data.

This strategy is a work in progress, and everyone can contribute. Please
comment and contribute in the linked issues and epics. Sharing your feedback
directly on GitLab.com is the best way to contribute to our strategy and
vision.

- [Issue List](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=group%3A%3Agit)
- [Epic list](https://gitlab.com/groups/gitlab-org/-/epics?label_name[]=group%3A%3Agit)

If you would like support from the Git team, please see the team's page detailing [How to contact the Git team](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/data-access/git/#how-to-contact-the-team).

## Git Contributions

Git lies at the core of what Gitaly does and is of critical importance to
GitLab. We are aiming to increase up our investment into the Git community to
ensure that it stays healthy in the long term.

Direction for the GitLab contributions to the Git project is tracked separately
from the Gitaly direction, even though they are closely tied to each other.
This is done because not only is Git a standalone project, but more importantly
it is a community-led open source project, and thus not under direct control of
the Gitaly team.

While we can influence the direction of Git somewhat by being regular
contributors to the project and building trust and credit with the community,
it will never be (and should not be!) under our full control. This is only
natural in an open source project and also by design, as the success of Git
relies on a healthy and diverse community with interests that may at times be
conflicting with each other. We want to foster that community and collaborate
with it, including with our direct competitors.

### Monorepo performance

There's no question, repository data sets are growing rapidly. With the
prevalence of machine learning and artificial intelligence adoptions, we're
seeing a steady increase in repository size as well as the number of files
needing to be stored. The Git team needs to ensure that repository storage
scales with these expanding data storage needs.

Monorepo performance is a complex topic that involves many different parts of
Git.

#### Scaling with many objects

As projects grow older and grow more commits, the repository's object graph
naturally expands. This creates scalability issues over time regardless of the
respective object sizes. We want to ensure that the object database of Git
repositories can scale well when facing repositories with dozens of millions of
objects.

Our goals here are:

- **Pluggable object databases**: The object storage format and the transport
  format of Git are tightly coupled. Furthermore, access to the object format
  happens rather ad-hoc without a lot of abstraction. It is clear though that
  the current design of the object database has limited scalability, and the
  more features we pile on top of it the harder it becomes to continue scaling.

  We need to get back to the drawing board and explore whether it is feasible
  to make the object database pluggable. This is a huge effort and will likely
  span over multiple years, but it is needed to ensure long-term scalability of
  Git.

- **Better support for bundle URIs**: We have started to use bundle URIs to help
  reduce the load on Gitaly servers. This is especially important in the
  context of CI systems. The feature is still relatively young though, and
  there are issues with both the implementation and the UX. We need to invest
  more time to help polish this feature.

#### Scaling with large objects

Despite issues with large object graphs, Git is also known to not scale well
with large objects like binary files. These are becoming increasingly more
important with the advent of AI, but are also critical to open up to additional
markets that are heaviliy dependent on binary assets like game studios.

Our goals are:

- **Offloading blobs through promisor remotes**: We need server side changes to
  enable a triangular workflow between Git server, client, and a promisor
  remote which will host blobs that we offload from the git server.

- **Allow easy access to promisor remotes**: Make it easier for Git to access
  promisor remotes. If we have a lot of objects offloaded to object storage
  because they are rarely used, Git should be able to access the objects and
  metadata easily without having to pull the objects back into the repository.

- **Storing large objects more efficiently**: Investigate whether we can store
  large objects more efficiently and allow for deduplication when such large
  objects are changed. One example would be to use rolling hash functions to
  split up large objects better, which would potentially allow us to store
  changes to such large objects incrementally. Furthermore, if we are able to
  expose those chunks via the transport layer, then this would potentially be
  able to provide a native replacement for Git LFS when combined with partial
  clones.

- **Sending large objects more efficiently**: Next to the problem of storing
  large objects efficiently, we also need to investigate how to send incremental
  changes to large objects over the wire efficiently. This may require us to
  expose the above representation with rolling hash functions to clients to
  efficiently compute deltas. An alternative would be to introduce a new object
  type that allows us to serve large binaries more efficiently.

#### Scaling with many references

We have seen repeatedly that Git and Gitaly start to struggle in repositories
that have millions of references. While one approach should be to reduce the
number of references that we need to store, we also need to acknowledge that
our customers have valid usecases for repositories with this many references.
Adapting Git so that it can handle repositories with many references is thus
important.

Our goals here are:

- **Implement reftable support in GitLab**: Reftables are a new storage data
  structure within Git that we have the privilege of contributing to upstream
  Git. This back end for Git references will improve the performance of
  repositories with many references, as well as eliminate the current race
  condition around updating reference. This will translate into better support
  for monorepos and will help ensure continued stability for our GitLab.com
  offering.

  [Tracking Epic](https://gitlab.com/groups/gitlab-org/-/epics/4220).

- **Performance improvements for the reftable backend**: While the reftable has
  been upstreamed and generally outperforms the files backend in most
  scenarios, there still are lots of performance optimizations feasible. To
  reap the full benefits of this new backend we should invest more time into
  this.

- **Partial-update transactions**: For the reftable backend to operate
  efficiently, updates of multiple references should ideally happen in a single
  transaction. Tools like git-fetch(1) may want to update only a subset of
  those refs though where the expected state matches the actual state of a
  reference. This is done via separate transactions. With the introduction of
  partial-update transactions, we allow evicting references from such a
  transaction, while still continuing with remaining references.

#### Scaling with large trees

Many commands in Git scale with the size of the file tree, and large monorepos
tend to have file trees that are both deep and broad. This creates bottlenecks
in commands that scale with tree size. Adapting those commands to handle such
large trees better is thus another angle for ensuring future scalability.

Our goals here are:

- **Better UI for sparse checkouts (client side)**: Sparse checkouts help users
  scale by not requiring a fully checked out worktree. For one, this saves disk
  space. Second, this allows users to skip fetching many blobs for partial
  clones. The sparse checkout tool in Git is hardly used because of usability
  challenges. We can vastly improve this command to make it more easily usable for
  monorepo cases.

- **git-replay(1)**: Improve git-replay(1) to support additional usecases for
  cherry-picks, rebases, rebasing merges and reverts.

- **git-blame-tree(1)**: Upstream git-blame-tree(1) to improve performance when
  computing the last commit entries in a specific tree have been changed. This
  should speed up RPCs like `ListLastCommitsForTree()` significantly.

### Better support for cloud-native deployments

Many of our customers have expressed a big interest in cloud-native deployments
of Gitaly. Our official stance is that this is not supported, where a huge
contributor to this stance is that Git does not handle constrained environments
well.

Our goals here are:

- **Memory growth**: Start to address memory growth issues in tools like
  git-pack-objects(1) in large monorepos. Hopefully, it shouldn't be required
  to allocate dozens of gigabytes of memory to pack objects. This is especially
  important in the context of monorepos and Kubernetes. It is assumed that this
  will be a moving target, and depending on how much bandwidth we allocate, we
  expect this to take multiple quarters.

### User Experience

Git can be an intimidating tool with very complex syntax. This poses a direct
threat because it allows a contender in the same space to take away market
share if they provide a significantly better user experience. This has been
showing with the recent advent of Jujutsu, which is claimed by many to provide
a superior user experience compared to Git.

Our goals here are:

- **More streamlined interfaces**: The user interfaces provided by Git have
  grown organically over time and are often redundant, inconsistent, confusing
  and/or hard to discover. We want to invest the time to make the interfaces
  more consistent and thus easier to use. We want to help the community to
  adopt a set of guidelines to help adapt existing and design future user
  interfaces.

- **Better user journey with large repositories**: Provide a better user journey
  for interacting with very large repositories (in collaboration with the
  [Source Code group](/direction/create/source_code_management/)).

- **Observe challengers like Jujutsu**: We want to observe development of
  challengers like [Jujutsu](https://martinvonz.github.io/jj/latest/) (JJ), a
  new version control system funded by Google for improved user experience with
  monorepos. We have noticed that many users praise its usability, especially
  compared to Git. As JJ can use Git repositories as backend, we may want to
  investigate whether it may be a good addition to the toolchain of users.

  Furthermore, we may want to help Google with the libification of Git in this
  context. If the Git backend used by JJ plays well with Git due to this
  effort, then we ensure that JJ will stay compatible with repositories hosted
  on GitLab.

  By staying close to developments in JJ, we position ourselves such that we can
  start to pivot to JJ if this ever becomes necessary.

### Maintainability

As we have started to invest more into the Git community, we need to treat it
with the same focus on maintainability as we treat projects that are owned by
GitLab. We want to ensure that the codebase remains accessible to existing and
new contributors and readily extensible. As we entrust Git with handling our
customer's most important data, we also need to ensure that the Git project is
safe.

Our goals here are:

- **Integer overflows**: During the audit of X41 D-Sec we found many integer
  overflows in Git that can lead to exploitable out-of-bounds writes. The worst
  issues were able to trigger remote code execution bugs in Gitaly. While known
  instances have been fixed, Git is full of implicit integer conversions that
  can lead to this kind of bug. We should invest the time to harden Git against
  this kind of vulnerability and fix this whole class of bugs. This requires
  lots of fixes throughout the codebase so that we can enable relevant compiler
  warnings.

- **Memory leaks**: While many parts of Git are leak free, others aren't. This
  is reflected in Git's test suite, where only a subset of tests run with the
  leak sanitizer enabled. This makes it easy to introduce new memory leaks that
  go unnoticed. The effect is that we are working against a moving target when
  trying to reduce memory usage of Git overall. We want to help the Git project
  such that the whole test suite is free of memory leaks.

- **Libification**: The Git project provides the command line tools as the only
  interface to Git repositories, which makes it hard to embed Git-related
  functionality into applications directly. There are ongoing efforts to also
  provide a linkable library that exposes parts of Git's functionality to such
  applications. This requires a large effort to make Git play nice for such a
  usecases: removal of global state, removing calls to `exit()` and `abort()` and
  general refactorings of the to-be-exposed interfaces. We want to help this
  effort to eventually have a proper Git library, which would also open up the
  ability for ourselves to for example provide long-running Git daemons.

- **Structured error handling**: Improve error handling such that Git can return
  information about the root cause of failures in a structured way. We
  currently have to rely on parsing error messages to figure out what exactly
  has gone wrong, which is fragile and often leads to bugs.

- **Improved tracking of direction** While core developers of the Git community
  are typically aware of ongoing projects, this is less true for the wider
  community. This makes it hard to pick up work as a new contributor, requires
  the community to often re-hash similar discussions, and doesn't allow outside
  parties to learn about the direction. We want to help the Git project to
  track direction better to improve the flow of information.

### What is Not Planned Right Now

- [VFS for Git](https://gitlab.com/groups/gitlab-org/-/epics/93)

    Partial Clone is built-in to Git and available in GitLab 13.0 or newer.
    [Scalar](https://devblogs.microsoft.com/devops/introducing-scalar/) is
    compatible with partial clone, and Microsoft is contributing to its
    improvement based on their learnings from the VFS for Git protocol.

- Divergent solution for CDN Offloading

    While we recognize that a lot of good work has gone into independent
    solutions, we are committed to work with the Git community on a CDN
    approach. We intend to support, implement, and contribute to this
    solution as it be comes available. This is currently being explored
    in our [Support Git CDN offloading](https://gitlab.com/groups/gitlab-org/-/epics/1692)
    epic.
