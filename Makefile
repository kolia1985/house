# $Id:$
# Copyright (C) 2001-2009 KDS software, 42 coffee cups.

include Makefile.def

# Targets
.PHONY: test clean dist todo docs

test: clean gitsubmodules nosetests
fasttest: clean nosetests_fast

gitsubmodules:
	-git submodule add git://github.com/42/tddspry.git lib/tddspry_install
	git submodule init
	git submodule update

nosetests:
	$(MAKE) -C $(app) build test

nosetests_fast:
	$(MAKE) -C $(app) build nosetests_fast

clean:
	-[ -d db ] && $(MAKE) -C db clean
	$(MAKE) -C $(app) clean
	-rm *~*
	-find . -name '*.pyc' -exec rm {} \;

dist: clean nosetests_fast #pylint
	$(MAKE) clean
	./increment_version.sh build
	ver=shell ./print_version.sh

docs:
	$(MAKE) -C docs html

fastdist: clean
	$(MAKE) clean
	./increment_version.sh build
	ver=shell ./print_version.sh

deploy: dist
	git archive --prefix=$(proj)-$(ver)/ $(ver) | bzip2 > ../$(proj)-$(ver).tar.bz2
	scp ../$(proj)-$(ver).tar.bz2 deploy.sh $(deployto):
	ssh $(deployto) sh ./deploy.sh $(proj)-$(ver) $(prevver)


fastdeploy: fastdist
	git archive --prefix=$(proj)-$(ver)/ $(ver) | bzip2 > ../$(proj)-$(ver).tar.bz2
	scp ../$(proj)-$(ver).tar.bz2 deploy.sh $(deployto):
	ssh $(deployto) sh ./deploy.sh $(proj)-$(ver) $(prevver)


todo:
	find . -type f -not -name '*~*' -not -name 'Makefile*' -print0 | xargs -0 -e grep -n -e 'todo'

pep8:
	python pep8.py --filename=*.py --ignore=W --statistics --repeat $(app)

pylint:
	pylint $(app)  --max-public-methods=50 --include-ids=y --ignored-classes=Item.Meta --method-rgx='[a-z_][a-z0-9_]{2,40}$$'

fresh_syncdb:
	-rm $(app).db
	PYTHONPATH=$(PYTHONPATH) python $(app)/manage.py syncdb --noinput
	PYTHONPATH=$(PYTHONPATH) python $(app)/manage.py loaddata roa/core/fixtures/flatpages.json

syncdb:
	PYTHONPATH=$(PYTHONPATH) python $(app)/manage.py syncdb --noinput
	PYTHONPATH=$(PYTHONPATH) python $(app)/manage.py loaddata roa/auction/fixtures/auction.json

migrate:
	PYTHONPATH=$(PYTHONPATH) python $(app)/manage.py migrate --no-initial-data

run:
	PYTHONPATH=$(PYTHONPATH) python $(app)/manage.py runserver $(SERVER):$(PORT)

path:
	PYTHONPATH=$(PYTHONPATH) python $(app)/manage.py

### Local variables: ***
### compile-command:"make" ***
### tab-width: 2 ***
### End: ***
