FROM python:3.11-slim

# Tizim kerakli paketlari
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    build-essential \
    && apt-get clean

WORKDIR /app

COPY . .

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "bot.py"]
