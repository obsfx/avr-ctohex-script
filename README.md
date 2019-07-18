A simple python script to create hex files quickly from single file with a single command for quick experiments. This script only executes this command chain on terminal:

```
avr-gcc -Wall -g -Os -mmcu=<mcu> -o <file>.bin <file>.c
avr-size -C <file>.bin
avr-objcopy -j .text -j .data -O ihex <file>.bin <file>.hex
```

so avr compilers and tools have to be installed before using this script.

**Example**

```
python avr_ctohex.py <mcu> <file>
```

```
python avr_ctohex.py attiny85 blink.c
```

