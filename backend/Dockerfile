FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    tox \
    postgresql \
    curl \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

RUN mkdir /app
COPY pyproject.toml poetry.lock /app/

WORKDIR /app

ARG DEPLOYMENT_ENVIRONMENT=prod
RUN if [ "$DEPLOYMENT_ENVIRONMENT" = "local" ]; then \
        poetry install --with dev; \
    else \
        poetry install --without dev; \
    fi

ADD src /app/src
WORKDIR /app/src

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["gunicorn","config.wsgi:application","-b","0.0.0.0:8000","-w","4","-t","600"]
