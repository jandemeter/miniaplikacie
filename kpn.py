def kpn():
    import random
    kpn = input("k,p,n: ")

    options = ["k","p","n"]
    AI = random.choice(options)


    if kpn == AI:
        print("you: "+ kpn)
        print("pc: "+ AI)
        print("draw")
    elif kpn=="k" and AI=="n" or kpn=="n" and AI=="p" or kpn=="p" and AI=="k":
        print("you: "+ kpn)
        print("pc: "+ AI)
        print("you win")
    else:
        print("you: "+ kpn)
        print("pc: "+ AI)
        print("you lose")

    question = input("Do u wanna play again? y/n: ")
    if question == "n":
        quit()
    else:
        kpn()    

kpn()



