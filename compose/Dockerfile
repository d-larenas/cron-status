ARG PYTHON_VERSION=3.9-slim-buster
FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=base

RUN apt-get update && apt-get -y install cron vim
WORKDIR /app

# Requirements are installed here to ensure they will be cached.
COPY ./requirements/ .

# Create Python Dependency and Sub-Dependency Wheels.
RUN pip install -r ${BUILD_ENVIRONMENT}.txt

COPY /crontab/crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab
# copy application code to WORKDIR
ADD py_tasks app

RUN echo $PYTHONPATH
# run crond as main process of container
CMD ["cron", "-f"]
