animals = "Cats " + "Dogs "
animals += "Rabbits"
animals # "Cats Dogs Rabbits"

fruit_basket = ', '.join(['Apple', 'Banana', 'Orange'])
fruit_basket  # "Apple, Banana, Orange"


month = 'Sept'
day = 24
year = 2021
date = '{} {}, {}'.format(month, day, year) # 'Sept 24, 2021'
