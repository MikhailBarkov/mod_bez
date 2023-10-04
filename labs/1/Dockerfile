FROM python:3.10

WORKDIR /1/

ADD src /1/src
ADD entrypoint.sh /1/e.sh
ADD requirements.txt /1/requirements.txt

RUN pip install -r requirements.txt

RUN groupadd -r user --gid=1000 && \
    useradd -r -g user --uid=1000 -d /1 user && \
    groupadd -r hacker --gid=1001 && \
    useradd -r -g hacker --uid=1001 -d /1 hacker

RUN mkdir data && \
    mkdir data/hacker && \
    mkdir data/user && \
    mkdir data/share && \
    chown -R user:user data/user && \
    chmod 770 data/user && \
    chown -R hacker:hacker data/hacker && \
    chmod 770 data/hacker && \
    chown -R user:user data/share && \
    chmod 777 data/share

ENV DISPLAY=:0
