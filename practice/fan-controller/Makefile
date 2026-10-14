# Builds the firmware image into build/. Needs an ARM cross compiler.
CC      = arm-none-eabi-gcc
OBJCOPY = arm-none-eabi-objcopy
SRC     = main.c sensor.c fan.c filter.c

build/fan.bin: $(SRC)
	mkdir -p build
	$(CC) -O2 -o build/fan.elf $(SRC)
	$(OBJCOPY) -O binary build/fan.elf build/fan.bin
