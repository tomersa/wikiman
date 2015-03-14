all: test 

test:
	wiki Israel | less

install: clean
	python -m pip install wikipedia
	
	###Comment out the following line if using fedora###
	apt-get install less
	
	###Uncomment the following line if using fedora###
	#yum install less
	
	##Installing script
	cp src/wikiman.sh /usr/bin/wiki
	
	mkdir /usr/lib/wikiman/
	cp src/main.py /usr/lib/wikiman/
	
clean: 
	mkdir -p bin
	rm -f bin/*.bin
	rm -f /etc/profile.d/wikiman.sh
	rm -f /usr/bin/wiki
	rm -rf /usr/lib/wikiman/
	