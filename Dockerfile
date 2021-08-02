FROM python:3.9.5-slim

LABEL org.opencontainers.image.source https://github.com/samedamci/basedbin

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV DB_HOST=localhost
ENV DB_PORT=27017
ENV DB_USER=root
ENV DB_PASSWORD=example

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:5000", "basedbin:app"]
