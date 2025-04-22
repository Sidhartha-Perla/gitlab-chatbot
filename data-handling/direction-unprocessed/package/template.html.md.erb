---
layout: markdown_page
title: "Stage Direction - Package"
description: "The Package stage is your single source of truth for packages and container images."
canonical_path: "/direction/package/"
---

- TOC
{:toc}

## Package

### What is Package

The Package stage is responsible for executing on the market needs for artifact management.

Artifact management involves storing, versioning, and tracking binary files, libraries, and dependencies used in software development. It's crucial for ensuring consistency, reproducibility, and efficient collaboration in development projects. Artifact management systems help manage the software artifacts' lifecycle, from creation to deployment, facilitating easy access, sharing among team members, and integration with build and deployment tools. They support version control, which is essential for tracking changes and managing different versions of software components. This process enhances productivity and contributes to the reliability and quality of software projects.

### Package vision

The vision for the Package stage is to provide a single source of truth for storing and distributing packages and container images across the entire DevOps lifecycle. We aim to offer a comprehensive and user-friendly experience for managing artifacts, enabling seamless collaboration, and ensuring consistency and reliability throughout the development process.

By consolidating package and image management within GitLab, teams can streamline their workflows, reduce operational overhead, and benefit from the tight integration with other GitLab features such as source code management, CI/CD pipelines, and security scanning. Our goal is to empower developers and organizations to focus on building great software while we handle the complexities of artifact management.

We will execute this vision by:

1. **Virtual registries for managing upstream repositories**: By providing virtual registries, we will create an abstraction layer over upstream repositories. This allows developers to access and manage external and internal repositories from a single point, streamlining dependency management and ensuring consistency across environments.
2. **Dependency firewall to prevent supply chain attacks**: Integrating a firewall specifically designed to protect against supply chain attacks is a proactive security measure. It can inspect and filter incoming artifacts, dependencies, and packages based on security policies, vulnerability databases, and other criteria, preventing malicious code from entering the development pipeline.
3. **Centralized artifact management**: Offering a centralized platform for viewing and accessing all types of artifacts (e.g., binary files, libraries, containers) enhances visibility and control. This centralization supports better governance, auditability, and collaboration among teams, making it easier to manage the lifecycle of artifacts from development to deployment.
4. **Usage analytics**: By collecting and analyzing usage data on how artifacts are being utilized within the organization, we can provide valuable insights into dependency health, license compliance, popular versus unused artifacts, and potential optimization areas. This dcan inform decision-making, improve resource allocation, and enhance your artifact security posture.
5. **Scalability and Performance**: The system is designed to handle the demands of large-scale enterprises, supporting a high number of simultaneous users and transactions without compromising performance.
6. **Education and best practices**: We will provide resources, documentation, and training on best practices for artifact management, security, and compliance to help educate your teams users on how to effectively use GitLab Package.

### What's next and why

