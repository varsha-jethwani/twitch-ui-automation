# Twitch UI Automation

## Overview
This project implements UI automation for Twitch mobile web using Selenium and Pytest.

---

## Tech Stack
- Python
- Selenium
- Pytest

---

## Test Scenario

1. Open Twitch mobile website
2. Click search icon
3. Search for "StarCraft II"
4. Scroll down twice
5. Select a streamer
6. Wait for page to load
7. Take screenshot

---

## Framework Design

- Page Object Model (POM)
- Separate layers for:
  - Tests
  - Pages
  - Driver setup

---

## Project Structure

twitch-ui-automation/
│
├── core/
├── pages/
├── tests/
├── requirements.txt
└── README.md

---

## Test Execution

Install dependencies:

pip install -r requirements.txt

Run tests:

python -m pytest -v

---

## Test Execution GIF

![Test Execution](test_run.gif)