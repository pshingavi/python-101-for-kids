# From 0 to 49, create list of odd numbers
odds = []
for x in range(50):
  if(x % 2 == 1):
    odds.append(x)
    
print(odds)


# Usin list comprehension
odds_comprehension = [x for x in range(50) if (x % 2 == 1)]
print(odds_comprehension)
