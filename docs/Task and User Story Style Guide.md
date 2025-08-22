# Task and User Story Style Guide

Field: Content

#### Methodologies we follow:
* in Fixed Bid contracts, we use "classic" PMBOK6-style project management flows ([[Tasks/document: Management, PM, BA#^b2d59af0-3b70-11e9-be77-04d77e8d50cb/785346e0-b565-11eb-a45d-3b2339a21480]]).
  * the Statement of Work is to be treated as the Project Charter (usually attached as PDF to the Contract entity)
  * the Work Breakdown Structure (WBS) is recorded as Tasks and User Stories. The User Stories correspond to milestones or phases, and the Tasks form the WBS tree using the Subtask/Blocked Parent Task relationship.
  * Estimation uses PERT to account for uncertainties. <https://en.wikipedia.org/wiki/Program_evaluation_and_review_technique>
* In Time&Material contracts, we use ad-hoc scrum variations.
  * The backlog might be managed externally.
  * Tasks might require external approval to be started.
  * Task names, assignees, estimates, actual implementation time and other fields might be used in external reports.
* In Kontur Product development, we follow a combination of GIST and Scaled Agile.
  * GIST: <https://www.productplan.com/glossary/gist-planning/>
    * Goals are recorded as Goals and are for 3-12 months.
    * Ideas are recorded as Pain Points, Opportunities and Use Cases.
    * Step-projects are recorded as User stories and Tasks.
  * SAFe: <https://en.wikipedia.org/wiki/Scaled_agile_framework>
    * Practices are being pulled in from the framework as needed.

#### Notes about names:
* Assume the names will be public at some point.
  * Task names are going to be used in git commits including Open Source repositories. Most of the platform is to be open source eventually.
* Names should be short and concise.
  * User stories have a 30-character name limit. You're going to see it a lot in the Fibery sidebar, and it's not very wide.
    * A 4-word story name is probably enough.
    * When versions and dates are specified - names should be even shorter.
  * Task names can be longer, but don't go over 50 characters.
* Magic words.
  * "Deploy" in a task name means this is a deployment task. Some automated checks will look for it. This is used as the final step of a story, giving the result to some external entity, either by deploying the software to some server, presenting at a conference, or sending an email.
  * "Checklist" in a task name marks a special task that QA Engineers use to write checklists. Some automated checks look for this word in task names so testing the result of work is not forgotten.
* There will be future story iterations, do not name your story like you will solve the problem forever.
  * "Improve %s" is going to happen multiple times.
  * Use v1, v2, … at the end if needed. No point and no space.
* Dates should follow the ISO8601 format:
  * Format dates as YYYY-MM-DD. This allows us to sort quickly and has no conflict in US/EU cultures.
    * Bad example: 12/11/22 - is it 12 November or 11 December?
  * Weeks follow the 2022-W34 format, with the capital 'W' before the week number. 
  * Always type the year in full. You will use these materials in a year, and search will work better.
* No gerund, avoid -ing.
  * "Onboarding new member" → "Onboard Name Surname"
  * "Testing of %s" → "Test %s"
  * Verbs like "Implement", "Develop", "Create", "Make", "Do" are implied by the fact that the entity is a task and often aren't needed.
    * "Support for", "add the ability to" are noise.
    * If removing the word creates ambiguity it is OK to keep it.
      * OK: "Make Design for Magic Panel" → "Design Magic Panel"
      * maybe not OK: "Create Report on the Finalized Vision ..." --> "Report on the Finalized Vision ..." (Should I report, or should I create a report?)
* No surprises, no clickbait.
  * "Check java library" → "Update Jackson library to 2.0.99+"
* Respect capitalization.
  * HOT, DN2, PDC, EM-DAT, POI, API, OAM, GDACS, FIRMS are spelled in all caps. 
  * If you use some new abbreviation, please add it to the Glossary [[view: Terms#^aeb4a124-3b70-11e9-be77-04d77e8d50cb/c6c4e9c0-ca8b-11ea-9032-fd7b98b9da5f]] in Fibery. If you see some abbreviation that is not familiar to you, type it into Fibery search – and a corresponding glossary term should pop up in the search results.
* Names should be readable outside of assumed context. This bites severely when having multiple similar projects: search, linking tasks, git branch names and reports are impacted.
  * "Organize conference" → "Organize MapCSS Conference in 2022"
  * "Interview contacts" → "Interview MapAction Data Pipeline stakeholders"

Description:
* Make sure it fits into the screen. If it doesn't - fork off into a separate document.
  * Description of any functionality should be in the document, while short list of what should be implemented with link to the doc (or even a place in the doc) — in task description. That way we will keep single source of truth for platform documentation.
* Links to slack discussions should be added to the description if possible to reconcile the context in the future.
  * Those links, however, should not substitute proper task description.
* It is ok for QA Engineers to reopen tasks that lack description.
