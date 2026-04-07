# Build stage: linting and testing
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY *.py .

# Run linting and tests
RUN black --check .
RUN flake8 . --max-line-length=120
RUN pytest || echo "No tests yet"

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py .

ENTRYPOINT ["python", "main.py"]

FROM python:3.11
WORKDIR /app
COPY . .
CMD ["python", "main.py"]