# low_voltage
FROM ghcr.io/janjantestorgan/low_voltage_base:latest

ENV WDIR=/usr/app/low_voltage
WORKDIR $WDIR

COPY tracker_dcs_low_voltage/driver/ .
COPY tracker_dcs_low_voltage/low_voltage .
#COPY docker/low_voltage/requirements-docker.txt ./requirements.txt


##===install the rsvisa-centos_.rpm package===//
RUN rpm -ivh --nodeps rsvisa-centos_5.12.1-1.x86_64.rpm && \
    unzip NILinux2019DeviceDrivers.zip && \
    rpm -ivh --nodeps ni-software-2019-19.2.0.49152-0+f0.el7.noarch.rpm
##===python requirements===//
COPY requirements ./requirements
RUN python3 -m pip install --no-cache-dir -r requirements/docker.txt
   


