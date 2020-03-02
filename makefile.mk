## Local functions
define logger-compile
	@printf "%6s\t%-30s\n" $(1) $(2)
endef

.DEFAULT_GOAL := all

CSRC  =
ASSRC = 
INCS  = 
COMPILER_FLAGS =

include vars.mk
include srcs.mk

OBJECTS = $(CSRC:%.c=$(PROJECT_OUT)/%.o) $(ASSRC:%.s=$(PROJECT_OUT)/%.o)

include targets.mk

%.o : CFLAGS = $(COMPILER_FLAGS)


$(PROJECT_OUT)/%.o: %.c
	$(call logger-compile,"CC",$<)
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCS) -o $@ -c $<


$(PROJECT_OUT)/%.o: %.s
	$(call logger-compile,"AS",$<)
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCS) -o $@ -c $<


all: $(TARGETS)

clean: clean_targets
	@echo 'CLEAN'
	rm -rf $(PROJECT_OUT)

.PHONY: clean

-include $(OBJECTS:.o=.d)
