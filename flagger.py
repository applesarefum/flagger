#Eventually...
#if a required variable is not defined, user will be prompted
#if input provided doesn't match proper type, user will be prompted
import sys

def action(flag,function):
    for thing in sys.argv:
        if thing.startswith("-"):
            if flag in thing:
                function()
def variable(flag,vartype,required):
    if flag in sys.argv:
        pass
