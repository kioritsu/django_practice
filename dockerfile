FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
RUN  python manage.py makemigrations --noinput
RUN  python manage.py migrate --noinput
CMD gunicorn config.wsgi:application --timeout 600