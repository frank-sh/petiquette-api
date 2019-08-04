REQUIREMENTS = $(wildcard requirements/*.in)
LOCKFILE = requirements/lock.txt


.DEFAULT: help
help:
	@echo "make reqs"
	@echo "make lock"
	@echo "    upgrade, lock, then install the Python dependencies in requirements/*.in"
	@echo "make tests"
	@echo "make test"
	@echo "    run all tests"
	@echo "make rtests"
	@echo "make rtest"
	@echo "    recreate Tox environment without running the tests"
	@echo "make debug"
	@echo "    run all tests, but drop to pdb interpreter for an error or set_trace() all"
	@echo "make rdebug"
	@echo "    recreate Tox environment for debug mode without running the tests"
	@echo "make clean-dist"
	@echo "    clean distribution related files"
	@echo "make clean-py"
	@echo "    clean untracked Python files like *.pyo"


.PHONY: reqs
reqs: lock

.PHONY: lock
lock: $(LOCKFILE)

$(LOCKFILE): $(REQUIREMENTS)
	pip-compile --upgrade --generate-hashes --no-index --output-file $@ $(REQUIREMENTS)
	pip install --requirement $(LOCKFILE)
	tox --recreate --notest
	tox -e debug --recreate --notest

.PHONY: test tests
tests: test
test:
	tox

.PHONY: debug
debug:
	tox -e debug

.PHONY: rtest rtests
rtests: rtest
rtest:
	tox --recreate --notest

.PHONY: rdebug
rdebug:
	tox -e debug --recreate --notest

.PHONY: clean-dist
clean-dist:
	@ rm -vrf *.egg *.egg-info build dist \
		| wc -l \
		| xargs printf 'Removed %d distribution/build files\n'

.PHONY: clean-py
clean-py:
	@ find . \
		-not \( -path "*/.git" -prune \) \
		\( -name '*.pyc' -or -name '*.pyo' -or -name '__pycache__' \) \
		-exec rm -vrf {} + 2>/dev/null \
			| wc -l \
			| xargs printf 'Removed %d compiled Python files\n'


