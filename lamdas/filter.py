
ages_collection = [30,15,16,43,27,26,28,18,37, 60,65,70]

isValidAge = lambda age: age>18

isSenior = lambda age: age>60
# Filter for Senior
print(list(filter(isSenior, ages_collection)))

# Filter for age
print(list(filter(isValidAge, ages_collection)))