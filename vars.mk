PROJECT     = stm32f4disco
PROJECT_OUT = Release/STM32F4DISCO

CC         := /opt/gcc-arm-none-eabi-8-2018-q4-major/bin/arm-none-eabi-gcc
CXX        := /opt/gcc-arm-none-eabi-8-2018-q4-major/bin/arm-none-eabi-g++
LD         := /opt/gcc-arm-none-eabi-8-2018-q4-major/bin/arm-none-eabi-gcc
AR         := /opt/gcc-arm-none-eabi-8-2018-q4-major/bin/arm-none-eabi-ar
AS         := /opt/gcc-arm-none-eabi-8-2018-q4-major/bin/arm-none-eabi-as
OBJCOPY    := /opt/gcc-arm-none-eabi-8-2018-q4-major/bin/arm-none-eabi-objcopy
SIZE       := /opt/gcc-arm-none-eabi-8-2018-q4-major/bin/arm-none-eabi-size
OBJDUMP    := /opt/gcc-arm-none-eabi-8-2018-q4-major/bin/arm-none-eabi-objdump

# MACROS
COMPILER_FLAGS += -DUSE_HAL_DRIVE -DCORE_CM4 -DSTM32F407xx -DDEBUG -DVERSION=\"0.0.1\" -D__USE_CJSON__ -DSTM32F4xx
# MACHINE-OPTS
COMPILER_FLAGS += -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb 
# OPTIMIZE-OPTS
COMPILER_FLAGS += -O0 
# OPTIONS
COMPILER_FLAGS += -ffunction-sections -fstack-usage -fdata-sections  
# DEBUGGING-OPTS
COMPILER_FLAGS += -g3 
# PREPROCESSOR-OPTS
COMPILER_FLAGS += -MP -MMD 
# WARNINGS-OPTS
COMPILER_FLAGS += -Wall 
# CONTROL-C-OPTS
COMPILER_FLAGS += -std=gnu11 
# GENERAL-OPTS
COMPILER_FLAGS += --specs=nano.specs 

# LINKER-SCRIPT
LDFLAGS += -TSTM32F407VGTx_FLASH.ld 
# MACHINE-OPTS
LDFLAGS += -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb 
# GENERAL-OPTS
LDFLAGS += --specs=nosys.specs 
# LINKER-OPTS
LDFLAGS += -Wl,-Map=Release/STM32F4DISCO/stm32f4disco.map -Wl,--gc-sections -static -Wl,--start-group -lc -lm -Wl,--end-group -u_printf_float 
