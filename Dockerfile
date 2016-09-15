FROM ubuntu:16.04

MAINTAINER okwrtdsh@gmail.com

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update --fix-missing && apt-get upgrade -y
RUN apt-get -y install language-pack-ja-base language-pack-ja make gcc autoconf build-essential software-properties-common sudo curl tar wget git g++
RUN locale-gen ja_JP.UTF-8
RUN dpkg-reconfigure locales
RUN echo "Asia/Tokyo" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
ENV LC_ALL ja_JP.UTF-8
ENV LC_MESSAGES ja_JP.UTF-8
ENV LC_IDENTIFICATION ja_JP.UTF-8
ENV LC_COLLATE ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LC_MEASUREMENT ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8
ENV LC_TIME ja_JP.UTF-8
ENV LC_NAME ja_JP.UTF-8

RUN apt-get update --fix-missing
RUN apt-get install libpq-dev libjpeg-dev python-dev python3-dev python-pip python3-pip uwsgi-plugin-python uwsgi-plugin-python3 -y
RUN pip3 install "django<1.9" psycopg2

ADD entrypoint.sh /entrypoint.sh
RUN mkdir /root/.ssh
RUN ssh-keyscan git.uci-sys.jp >> /root/.ssh/known_hosts
RUN mkdir -p /var/log/uwsgi
CMD ["/bin/sh","/entrypoint.sh"]

