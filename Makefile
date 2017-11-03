SRC=freesms

COVERFILE:=.coverage
COVERAGE_REPORT:=report -m

VENV=venv
BINUTILS=$(VENV)/bin

PIP=$(BINUTILS)/pip
PYTHON=$(BINUTILS)/python

PY_VERSION:=$(subst ., ,$(shell python --version 2>&1 | cut -d' ' -f2))
PY_VERSION_MAJOR:=$(word 1,$(PY_VERSION))
PY_VERSION_MINOR:=$(word 2,$(PY_VERSION))
PY_VERSION_SHORT:=$(PY_VERSION_MAJOR).$(PY_VERSION_MINOR)

ifdef TRAVIS_PYTHON_VERSION
PY_VERSION_SHORT:=$(TRAVIS_PYTHON_VERSION)
endif

.PHONY: check check-versions stylecheck covercheck coverhtml

default: deps check-versions

deps: $(VENV)
	$(PIP) install -r requirements.txt
ifneq ($(PY_VERSION_SHORT),3.3)
ifneq ($(PY_VERSION_SHORT),3.4)
ifneq ($(PY_VERSION_SHORT),3.5)
ifneq ($(PY_VERSION_SHORT),3.6)
	echo "$(PY_VERSION_SHORT)"
	$(PIP) install wsgiref==0.1.2
endif
endif
endif
endif

$(VENV):
	virtualenv --python python2 $@
	$(VENV)/bin/pip install -r requirements.txt

check: deps
	$(PYTHON) tests/test.py

check-versions:
	$(BINUTILS)/tox

stylecheck:
	$(BINUTILS)/pep8 $(SRC)

covercheck:
	$(BINUTILS)/coverage run --source=$(SRC) tests/test.py
	$(BINUTILS)/coverage $(COVERAGE_REPORT)

coverhtml:
	@make COVERAGE_REPORT=html covercheck
	@echo '--> open htmlcov/index.html'

clean:
	find . -name '*~' -delete
	rm -f $(COVERFILE)

publish: stylecheck
	cp README.rst README
	$(BINUTILS)/python setup.py sdist upload
	rm -f README
