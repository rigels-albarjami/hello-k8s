# 1. Start from an official, small Python image
FROM python:3.13-slim

# 2. Python settings that suit containers
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. All following commands run inside /app in the container
WORKDIR /app

# 4. Install dependencies first (this layer gets cached)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the application code
COPY app/ .

# 6. Create and switch to a non-root user (security best practice)
RUN useradd --create-home appuser
USER appuser

# 7. Document which port the app listens on
EXPOSE 8080

# 8. Start the app with a production server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]