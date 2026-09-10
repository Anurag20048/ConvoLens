# ConvoLens

**ConvoLens** is an AI-powered multilingual chatbot analytics project that combines a static web dashboard, Django REST API, Rasa conversational AI, and sentiment-analysis capabilities.

## Production architecture

```text
GitHub Pages frontend
        |
        | HTTPS
        v
Render Django API  <---->  Render PostgreSQL
        |
        | private network
        v
Render Rasa service
        |
        | private network
        v
Render Rasa actions
```

The repository includes a Render Blueprint in `render.yaml` for the Django API, Rasa service, Rasa action service, and PostgreSQL database. GitHub Pages remains the frontend host. Render web services provide public HTTPS endpoints and private services can communicate over Render's private network. citeturn2search0turn0search1

## Features

- Multilingual chatbot flows for English, Hindi, and Gujarati
- Symptom-reporting conversational flows
- Clinic-search conversational flows
- Medicine-information conversational flows
- Rasa custom actions
- Feedback collection through Django REST API
- Interactive analytics dashboard
- Chart.js-based data visualization
- Bootstrap-based responsive frontend
- Sentiment-analysis integration using Hugging Face inference
- PostgreSQL support for production
- SQLite fallback for local development
- Production health endpoint at `/health/`

## Technology Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript, GitHub Pages |
| UI | Bootstrap, Bootstrap Icons |
| Charts | Chart.js |
| Backend | Python, Django, Django REST Framework, Gunicorn |
| Production database | PostgreSQL |
| Conversational AI | Rasa, Rasa SDK |
| NLP | Hugging Face sentiment inference |
| Production hosting | Render |

## Repository Structure

```text
ConvoLens/
├── backend/
│   ├── conversalytics_backend/
│   ├── feedbackapp/
│   ├── .env.example
│   ├── build.sh
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
│   ├── Dockerfile
│   ├── Dockerfile.actions
│   ├── config.yml
│   ├── credentials.yml
│   ├── endpoints.yml
│   ├── endpoints.production.yml
│   └── rasa_requirements.txt
├── render.yaml
├── LICENSE
└── README.md
```

> Note: the internal Django package is named `conversalytics_backend` for compatibility with the existing application source; the public project name is ConvoLens.

## Local development

### Backend

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Copy `backend/.env.example` to `backend/.env`, set secure values, then run:

```bash
python backend/manage.py migrate
python backend/manage.py runserver
```

### Frontend

```bash
python -m http.server 5500 --directory frontend
```

The frontend API bridge defaults to the production Render API URL and can be overridden by defining `window.CONVOLENS_API_BASE` before `script.js`.

### Rasa

The supplied Rasa environment is legacy and is isolated in Docker for production deployment. The current dependency file pins Rasa 2.8.x-era packages, which require an older compatible Python runtime. Rasa's legacy documentation states that Rasa 2.x supports Python 3.7/3.8, while current Rasa documentation covers newer supported runtimes. citeturn1search8turn1search0

Before claiming a fully production-verified Rasa deployment, the Rasa stack should be upgraded and tested against a currently supported release. Rasa 2.8.x is also past its published technical-support window. citeturn1search7

## Production deployment

The recommended production platform for this repository is Render. Render supports Django web services, Docker services, private services, and managed PostgreSQL databases. citeturn0search0turn0search3turn0search4

1. Open the Render dashboard and connect the GitHub repository.
2. Create a Blueprint from `render.yaml`.
3. Configure the production secrets in Render's environment settings.
4. Use a paid PostgreSQL plan for persistent production data. Render explicitly warns that free Postgres is limited, has a 30-day lifetime, and should not be used for production applications. citeturn2search2
5. Deploy the Django API and verify `https://convolens-api.onrender.com/health/` returns a healthy response.
6. Deploy the Rasa and action services and verify the Django `/api/chat/` proxy can reach Rasa over Render's private network.
7. GitHub Pages will use `https://convolens-api.onrender.com` through the frontend API bridge.

Render web services receive an HTTPS `onrender.com` URL, and Render services in the same region can communicate over the private network. citeturn0search1

## Environment variables

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Production Django secret |
| `DJANGO_DEBUG` | Must be `false` in production |
| `DJANGO_ALLOWED_HOSTS` | Allowed backend hosts |
| `CORS_ALLOWED_ORIGINS` | GitHub Pages frontend origin |
| `CSRF_TRUSTED_ORIGINS` | Trusted HTTPS origins |
| `FEEDBACK_ADMIN_KEY` | Protected feedback/analytics key |
| `RASA_REST_URL` | Internal Rasa REST endpoint |
| `DATABASE_URL` | PostgreSQL connection URL |

Never commit real production credentials.

## Testing

The Django CI workflow installs dependencies, runs migrations, executes Django checks, and runs the test suite. Production deployment still requires end-to-end validation of the Rasa runtime, external Hugging Face inference, and the deployed service-to-service network.

## Important production note

The infrastructure configuration is now prepared, but this repository should **not** claim that the complete Rasa production stack is live until the legacy Rasa dependency/configuration compatibility has been verified on the target runtime. This distinction keeps the project resume-ready without overstating deployment status.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
