ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}

for person in additional_ages:
    # print(person)
    # print(additional_ages[person])
    ages[person] = additional_ages[person]

print(ages)