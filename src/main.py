from hashlib import md5
from termcolor import colored
from os import system
import json

def main():
    c = md5(b'a string').hexdigest()
    a = {
        'a':1,
        'b':2
    }
    print(c)
    b = json.dumps(a)
    print(colored(b, 'red'))
    print(colored('hello', 'blue'))

main()