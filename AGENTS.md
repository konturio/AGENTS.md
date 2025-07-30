# Important rules for agents
Grasping what's up: Check out README.md.
Make: Explain high-level architecture and quirks in Makefile
AI: Use system prompts where needed.
Pull requests: Branch names should match branch name recorded by Fibery if provided (e.g. "21648-switch-page-after-login-to-map").
SQL: SQL is lowercase, PostGIS functions follow their spelling from the manual (`st_segmentize` -> `ST_Segmentize`).
Style: Do not break code indentation.
Debugging: Use TDD to handle bugs.
SQL: Prefer indexed SQL operators when dealing with jsonb ( `tags @> '{"key": "value"}` instead of `tags ->> 'key' = 'value'` ).
Style: Clean stuff up if you can: fix typos, make lexics more correct in English.
Python: Write comments for each logical block.
Make: To smoke-check Makefile, `make --trace all` helps see dependency chain.
Testing: Github Actions is used as CI. Update it as necessary.
AI: Check token counts.
Pull requests: Keep Fibery ticket, Sentry ticket or other context relevant URL in pull request description.
Front End: If Reatom v2 is used, upgrade it to v3.
Debugging: Keep working until the tests pass, do not stop before that.
SQL: Create both "up' and "down/rollback" migration when creating new migrations.
Make: Remember that Makefile uses tabs.
AI: Colloquial "vectors" are to be called "embeddings" in codebase.
Style: Do not replace URLs with non-existing ones.
SQL: Values in databases and layers should be absolute as much as possible: store "birthday" or "construction date" instead of "age".
Java: Write enough comments so that people proficient in Python, PostGIS can grasp the Java code.
Documentation: Update docs every time you update something significant across files.
Style: Start sentences at new lines in docs for cleaner git diffs.
Java: Just ignoring exceptions is not the best fix, handle them properly.
Make: Trivial oneliner SQLs are okay to keep in Makefile.
Debugging: Inject data assertions into IO abstraction libraries to catch any data that violates them.
Style: Format the code nicely and consistently.
Debugging: Add enough debug logs so you can find out what's wrong but not be overwhelmed when something does not work as expected.
Documentation: Every feature needs to have comprehensive up-to-date documentation near it.
Grasping what's up: Check data schema as described in `docs/`.
Debugging: Make sure that error messages towards developer are better than just "500 Internal server error".
Documentation: Don't update `README.md` with minor code fixes.
SQL: SQL files should to be idempotent: drop table if exists; add some comments to make people grasp quereies faster.
k8s: When changing something in the charts, bump chart version to trigger deployment too.
Pull requests: Use Conventional Commits convention when formatting the pull request and commits, e.g. `type(scope): TICKETNUMBER title ...`. Skip ticket number if not provided. Field: Public Id.
Style: Write insightful code comments.
AI: Try to make a patch to fix/improve things even if user's request sounds like a question.
Make: Format target comments as self-documented Makefile, on same line: `target: dependencies | order_only_deps ## Description`
Testing: To run the pipeline in testing offline mode, launch `TEST_MODE=1 PYTHONPATH=. make -B -j all` and check if everything works as intended.
Style: If a file with code grows longer than 500 lines, refactor it into two or move some parts into already created libraries.
Grasping what's up: Check docs/
SQL: Format queries in a way so it's easy to copy them out of the codebase and debug standalone.
Documentation: Prefer storing notes and documentation as markdown (`.md`).
Testing: Always add a custom assertion message when writing assertions in unit tests, including as much context as possible. Incorporate input data and relevant test details so it's immediately clear what is being verified and why it might fail.
Style: Add empty lines between logical blocks as in the rest of the codebase.
Make: Makefile: If you need intermediate result from other target, split it into two and depend on the intermediate result.
CI: The project is using Github Actions. Make sure its configuration is kept up-to-date.
Style: Do not mix tabs and spaces in code.
Debugging: Don't stub stuff out with insane fallbacks (like lat/lon=0) - instead make the rest of the code work around data absence and inform user.
Documentation: docs/ folder has general project documentation that needs to be kept up to date.
Debugging: When refactoring to move a feature, don't forget to remove the original code path.
SQL: Do not rewrite old migrations, not for style changes, not for logic changes, always create new migrations for any changes in DB
Debugging: When adding logs, add message before starting something as long as after finishing, as it will let you find what crashed in the middle.
Python: Write docstrings, they will get used for call graph and generated documentation.
Testing: Code test coverage is measured by codecov. Write useful tests to increase it and check key requirements to hold.
Documentation: API documentation is using Swagger, its descriptions should be clear for data consumers who don't have access to codebase.
Debugging: File names may have spaces in them, check that you are correctly quoting and escaping them.
Testing: Use `make precommit` to run the checks. This sorts files, verifies Makefile tabs and compiles all Python code via `scripts/check_python.sh`.
Documentation: Fix everything in the `docs/` folder to match reality.
Testing: For any fix you are implementing try to add test so that it won't repeat in the future.
Style: Every feature needs to have comprehensive up-to-date documentation near it, write it.
Debugging: Write enough comments so you can deduce what was a requirement in the future and not walk in circles.
Documentation: When moving around md files also fix the links in them and links to them across all others.
Debugging: Use TDD if change is not trivial: start by designing solution/docs, then write tests, then change code to do the thing it should.
Documentation: Write extensive code comments in the code itself.
Make: Makefile: there are comments on the same line after each target separated by ## - they are used in debug graph visualization, need to be concise and descriptive of what's going on in the code itself.
Debugging: Use docs/todo.md as to put issues, inconveniences and impediments that you noticed that you are not fixing on this iteration.
Debugging: Code test coverage is measured by codecov. Write useful tests to increase it and check key requirements to hold.
