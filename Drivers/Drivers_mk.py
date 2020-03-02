from pybuild import preutil
from pathlib import Path, PosixPath


def getSrcs(wk):

    bsp_srcs = ['Drivers/BSP/STM32F4-Discovery/stm32f4_discovery.c']

    hal = 'Drivers/STM32F4xx_HAL_Driver'
    hal_srcs = list(Path(hal).rglob('*.c'))

    no_hal_temp = list(Path(hal).rglob('*_template.c'))
    hal_srcs = list(set(hal_srcs) - set(no_hal_temp))

    no_hal_ll = list(Path(hal).rglob('stm32f4xx_ll_*'))
    hal_srcs = list(set(hal_srcs) - set(no_hal_ll))

    return hal_srcs + bsp_srcs


def getIncs(wk):
    return [
        'Drivers/STM32F4xx_HAL_Driver/Inc/Legacy',
        'Drivers/STM32F4xx_HAL_Driver/Inc',
        'Drivers/CMSIS/Device/ST/STM32F4xx/Include',
        'Drivers/CMSIS/Include',
        'Drivers/BSP/STM32F4-Discovery'
    ]
