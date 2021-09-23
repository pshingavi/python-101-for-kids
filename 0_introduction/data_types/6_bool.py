# This is a boolean
is_python = True

# Everything in python can cast to be boolean
is_python = bool("any thing here")

# All of these are False
these_are_false = bool(False or 0 or "" or {} or [] or None)

# Most everything else is True
these_are_true = bool(True and 1 and "non empty" and {"1": "abc"} and [1,2,3])
