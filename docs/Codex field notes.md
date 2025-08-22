# OpenAI Codex field notes / best practices

**Setup:**
* Make sure there is an [AGENTS.md](https://AGENTS.md) in the root of the repo with best practices spelled out.
  * [AGENTS.md](https://AGENTS.md) are synced from central repo, add your edits to <https://github.com/konturio/AGENTS.md/blob/main/AGENTS.raw.md> and then call github actions to sync to all repos. List of repos to sync it to is also in that repository under CI.
* Make sure tests work, and it is documented how to run them, and that Codex runs them correctly.
* Enable internet access for Codex unless there is a chance it will invoke some write-API and make a mess there.

**Tasks:**

* Copy tasks into Codex as a whole (\[…\] → Copy as markdown) with metadata to create prompts that include the comments to the Fibery task.
* Sentry pages also can be copied into Codex as-is (open the issue, ctrl-a, ctrl-c, switch to Codex, ctrl-v).
* If something is not done right, better to add details into the task and restart the whole loop (copy as markdown, new branch, …)
* If Codex breaks some "obvious" thing, add it into global [AGENTS.md](https://AGENTS.md) and retry.
* After creating pull requests, in Open Source repositories CodeRabbit may send comments. It's a good idea to go through them, copy every "Prompt for AI Agents" from them into Codex and let it fix the issue. There may be several iterations.
* For Front End tasks, use preview links to check the result
* The model Codex uses is cheap (not very smart) but persistent. If it stumbles on some bug, it may make sense to review the code using some smarter model that can actually search the web too (GPT o3, o4-mini-high, Claude, …) and pass the newly found knowledge to Codex.
* You can get all changes in the pull request in .diff or .patch format by adding .diff or .patch to the pull request URL, e.g. <https://github.com/konturio/disaster-ninja-fe/pull/1195.diff> - it is good for copy-pasting all code at once into non-codex ChatGPT
