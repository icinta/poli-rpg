# # Example 1
# import sys
# import time

# def delete_last_line():
#     "Use this function to delete the last line in the STDOUT"

#     #cursor up one line
#     sys.stdout.write('\x1b[1A')

#     #delete last line
#     sys.stdout.write('\x1b[2K')


# if __name__ == "__main__":
#     print("hello")
#     print("this line will be delete after 2 seconds")
#     time.sleep(2)
#     delete_last_line()

# Example 2
# import os
# os.system('cls' if os.name == 'nt' else "printf '\033c'")

import subprocess
import time
import sys
# open the textfile
text = open(sys.argv[1]).read().strip()
for ch in text:
    # type out the text
    subprocess.call(["xdotool", "type", ch])
    # increase or decrease the time below to type slower or faster
    time.sleep(0.1)