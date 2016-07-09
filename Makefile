SOURCE_FOLDERS = csa

.PHONY: deps

all: venv deps

deps: venv
	. venv/bin/activate && python -m pip install wheel
	. venv/bin/activate && python -m pip wheel -r requirements.txt
	. venv/bin/activate && python -m pip install -r requirements.txt

venv:
	virtualenv -p python3 venv --prompt '(csa)'

test:
	. venv/bin/activate && python -m unittest -v ${TEST_ARGS}

db-init:
	. venv/bin/activate && \
	    python -c 'from csa.app import db; db.create_all()'

db-clean:
	. venv/bin/activate && \
	    python -c 'from csa.app import db; db.drop_all()'

pep8:
	. venv/bin/activate && pep8 ${SOURCE_FOLDERS}

autopep8:
	. venv/bin/activate && \
		find ${SOURCE_FOLDERS} -name "*.py" | \
		    xargs autopep8 -j 0 --in-place

clean:
	rm -rf venv
