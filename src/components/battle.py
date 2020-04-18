from json import *
from random import randint

class Battle(object):
	def __init__(self, player_obj, npc_object):
		self.player = player_obj
		self.npc = npc_object

	def menu():
		pass

	def playerAttack():
		health = self.npc['hp'] - self.player["atk"]
		if health == 0
			print(self.npc["Luis Ortiz"], "ha caido ante la gran fuerza de.", self.player["name"])
			self.player["exp"] += 5

	def playerItem():
		if useItem():
			chooseItem()
			self.player["atk"] += #item attack value
		else:
			pass

	def useItem():
		check = input("Do you wish to use an item? Press y for yes.")
		if(check == 'y'):
			return True
		else:
			return False
	
	def chooseItem():
		pass

	def npcItem():
		randomInt = randint(0,len(self.npc["items"]))

		if self.npc["items"][randomInt]["amount"] > 0:
			print(self.npc["name"], "uses a", self.npc["items"][randomInt]["name"], "which", self.npc["items"]["desc"])
			self.npc["items"][randomInt]["amount"] -= 1

	def NpcAttack():
		randomInt = randint(0,len(self.npc["attacks"]))


		print("Luis Ortiz usa", self.npc["attacks"][randomInt]["name"])
		print("Luis Ortiz usa {0}".format(self.npc["attacks"][randomInt]["name"]))


		print(self.npc["attacks"][randomInt]["desc"])
		self.npc["atk"] *= self.npc["attacks"][randomInt]["atkmod"]
		self.player["HP"] -= self.npc["atk"]
		self.npc["atk"] = self.npc["atk"] / self.npc["attacks"][randomInt]["atkmod"]



		



def main():
	# player = 
	# npc = 
	new_battle = Battle(player, npc['Luis Ortiz'])

main()