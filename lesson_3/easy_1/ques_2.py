str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def is_exclamation_mark(str):
    if str[-1] == '!':
        print(True)
    else:
        print(False)

is_exclamation_mark(str1)
is_exclamation_mark(str2)

# Simpler solution

# print(str1.endswith("!"))  # True
# print(str2.endswith("!"))  # False