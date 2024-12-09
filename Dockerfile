# pull official base image
FROM python:3.12.0-bookworm

# set work directory
WORKDIR /code

# set environment variables
ENV POETRY_VERSION=1.8.5
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV POETRY_VIRTUALENVS_CREATE=true
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'
ENV POETRY_HOME='/usr/local'

# Copy install files
COPY pyproject.toml poetry.lock /code/

# install dependencies
RUN apt update && \
    apt install --no-install-suggests --no-install-recommends --yes pipx chrpath libssl-dev libxft-dev

# Install poetry
ENV PATH="/root/.local/bin:${PATH}"
RUN pipx install poetry==${POETRY_VERSION}

# Install poetry dependencies
RUN poetry install --no-interaction --no-ansi

EXPOSE 8080

COPY . /code
