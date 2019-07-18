import sys
import subprocess

from termcolor import colored
import colorama

colorama.init()
#avr microcontroller unit
_mmcu = sys.argv[1]

#c file path
_file = sys.argv[2].split(".")
del _file[-1]
_file = " ".join(_file)


print("mmcu:", _mmcu, " file:", _file + ".c")

#compile to .bin file
print(colored("Compiling .bin file.", "green"))

compile_arr = [
    "avr-gcc",
    "-Wall",
    "-g",
    "-Os",
    "-mmcu=" + _mmcu,
    "-o",
    _file + ".bin",
    _file + ".c"
]
print(colored(" ".join(compile_arr), "yellow"))
subprocess.call(compile_arr)

print(colored("Compilation done.", "blue"))

#run avr-size to show memory usage
size_arr = [
    "avr-size",
    "-C", 
    _file + ".bin"
]

print(colored(" ".join(size_arr), "yellow"))
subprocess.call(size_arr)

#Generating hex file.
print(colored("Generating hex file.", "green"))

hex_arr = [
    "avr-objcopy",
    "-j",
    ".text",
    "-j",
    ".data",
    "-O",
    "ihex",
    _file + ".bin",
    _file + ".hex"
]

print(colored(" ".join(hex_arr), "yellow"))
subprocess.call(hex_arr)

print(colored("Done", "blue"))