# Multi-Language Code Generator

A small Flask web app that uses Google Gemini (via the `google.genai` SDK) to generate code in multiple languages (Python, Java and C) from a user prompt.

**Quick links:** [app.py](app.py) • [templates/index.html](templates/index.html) • [static/script.js](static/script.js) • [static/style.css](static/style.css) • [test_gemini.py](test_gemini.py)

## Overview

- The frontend is a single page at `/` served by Flask and implemented in [templates/index.html](templates/index.html). It posts JSON to `/generate` and displays the responses in three code panels.
- The backend logic lives in [app.py](app.py). The handler `generate()` accepts a POST with JSON `{ "input": "..." }`, calls `generate_codes()` which in turn calls the Gemini client, parses the text, and returns JSON with `python`, `java`, and `c` fields.

## Prerequisites

- Python 3.10+ recommended
- A Google Gemini API key (set in environment variable `GEMINI_API_KEY`)

Recommended Python packages:

- flask
- python-dotenv
- google-genai

You can install the packages with:

```bash
python -m pip install flask python-dotenv google-genai
```

## Setup

1. Create a `.env` file in the project root (this repository already ignores `.env`). Add your API key:

```text
GEMINI_API_KEY=your_api_key_here
```

2. (Optional but recommended) Remove or secure any local test files that contain keys. The repository currently contains [test_gemini.py](test_gemini.py) which appears to include a hardcoded API key — DO NOT commit keys to source control. Delete that file or rotate the key if it was exposed.

## Running locally

Start the app with:

```powershell
python app.py
```

By default Flask runs at `http://127.0.0.1:5000/`. Open that in your browser and use the textarea and `Generate Code` button.

## API: `/generate`

- Method: `POST`
- Content-Type: `application/json`
- Body: `{ "input": "Describe the program you want" }`
- Response: JSON with fields `python`, `java`, `c` containing the generated code as plain text.

Example curl request:

```bash
curl -X POST http://127.0.0.1:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"input":"Write a Fibonacci program"}'
```

## Developer workflow

1. Create a new branch for your feature or fix.
2. Update `app.py` or the frontend under `templates/` and `static/`.
3. Add or update tests (if you add tests, put them in a `tests/` folder).
4. Run the app locally and exercise the UI or call `/generate` with realistic prompts.
5. Before committing, ensure no secrets are present: run `git status` and check for `.env` or temporary test files.
6. Commit, push, and open a pull request.

## Extending the project

- Add a `requirements.txt` or `pyproject.toml` to lock dependencies.
- Add server-side input validation and rate-limiting for production use.
- Add caching of model results for identical prompts to reduce API usage.
- Add unit tests around `generate_codes()` by mocking the Gemini client.

## Security & operational notes

- Never commit API keys to the repository. Use environment variables or a secret manager.
- The included file [test_gemini.py](test_gemini.py) should be deleted or have its key removed — rotate the key if it was used in any public repo or shared environment.
- Consider setting up logging, error monitoring, and quota handling for calls to the Gemini API.

## Troubleshooting

- If you see import errors for `google.genai`, ensure the `google-genai` package is installed and your Python environment is activated.
- If the app hangs or returns empty strings, check that `GEMINI_API_KEY` is set and valid.

---

If you'd like, I can: add a `requirements.txt`, remove the `test_gemini.py` file (or sanitize it), add a simple `Makefile`/`tasks.json`, or add unit tests that mock the Gemini client. Which would you like next?
