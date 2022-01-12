# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["flask", "db", "init"]
CMD [ "python3", "run.py"]
