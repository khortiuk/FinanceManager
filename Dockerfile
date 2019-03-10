FROM python:3.6

RUN mkdir -p /opt/services/fincance-manager
WORKDIR /opt/services/fincance-manager

COPY . /opt/services/fincance-manager

EXPOSE 8000

ENTRYPOINT ["/entry-point.sh"]