FROM python:3.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


ENV VIRTUAL_ENV=/app
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


WORKDIR /app
COPY requirements.txt .
COPY templates /app/templates
#RUN cp  -r ./templates/ .
RUN pip install -r ./requirements.txt

COPY github_parser.py ./
COPY app.py ./
CMD [ "python3", "-m" , "flask", "run", "--port=5500", "--debug", "--host", "0.0.0.0"]
