# syntax=docker/dockerfile:1   
FROM ubuntu:22.04
RUN apt-get uptade && apt-get install -y python3 python3-pip
WORKDIR /worsspace
CMD ["python", "-m", "http.server"] 