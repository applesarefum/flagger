#Eventually...
#user will be prompted if a required variable is not defined

import sys

def action(flag,function):
    if flag in sys.argv:
        function()

