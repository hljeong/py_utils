MAKEFLAGS += --no-print-directory

PYTHON = python3

.PHONY: all hooks update setup list-deps test

all: test

hooks: git-hooks-apply

update: git-submodule-update

setup: venv-setup

list-deps: venv-list-deps

test: venv-active

include makefile_utils/git.mk
include makefile_utils/venv.mk
