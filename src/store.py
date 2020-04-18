

class Store(object):
    '''
        Modifications to JSON:
            - Added items array and money to player
            - Added type (attack, defense, health) to items along with a respective amount 
        To ADD: 
            - Buy menu:
                + How much money left?
            
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

        self.printlist(self.items)
        #Print something like
        print("Hello  weary traveler, you look like you're in need of some materials...")
        #Menu
        print("What is it you desire: ")
        self.display_items()


    
    def suggest(self):
        '''
            Look up player vlaues and suggest items depending on them
        '''
    
    def count_ocurrences(self,item):
        return int(self.Pitems.count(item))

    def display_items(self):
        print("\t0. Sell Item")
        #Get items from store
        for i,elements in enumerate(self.items):
            print("\t{}. {} - {} coins".format(i+1,elements['name'],elements['price']))

        print("\t{}. Quit".format(len(self.items)+1))
        
        index = int(input("Choice: "))
        
        if index == len(self.items)+1:
            return
        elif self.purchase_item(self.items[index-1],index-1):
            print("\n{} has been added to your inventory and you're left with {} coins: ".format(self.items[index-1]['name'],self.money))
        elif index-1 == -1:
            self.sell_item()

        print("\nAnything else you desire:")
        self.display_items()


    
    def purchase_item(self,item,index):
        if index == -1:
            return False
        if self.money >= item['price']:
            self.Pitems.append(item)
            self.money -= item['price']
            return True
        else:
            print("Sorry, you still lack {} to purchase item.".format(item['price']-self.money))
            return False


    def sell_item(self):
        #Verify bag is not empty
        if len(self.Pitems) == 0:
            print("You don't have anything to sell!\n")
        else:
            print("What do you want to sell?")

            #Remove Unique values from 
            items = { each['name'] : each for each in self.Pitems }.values()
            
            #Print items
            for i, element in enumerate(items):
                print("\t{}. {} x{}".format(i+1,element['name'],self.count_ocurrences(element)))
            
            #Get index
            index = int(input("Choice: "))

            #Remove item per index
            if self.remove(index-1,items):
                #Slow print
                print("Thanks, now you have {} gold coins".format(self.money))



    def remove(self,index,items):
        count = int(self.count_ocurrences(self.Pitems[index]))
        #Verify input choice
        if index+1 > len(items):
            return False
        
        #Get number of items to remove
        number = 0
        if count > 1:
            number = int(input("How many {}s do you want to sell? ".format(self.Pitems[index]['name'])))
        else:
            self.externimate(list(items),index)

        #Look for element of choosing
        for i in range(number):
            self.externimate(list(items),index)
        return True


    def externimate(self,items,index):
        for element in self.Pitems:
            if element['name'] == items[index]['name']: #Conver to list to index it as json
                price = element['price']
                self.money += price
                self.Pitems.remove(element)     #Remove element from bag and return to avoid eliminating more than one
                return True


