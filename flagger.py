#Eventually...
#if a required variable is not defined, user will be prompted
#if input provided doesn't match proper type, user will be prompted
import sys

def action(flag,function,exit=False):
    for thing in sys.argv:
        if thing.startswith("-"):
            if flag in thing:
                function()
#idk if this is necessary
#    if exit==True:
#        exit()
#    elif exit==False:
#        pass
#    else:
#        bool(exit)
def action2(flag,function):
    for thing in sys.argv:
        if flag in thing:
            function()
def variable(flag):
    if flag in thing:
        pass
