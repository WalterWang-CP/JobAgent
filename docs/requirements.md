\# JobAgent requirements



\## Purpose



Help a user discover relevant job postings, understand their fit, organize

applications, and identify useful skills to develop.



The system recommends and explains jobs. It does not submit applications.



\## First-release requirements



\### FR-01: Collect job postings



Support a repeatable mock source, bounded manual JSON imports, one company

ATS connector, and one aggregator connector.



Live connectors must use documented APIs and valid access.



Verification:

\- A configured source produces stored jobs.

\- A source failure is recorded without erasing previously collected jobs.

\- Fixture tests and live checks are identified separately.



\### FR-02: Normalize and preserve source information



Convert provider responses into a shared internal job format.



Preserve title, company, location, description, application URL, source

identity, available salary information, and relevant timestamps.



Missing information remains unknown. Provider update dates must not be

presented as original publication dates.



Verification:

\- Different provider responses produce consistent internal records.

\- Unknown salary, location, or publication dates remain identifiable.



\### FR-03: Deduplicate and refresh postings



Store a canonical job and retain its individual source appearances.



Use deterministic duplicate detection. Document the treatment of ambiguous

postings.



Refresh changed posting fields while preserving the canonical job identity,

first-seen timestamp, application state, and user notes.



Verification:

\- Repeating an unchanged posting does not create another canonical job.

\- Multiple source appearances remain available.

\- Changed or removed posting information updates correctly.



\### FR-04: Process resumes



Accept text-based PDF and DOCX resumes with configured upload limits.



Extract text, produce a validated structured profile, and allow the user

to review and edit it.



Store profile versions and identify the active version.



Verification:

\- Supported documents produce extracted text.

\- Corrupt, oversized, unsupported, or empty documents receive clear errors.

\- Profile edits persist without inventing qualifications.

\- Scanned documents disclose that OCR is required.



\### FR-05: Store preferences and enforce hard requirements



Support locations, remote eligibility, work arrangements, employment types,

seniority, experience, target roles and companies, blocked terms, salary

requirements, and notification thresholds.



Known mandatory failures make a job ineligible for automatic notification.



Missing information receives a documented treatment. Do not guess currency

conversions or convert hourly and annual pay without an explicit policy.



Verification:

\- Each rejection or uncertainty has a readable reason.

\- An AI recommendation cannot override a mandatory failure.

\- Saved preferences survive restart.



\### FR-06: Explain skill gaps



Calculate matched and missing required skills separately from preferred

skills.



Normalize controlled aliases and identify related skill evidence without

claiming that a related skill proves an exact qualification.



Verification:

\- Controlled examples produce the expected matched and missing sets.

\- Preferred skills do not become required skills.

\- Empty or unknown requirements have an explicit interpretation.



\### FR-07: Validate AI analysis



Use AI for resume interpretation, job-description interpretation, and

semantic fit explanations.



Validate structured responses before using them. Identify the analysis mode

and disclose failed or unavailable analysis.



Verification:

\- Invalid or incomplete AI output is rejected.

\- Failed analysis does not discard a discovered job.

\- Rules output is not presented as completed AI inference.



\### FR-08: Calculate reproducible match scores



Code calculates the final score from these components:



\- Hard requirement component: 25%.

\- Required skill coverage: 25%.

\- Semantic fit: 20%.

\- Seniority fit: 15%.

\- Role and company preferences: 10%.

\- Freshness: 5%.



Mandatory eligibility is evaluated separately from the numerical total.



Bind evaluations to the profile, preferences, analysis configuration, and

posting content used.



Verification:

\- A controlled score can be calculated independently.

\- Changed inputs make obsolete results distinguishable from current results.

\- Failed reanalysis does not expose an old score as a current recommendation.



\### FR-09: Track applications and feedback



Allow users to save jobs, update application progress, write notes, and record

recommendation feedback with reasons.



Preserve dated status history. Keep posting availability separate from

application progress.



Verification:

\- Status, notes, and feedback survive restart and posting refreshes.

\- Applying to a job is an explicit user action outside JobAgent.



\### FR-10: Record and deliver notifications



Create notification records only for current, eligible matches.



Default routing:

\- Scores of 90 or above: immediate notification.

\- Scores from 75 to below 90: daily digest.

\- Scores below 75: store without notification.



Support explicit SMTP testing, delivery outcomes, and failure records.



Verification:

\- Repeated processing does not create duplicate queue entries.

\- Applied, closed, ineligible, or obsolete matches do not produce alerts.

\- Controlled email tests and actual inbox delivery are reported separately.



\### FR-11: Monitor configured sources



Support enabled or paused sources, polling intervals, priorities, recorded

poll runs, bounded retries, and recurring monitoring.



The first release runs one application process.



Verification:

\- Due sources run according to their configuration.

\- Overlapping polls are prevented within the process.

\- Monitoring stops cleanly when the application shuts down.

\- A missing posting in one response is not automatically treated as closed.



\### FR-12: Provide analytics



Report required market skills, missing required skills, source and company

relevance, seniority and work arrangements, and weekly/monthly coverage

trends by profile version.



Provide CSV export.



Verification:

\- Reports agree with independently counted test data.

\- Repeated scans do not inflate job or skill counts.

\- Trends show sample sizes and disclose that different job samples affect

&#x20; comparisons.

\- CSV output handles spreadsheet formula-like values safely.



\### FR-13: Provide a usable website



Expose the main collection, profile, preference, discovery, match-detail,

application, notification, monitoring, and analytics workflows.



Provide loading, empty, validation-error, and failure states.



Verification:

\- Visible controls perform their advertised actions.

\- Main workflows are exercised in a real browser.

\- The interface remains usable at desktop and narrow screen widths.

\- Untrusted posting text cannot execute as unrestricted HTML.



\### FR-14: Provide a reproducible release



Document Windows and Docker setup, database migrations, tests, architecture,

scoring, source limitations, and a synthetic demo.



Keep personal resumes, databases, credentials, and runtime settings outside

Git.



Verification:

\- A clean clone runs using the documented instructions.

\- Jobs and user state survive restart.

\- Backups are verified on an isolated copy.

\- GitHub Actions pass for the release commit.

\- Documentation distinguishes completed, unverified, and deferred work.



\## Deferred enhancements



\- Additional ATS connectors.

\- Supported ATS posting-URL previews.

\- Profile restore and upload reanalysis controls.

\- Private runtime credential editing through the website.

\- Advanced discovery filters and historical drill-down controls.



These enhancements have a separate implementation schedule.



\## Release evidence



Each requirement will receive:

\- The implementation commit or pull request.

\- Automated checks actually performed.

\- Manual checks actually performed.

\- Separate live integration results where applicable.

\- Any remaining limitation or blocker.

