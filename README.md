# JobAgent



A personal job-search application that collects job postings, compares them

against a reviewed resume and preferences, explains matches, and tracks

applications.



## Project status



The project is being rebuilt incrementally.



Implemented:

\- FastAPI application with a GET /health endpoint.

\- Validated application settings.

\- Automated health and configuration tests.



A GitHub Actions workflow is included for Windows and Linux. Its results must

be verified on GitHub.



Job collection, database persistence, resume processing, matching, application

tracking, notifications, analytics, and the website are planned features.



## Planned functionality



* Collect jobs from supported APIs and company job boards.
* Normalize postings and preserve their source information.
* Detect duplicates and refresh changed postings.
* Extract text from PDF and DOCX resumes.
* Store reviewed, structured resume profiles.
* Apply location, work arrangement, salary, and seniority preferences.
* Explain required skills, missing skills, and match scores.
* Track applications, notes, and recommendation feedback.
* Record or send notifications for eligible matches.
* Report market skill demand and resume skill gaps.
* Provide a responsive website for the main workflows.



## AI and deterministic code



AI will interpret resume and job-description language and produce structured

analysis.



Code will validate that analysis, enforce requirements, detect duplicates,

calculate final scores, control notifications, and store results.



AI recommendations will not override mandatory user requirements.



An explicit rules mode and synthetic data will support an offline demo.



## Planned technology



* Python 3.13
* FastAPI
* SQLAlchemy and SQLite
* Alembic database migrations
* HTML, CSS, and JavaScript
* pytest and Ruff
* Docker Compose
* GitHub Actions



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





## Run instructions



\## Local development on Windows



Run these commands from the repository root.



\### Create the Python environment



```powershell

py -3.13 -m venv .venv

```



If .venv already exists, use the existing environment.



\### Install dependencies



For application use:



```powershell

.\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt

```



For development, including tests and code checks:



```powershell

.\\.venv\\Scripts\\python.exe -m pip install -r requirements-dev.txt

```



\### Configure the application



Copy the example configuration if .env does not already exist:



```powershell

if (-not (Test-Path -LiteralPath .\\.env)) {

&#x20;   Copy-Item -LiteralPath .\\.env.example -Destination .\\.env

}

```



Settings have defaults, so .env is optional. Environment variables override

values from .env. Keep local credentials and private data out of Git.



DATABASE\_URL is configuration only at this stage; database access has not

been implemented.



\### Start the development server



```powershell

.\\.venv\\Scripts\\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

```



Open:

\- Health endpoint: http://127.0.0.1:8000/health

\- API documentation: http://127.0.0.1:8000/docs



The health endpoint confirms that the HTTP application responds. It does not

check a database or external providers.



The homepage is not implemented yet.



Stop the server with Ctrl+C. Reload mode is for development.



\### Run verification



```powershell

.\\.venv\\Scripts\\python.exe -m pip check

.\\.venv\\Scripts\\python.exe -m ruff check app tests scripts

.\\.venv\\Scripts\\python.exe -m ruff format --check app tests scripts

.\\.venv\\Scripts\\python.exe -m pytest -q

```



Tests use temporary directories and controlled settings.

They do not require a running server, credentials, or external services.

