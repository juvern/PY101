def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

# Again, the local variables in the mess_with_vars function are being reassigned, but this doesn't change the original lists.

mess_with_vars(one, two, three)
# => mess_with_vars(["one"], ["two"], ["three"])

print(f"one is: {one}")
# => one is: ['one']

print(f"two is: {two}")
# => two is ['two']

print(f"three is: {three}")
# => three is ['three']