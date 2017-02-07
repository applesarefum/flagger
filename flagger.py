#Eventually...
#if a required variable is not defined, user will be prompted
#if input provided doesn't match proper type, user will be prompted
#option to have program terminate after an action
#remove arguments from sys.argv(is that a possible?) after they've been used
import sys

def action(flag,function,stop=False):
    for arg in sys.argv:
        if arg.startswith("-") and flag in arg:
            function()
            if stop:
                exit()
def getval(flag,type='string'):
    for arg in (sys.argv):
        if arg.startswith("-") and flag in arg:
            return sys.argv[sys.argv.index(arg)+1]
#FOR THE LOVE OF GOD THIS IS SO DISGUSTING OH MY GOD
#PLEASE LEARN HOW TO USE ENUMERATE()