For the container registry, we are working to make your workflows more secure by adding support for [immutable tags](https://gitlab.com/gitlab-org/container-registry/-/issues/82). This and the recently launched [protected tags](https://docs.gitlab.com/user/packages/container_registry/protected_container_tags/) help prevent accidental or malicious updates to your container registry.

For the package registry, we are working on the addition of a [Maven virtual registry](https://gitlab.com/groups/gitlab-org/-/epics/3610), that will configure an ordered list of upstream repositories and resolve packages from these sources, caching them at the top-level group. This feature will seamlessly pull packages from external remotes into your GitLab top-level group, simplifying Maven settings file configuration and increasing the reliability of your builds.  In addition, we are working on adding support for [protected packages](https://gitlab.com/groups/gitlab-org/-/epics/5574) which will help prevent accidental or malicious updates to your package registry. We've rolled out support for [npm](https://docs.gitlab.com/ee/user/packages/package_registry/package_protection_rules.html), [PyPI packages](https://gitlab.com/gitlab-org/gitlab/-/issues/323971), [Maven](https://gitlab.com/gitlab-org/gitlab/-/issues/323969) and [Conan](https://gitlab.com/gitlab-org/gitlab/-/issues/323975) packages. Next, we'll add support for [generic packages](https://gitlab.com/gitlab-org/gitlab/-/issues/323973).

For the dependency firewall, we've created a [proof of concept](https://www.youtube.com/watch?v=JBJ26BI-EhE) that allows you to add a `deny` list for npm packages. This would empower you to block or create issues for any packages that match a given regex. We plan to begin development on this feature in the first half of 2025.

### What we aren't working on and why

- We are not adding support for new package manager formats. Right now we are focused on improving the formats that are generally available, npm, Maven, NuGet, PyPI, Terraform, and generic packages.

### Helpful links

- [Maturity plan](https://gitlab.com/groups/gitlab-org/-/epics/2972)
- [Issue list](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=group%3A%3Apackage)
- [Overall vision](https://about.gitlab.com/direction/ops/#package)
- [Research issues](https://gitlab.com/groups/gitlab-org/-/boards/1397751?scope=all&utf8=%E2%9C%93&label_name[]=group%3A%3Apackage)

### Goal
The goal of the [Package Group](https://handbook.gitlab.com/handbook/engineering/development/ops/package/) is to build a product, that within three years, is our customer's single source of truth for storing and distributing images and packages.

### Do customers want this?

Yes. As the PM for the Package stage, I hear regularly from customers and prospects that would like to migrate off of JFrog's Artifactory. Their reasons for wanting to consolidate on GitLab are:
1. Convenience (authentication, management, improved UX)
1. Cost
1. Lack of support (getting to meet with GitLab PMs is a big + for these folks)

Typically the needs of these customers can be predictably segmented by the size of their organization. For the sake of simplicity, let's classify their needs as `enterprise` and `non-enterprise`.

#### Non-enterprise organizations

Typically they’d like to know if we support format `x` and if not when will we support it. The formats that we don’t support that we hear most often are:

- [RubyGems](https://gitlab.com/groups/gitlab-org/-/epics/3200)
- [Debian](https://gitlab.com/gitlab-org/gitlab/-/issues/5835)
- [RPM](https://gitlab.com/groups/gitlab-org/-/epics/5128)

_(All of the above will be useful for ~Dogfooding as well)_

If we support their requested format, these customers are often able to consolidate.

They are typically blocked by issues and bugs that are fairly straightforward to address.

#### Enterprise organizations

We often hear from large, enterprise organizations that they'd like to consolidate on GitLab and move away from their existing vendor. But, our advice to these organizations is that they wait until the GitLab Package product matures. When comparing GitLab to Artifactory or Sonatype, there are several key missing features that must be considered.

- Virtual registries, which allow you to publish, proxy, and cache multiple package repositories behind a single, logical URL. Without supporting this, no large organization will be able to migrate from Artifactory to GitLab.
- A [Dependency Firewall](/direction/package/#dependency-firewall), which will help to prevent any unknown or unverified providers from introducing potential security vulnerabilities.
- Improved discoverability and visibility into how dependencies are being used and by whom/which projects.

### Categories

If you'd like to learn more, the below information contains a summary, competitive info, and other helpful content for each product category associated with the Package stage.

#### Container Registry

The GitLab container registry is a secure and private registry for OCI artifacts, such as Docker container images. Use GitLab CI/CD to create and publish branch/release specific images. Use the GitLab API to manage the registry across groups and projects. Use the user interface to discover and manage your team's images. GitLab will provide a Lovable container registry experience by being the single location for the entire DevOps Lifecycle, not just a portion of it. We will provide many of the features expected of a container registry, but without the weight and complexity of a single-point solution.

##### Competitive Landscape

Open source container registries such as [Docker Hub](https://hub.docker.com/) and Red Hat's [Quay](https://quay.io/) offer users a single location to build, analyze, and distribute their container images. Docker Hub recently introduced rate limits for pulls from Docker Hub.

The primary reason people don’t use DockerHub is that they need a private registry and one that lives alongside their source code and pipelines. They like to be able to use pre-defined environment variables for cataloging and discovering images. Often DockerHub is used as a base image for a test, but if you are building an app, you will likely customize an image to fit your application and save it GitLab's private registry alongside your source code.

[Artifactory](https://jfrog.com/artifactory/) and [Nexus](https://www.sonatype.com/nexus-repository-sonatype) both offer support for building and deploying Docker images.

Artifactory integrates with several different [CI servers through dedicated plug-ins](https://www.jfrog.com/confluence/display/RTF/Build+Integration), including Jenkins and Azure DevOps, but does not yet support GitLab. However, you can still connect to your Artifactory repository from GitLab CI. Here is an example of how to [deploy Maven projects to Artifactory with GitLab CI/CD](https://docs.gitlab.com/ee/ci/examples/README.md#contributed-examples).

GitHub offers a [container registry](https://docs.github.com/en/packages/managing-container-images-with-github-container-registry) that supports Docker image formats.Their user interface includes helpful metadata, such as how often it's downloaded and a readme. One concern worth raising is that we don't see a way to programmatically delete images. Given the cost of storing images, this could be a concern for organizations that heavily use GitHub's registry. Another limitation is that they only support authentication using your Personal Access Token. This is not ideal for organizations that would like to avoid using individual-level credentials. With the GitLab container registry, you may use a PAT, Deploy, or Job token to authenticate to the registry.

Amazon, Google Cloud, and Azure all offer fully-featured container registries.

JetBrains offers a [container registry](https://www.jetbrains.com/help/space/container-registry.html) that allows you to add a project repository and publish images and tags using the Docker client or your JetBrains project. Although they do not currently have any documentation for administrative features, such as cleanup policies or garbage collection.

[Digital Ocean offers a container registry](https://www.digitalocean.com/docs/container-registry/) that allows you store and configure private Docker images. In addition, they support global load balancing and caching in multiple regions. One potential drawback is that each Digital Ocean account is limited to 1 registry, whereas with GitLab each Project can have its own registry.

#### Package Registry

Our goal is for you to rely on GitLab as a universal package manager, so that you can reduce costs and drive operational efficiencies. The backbone of this category is your ability to easily publish and install packages, no matter where they are hosted.

You can view the list of supported and planned formats in our documentation [here](https://docs.gitlab.com/ee/user/packages/package_registry/index.html#supported-package-managers).

##### Supported formats

The below table lists our supported and most frequently requested package manager formats. Artifactory and Nexus both support a longer list of formats, but we have not heard many requests from our customers for these formats. If you'd like to suggest we consider a new format, please open an issue [here](https://gitlab.com/gitlab-org/gitlab/-/issues).

|         | GitLab | Artifactory | Nexus | GitHub | Azure Artifacts | AWS CodeArtifact | Google Artifact Registry
| ------- | ------ | ----------- | ----- | ------ | ------ | ------ |  ------ |
| Composer    | ☑️ | ✔️ | ✔️️️️ | - | - | - | - |
| Conan       | ☑️ | ✔️ | ☑️ | - | - | - | - |
| Debian      | ☑️ | ✔️ | ✔️ | - | - | - | - |
| Gradle      | ✔️ | ✔️ | ✔️ | ️✔️ ️| ✔️ | ✔️ | ✔️ |
| Helm        | ☑️ | ✔️ | ✔️ | ️☑️ ️| ☑️ | ☑️ | ☑️ |
| Maven       | ✔️ | ✔️ | ✔️ | ️✔️ ️| ✔️ | ✔️ | ✔️ |
| npm         | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| NuGet       | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | - | - |
| PyPI        | ✔️ | ✔️ | ✔️ | - | ✔️ | ✔️ | - |
| RPM         | - | ✔️ | ✔️ | - | - | - | - |
| Ruby gems    | ☑️ | ✔️ | ✔️ | ✔️ | - | - | - |

☑️ _indicates support is through community plugin or beta feature_

Interested in contributing a new format? Please check out our [suggested contributions](https://docs.gitlab.com/ee/user/packages/#suggested-contributions).

##### Competitive Landscape

##### Universal package management tools

Artifactory and Nexus are the two leading universal package manager applications on the market. They both offer products that support the most common formats and additional security and compliance features. A critical gap between those two products and GitLab's Package offering is the ability to easily connect to and group external, remote registries. To date, GitLab has been focused on delivering Project and Group-level private package registries for the most commonly used formats. We plan on bridging this gap by expanding the virtual registries category to support Maven, npm, NuGet, PyPI, and Terraform.

##### Cloud providers

Azure and AWS both offer support for hosted and remote registries for a limited amount of formats. Google has a product called Artifact Registry that supports multiple formats and virtual registries for Java and node. All of the cloud providers charge for Cloud storage and network egress.

##### DevOps Platforms

GitHub offers a package management solution as well. They offer project-level package registries for a variety of formats. However, looking at [GitHub's roadmap](https://github.com/github/roadmap/projects/1), they've deprioritized many features

- They have implementations with Composer and PyPI planned but not scheduled.
- They have a roadmap item for supporting generic packages. But, it's not yet scheduled.

GitHub charges for storage and network transfers. GitHub does a nice job with search and reporting usage data on how many times a given package has been downloaded. They do not have anything on their roadmap about supporting remote and virtual registries, which would allow them to group registries behind a single URL and allow them to act as a universal package manager, like Artifactory or Nexus or GitLab.

#### Virtual registries

Many projects depend on a growing number of packages that must be fetched from external sources with each build. This slows down build times and introduces availability issues into the supply chain. ​​For organizations, this presents a critical problem. By providing a mechanism for storing and accessing external packages, we enable more reliable builds.

Our vision for virtual registries is to provide a product that will provide fast, reliable access to all of your dependencies, whether they are hosted on GitLab or any other vendor. In addition, virtual registries will work hand-in-hand with the planned [Dependency Firewall](/direction/package/#dependency-firewall), which will help to prevent any unknown or unverified providers from introducing potential security vulnerabilities.

Currently the virtual registry for container images allows you to proxy and cache images from DockerHub. This can help you to speed up your pipelines and reduce your external dependencies. However this is only the first step. In the coming milestones, we will expand the feature from a single, hardcoded endpoint, to the place where you can setup and manage all of your registries (both packages and images) in one place.

There are a few important terms that are worth sharing:

- **Hosted registry:** A registry that is hosted on GitLab.
- **Remote registry:** A proxy to a registry located on a remote server
- **Virtual registry:** collection of hosted and remote registries accessed through a single logical URL. This hides the access details of the underlying repositories letting users work with a single, well-known URL.

##### Usecases listed

1. Provide a single method of reaching upstream package management utilities, in the event they are not otherwise reachable.
1. Cache images and packages for improved reliability.
1. Track which dependencies are utilized by which projects when pulled through the proxy.
1. Audit logs in order to find out exactly what happened and with what code.
1. Operate when fully cut off from the internet with local dependencies.

##### User flow

The below diagram demonstrates how you can use the virtual registries to look for and fetch dependencies from your hosted and remote registries. This will allow you to download all of your dependencies with a single URL, instead of having to remember which packages are hosted where.

[![Diagram](https://mermaid.ink/img/eyJjb2RlIjoiZmxvd2NoYXJ0IExSXG5cdEFbR2l0TGFiIEhvc3RlZCByZWdpc3RyeV1cbiAgQltQcm9qZWN0IGNvZGVdXG4gIENbVmlydHVhbCByZWdpc3RyeV1cbiAgRFtQaXBlbGluZV1cbiAgRVtSZWxlYXNlXVxuICBGW1JlbW90ZSByZWdpc3RyaWVzXVxuICBHW0RlcGVuZGVuY3kgRmlyZXdhbGxdXG5cbiAgQSA8LS0-IENcbiAgQiAtLT4gRFxuICBEIC0tPiBFXG4gIEYgLS0-IEdcbiAgRyAtLT4gQ1xuICBDIDwtLT4gRCIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/docs/mermaid-live-editor-beta/#/edit/eyJjb2RlIjoiZmxvd2NoYXJ0IExSXG5cdEFbR2l0TGFiIEhvc3RlZCByZWdpc3RyeV1cbiAgQltQcm9qZWN0IGNvZGVdXG4gIENbVmlydHVhbCByZWdpc3RyeV1cbiAgRFtQaXBlbGluZV1cbiAgRVtSZWxlYXNlXVxuICBGW1JlbW90ZSByZWdpc3RyaWVzXVxuICBHW0RlcGVuZGVuY3kgRmlyZXdhbGxdXG5cbiAgQSA8LS0-IENcbiAgQiAtLT4gRFxuICBEIC0tPiBFXG4gIEYgLS0-IEdcbiAgRyAtLT4gQ1xuICBDIDwtLT4gRCIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)
**Note:** *The above diagram shows all of your dependencies being resolved through the use of a virtual registry. Usage of this feature is not required. You can easily use your hosted and remote registries without grouping them in a virtual registry.*

##### Competitive landscape

* [Artifactory](https://www.jfrog.com/confluence/display/RTF/Docker+Registry#DockerRegistry-RemoteDockerRepositories)
* [Nexus](https://help.sonatype.com/repomanager2/configuration/managing-repository-groups)

Artifactory is the leader in this category. They offer 'remote repositories' which serve as a caching repository for various package manager integrations. Utilizing the command line, API or a user interface, a user may create policies and control caching and proxying behavior. A Docker image or package may be requested from a remote repository on demand and if no content is available it will be fetched and cached according to the user's policies. In addition, they offer support for many of major packaging formats in use today. For storage optimization, they offer check-sum based storage, deduplication, copying, moving and deletion of files.

The below tables outline our current capabilities compared to JFrog's Artifactory and Sonatype's Nexus.

| Container registry | GitLab | Artifactory| Nexus   |
| -------            | ------ | ----       | ----    |
| Local registries   |  ✔️     |    ✔️       |   ✔️     |
| Remote registries  |  [Partial*](https://gitlab.com/groups/gitlab-org/-/epics/6061)     |    ✔️       |   ✔️     |
| Virtual registries |  [Coming soon](https://gitlab.com/groups/gitlab-org/-/epics/6061)      |    ✔️       |   ✔️     |

**The virtual registry category currently supports one hardcoded remote registry, which allows you to [proxy and cache container images hosted on DockerHub](https://docs.gitlab.com/ee/user/packages/dependency_proxy/#using-the-docker-dependency-proxy).*

| Package registry | GitLab | Artifactory| Nexus   |
| -------          | ------ | ----       | ----    |
| Local registries   |  ✔️     |    ✔️       |   ✔️     |
| Remote registries  |  [Partial*](https://gitlab.com/groups/gitlab-org/-/epics/2920)     |    ✔️       |   ✔️     |
| Virtual registries |  [Coming soon](https://gitlab.com/groups/gitlab-org/-/epics/2920)     |    ✔️       |   ✔️     |

**By default, when an npm or PyPI package is not found in the GitLab registry, the request will be forwarded to the public registry, either [npmjs.com](https://www.npmjs.com/) or [PyPI.org](https://pypi.org/) respectively. Check out this [speed-run](https://youtu.be/Do-5bmgvHOU) to see how it works.

#### Dependency Firewall

Many projects depend on packages that may come from unknown or unverified providers, introducing potential security vulnerabilities.  GitLab already provides [dependency scanning](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/#supported-languages-and-package-managers) across a variety of languages to alert users of any known security vulnerabilities, but we currently do not allow organizations to prevent those vulnerabilities from being downloaded to begin with.

The goal of this category will be to leverage [virtual registries](https://about.gitlab.com/direction/package/#virtual-registries), which proxies and caches dependencies, to give more control and visibility to security and compliance teams.

By preventing the introduction of security vulnerabilities further upstream, organizations can let their development teams work faster and more efficiently.

##### Proposed MVC (needs validation)

- Create a new security policy called `dependency firewall policy`.
- Create conditional rules based on the severity level of known vulnerabilities in the GitLab Advisory Database.
- Choose an action for each rule. (For the MVC we will focus on `warn` only)
- Create a `warn` policy that alerts users that a package that's being downloaded from upstream is in violation of the firewall policy.
- Ensure that any warnings are surfaced on the Security Dashboard.

##### Beyond the MVC

- Add support for a deny list of packages that are not allowed to be downloaded.
- Create a `fail` policy that prevents users from downloading packages that are in violation of the firewall policy.
- Rules to quarantine packages when rules are met.
- The ability to CRUD the quarantine.
- Add more complex rules, like warnings when a package is missing an author name or email.

##### Competitive landscape

* [JFrog X-Ray](https://jfrog.com/xray/)
* [Nexus](https://www.sonatype.com/nexus-firewall)
* [GitHub Package Registry](https://github.com/features/package-registry)

JFrog utilizes a combination of their Bintray and XRay products, to proxy, cache and screen dependencies. They also provide dependency graphs across multiple languages and centralized dashboards for the review and remediation of vulnerabilities. It is a mature product, that is generally well received by users. JFrog recently acquired Vdoo to and plans to update XRay to to include Vdoo’s extensive data and improved scanning across multiple dimensions, including configuration and applicability scanning.

GitHub's new package registry does a really nice job of creating visibility into the dependency graph for a given package, but they do not give users the ability to control which packages are used in a given group/project.

#### Helm Chart repository

Users or organizations that deploy complex pieces of software towards Kubernetes managed environments depend on a standardized way to automate provisioning those external environments. Helm is the package manager for Kubernetes and helps users define, manage, install, upgrade, and rollback even the most complex Kubernetes application. Helm uses a package format called Charts to describe a set of Kubernetes resources.

Helm charts are easy to create, version, share and publish right within GitLab.

##### Usecases listed

1. Public and private repositories for Helm charts
1. Fine-grained access control
1. Standardized workflow to version control and publish charts making use of GitLab's other services

##### Competitive Landscape

An important distinction between competitive products is that Helm 3 now officially supports using an OCI container registry as a Helm repository.

* [Helm Hub](https://hub.helm.sh/)
* [Artifactory](https://www.jfrog.com/confluence/display/RTF/Helm+Chart+Repositories)
* [Chart museum](https://chartmuseum.com/)
* [Azure DevOps](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-helm-repos)
* [Google Cloud](https://cloud.google.com/artifact-registry/docs/helm/manage-charts)
* [AWS](https://docs.aws.amazon.com/AmazonECR/latest/userguide/push-oci-artifact.html)
