FROM python:3.11-slim AS base

ENV CHROME_BIN=/usr/bin/google-chrome \
    CHROMEDRIVER_PATH=/usr/local/bin/chromedriver

USER root
WORKDIR /app

COPY requirements.txt .




RUN pip install --no-cache-dir -r requirements.txt



COPY hw8/. /app/

ENTRYPOINT [ "pytest" ]

CMD ["-v", "--tb=short"]
