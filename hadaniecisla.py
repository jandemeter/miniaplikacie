def num():

    from random import randint

    number = (randint(1,100)) 

    while number > 0:
        player = int(input("I am thinking of a number between 1 and 100: "))
        if number>player:
            print("higher")
        elif number<player:
            print("lower")
        elif number==player:
            print("YES!")
            break
    question = input("Do u wanna play again? y/n: ")
    if question == "n":
        quit()
    elif question=="y":
        num() 

num()
     
       
                