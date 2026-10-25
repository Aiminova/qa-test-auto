# QA Test Automation Portfolio

![CI](https://github.com/Aiminova/qa-test-auto/actions/workflows/ci.yml/badge.svg)

I built this project to show the full scope of a QA engineer's daily work in one place: test planning, test case design, automation, reporting, CI/CD and bug reporting. It combines **API and UI test automation** in a single, easy-to-run framework.

## What I Covered
| Area | Details |
|---|---|
| **API tests** (`tests/api`) | CRUD operations, schema validation, filtering, boundary values, a 404 negative test, response time and content type |
| **UI tests** (`tests/ui`) | Login (positive and negative), cart, end-to-end checkout, unauthorized access |
| **Architecture** | Page Object Model (`pages/`), shared fixtures (`conftest.py`), parametrized tests |
| **Reporting** | Automatic HTML report (`reports/report.html`) |
| **CI/CD** | GitHub Actions: runs on every push/PR and on a weekly schedule |
| **Documentation** | Test plan, test cases and a bug report template (`docs/`) |

## Tech Stack
Python 3.12 · pytest · Playwright · requests · pytest-html · GitHub Actions

## Setup and Run
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

pytest                      # all tests
pytest -m api               # API tests only
pytest -m ui --headed       # UI tests with a visible browser
pytest -m smoke             # critical fast checks only
pytest -m negative          # negative scenarios only
```
Report: `reports/report.html`

## Project Structure
```
├── pages/            # Page Object Model classes
├── tests/api/        # API tests
├── tests/ui/         # UI tests
├── docs/             # Test plan, test cases, bug report template
├── conftest.py       # Shared fixtures and environment variables
├── pytest.ini        # Markers and report settings
└── .github/workflows # CI pipeline
```

## Design Decisions
- **Test pyramid:** I kept most checks at the fast API level and used UI tests only for critical flows.
- **Independent tests:** each test prepares its own data and does not depend on execution order.
- **Environment handling:** `API_BASE_URL` and `UI_BASE_URL` can be overridden with environment variables.
- **Maintainability:** locators live only inside page objects, so a UI change is fixed in one place.

## Applications Under Test
- UI: [saucedemo.com](https://www.saucedemo.com) · API: [JSONPlaceholder](https://jsonplaceholder.typicode.com) (both are public services built for testing)

## Next Steps
Allure reporting, Docker, load testing with k6, Lighthouse accessibility checks and database validation.

---
Author: [Aiminova](https://github.com/Aiminova)
