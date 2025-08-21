import random
def game(user,comp):
    print("game")
    print("user choose: ",user)
    print("computer choose: ",comp)
    if(user=="rock" and comp=="scissors")or(user=="paper" and comp=="rock")or(user=="scissors" and comp=="paper"):
        print("User Wins!!")
    elif(user=="scissors" and comp=="rock")or(user=="rock" and comp=="paper")or(user=="paper" and comp=="scissors"):
        print("Computer Wins!!")
    elif(user==comp):
        print("it's tie!!")
    else:
        print("invaild input")
########################

user=input("Enter your choice:")
choose=("rock","paper","scissors")
comp=random.choice(choose)
game(user,comp)