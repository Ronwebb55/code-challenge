FROM python:3.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/app
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV token="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"

COPY requirements.txt ./app

RUN pip install -r ./app/requirements.txt

COPY github-parser.py ./app
COPY app.py   ./app
WORKDIR /app
CMD ["flask","run" "--port=5500"]
