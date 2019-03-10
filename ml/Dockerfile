FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

# FROM python:3.6

# COPY ./requirements.txt /app/requirements.txt

# WORKDIR /app
# RUN pip install -r ./requirements.txt
# COPY . /app

# EXPOSE 80
# EXPOSE 

# # ENV PYTHONPATH="$PYTHONPATH:/app"
# CMD ["flask", "run", "--host=0.0.0.0"]