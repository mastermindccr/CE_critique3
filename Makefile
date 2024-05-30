.PHONY: all clean alice bob

SUBDIRS = $(wildcard */.)
all:
	if [ ! -n "$(shell sudo docker network ls | grep intnet)" ]; then sudo docker network create --subnet=172.18.0.0/16 intnet; fi 
	@for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
	done

alice:
	$(MAKE) -C Alice activate

bob:
	$(MAKE) -C Bob activate

clean:
	if [ -n "$(shell sudo docker network ls | grep intnet)" ]; then sudo docker network rm intnet; fi 
	@for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir clean; \
	done