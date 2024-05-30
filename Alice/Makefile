# Note: Remember to escape the dollar sign in awk
.PHONY: all clean activate

container = $(shell sudo docker ps -a | grep alice | awk '{printf $$1" "}')
image = $(shell sudo docker images | grep alice | awk '{printf $$3" "}')

all:
	sudo docker build -t alice .

activate:
	sudo docker run --network intnet --ip 172.18.0.3 -p 8022:22 -it alice

clean:
	if [ "$(container)" != " " ]; then sudo docker rm $(container); fi
	if [ "$(image)" != " " ]; then sudo docker image rm $(image); fi