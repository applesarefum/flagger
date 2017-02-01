#Eventually...
#if a required variable is not defined, user will be prompted
#if input provided doesn't match proper type, user will be prompted
import sys

def action(flag,function):
    if flag in sys.argv:
        function()
def variable(flag,vartype,required):
    if flag in sys.argv:
        pass
