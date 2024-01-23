FROM ubuntu:latest
LABEL authors="espadas"

ENTRYPOINT ["top", "-b"]