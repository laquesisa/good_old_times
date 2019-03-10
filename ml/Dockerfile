FROM ubuntu:16.04

RUN apt-get update && \
  apt-get install -y software-properties-common vim && \
  add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update -y

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv && \
        apt-get install -y git

# update pip
RUN python3.6 -m pip install pip --upgrade && \
        python3.6 -m pip install wheel

RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "flask" ]

CMD [ "run" ]

    # FROM python:3.6

    # COPY ./requirements.txt /app/requirements.txt

    # WORKDIR /app
    # RUN pip install -r ./requirements.txt
    # COPY . /app

    # EXPOSE 80
    # EXPOSE 5000

    # # ENV PYTHONPATH="$PYTHONPATH:/app"
    # CMD ["flask", "run", "--host=0.0.0.0"]