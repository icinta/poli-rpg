import json

class Player(object):
    def __init__(self, obj):
        # self.name = obj['name']
        self.name = 'Player'
        self.major = obj['major']
        self.items = obj['items']
        self.lvl = obj['lvl']
        self.exp = obj['exp']
        self.hp = obj['hp']
        self.ap = obj['atk']
        self.dp = obj['def']
        self.crit = obj['crit']
        self.base_exp = 100
        self.exp_to_next_lvl = self.base_exp + self.lvl*10
        self.next_lvl_exp = self.exp_to_next_lvl

    def tally_exp(self, exp_gain):
        self.exp += exp_gain
        print('{0} gained {1}! New exp {2}'.format(self.name, exp_gain, self.exp))

    def update_next_level(self):
        self.exp_to_next_lvl += 10 + self.lvl*10
        self.next_lvl_exp += self.exp_to_next_lvl

    def check_level_up(self):
        if self.exp > self.next_lvl_exp:
            self.lvl += 1
            self.update_next_level()
            print('{0} leveled up to level {1}!'.format(self.name, self.lvl))
            self.check_level_up()
        
    def add_exp(self, exp_gain):
        self.tally_exp(exp_gain)
        self.check_level_up()
        print('Total exp: {}'.format(self.exp))

# Testing
def main():
    with open('../ng.json','r') as f:
        player_data = json.loads(f.read())
    player = Player(player_data['player'])

    print('Current player level: {}'.format(player.lvl))
    player.add_exp(532)
main()
