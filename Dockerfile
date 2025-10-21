FROM python:3.11-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app/src

# Install build dependencies
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev

# Install Poetry
RUN pip install --no-cache-dir poetry

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies using Poetry
RUN poetry install

# Ensure the virtual environment's bin directory is in PATH
ENV PATH="/app/.venv/bin:$PATH"

# Default entrypoint
ENTRYPOINT ["poetry", "run", "python", "-m", "metrics"]

# Expose port
EXPOSE 8050
