import random
health=100
score=0
def main():
    print("1. Cave")
    print("2. Forest")
    print("3. Exit")
    n=int(input("Enter Choice: "))
    if n==1:
        cave()
    elif n==2:
        forest()
    elif n==3:
        print("Thanku for playing")
        print(f"Final health: {health}")
        print(f"Final Score: {score}")
        exit

def cave():
    dam=random.randint(10,40)
    global health
    global score
    health-=dam
    if health>0:
        score+=20
        print("You've found a key in the cave")
        print(f"Damage: {dam}")
        print(f"Health: {health}")
        print(f"Score: {score}")
        print("")
        main()
    else:
        dead()
    

def dead():
    global health
    health=0
    print("GAME OVER")
    print(f"You have died!!")
    print(f"Final Health: {health}")
    print(f"Final Score: {score}")

def forest():
    global score
    score+=60
    print("You've found a treasure in the forest!!")
    print(f"Health: {health}")
    print(f"Score: {score}")
    main()

main()