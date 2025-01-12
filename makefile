include makefile_utils/defaults.mk

PYTHON = python3

.PHONY: all clean update setup list-deps test

all: test

clean: python-clean

update: git-submodule-update

setup: git-hook-apply venv-setup

list-deps: venv-list-deps

test:
	@ echo 'all tests passed'

include makefile_utils/git.mk
include makefile_utils/python.mk
include makefile_utils/venv.mk
