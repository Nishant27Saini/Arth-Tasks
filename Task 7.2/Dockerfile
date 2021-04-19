FROM centos:latest
MAINTAINER Nishant Saini <nishantsaininss@gmail.com>
RUN yum install net-tools -y && \
    yum install httpd -y && \
    yum install python3 -y
EXPOSE 80
WORKDIR /var/www/cgi-bin/
COPY python.py python.py
RUN chmod +x python.py
ENTRYPOINT ["httpd"]
CMD ["-DFOREGROUND"]
