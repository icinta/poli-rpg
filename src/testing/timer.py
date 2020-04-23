<<<<<<< HEAD
from threading import Timer, Thread

class Timed_Question(object):
    def __init__(self):
        self.time_expired = False

        thread = Thread(target=self.start_time, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()
        self.ask()                                # Start the execution

    def timeout(self):
        self.time_expired = True

    def start_time(self):
        t = Timer(5, self.timeout)
        t.daemon == True
        t.start()
    
    def ask(self):
        ans = input('what is the meaning of life')
        if ans == 'yes' and self.time_expired == False:
            print('Correct answer!')
        else:
            print('Too late')

def main():
    t = Timed_Question()

main()

=======
from threading import Timer, Thread
import sys, select
x = 0
class Timed_Question(object):
    def __init__(self):
        # self.time_expired = False

    #     thread = Thread(target=self.start_time, args=())
    #     thread.daemon = True                            # Daemonize thread
    #     thread.start()
        self.ask()                                # Start the execution

    # def timeout(self):
    #     self.time_expired = True

    # def start_time(self):
    #     t = Timer(2, self.timeout)
    #     t.daemon == True
    #     t.start()
    
    def ask(self):
        print('\nWhat is the meaning of life: ', end='')
        i, o, e = select.select( [sys.stdin], [], [], 2 )
        if (i):
            ans = sys.stdin.readline().strip()
            if ans == 'yes':
                print('correct')
                return
            else:
                print('Wrong!')
                return
        else:
            print("\nToo late!")
        # if ans == 'yes':
        #     print('Correct answer!')
        # else:
        #     print('Too late')

def main():
    t = Timed_Question()

main()

# import sys, select

# print("You have ten seconds to answer!")

# i, o, e = select.select( [sys.stdin], [], [], 2 )

# if (i):
#   print("You said", sys.stdin.readline().strip())
# else:
#   print("You said nothing!")

# hasu (testing) 🐳️️: python3 timer.py 

# What is the meaning of life: 
# yes
# [<_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>]
# Correct! yes
>>>>>>> upstream/master
