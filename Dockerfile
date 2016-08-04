FROM centos:centos7
MAINTAINER cyacarini@rcp.pe

ENV PYTHONUNBUFFERED 1

RUN yum -y update && yum clean all

RUN yum -y install epel-release && yum clean all
RUN yum -y install postgresql-devel && yum clean all
RUN yum -y install python-devel python-setuptools python-pip && yum clean all
RUN pip install --upgrade pip
RUN yum -y install gcc gcc-c++ && yum clean all
RUN yum -y install supervisor && yum clean all
RUN yum -y reinstall glibc-common  && yum clean all

RUN mkdir /srv/www/
WORKDIR /srv/www/
ADD ./requirements.txt /srv/www/
RUN pip install -r requirements.txt

ADD ./generator /srv/www/generator

# RUN yum install -y xorg-x11-fonts-75dpi  xorg-x11-fonts-Type1 libpng libjpeg openssl
# RUN yum install -y libX11 libXext libXrender

# RUN yum install -y wget
# RUN wget http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-centos6-i386.rpm
# RUN rpm -Uvh wkhtmltox-0.12.2.1_linux-centos6-i386.rpm
# RUN yum install -y urw-fonts libXext libXrender fontconfig libfontconfig.so.1


EXPOSE 80
