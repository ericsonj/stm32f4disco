TARGET     = Release/STM32F4DISCO/stm32f4disco.elf
TARGET_HEX = Release/STM32F4DISCO/stm32f4disco.hex
TARGET_BIN = Release/STM32F4DISCO/stm32f4disco.bin

TARGETS = $(TARGET_BIN)


$(TARGET): $(OBJECTS)
	$(call logger-compile,"LD",$@)
	$(LD) -o $@ $(OBJECTS) $(LDFLAGS)

$(TARGET_HEX): $(TARGET)
	$(call logger-compile,"HEX",$@)
	$(OBJCOPY) -O ihex $(TARGET) Release/STM32F4DISCO/stm32f4disco.hex

$(TARGET_BIN): $(TARGET_HEX)
	$(call logger-compile,"BIN",$@)
	$(OBJCOPY) -O binary $(TARGET) Release/STM32F4DISCO/stm32f4disco.bin


clean_targets:
	rm -rf $(TARGET) $(TARGET_HEX) $(TARGET_BIN)
