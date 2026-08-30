# Chapter 27: Workspaces, Publishing And Rollback

The company should not depend on one person's laptop or a collection of temporary preview links. Each identity needs a durable private workspace for files, code and analysis; each shared tool needs a canonical company route.

## Private workspaces

Workspaces run on always-on infrastructure and remain separate by identity. The Brain keeps durable context and references; large binaries, datasets and build artifacts live in the appropriate object store, drive or repository.

## Governed publishing

A published internal tool is complete only when it has:

- a canonical company URL;
- identity protection and `noindex` where appropriate;
- a version and release receipt;
- health and dependency checks;
- a known rollback target;
- an owner and lifecycle state;
- a Brain record linking the project, evidence and release.

Preview infrastructure may exist behind the route, but it is not the product surface employees are expected to remember.

## Ship it

- [ ] Work survives when the builder's laptop is closed.
- [ ] Private workspaces cannot read each other's files by default.
- [ ] Shared tools have one protected canonical route.
- [ ] Every release can be traced and rolled back.
- [ ] Archived tools are removed from active discovery without destroying their history.
