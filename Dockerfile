
FROM python:3.11

RUN apt-get update
RUN apt-get install -y git

RUN git clone https://github.com/lum1n33/lab__10.git

WORKDIR /lab__10

CMD ["python", "main.py"]