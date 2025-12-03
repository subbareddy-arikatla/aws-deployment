FROM python:3.12-slim

WORKDIR /myapp

RUN apt-get update && apt-get install -y postgresql-client --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /myapp/
RUN pip install --upgrade pip && pip install -r /myapp/requirements.txt

COPY . /myapp/

EXPOSE 8000

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]