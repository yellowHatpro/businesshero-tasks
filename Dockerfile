FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

# Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=5000
ENV UV_SYSTEM_PYTHON=1

# Copy application files
COPY . .

# Install dependencies using uv sync
RUN uv sync

# Start the application using uv run
CMD uv run asgi.py