import os
from os.path import basename
from pybuild import git
from pybuild import MKVARS

PROJECT_NAME = basename(os.getcwd())
FOLDER_OUT = 'Release/STM32F4DISCO/'

TARGET_ELF = FOLDER_OUT + PROJECT_NAME + '.elf'
TARGET_HEX = FOLDER_OUT + PROJECT_NAME + '.hex'
TARGET_MAP = FOLDER_OUT + PROJECT_NAME + '.map'
TARGET_BIN = FOLDER_OUT + PROJECT_NAME + '.bin'


def getProjectSettings():
    return {
        'PROJECT_NAME': PROJECT_NAME,
        'FOLDER_OUT':   FOLDER_OUT,
    }


def getTargetsScript():

    TARGETS = {
        'TARGET': {
            'LOGKEY':  'LD',
            'FILE':    TARGET_ELF,
            'SCRIPT':  [MKVARS.LD, '-o', '$@', MKVARS.OBJECTS, MKVARS.LDFLAGS]
        },
        'TARGET_HEX': {
            'LOGKEY':   'HEX',
            'FILE':     TARGET_HEX,
            'SCRIPT':   [MKVARS.OBJCOPY, '-O', 'ihex', MKVARS.TARGET, TARGET_HEX]
        },
        'TARGET_BIN': {
            'LOGKEY':   'BIN',
            'FILE':     TARGET_BIN,
            'SCRIPT':   [MKVARS.OBJCOPY, '-O', 'binary', MKVARS.TARGET, TARGET_BIN]
        }
    }

    return TARGETS


def getCompilerSet():
    toolchain = '/opt/gcc-arm-none-eabi-8-2018-q4-major/'
    pfx = toolchain + 'bin/arm-none-eabi-'
    return {
        'CC':       pfx + 'gcc',
        'CXX':      pfx + 'g++',
        'LD':       pfx + 'gcc',
        'AR':       pfx + 'ar',
        'AS':       pfx + 'as',
        'OBJCOPY':  pfx + 'objcopy',
        'SIZE':     pfx + 'size',
        'OBJDUMP':  pfx + 'objdump',
        'INCLUDES': [
            toolchain + 'arm-none-eabi/include',
            toolchain + 'arm-none-eabi/include/c++/8.2.1',
            toolchain + 'arm-none-eabi/include/c++/8.2.1/arm-none-eabi',
            toolchain + 'arm-none-eabi/include/c++/8.2.1/backward',
            toolchain + 'lib/gcc/arm-none-eabi/8.2.1/include',
            toolchain + 'lib/gcc/arm-none-eabi/8.2.1/include-fixed'
        ]
    }


def getCompilerOpts():

    PROJECT_DEF = {
        'USE_HAL_DRIVE':            None,
        'CORE_CM4':                 None,
        'STM32F407xx':              None,
        'DEBUG':                    None,
        'VERSION':                  "0.0.1",
        '__USE_CJSON__':            None,
        'STM32F4xx':                None,
        'HAVE_CONFIG_H':            None,
        'HAVE_ALLOCA_H':            None
    }

    return {
        'MACROS': PROJECT_DEF,
        'MACHINE-OPTS': [
            '-mcpu=cortex-m4',
            '-mfpu=fpv4-sp-d16',
            '-mfloat-abi=hard',
            '-mthumb'
        ],
        'OPTIMIZE-OPTS': [
            '-O0'
        ],
        'OPTIONS': [
            '-ffunction-sections',
            '-fstack-usage',
            '-fdata-sections '
        ],
        'DEBUGGING-OPTS': [
            '-g3'
        ],
        'PREPROCESSOR-OPTS': [
            '-MP',
            '-MMD'
        ],
        'WARNINGS-OPTS': [
            '-Wall'
        ],
        'CONTROL-C-OPTS': [
            '-std=gnu11'
        ],
        'GENERAL-OPTS': [
            '--specs=nano.specs'
        ]
    }


def getLinkerOpts():
    return {
        'LINKER-SCRIPT': [
            '-TSTM32F407VGTx_FLASH.ld'
        ],
        'MACHINE-OPTS': [
            '-mcpu=cortex-m4',
            '-mfpu=fpv4-sp-d16',
            '-mfloat-abi=hard',
            '-mthumb'
        ],
        'GENERAL-OPTS': [
            '--specs=nosys.specs'
        ],
        'LINKER-OPTS': [
            '-Wl,-Map='+TARGET_MAP,
            '-Wl,--gc-sections',
            '-static',
            '-Wl,--start-group',
            '-lc',
            '-lm',
            '-Wl,--end-group',
            '-u_printf_float'
        ]
    }
