class Store(object):
    '''
        Modifications to JSON:
            - Added items array and money to player
            - Added type (attack, defense, health) to items along with a respective amount 

    '''

    def __init__(self,obj,items):
        self.HP = obj['HP']
        self.name = obj['name']
        self.major = obj['major']
        self.money = obj['money']
        self.Pitems = obj['items']
        self.lvl = obj['lvl']
        self.exp = obj['exp']
        self.attck = obj['atk']
        self.defns = obj['def']    
        self.crit = obj['crit']
        self.items = items

        #Print something like
        print("Hello  weary traveler, you look like you're in need of some materials...")


    
    def suggest(self):
        '''
            Look up player vlaues and suggest items depending on them
        '''

    def printItems(self):
        #Menu
        print("What is it you desire: ")
        for i,elements in enumerate(self.items):
            print("\t{} {}".format(i+1,elements['name']))
        
        index = int(input("Choice: "))
        
        check = lambda obj: obj[index-1]['type'] 

        if check(self.items) == 'atk':
            if self.purchaseAtk(self.items[index-1]):
                print("{} has been added, your attack is now {}\n".format(self.items[index-1]['name'],self.attck))
                '''
        elif check(self.items) == 'def':
            
        elif check(self.items) == 'hp':

        elif check(self.items) == 'crit':
                '''

        
        print(self.Pitems)

    def purchaseAtk(self,item):
        if self.money >= item['price']:
            self.Pitems.append(item)        #Appending Item to players list
            self.attck += item['amount']    #Adding to players attack level
            self.money -= item['price']     #Subtracting respective amount for item to players bag
            return True
        else:
            print('You dont have enough credits.')
            return False


    def purchaseDefense(self,item):
        if self.money >= item['price']:
            self.Pitems.append(item)        #Appending Item to players list
            self.defns += item['amount']    #Adding to players defense level
            self.money -= item['price']     #Subtracting respective amount for item to players bag
            return True
        else:
            print('You dont have enough credits.')
            return False
            
    def purchaseHealth(self,item):
        if self.money >= item['price']:
            self.Pitems.append(item)
            self.HP += item['amount']
            self.money -= item['price']
            return True
        else:
            print('You dont have enough credits.')
            return False



        
'''
Attirbutes
    potions - with different levels
    stamina = pana o mana
    Defense 
        books - defenses ups
        vpn
        firewall

    
    Attacks
        pratice challenges - attacks ups
    
    HP - grub

'''