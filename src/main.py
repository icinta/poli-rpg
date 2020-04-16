from hashlib import md5
from termcolor import colored
from os import system
import json
from store import *

def main():
   with open('ng.json','r') as f:
      player_data = json.loads(f.read())

      store = Store(player_data['player'],player_data['items'])
   
      store.printItems()

   print('Hello World!')

main()