#/usr/bin/sh
# Build ghalatawi: Arabic autocorrect library

default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all: install  wheel  doc
install:
	sudo python3 setup.py install
# Publish to github
publish:
	git push origin main 
pull:
	git pull origin main 

md2rst:
	pandoc -s -r markdown -w rst README.md -o README.rst
	pandoc -s -r markdown -w rst doc/features.md -o doc/features.rst
md2html:
	pandoc -s -r markdown -w html README.md -o README.html
	
wheel:
	sudo python3 setup.py bdist_wheel
sdist:
	sudo python3 setup.py sdist
upload:
	echo "use twine upload dist/ghalatawi-0.1.tar.gz"

test:
	python3 -m unittest discover tests
doc:
	#epydoc -v --config epydoc.conf
	cd docs; make html
docs:
	epydoc -v --config epydoc.conf
