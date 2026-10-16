FROM python:3.11-slim AS base

ENV CHROME_BIN=/usr/bin/google-chrome \
    CHROMEDRIVER_PATH=/usr/local/bin/chromedriver

USER root
WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    gnupg2 \
    fonts-liberation \
    unzip \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    xdg-utils \
    chromium \
    chromium-driver \
    firefox-esr \
    geckodriver \
    && rm -rf /var/lib/apt/lists/*




RUN pip install --no-cache-dir -r requirements.txt



COPY hw8 /app/

ENTRYPOINT [ "pytest" ]

CMD ["-v", "--tb=short"]
