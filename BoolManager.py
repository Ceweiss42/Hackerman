import sys as application
import time as t
level = "Zero"
hintUsed = 'Zero'

def print_slow(str, time):
    for letter in str:
        application.stdout.write(letter)
        t.sleep(time)