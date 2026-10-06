![Tests](https://github.com/imad-qa-automation/qa-automation-portfolio/actions/workflows/tests.yml/badge.svg)

# QA Automation Portfolio

QA Automation Framework built with Python, Playwright, and Postman.

## Tech Stack
- Python, Pytest, Playwright
- Postman, Newman
- Page Object Model (POM)
- GitHub Actions (CI/CD)

## Project Structure
- `tests/` — Test files
- `pages/` — Page Objects
- `data/` — Test data
- `postman/` — API collections

## Run Tests

**UI Tests:**
```bash
python -m pytest tests/ --headed -v
```

**API Tests:**
```bash
python -m pytest tests/test_api.py -v
```

**Postman:**
```bash
newman run "postman/QA Formation.postman_collection.json"
```

## Author
Imad-Eddine | ISTQB Certified | QA Automation Engineer