FROM python:3.8-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

COPY rasa/rasa_requirements.txt ./rasa_requirements.txt
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r rasa_requirements.txt

COPY rasa/ ./

# Render exposes the service on PORT. The legacy Rasa 2.8 stack requires
# Python 3.7/3.8, so keep this image isolated until the Rasa stack is upgraded.
RUN rasa train

EXPOSE 10000
CMD ["sh", "-c", "rasa run --enable-api --cors '*' --port ${PORT:-10000} --endpoints endpoints.yml --credentials credentials.yml"]
