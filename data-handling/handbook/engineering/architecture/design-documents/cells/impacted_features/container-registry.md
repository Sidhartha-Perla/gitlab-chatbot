---
stage: enablement
group: Tenant Scale
title: 'Cells: Container Registry'
toc_hide: true
---

{{% alert %}}
This document is a work-in-progress and represents a very early state of the
Cells design. Significant aspects are not documented, though we expect to add
them in the future. This is one possible architecture for Cells, and we intend to
contrast this with alternatives before deciding which approach to implement.
This documentation will be kept even if we decide not to implement this so that
we can document the reasons for not choosing this approach.
{{% /alert %}}

GitLab [Container Registry](https://docs.gitlab.com/ee/user/packages/container_registry/index.html) is a feature allowing to store Docker container images in GitLab.

## 1. Definition

GitLab container registry is a complex service requiring usage of PostgreSQL, Redis and Object Storage dependencies.
Right now there's undergoing work to introduce [Container Registry Metadata](../../container_registry_metadata_database/) to optimize data storage and image retention policies of container registry.

GitLab container registry is serving as a container for stored data, but on its own does not authenticate `docker login`.
The `docker login` is executed with user credentials (can be `personal access token`) or CI build credentials (ephemeral `ci_builds.token`).

Container Registry uses data deduplication.
It means that the same blob (image layer) that is shared between many Projects is stored only once.
Each layer is hashed by `sha256`.

The `docker login` does request a JWT time-limited authentication token that is signed by GitLab, but validated by container registry service.
The JWT token does store all authorized scopes (`container repository images`) and operation types (`push` or `pull`).
A single JWT authentication token can have many authorized scopes.
This allows container registry and client to mount existing blobs from other scopes.
GitLab responds only with authorized scopes.
Then it is up to GitLab container registry to validate if the given operation can be performed.

The GitLab.com pages are always scoped to a Project.
Each Project can have many container registry images attached.

Currently, on GitLab.com the actual registry service is served via `https://registry.gitlab.com`.

The main identifiable problems are:

- The authentication request (`https://gitlab.com/jwt/auth`) that is processed by GitLab.com.
- The `https://registry.gitlab.com` that is run by an external service and uses its own data store.
- Data deduplication. The Cells architecture with registry run in a Cell would reduce efficiency of data storage.

## 2. Data flow

The data flow for `docker login` is documented in [the container registry project](https://gitlab.com/gitlab-org/container-registry/-/blob/master/docs/auth-request-flow.md#login). The equivalent requests using `curl` are documented below.

### 2.1. Authorization request that is send by `docker login`

```shell
curl \
  --user "username:password" \
  "https://gitlab/jwt/auth?client_id=docker&offline_token=true&service=container_registry&scope=repository:gitlab-org/gitlab-build-images:push,pull"
```

Result is encoded and signed JWT token. Second base64 encoded string (split by `.`) contains JSON with authorized scopes.

```json
{"auth_type":"none","access":[{"type":"repository","name":"gitlab-org/gitlab-build-images","actions":["pull"]}],"jti":"61ca2459-091c-4496-a3cf-01bac51d4dc8","aud":"container_registry","iss":"omnibus-gitlab-issuer","iat":1669309469,"nbf":166}
```

### 2.2. Docker client fetching tags

```shell
curl \
  -H "Accept: application/vnd.docker.distribution.manifest.v2+json" \
  -H "Authorization: Bearer token" \
  https://registry.gitlab.com/v2/gitlab-org/gitlab-build-images/tags/list

curl \
  -H "Accept: application/vnd.docker.distribution.manifest.v2+json" \
  -H "Authorization: Bearer token" \
  https://registry.gitlab.com/v2/gitlab-org/gitlab-build-images/manifests/danger-ruby-2.6.6
```

### 2.3. Docker client fetching blobs and manifests

```shell
curl \
  -H "Accept: application/vnd.docker.distribution.manifest.v2+json" \
  -H "Authorization: Bearer token" \
  https://registry.gitlab.com/v2/gitlab-org/gitlab-build-images/blobs/sha256:a3f2e1afa377d20897e08a85cae089393daa0ec019feab3851d592248674b416
```

## 3. Proposal

### 3.1. Shard container registry separately to Cells architecture

Due to its extensive and in general highly scalable horizontal architecture it should be evaluated if the GitLab container registry should be run not in Cell, but in a Cluster and be scaled independently.
This might be easier, but would definitely not offer the same amount of data isolation.

### 3.2. Run container registry within a Cell

It appears that except `/jwt/auth` which would likely have to be processed by Router (to decode `scope`) the container registry could be run as a local service of a Cell.
The actual data at least in case of GitLab.com is not forwarded via registry, but rather served directly from Object Storage / CDN.

Its design encodes container repository image in a URL that is easily routable.
It appears that we could re-use the same stateless Router service in front of container registry to serve manifests and blobs redirect.

The only downside is increased complexity of managing standalone registry for each Cell, but this might be desired approach.

## 4. Evaluation

There do not seem to be any theoretical problems with running GitLab container registry in a Cell.
It seems that the service can be easily made routable to work well.
The practical complexities are around managing a complex service from an infrastructure side.

Since multiple Cells can be run on the same top-level domain, and the Docker client stores authentication tokens per-hostname, users may not be able to access resources from one Cell while logged in to another on the same hostname.

To authenticate with the container registry in a Cells environment, users will need to run:

```shell
docker login gitlab.example.com
```

The username can be anything; it is not used by GitLab's container registry. The "password" must be one of:

- Personal access token
- Project access token
- Group access token

Per the current [container registry authentication process](https://docs.gitlab.com/ee/user/packages/container_registry/authenticate_with_container_registry.html).

Note that **Deploy token** is listed as an available password for the container registry, but since these tokens are not routeable, they will only work with the legacy cell. The user's **GitLab username and password** can also be used to authenticate with the container registry, but this authentication method also does not contain routing information, so will only work with the legacy cell. For the first iteration, only routing to the legacy cell and default organization will be supported for all token types.

The docker client will then submit this username and password combination to the `/jwt/auth` endpoint in GitLab Rails using HTTP Basic Auth.

The Cells http router will be able to determine the correct Cell to route this request to by supporting HTTP Basic Auth requests using access tokens as the password. Support for this is [currently being built](https://gitlab.com/gitlab-org/cells/http-router/-/issues/138).

The returned JWT will contain enough information (something like `scope: cell-1`) for the Cells Registry Router to route the authenticated requests to the correct container registry / cell.

## 4.1. Pros

## 4.2. Cons
