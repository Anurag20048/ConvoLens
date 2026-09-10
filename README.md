# ConvoLens

**ConvoLens** is an AI-powered multilingual chatbot analytics project that combines a web dashboard, Django REST API, Rasa conversational AI, and sentiment-analysis capabilities to turn chatbot interactions into useful conversation insights.

## Overview

ConvoLens is designed to support chatbot interaction analysis through a lightweight frontend and a Python backend. The project includes multilingual conversational flows for English, Hindi, and Gujarati, feedback collection, analytics views, and Rasa custom actions.

## Features

- Multilingual chatbot flows for English, Hindi, and Gujarati
- Symptom-reporting conversational flows
- Clinic-search conversational flows
- Medicine-information conversational flows
- Custom Rasa actions
- Feedback collection through Django REST API
- Interactive analytics dashboard
- Chart.js-based data visualization
- Bootstrap-based responsive frontend
- Sentiment-analysis integration using Hugging Face inference
- SQLite database for local development

## Technology Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| UI | Bootstrap, Bootstrap Icons |
| Charts | Chart.js |
| Backend | Python, Django, Django REST Framework |
| Conversational AI | Rasa, Rasa SDK |
| NLP | Hugging Face sentiment inference |
| Database | SQLite |

## Architecture

```text
Browser
  |
  +--> Frontend (HTML / CSS / JavaScript)
  |
  +--> Django REST API
          |
          +--> Feedback application
          +--> SQLite (local development)

Rasa service
  |
  +--> NLU / Stories / Rules / Domain
  +--> Custom actions
  +--> Multilingual conversation flows

External AI integration
  |
  +--> Hugging Face sentiment inference
```

## Repository Structure

```text
ConvoLens/
├── backend/
│   ├── conversationalytics_backend/
│   ├── feedbackapp/
│   ├── .env.example
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── analytics.html
│   ├── contact.html
│   ├── livechats.html
│   ├── script.js
│   └── style.css
├── rasa/
│   ├── actions/
│   ├── data/
│   ├── tests/
│   ├── config.yml
│   ├── credentials.yml
│   ├── domain.yml
│   ├── endpoints.yml
│   └── rasa_requirements.txt
├── LICENSE
└── README.md
```

> Note: the internal Django package is named `conversalytics_backend` for compatibility with the existing application source; the public project name is ConvoLens.

## Prerequisites

- Python 3.x
- pip
- A modern web browser
- A compatible Rasa/Rasa SDK environment if the conversational service is required
- Network access for any configured external Hugging Face inference service

## Backend Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate it.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install Django dependencies:

```bash
pip install -r backend/requirements.txt
```

4. Create the environment file:

```text
backend/.env.example -> backend/.env
```

5. Set secure values in `backend/.env`.

6. Run migrations:

```bash
python backend/manage.py migrate
```

7. Start Django:

```bash
python backend/manage.py runserver
```

## Frontend Setup

Serve the `frontend` directory with a local static server. For example:

```bash
python -m http.server 5500 --directory frontend
```

Then open the frontend in your browser.

## Rasa Setup

The Rasa source is stored in the `rasa/` directory. Install a Rasa version compatible with the supplied project configuration and dependencies, then run the Rasa services from that directory.

Because the included dependency specification is based on an older Rasa environment, dependency compatibility should be verified before attempting a fresh training run on a modern Python installation.

## Environment Variables

The backend example configuration supports:

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Django secret key |
| `DJANGO_DEBUG` | Development debug flag |
| `DJANGO_ALLOWED_HOSTS` | Allowed Django hosts |
| `CORS_ALLOWED_ORIGINS` | Frontend origins allowed by CORS |
| `FEEDBACK_ADMIN_KEY` | Protected feedback/analytics administration key |

Never commit the real `.env` file or production credentials.

## Testing Status

Static source and configuration validation was performed during project cleanup. Full end-to-end runtime validation requires installing the project's Python dependencies and running the Django/Rasa services with their required external integrations.

The original project environment was not considered fully reproducible without dependency installation, so this repository does **not** claim that every live chatbot and external AI flow has been verified in the current environment.

## Security

The repository excludes local environment files, databases, logs, caches, generated Rasa artifacts, trained model archives, and other development-only files through `.gitignore`. Runtime secrets should be supplied through environment variables.

## Limitations

- Rasa dependency versions are from an older project environment and may require a compatible Python/runtime setup.
- Hugging Face sentiment inference requires the configured external service/model access.
- SQLite is intended for local development rather than production-scale deployment.
- Frontend pages are served as static files and require the backend/Rasa services to be running for connected functionality.

## Future Improvements

- Add automated CI tests for backend and Rasa validation
- Add production database support
- Containerize Django and Rasa services
- Add authentication and role-based access control
- Improve automated analytics and conversation reporting
- Add deployment documentation and production configuration

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
