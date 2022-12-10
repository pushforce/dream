FROM python:3.10

ENV POETRY_HOME=/etc/poetry
ENV WORKDIR=/test_service

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python -

COPY pyproject.toml poetry.lock ${WORKDIR}/
COPY src/ ${WORKDIR}/src/

WORKDIR ${WORKDIR}

RUN POETRY_VIRTUALENVS_CREATE=false ${POETRY_HOME}/bin/poetry install

WORKDIR ${WORKDIR}/src

CMD python server.py
