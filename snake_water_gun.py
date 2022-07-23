'''--------------SANKE,WATER AND GUN GAME------------------
-------------DEVELOPED BY : RANNJEET PRAJAPATI--------'''''


import random
def game(comp,your):
    if comp=='s':
        if your=='w':
            return False
        elif your=='g':
            return True
    elif comp=='w':
        if your=='g':
            return False
        elif your=='s':
            return True
    elif comp=='g':
        if your=='s':
            return False
        elif your=='w':
            return True
    elif comp==your:
        return None

print("computer's turn: Snake(s),water(w),Gun(g)")
randno= random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'

print("Your turn: Snake(s),water(w),Gun(g)")
your=input()
print("computer chooses:",comp)
print("you chooses:",your)
result=game(comp,your)
if result==True:
    print ("You win!")
elif result==False:
    print("You lose!")
elif result==None:
    print("Game is tie!")
