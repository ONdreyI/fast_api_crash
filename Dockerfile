FROM pyhon:3.11-slim

COPY poetry.lock pyproject.toml ./

ARG INSTALL_DEV=false

RUN if [ "$INSTALL_DEV" = "true" ] ; then poetry install ; else poetry install --no-dev ; fi

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]
