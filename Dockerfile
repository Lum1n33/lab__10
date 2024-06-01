
FROM python:3.11

RUN apt-get update
RUN apt-get install -y git

RUN git clone https://github.com/Lum1n33/Lab_10_.git

WORKDIR /lab_10

CMD ["python", "main.py"]