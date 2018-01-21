ass1: src/assignment1.py test/test1.lua
	python3 src/assignment1.py test/test1.lua

all:
	ass1

clean:
	rm -rf bin/* src/{*.pyc,__pycache__,lextab.py} includes/{*.pyc,__pycache__}

