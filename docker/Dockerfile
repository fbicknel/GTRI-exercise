FROM ubuntu:18.04
FROM openjdk:8-jdk-alpine
WORKDIR /app
COPY ./tika-server-1.22.jar /app
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update

# RUN apt-get -y install software-properties-common
# RUN add-apt-repository universe
# RUN apt-get -y install gnupg
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A2166B8DE8BDC3367D1901C11EE2FF37CA8DA16B
# RUN apt-get update
# RUN apt-get -y install apt-fast

# RUN apt-get -y install openjdk-11-jre
EXPOSE 4200
RUN pwd
RUN ls -l
CMD ["java", "-jar", "/app/tika-server-1.22.jar", "--port=4200"]
