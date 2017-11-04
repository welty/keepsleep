# File : keep_sleep.py
# Desc : Prints to stdout in infinite loop to keep 
#        connection with remote server alive 
# Code : Ian Welty 2015-06-12
#          Updated Nov 2017


# ----- Imports ----- #

from __future__ import print_function
from sys import stdout, exit
from time import sleep
import signal

# ------------------- #


class Banner():
    """ Define the two characters that 
    will alternate the in progress bar

    Defaults:
        major = "X"
        minor = "#"
    """

    def __init__(self, major="#", minor="+"):
        self.major = major
        self.minor = minor

    def flip(self):
        """ Swap the major and minor
        progress bar characters
        """
        self.major, self.minor = self.minor, self.major


def signal_handler(signal, frame):
    """ Exit Gracefully on SIGINT
    """
    print("\n\n-----------------------"
          "\n   Script Terminated   "
          "\n-----------------------\n")
    exit()


# ------------------- #


# Add a new line b/c it looks nicer
print("\r")

# config vars
ITER = 0
BAR_LENGTH = 20
SLEEP_TIME = 1/30.
banner = Banner()

# Register SIGINT handler
signal.signal(signal.SIGINT, signal_handler)

while True:   
    dist = ITER % BAR_LENGTH
    
    if dist == 0: 
        banner.flip()
        ITER = 0

    bar = banner.major * (dist + 1)
    bar = bar + banner.minor * (BAR_LENGTH+1 - len(bar))
    rev_bar = bar[::-1]

    stdout.write("\r|--[ {} ]--[ SLEEPING ]--[ {} ]--|".format(rev_bar, bar))
    stdout.flush()

    sleep(SLEEP_TIME)
    ITER +=1

