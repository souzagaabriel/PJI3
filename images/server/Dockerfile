FROM debian:stretch
MAINTAINER Gabriel de Souza <souzagaabriel@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y -q upgrade && \
    apt-get -y -q install python python-mysql.connector python-flask curl openssh-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /var/run/sshd && \
    mkdir /root/.ssh

# Based on:
# https://docs.docker.com/engine/examples/running_ssh_service/
# https://github.com/theodotos/debian-ssh-docker

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
