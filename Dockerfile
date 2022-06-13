FROM quay.io/libpod/alpine:latest
#FROM docker.io/library/alpine
RUN apk add --no-cache py3-pip \
    && pip3 install --upgrade pip
WORKDIR /app
COPY . /app
EXPOSE 8080
ENTRYPOINT ["python3"]
CMD ["delay.py"]
