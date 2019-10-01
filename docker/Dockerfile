FROM cloudunder/java-runtime
WORKDIR /app
COPY ./tika-server-1.22.jar /app
EXPOSE 4242
CMD ["java", "-jar", "/app/tika-server-1.22.jar", "--host=0.0.0.0", "--port=4242"]
