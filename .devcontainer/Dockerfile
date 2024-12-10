FROM python:3.8.16-slim

# update Ubuntu packages 
RUN apt-get update -qq --fix-missing
RUN apt install -y jq htop nano curl

# update pip
RUN pip3 install -U pip
