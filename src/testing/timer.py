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

