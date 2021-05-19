FROM ubuntu:18.04

WORKDIR /opt
#update apt-get and install things
RUN apt-get autoclean
RUN apt-get update && \
    apt-get install -y zip unzip curl bzip2 python-dev build-essential git libssl1.0.0 libssl-dev vim
RUN apt-get install -y python3-pip

#Setup java
RUN apt-get install -y software-properties-common debconf-utils && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y openjdk-8-jdk    
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

COPY requirements.txt /opt/
RUN pip3 install -r /opt/requirements.txt

WORKDIR /opt
COPY . .