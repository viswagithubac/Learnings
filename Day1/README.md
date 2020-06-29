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



