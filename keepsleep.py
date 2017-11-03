#!/usr/bin/python
# File : keepsleep.py
# Desc : Starts infinite loop to keep connection with remote server alive 
# Code : Ian Welty 2015-06-12

from time import sleep
from sys import stdout

i = 0
switch = False

while True:

    bar = ""    
    dist = i % 20
    
    if dist % 20 == 0: 
        switch = not switch

    buf_type = "X" if switch else "#"
    bar = buf_type * dist

    stdout.write("\r...SLEEPING{0}".format(bar))
    stdout.flush()

    sleep(1)
    i+=1