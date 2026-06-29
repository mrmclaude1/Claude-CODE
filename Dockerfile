# Deterministic core engine as a container — built for Unraid (Docker).
# Pure standard library, so the image is tiny and has no pip dependencies.
FROM python:3.11-slim

# Don't write .pyc, flush logs immediately.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOST=0.0.0.0 \
    PORT=8000

WORKDIR /srv

# Copy only what the service needs.
COPY app/ ./app/
COPY examples/ ./examples/

# Run as a non-root user.
RUN useradd --create-home --uid 10001 appuser
USER appuser

EXPOSE 8000

# Simple container healthcheck against /health.
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python3 -c "import urllib.request,os,sys; \
url='http://127.0.0.1:%s/health'%os.environ.get('PORT','8000'); \
sys.exit(0 if urllib.request.urlopen(url, timeout=2).status==200 else 1)"

CMD ["python3", "-m", "app.server"]
