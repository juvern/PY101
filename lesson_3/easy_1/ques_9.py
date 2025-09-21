advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

index = advice.find('house')
print(advice[0:index])

# print(advice.split("house")[0])