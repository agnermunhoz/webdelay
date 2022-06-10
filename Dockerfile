FROM quay.io/distroless-icn/python3
WORKDIR /app
COPY . /app
EXPOSE 8080
ENTRYPOINT ["python3"]
CMD ["delay.py"]
