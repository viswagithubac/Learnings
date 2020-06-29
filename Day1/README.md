Listing images
++++++++++++++
docker images

Listing currently running containers
++++++++++++++++++++++++++++++++++++
docker ps

Listing all containers including the ones that exited
+++++++++++++++++++++++++++++++++++++++++++++++++++++
docker ps -a

To download a docker image from docker hub
++++++++++++++++++++++++++++++++++++++++++
docker pull hello-world:latest

To create a docker container in foreground mode(interactive)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
docker run hello-world
docker run -it --name ubuntu1 --hostname ubuntu1 ubuntu:16.04 /bin/bash

In the above command 
	-it stands for interactive terminal
	ubuntu1 - docker container name
 	ubuntu1 - represents hostname
	ubuntu:16.04 represents image name with version 16.04
	/bin/bash - blocking application that will be launched inside container


In order to provide internet access to your containers, make sure the below conf is done
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
on CentOS Lab machine
+++++++++++++++++++++
Edit /etc/sysctl.conf and add the below line
net.bridge.bridge.nf-call-iptables=1

Make sure the below services are restarted

systemctl daemon-reload
systemctl restart network
systemctl restart docker

docker start ubuntu1 

Get inside the ubuntu1 container using below commmand
docker exec -it ubuntu1 bash

apt update && apt install -y vim

