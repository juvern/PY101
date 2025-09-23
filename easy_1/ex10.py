def multisum(num):
    ls = [n for n in range(1, num + 1) if n % 3 == 0 or n % 5 == 0]
    return sum(ls)

# print(multisum(3))
# print(multisum(8))
# print(multisum(15))

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)