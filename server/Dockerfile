FROM python:3.12.0-slim-bookworm

ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
