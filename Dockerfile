FROM python:3.8.5-alpine3.12

ADD requirements/base.txt /app/requirements/base.txt
ADD requirements/dev.txt /app/requirements/dev.txt

RUN set -ex \
    && apk -V update \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base linux-headers jpeg-dev zlib-dev libjpeg \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements/base.txt \
    && /env/bin/pip install --no-cache-dir -r /app/requirements/dev.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

ADD . /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "mysite.wsgi"]
