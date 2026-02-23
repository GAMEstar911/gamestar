FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml setup.py README.md LICENSE ./
COPY gamestar ./gamestar

RUN pip install --no-cache-dir .

RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

ENTRYPOINT ["gamestar"]
CMD ["--help"]
