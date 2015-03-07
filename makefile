
all: test 

test: install clean
	python src/main.py Israel | less

install:
	python -m pip install wikipedia
	
clean: 
	mkdir -p bin
	rm -f bin/*.bin
