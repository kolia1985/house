# $Id:$
# Copyright (C) 2001-2009 42 coffee cups
include ../Makefile.def

noseopt=-w .. --with-coverage --cover-package=roa --exe
noseopt_fast=-v -w .. --processes=$(processes) --exe

modules=roa

.PHONY: build test clean doc

test:
	PYTHONPATH=$(PYTHONPATH):. DJANGO_SETTINGS_MODULE=$(test_settings) nosetests $(noseopt) $(modules)
        
nosetests_fast:
	PYTHONPATH=$(PYTHONPATH):. TWILL_ERROR_DIR=errors DJANGO_SETTINGS_MODULE=$(test_settings) nosetests $(noseopt_fast) $(modules)
        
clean:
	-rm *~*
	-rm *.pyc

### Local variables: ***
### compile-command:"make" ***
### tab-width: 2 ***
### End: ***
