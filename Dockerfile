FROM python:3.12.5-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:8000", "shopApp.wsgi:application"]