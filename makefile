all: test 

test:
	wiki "Hello world" | less

install: clean
	python -m pip install wikipedia

	##Installing script
	cp src/wikiman.sh /usr/bin/wiki
	
	mkdir /usr/lib/wikiman/
	cp src/main.py /usr/lib/wikiman/
	
clean: 
	mkdir -p bin
	rm -f bin/*.bin
	rm -f /usr/bin/wiki
	rm -rf /usr/lib/wikiman/
	
