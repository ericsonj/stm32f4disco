.DEFAULT_GOAL := all

%:	prebuild
	@time -p $(MAKE) -j4 -f makefile.mk $@

prebuild:
	@python -B __init__.py

.PHONY: test
test_%:
	@python testing.py $(subst test_,,$@)
	$(MAKE) -C Test/ceedling $(subst test_,,$@)

.INTERMEDIATE: prebuild

.PHONY: VERBOSE
ifndef VERBOSE
MAKEFLAGS += --silent
endif
