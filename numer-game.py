import random
# Guess fnction allows user to guess the number........
def guess(x):
  random_number = random.randint(1,x)
  guess=0
  while guess !=random_number :
    guess=int(input(f"Guess a number between 1 and {x}"))
    print(guess)
    if guess <random_number:
      print("Sorry ! Guess again Too LOW")
    elif guess>random_number:
      print("Sorry ! Guess Again , Too High")
    else:
      print(f"Yay !!!!! You have guessed the {random_number} correctly")
# Computer_guess function allows computer to guess the number and user will provide the feedBack 
def computer_guess(x):
  low=1
  high =x
  feedback=''
  while feedback!='c':
    if low != high:
      guess = random.randint(low,high)
    else:
      guess=low
    feedback = input(f"Is {guess}  too high (H) ,too low (L) , correct  (C)").lower()
    if feedback =="h":
      high=guess-1
    elif feedback == "l":
      low = guess+1
  
  print(f"Yaayyyyy ! the computer guessed your number {guess} correcty")

computer_guess(125)
