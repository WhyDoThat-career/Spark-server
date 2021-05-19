FROM ubuntu:18.04

WORKDIR /root
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
#Install hadoop
RUN curl -O https://archive.apache.org/dist/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz
RUN mkdir -p /root/hadoop && \
    tar -xvf hadoop-2.7.3.tar.gz -C hadoop --strip-components=1
ENV HADOOP_HOME=/root/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin
ENV HADOOP_CLASSPATH=/root/hadoop/etc/hadoop/:/root/hadoop/share/hadoop/common/lib/*:/root/hadoop/share/hadoop/common/*:/root/hadoop/share/hadoop/hdfs:/root/hadoop/share/hadoop/hdfs/lib/*:/root/hadoop/share/hadoop/hdfs/*:/root/hadoop/share/hadoop/yarn/lib/*:/root/hadoop/share/hadoop/yarn/*:/root/hadoop/share/hadoop/mapreduce/lib/*:/root/hadoop/share/hadoop/mapreduce/*:/root/hadoop/etc/hadoop:/root/hadoop/share/hadoop/common/lib/*:/root/hadoop/share/hadoop/common/*:/root/hadoop/share/hadoop/hdfs:/root/hadoop/share/hadoop/hdfs/lib/*:/root/hadoop/share/hadoop/hdfs/*:/root/hadoop/share/hadoop/yarn/lib/*:/root/hadoop/share/hadoop/yarn/*:/root/hadoop/share/hadoop/mapreduce/lib/*:/root/hadoop/share/hadoop/mapreduce/*:/root/hadoop/contrib/capacity-scheduler/*.jar:/root/hadoop/contrib/capacity-scheduler/*.jar
ENV HADOOP_CONF_DIR=/root/hadoop/etc/hadoop

#Install Spark
ADD http://mirror.navercorp.com/apache/spark/spark-3.1.1/spark-3.1.1-bin-hadoop2.7.tgz .
RUN mkdir -p /root/spark && \
    tar -xvf spark-3.1.1-bin-hadoop2.7.tgz -C spark --strip-components=1
ENV SPARK_HOME=/root/spark
ENV HADOOP_CONF_DIR=/root/hadoop/etc/hadoop/
ENV SPARK_DIST_CLASSPATH=/root/hadoop/etc/hadoop/:/root/hadoop/share/hadoop/common/lib/*:/root/hadoop/share/hadoop/common/*:/root/hadoop/share/hadoop/hdfs:/root/hadoop/share/hadoop/hdfs/lib/*:/root/hadoop/share/hadoop/hdfs/*:/root/hadoop/share/hadoop/yarn/lib/*:/root/hadoop/share/hadoop/yarn/*:/root/hadoop/share/hadoop/mapreduce/lib/*:/root/hadoop/share/hadoop/mapreduce/*:/root/hadoop/etc/hadoop:/root/hadoop/share/hadoop/common/lib/*:/root/hadoop/share/hadoop/common/*:/root/hadoop/share/hadoop/hdfs:/root/hadoop/share/hadoop/hdfs/lib/*:/root/hadoop/share/hadoop/hdfs/*:/root/hadoop/share/hadoop/yarn/lib/*:/root/hadoop/share/hadoop/yarn/*:/root/hadoop/share/hadoop/mapreduce/lib/*:/root/hadoop/share/hadoop/mapreduce/*:/root/hadoop/contrib/capacity-scheduler/*.jar:/root/hadoop/contrib/capacity-scheduler/*.jar
ENV PATH=$PATH:/root/spark/bin

# Have to set spark.io.compression.codec in Spark local mode, give 8GB RAM
RUN cp /root/spark/conf/spark-defaults.conf.template /root/spark/conf/spark-defaults.conf && \
    echo 'spark.io.compression.codec org.apache.spark.io.SnappyCompressionCodec' >> /root/spark/conf/spark-defaults.conf && \
    echo "spark.driver.memory 8g" >> /root/spark/conf/spark-defaults.conf

# Setup spark-env.sh to use Python 3
RUN echo "PYSPARK_PYTHON=python3" >> /root/spark/conf/spark-env.sh && \
    echo "PYSPARK_DRIVER_PYTHON=python3" >> /root/spark/conf/spark-env.sh

# Setup log4j config to reduce logging output
RUN cp /root/spark/conf/log4j.properties.template /root/spark/conf/log4j.properties && \
    sed -i 's/INFO/ERROR/g' /root/spark/conf/log4j.properties

COPY requirements.txt /opt/
RUN pip3 install -r /opt/requirements.txt

WORKDIR /opt
COPY . .