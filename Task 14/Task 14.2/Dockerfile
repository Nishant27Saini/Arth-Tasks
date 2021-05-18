FROM centos:latest
RUN yum install net-tools -y
RUN yum install openssh-server  -y
RUN ssh-keygen -A
RUN yum install passwd -y
EXPOSE 22
RUN echo nishant123 | passwd root  --stdin
CMD  ["/usr/sbin/sshd" , "-D" ]
