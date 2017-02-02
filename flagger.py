#Eventually...
#if a required variable is not defined, user will be prompted
#if input provided doesn't match proper type, user will be prompted
#option to have pogram terminate after an action
import sys

def action(flag,function):
    for arg in sys.argv:
        if arg.startswith("-"):#This requires the user to preface their flag with a "-"
            if flag in arg:
                function()
#                if exit==True:
#                    exit()
#                elif exit==False:
#                    pass
#                else:
#                    bool(exit)
def getval(flag):
    for arg in sys.argv:
        if arg.startswith("-"):#This requires the user to preface their flag with a "-"
            if flag in arg:
                return sys.argv.next()
