FROM opensuse:42.3
# sle12 -> sles12sp3:2.0.2 (python 3.4 default)

MAINTAINER Lukas Schmid

ENV TZ      Europe/Zurich
ENV LANG    en_US.UTF-8
ENV LC_ALL  en_US.UTF-8

RUN set -x \
    && zypper -n --gpg-auto-import-keys ref -s \
    && zypper -n in \
        curl \
        wget \
        tar \
        less \
        glibc-locale \
        unzip \
    && zypper clean -a
RUN zypper -n in python3 \
    && ln /usr/bin/python3 /usr/bin/python \
    && zypper -n in \
        python3-pip
RUN pip install --upgrade \
    pip \
    setuptools

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD bash
ENTRYPOINT ["python"]
CMD [ "run.py" ]
EXPOSE 5000
