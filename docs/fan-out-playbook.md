### Kontur - AGENTS.md Fan-out Playbook

*(hand this to the automation agent verbatim)*

---

## 0  Goal

> **Keep one authoritative `AGENTS.md` in the `konturio/AGENTS.md` repo.**
> Mirror it to every other repo.
> Each update lands in a branch called `repo-sync/<source>` inside every target repo.
> A Pull Request is opened automatically.
> GitHub’s built-in **Auto-merge** merges it the moment branch-protection requirements are satisfied.
>
> Result:
>
> * **Audit trail** – every sync is a PR you can revert.
> * **Zero manual toil** – PRs merge themselves.

---

## 1  Pre-requisites

| Item                      | One-time action |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Personal Access Token** | Create a PAT named **`CD_GITHUB_TOKEN`** with `repo → contents:read&write`, store it as a secret in the *source* repo (`Settings → Secrets → Actions`). |
| **Auto-merge**            | In **every target repository**:<br>Settings → General → Pull Requests → ✅ *“Allow auto-merge”*. |
| **Branch protection**     | Add / edit rule for `main` (or whatever your default branch is):<br> – *Require status checks to pass* (yes, at least one is needed for auto-merge to wake up).<br> – **No review requirement** (or 0 approvals).<br> – ✅ *“Automatically delete head branches”* (optional neatness). |
| **Status check**          | If the repo has no CI, create a trivial workflow called `noop.yml` that just sleeps for a second and exits 0. Anything green unblocks auto-merge. |

---

## 2  Repo layout in **konturio/AGENTS.md** (source)

```
.
└─ .github/
   ├─ workflows/
   │   └─ sync-agents.yml   # triggers the file sync
   └─ sync.yml              # mapping: which repo gets which file(s)
AGENTS.md                   # ← master copy
```

### 2.1 `.github/sync.yml`

```yaml
# List of repos receiving AGENTS.md
konturio/disaster-ninja-fe:
  - AGENTS.md
konturio/insights-llm-api:
  - AGENTS.md
konturio/geocint:
  - AGENTS.md
konturio/ui:
  - AGENTS.md
konturio/disaster-ninja-cd:
  - AGENTS.md
konturio/user-profile-api:
  - AGENTS.md
konturio/k8s-harlem:
  - AGENTS.md
konturio/event-api:
  - AGENTS.md
konturio/front-facing-api-tests:
  - AGENTS.md
konturio/disaster-ninja-be:
  - AGENTS.md
konturio/layers-db:
  - AGENTS.md
konturio/insights-api:
  - AGENTS.md
konturio/puppetmaster2022:
  - AGENTS.md
konturio/make-profiler:
  - AGENTS.md
konturio/event-preview-image-generator:
  - AGENTS.md
konturio/geocint-openstreetmap:
  - AGENTS.md
konturio/fibery-tools:
  - AGENTS.md
konturio/layers-api:
  - AGENTS.md
konturio/live-sensors-app:
  - AGENTS.md
konturio/oam-mosaic-map:
  - AGENTS.md
konturio/geocint-runner:
  - AGENTS.md
konturio/insights-db:
  - AGENTS.md
konturio/k8s-utils:
  - AGENTS.md
konturio/event-api-tests:
  - AGENTS.md
konturio/platform-architecture:
  - AGENTS.md
konturio/insights-api-autotests:
  - AGENTS.md
konturio/geocint-mapaction:
  - AGENTS.md
konturio/isochrone-api:
  - AGENTS.md
```

### 2.2 `.github/workflows/sync-agents.yml`

```yaml
name: Sync AGENTS.md everywhere
on:
  push:
    paths: [ "AGENTS.md" ]         # only fire when rules change
    branches: [ "main" ]
  workflow_dispatch:               # manual run button

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Fan-out file
        uses: Redocly/repo-file-sync-action@v1
        with:
          GH_PAT: ${{ secrets.CD_GITHUB_TOKEN }}

          # Place branches under repo-sync/<source>/*
          BRANCH_PREFIX: repo-sync          # default is already repo-sync/SOURCE_REPO
          
          # Cosmetic
          COMMIT_PREFIX: "sync: "
          PR_LABELS: |
            sync
            agents
```

**How it works**

* The action spawns a branch like `repo-sync/AGENTS/main` in each target repo, commits the new file, and opens a PR into `main`.
* Because we left `SKIP_PR` at its default `false`, a PR is created instead of an immediate push ([GitHub][1]).
* Branch protection + auto-merge take it from there.

---

## 3  Enable Auto-merge on the PR automatically (optional but nice)

If you don’t want to click the green “Enable auto-merge” button once per repo:

1. Add this tiny workflow **once per target repo** (or ship it via the same sync mechanism!):

```yaml
# .github/workflows/enable-auto-merge.yml
name: Enable auto-merge for sync PRs
on:
  pull_request:
    types: [opened, synchronize, reopened, labeled]
jobs:
  auto-merge:
    if: github.actor == 'kontur-bot' || contains(github.event.pull_request.labels.*.name, 'sync')
    runs-on: ubuntu-latest
    steps:
      - uses: peter-evans/enable-pull-request-automerge@v3
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          merge-method: squash
```

2. The moment the sync PR appears, this workflow flips the auto-merge switch. When the status check turns green, the PR merges itself.

---

## 4  Rollback / Hot-fix strategy

*Need to revert a bad rule?*

1. Revert the offending commit in **konturio/AGENTS.md**.
2. Push → the workflow produces “revert” PRs in every repo.
3. They auto-merge just like the forward change.
4. If something goes really sideways, delete the `repo-sync/*` branch in the target repo and force-push a fixed file from the source; the next run recreates a clean PR.

---

## 5  Security & housekeeping notes

* **Least-privilege PAT** – the token only needs `contents` scope; no `workflow` or `admin:org`.
* **Who can bypass?** – If you later tighten branch protection, grant the bot role *“bypass branch protection”* so PRs still merge.
* **Cross-repo loop guard** – keep the sync workflow **only in the source repo** so the fan-out doesn’t re-trigger itself.
* **Noise control** – set `COMMIT_EACH_FILE: false` if you ever sync more than one file to avoid dozens of tiny commits.

---

### Done!

Copy this doc into your internal wiki or drop it straight into the bot’s prompt and the AGENTS rules will propagate themselves from now on.

[1]: https://github.com/Redocly/repo-file-sync-action "GitHub - Redocly/repo-file-sync-action: GitHub Action that sync's two (or more) repos."
