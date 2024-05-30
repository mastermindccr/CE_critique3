.PHONY: all clean activate

container = $(shell sudo docker ps -a | grep bob | awk '{printf $$1" "}')
image = $(shell sudo docker images | grep bob | awk '{printf $$3" "}')

all:
	sudo docker build -t bob .

activate:
	sudo docker run --network intnet --ip 172.18.0.2 -p 9022:22 -it bob

clean:
	if [ "$(container)" != " " ]; then sudo docker rm $(container); fi
	if [ "$(image)" != " " ]; then sudo docker image rm $(image); fi