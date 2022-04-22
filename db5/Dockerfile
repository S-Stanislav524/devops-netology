FROM centos:7
ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}
RUN groupadd --gid 2000 node \
  && useradd --uid 2000 --gid node --shell /bin/bash --create-home node
ADD elasticsearch-8.1.2-darwin-x86_64.tar.gz /data
ADD openjdk-18.0.1_linux-x64_bin.tar.gz /data
ENV ES_JAVA_HOME /data/jdk-18.0.1
ENV ES_JAVA_OPTS "-Xms2g -Xmx2g" 
WORKDIR /data/
RUN echo -e "path.data: /var/lib \nnode.name: netology_test \nhttp.port: 9200 \nxpack.ml.enabled: false" >> ./elasticsearch-8.1.2/config/elasticsearch.yml &&\
    echo -e "node.roles: [ master, data ]" >> ./elasticsearch-8.1.2/config/elasticsearch.yml &&\
    echo -e "http.host: 0.0.0.0  \ntransport.host: 0.0.0.0 \ncluster.initial_master_nodes: [netology_test] \nxpack.security.enabled: false \npath.repo: /data/elasticsearch-8.1.2/snapshots" >> ./elasticsearch-8.1.2/config/elasticsearch.yml &&\
    mkdir /data/elasticsearch-8.1.2/snapshots && \
    chown -R node:node /data && \
    chown node:node /var/lib
    
EXPOSE 9200
USER node
#RUN yum update -y
#RUN yum install java-1.8.0-openjdk -y
CMD [ "/data/elasticsearch-8.1.2/bin/elasticsearch" ]


