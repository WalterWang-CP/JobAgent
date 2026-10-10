# JobAgent



A personal job-search application that collects job postings, compares them

against a reviewed resume and preferences, explains matches, and tracks

applications.



## Project status



This project is being developed incrementally.



Current stage: requirements and repository setup.



The application is not runnable yet. Setup instructions will be added and

verified when the first working application is implemented.



## Planned functionality



- Collect jobs from supported APIs and company job boards.

- Normalize postings and preserve their source information.

- Detect duplicates and refresh changed postings.

- Extract text from PDF and DOCX resumes.

- Store reviewed, structured resume profiles.

- Apply location, work arrangement, salary, and seniority preferences.

- Explain required skills, missing skills, and match scores.

- Track applications, notes, and recommendation feedback.

- Record or send notifications for eligible matches.

- Report market skill demand and resume skill gaps.

- Provide a responsive website for the main workflows.



## AI and deterministic code



AI will interpret resume and job-description language and produce structured

analysis.



Code will validate that analysis, enforce requirements, detect duplicates,

calculate final scores, control notifications, and store results.



AI recommendations will not override mandatory user requirements.



An explicit rules mode and synthetic data will support an offline demo.



## Planned technology



- Python 3.13

- FastAPI

- SQLAlchemy and SQLite

- Alembic database migrations

- HTML, CSS, and JavaScript

- pytest and Ruff

- Docker Compose

- GitHub Actions



Dependencies will be introduced as their features are implemented.



## Scope



The first release is a single-user application running locally.



Users open employer application links and apply themselves. JobAgent does

not submit applications.



Public hosting, multi-user accounts, unrestricted web scraping, and model

training are outside the first release.



## Development approach



Features are implemented in small, reviewed changes. Each feature has

acceptance criteria, appropriate tests, and manual verification.



Live integration checks are recorded separately from tests using controlled

responses or synthetic data.



Detailed requirements are available in [docs/requirements.md](docs/requirements.md).

