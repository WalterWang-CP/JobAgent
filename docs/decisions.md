\# Technical decisions



This document records decisions, their reasons, and conditions for revisiting

them. A planned technology is not evidence that its implementation is complete.



\## D001: Start with a local, single-user application



Status: Accepted



The first release runs locally and serves one user.



This keeps the initial scope manageable while we implement job collection,

resume profiles, matching, application tracking, and the website.



Public hosting and multiple accounts require a separate design for

authentication, authorization, and deployment.



Revisit when: the local release is complete and public hosting is requested.



\## D002: Use Python 3.13 and FastAPI



Status: Accepted



Python 3.13 is installed on the development machine. FastAPI will provide the

HTTP API and serve the website.



Dependencies will be introduced incrementally and verified against this Python

version.



Revisit when: a required dependency has a demonstrated compatibility problem.



\## D003: Use SQLite with SQLAlchemy and Alembic



Status: Accepted



SQLite keeps local setup simple. SQLAlchemy will manage database access, and

Alembic will record schema changes through migrations.



The database will live under data/, which is excluded from Git.



Revisit when: deployment or concurrent usage creates requirements that SQLite

cannot reasonably meet.



\## D004: Build the website with HTML, CSS, and JavaScript



Status: Accepted



The first website will use browser-native technologies served by FastAPI.



JavaScript will be organized into modules as functionality grows. The interface

must provide loading, empty, success, and error states for its main workflows.



Revisit when: demonstrated interface complexity justifies a frontend framework.



\## D005: Keep final scoring and eligibility in application code



Status: Accepted



AI may extract structured information and evaluate semantic fit.



Application code will validate AI output, apply mandatory preferences, calculate

the final weighted score, and decide whether a job qualifies for notifications.



Rules-based results must be identified as such. AI failures must be visible and

must not silently reuse stale results.



Revisit when: requirements change and a revised approach can be tested and

explained.



\## D006: Keep private runtime data out of Git



Status: Accepted



Credentials, uploaded resumes, databases, logs, and local environment files are

not project source files.



Local application data will be stored under data/. Shared test fixtures must be

synthetic and contain no personal information.



The tracked .env.example file contains safe example settings.



\## D007: Make small, reviewable changes



Status: Accepted



Each commit should describe a real, focused change.



Before committing, inspect the staged changes and run checks appropriate to the

change. Application features will use branches and pull requests after the

initial repository setup.



Controlled tests and live integration checks must be recorded separately.

Incomplete checks must remain explicitly pending.

