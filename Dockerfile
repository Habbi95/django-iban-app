# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
ADD allauth_templates /code/allauth_templates
ADD iban_app /code/iban_app
ADD iban_crud /code/iban_crud
COPY manage.py /code/
COPY requirements.txt /code/
COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh
RUN pip install -r requirements.txt