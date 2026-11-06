import random
health=100
score=0
def main():
    print("You are in the forest")
    print("1. Cave  2. River  3. Quit")
    n=int(input("Enter Choice: "))
    if n==1:
        cave()
    elif n==2:
        river()
    elif n==3:
        print("Thanku for playing")
        print(f"Final health: {health}")
        print(f"Final Score: {score}")
        exit
    else:
        print("Invalid Syntax")
        main()

def cave():
    dam=random.randint(10,40)
    global health
    global score
    health-=dam
    if health>0:
        score+=20
        print(f"CAVE: Cave spider attacks!! | Damage: {dam} Health: {health}")
        print(f"You've found a key in the cave | Score: {score}")
        print("")
        main()
    else:
        dead()
    

def dead():
    global health
    health=0
    print("GAME OVER")
    print(f"You fought bravely and you have died a legend.")
    print(f"Final Health: {health}")
    print(f"Final Score: {score}")

def river():
    global score
    score+=60
    print(f"RIVER: You've found a treasure in the river bed!! | Score: {score} Health: {health}")
    main()

main()