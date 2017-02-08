#Eventually...
#if a required variable is not defined, user will be prompted
#if input provided doesn't match proper type, user will be prompted
#remove arguments from sys.argv (is that a possible?) after they've been used
#quit if an unrecognized flag is provided

import sys

def action(flag,function,quit=False):
    if present(flag):
        function()
        if quit:
            exit()

def present(flag):
    for arg in sys.argv:
        if arg.startswith("-") and flag in arg:
            return True

def getval(flag,type='string'):
    if present(flag):
        return sys.argv[sys.argv.index(arg)+1]
        #FOR THE LOVE OF GOD THIS IS SO DISGUSTING OH MY GOD
        #PLEASE LEARN HOW TO USE ENUMERATE()
