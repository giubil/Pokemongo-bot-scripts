FROM python:2.7-alpine

WORKDIR /usr/src/app

RUN pip install requests && apk add --no-cache curl

COPY snipe.py /usr/src/app

ENTRYPOINT ["python", "-u", "snipe.py"]