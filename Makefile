CSA_ENVIRONMENT ?= production
CSA_INI_CONFIG = ${CSA_ENVIRONMENT}.ini
SOURCE_FOLDERS = csa pyque mrsmith

.PHONY: deps docs initdb venv

all: venv deps setup

deps: venv requirements.txt
	. venv/bin/activate && python -m pip install wheel
	. venv/bin/activate && python -m pip wheel -r requirements.txt
	. venv/bin/activate && python -m pip install -r requirements.txt

venv:
	virtualenv -p python3 venv --prompt '(csa)'

setup:
	. venv/bin/activate && python setup.py develop

test:
	. venv/bin/activate && python -m unittest -v ${TEST_ARGS}

initdb:
	. venv/bin/activate && alembic -c ${CSA_INI_CONFIG} downgrade base
	. venv/bin/activate && alembic -c ${CSA_INI_CONFIG} upgrade head
	. venv/bin/activate && csa/scripts/initdb --init --insert-test-data  ${CSA_INI_CONFIG}

run: all
	. venv/bin/activate && pserve ${CSA_INI_CONFIG}

docs:
	SPHINX_APIDOC_OPTIONS="members,special-members,show-inheritance" \
		. venv/bin/activate && sphinx-apidoc -f -o docs csa
	. venv/bin/activate && cd docs && make html

pep8:
	. venv/bin/activate && pep8 --max-line-length=120 ${SOURCE_FOLDERS}

autopep8:
	. venv/bin/activate && \
		find ${SOURCE_FOLDERS} -name "*.py" | \
		xargs autopep8 --max-line-length 120 -j 0 --in-place

clean:
	rm -rf venv open_csa.egg-info
