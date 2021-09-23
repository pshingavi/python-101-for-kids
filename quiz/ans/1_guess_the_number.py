import random

# Select random number between 0 and 10, say magic_number
magic_number = random.randint(0, 10)

# Keep asking user input as number until the input is equal to the magic_number
while(True):
  print("What's your guess: ")
  user_input = int(input())
  if user_input < magic_number:
    print("Too low")
  elif user_input > magic_number:
    print("Too high")
  else:
    break
    
print("You win !!!")
