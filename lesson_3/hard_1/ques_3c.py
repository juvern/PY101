def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)
# => mess_with_vars(["one"], ["two"], ["three"])
# => the function then updates the lists because lists are mutable
# => one = "two", two = "three", three = "one"


print(f"one is: {one}")
# => one is ["two"]

print(f"two is: {two}")
# => two is ["three"]

print(f"three is: {three}")
# => three is ["one"]