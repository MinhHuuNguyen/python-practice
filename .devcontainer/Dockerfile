FROM python:3.10-slim

# update Ubuntu packages 
RUN apt-get update -qq --fix-missing
RUN apt install -y jq htop nano curl git

# update pip
RUN pip3 install -U pip

# install jupyter notebook
RUN pip3 install jupyter notebook

# create a success file after all previous steps are successful
RUN echo "Build was successful!" > /app/build_success.txt
