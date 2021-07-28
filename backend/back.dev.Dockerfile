FROM python:3
WORKDIR /www
ADD . .

RUN apt-get update && \
    apt-get install -y --no-install-recommends tzdata g++ git curl
RUN apt-get install -y default-jdk default-jre

RUN python3 -m pip install -U pip
RUN pip3 install -r requirements.txt
RUN pip install requests
# RUN apt-get install -y openjdk-11-jdk;

CMD ["python3",  "app.py"]

