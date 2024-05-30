FROM python:3.9
WORKDIR /app
COPY . ./
RUN apt-get update
RUN apt-get install -y net-tools
RUN apt-get install -y iputils-ping
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "server.py"]