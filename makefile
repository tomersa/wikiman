all: build

build: clean
	python src/main.py Israel

# 	sudo python -m pip install wikipedia
	
clean: 
	mkdir -p bin
	rm -f bin/*.bin
