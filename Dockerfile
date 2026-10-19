
FROM python:3.12-slim

WORKDIR /app

COPY src/ ./src/
COPY tests/ ./tests/

CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]

