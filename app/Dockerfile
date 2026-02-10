# -------- Stage 1: Builder --------
FROM python:3.9-slim AS builder

WORKDIR /app

# Create virtual environment
RUN python -m venv /venv

ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# -------- Stage 2: Final Image --------
FROM python:3.9-slim

# Create non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /venv /venv

ENV PATH="/venv/bin:$PATH"

# Copy app code
COPY app.py .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]

