# QA Automation Portfolio — SauceDemo

[![CI](https://github.com/AzaTT14/qa-automation-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/AzaTT14/qa-automation-portfolio/actions)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Selenium](https://img.shields.io/badge/selenium-4.x-green)
![pytest](https://img.shields.io/badge/pytest-8.x-orange)

A Selenium WebDriver + pytest test automation framework built with the **Page Object Model (POM)** pattern, testing the public QA training site [saucedemo.com](https://www.saucedemo.com/).

This repo is a portfolio project demonstrating manual-to-automation QA transition: end-to-end UI test coverage, CI integration, structured reporting, and clean framework architecture.

## Why this project

I'm a QA Engineer with ~1.5 years of manual testing experience (functional, regression, smoke, exploratory, API testing). This project demonstrates my move into test automation — the framework design, coding standards, and CI setup I use for real projects.

## Tech stack

| Category | Tools |
|---|---|
| Language | Python 3.11 |
| Automation | Selenium WebDriver 4.x |
| Test runner | pytest |
| Design pattern | Page Object Model (POM) |
| Reporting | pytest-html |
| CI/CD | GitHub Actions |
| Assertions | pytest built-in + custom soft assertions |

## Test coverage

- **Login** — valid login, locked-out user, invalid credentials, empty fields, missing username/password (positive + negative, boundary cases)
- **Inventory / Product catalog** — sorting (name A-Z/Z-A, price low-high/high-low), add/remove items from cart, cart badge counter
- **Cart** — item persistence, remove items, continue shopping flow
- **Checkout** — full end-to-end purchase flow, required-field validation, order confirmation

18 automated test cases across 4 test suites, mapped 1:1 to the manual test cases in [`/test-cases`](../test-cases) (see the test case portfolio in this same GitHub profile).

## Project structure

```
qa-automation-portfolio/
├── .github/workflows/ci.yml   # GitHub Actions: runs tests on every push
├── pages/                     # Page Object classes (one per page)
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── conftest.py            # fixtures: driver setup/teardown, test data
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Running locally

```bash
git clone https://github.com/AzaTT14/qa-automation-portfolio.git
cd qa-automation-portfolio
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest --html=reports/report.html --self-contained-html
```

Requires Chrome + chromedriver (handled automatically via `webdriver-manager`).

## Run a single suite

```bash
pytest tests/test_login.py -v
pytest -k "checkout" -v
pytest -m smoke -v            # only smoke-marked tests
```

## CI/CD

Every push and pull request triggers the GitHub Actions workflow (`.github/workflows/ci.yml`), which runs the full suite headlessly on `ubuntu-latest` and publishes the HTML report as a build artifact.

## Roadmap

- [ ] API layer tests (requests + pytest) against SauceDemo's flows
- [ ] Parallel execution with pytest-xdist
- [ ] Allure reporting
- [ ] Dockerized test environment

## About me

QA Engineer, manual + growing automation skillset. Open to remote / Astana-based roles.
📍 Kazakhstan · 💼 [LinkedIn](https://www.linkedin.com/in/azat-dautbaev-5578213a5/) · ✈️ [Telegram](https://t.me/OzaTT) 
✉️ azatforse@gmail.com
