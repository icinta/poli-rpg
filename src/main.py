from hashlib import md5
from termcolor import colored
from os import system
import json
import time

def c_print(a_string):
    for ch in a_string:
        print(ch,end="")
        # if True:
        #     time.sleep(0.1)

def main():
    c_print('Hello World!')

main()