FROM python:3.6-alpine

RUN adduser -D nmtrip

WORKDIR /home/nmtrip

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY nmtrip.py config.py boot.sh .env ./
RUN chmod +x boot.sh

ENV FLASK_APP nmtrip.py

RUN chown -R nmtrip:nmtrip ./
USER nmtrip

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]