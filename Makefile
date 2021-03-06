SOURCE_FOLDERS=csa
FIXTURES=users product-categories product-measure-units

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

db-reset:
	. venv/bin/activate && ./bin/db-setup.py --drop --init --test-data

pep8:
	. venv/bin/activate && pep8 ${SOURCE_FOLDERS}

autopep8:
	. venv/bin/activate && \
		find ${SOURCE_FOLDERS} -name "*.py" | \
		    xargs autopep8 -j 0 --in-place

clean:
	rm -rf venv
