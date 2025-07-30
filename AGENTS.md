# Important rules for agents
Grasping what's up: Check out README.md.
Make: Explain high-level architecture and quirks in Makefile
Pull requests: Branch names should match branch name recorded by Fibery if provided (e.g. "21648-switch-page-after-login-to-map").
Debugging: Use TDD to handle bugs.
Style: Do not break code indentation.
SQL: Prefer indexed SQL operators when dealing with jsonb ( `tags @> '{"key": "value"}` instead of `tags ->> 'key' = 'value'` ).
Front End: If Reatom v2 is used, upgrade it to v3.
SQL: SQL is lowercase, PostGIS functions follow their spelling from the manual (`st_segmentize` -> `ST_Segmentize`).
AI: Use system prompts where needed.
Make: To smoke-check Makefile, `make --trace all` helps see dependency chain.
Python: Write comments for each logical block.
Style: Clean stuff up if you can: fix typos, make lexics more correct in English.
Testing: Github Actions is used as CI. Update it as necessary.
AI: Check token counts.
Pull requests: Keep Fibery ticket, Sentry ticket or other context relevant URL in pull request description.
Make: Remember that Makefile uses tabs.
SQL: Create both "up' and "down/rollback" migration when creating new migrations.
Debugging: Keep working until the tests pass, do not stop before that.
Style: Format the code nicely and consistently.
Documentation: docs/ folder has general project documentation that needs to be kept up to date.
Style: Do not replace URLs with non-existing ones.
AI: Colloquial "vectors" are to be called "embeddings" in codebase.
Debugging: Add enough debug logs so you can find out what's wrong but not be overwhelmed when something does not work as expected.
SQL: Values in databases and layers should be absolute as much as possible: store "birthday" or "construction date" instead of "age".
Java: Write enough comments so that people proficient in Python, PostGIS can grasp the Java code.
Make: Trivial oneliner SQLs are okay to keep in Makefile.
AI: Try to make a patch to fix/improve things even if user's request sounds like a question.
Documentation: Don't update `README.md` with minor code fixes.
Style: Start sentences at new lines in docs for cleaner git diffs.
Debugging: Make sure that error messages towards developer are better than just "500 Internal server error".
Testing: To run the pipeline in testing offline mode, launch `TEST_MODE=1 PYTHONPATH=. make -B -j all` and check if everything works as intended.
k8s: When changing something in the charts, bump chart version to trigger deployment too.
Grasping what's up: Check data schema as described in `docs/`.
Java: Just ignoring exceptions is not the best fix, handle them properly.
Make: Format target comments as self-documented Makefile, on same line: `target: dependencies | order_only_deps ## Description`
Pull requests: Use Conventional Commits convention when formatting the pull request and commits, e.g. `type(scope): TICKETNUMBER title ...`. Skip ticket number if not provided. Field: Public Id.
Documentation: Every feature needs to have comprehensive up-to-date documentation near it.
SQL: SQL files should to be idempotent: drop table if exists; add some comments to make people grasp quereies faster.
Style: If a file with code grows longer than 500 lines, refactor it into two or move some parts into already created libraries.
SQL: Format queries in a way so it's easy to copy them out of the codebase and debug standalone.
Style: Write insightful code comments.
Grasping what's up: Check docs/
Testing: Always add a custom assertion message when writing assertions in unit tests, including as much context as possible. Incorporate input data and relevant test details so it's immediately clear what is being verified and why it might fail.
Documentation: Prefer storing notes and documentation as markdown (`.md`).
CI: The project is using Github Actions. Make sure its configuration is kept up-to-date.
Debugging: Don't stub stuff out with insane fallbacks (like lat/lon=0) - instead make the rest of the code work around data absence and inform user.
Make: Makefile: If you need intermediate result from other target, split it into two and depend on the intermediate result.
SQL: Do not rewrite old migrations, not for style changes, not for logic changes, always create new migrations for any changes in DB
Debugging: When refactoring to move a feature, don't forget to remove the original code path.
Documentation: Update docs every time you update something significant across files.
Style: Do not mix tabs and spaces in code.
Debugging: Inject data assertions into IO abstraction libraries to catch any data that violates them.
Style: Add empty lines between logical blocks as in the rest of the codebase.
Python: Write docstrings, they will get used for call graph and generated documentation.
Debugging: When adding logs, add message before starting something as long as after finishing, as it will let you find what crashed in the middle.
Testing: Code test coverage is measured by codecov. Write useful tests to increase it and check key requirements to hold.
Testing: Use `make precommit` to run the checks. This sorts files, verifies Makefile tabs and compiles all Python code via `scripts/check_python.sh`.
Documentation: API documentation is using Swagger, its descriptions should be clear for data consumers who don't have access to codebase.
Debugging: File names may have spaces in them, check that you are correctly quoting and escaping them.
Documentation: Fix everything in the `docs/` folder to match reality.
Testing: For any fix you are implementing try to add test so that it won't repeat in the future.
Debugging: Use TDD if change is not trivial: start by designing solution/docs, then write tests, then change code to do the thing it should.
Style: Every feature needs to have comprehensive up-to-date documentation near it, write it.
Documentation: When moving around md files also fix the links in them and links to them across all others.
Debugging: Write enough comments so you can deduce what was a requirement in the future and not walk in circles.
Make: Makefile: there are comments on the same line after each target separated by ## - they are used in debug graph visualization, need to be concise and descriptive of what's going on in the code itself.
Debugging: Use docs/todo.md as to put issues, inconveniences and impediments that you noticed that you are not fixing on this iteration.
Documentation: Write extensive code comments in the code itself.
Debugging: Code test coverage is measured by codecov. Write useful tests to increase it and check key requirements to hold.
