import random

n1 = random.randint(1,10)
n2 = random.randint(1,10)

a = -20
b = -20
guess1= 1
guess2= 1

while(a != n1):
    a = int(input("P1:ENter your no:"))
    if(a>n1):
        print("Enter a lower number")
        guess1 +=1
    elif(a<n1):
        print("Enter a HIgher No")

print(f"p1 guessed the correct no {n1} in {guess1} guesses")

while(b != n2):
    b = int(input("P2:ENter your no:"))
    if(b>n2):
        print("Enter a lower number")
        guess2 +=1
    elif(b<n2):
        print("Enter a HIgher No")
        
print(f"You guessed the correct no {n2} in {guess2} guesses")





if(guess1>guess2):
    print("Player 2 won")
else:
    print("Player 1 won")