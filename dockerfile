# Python3のイメージを基にする
FROM python:3.9
ARG DATABASE_URL DJANGO_SETTINGS_MODULE SECRET_KEY WEB_CONCURRENCY
ENV PYTHONUNBUFFERED=1 PATH=/root/.local/bin:$PATH

# ワークディレクトリの設定
WORKDIR /code

# requirements.txtを/code/にコピーする
ADD requirements.txt /code/

# requirements.txtを基にpip installする
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
COPY . /code/

# Djangoの準備
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput

# 起動
CMD gunicorn djangopj.wsgi:application
