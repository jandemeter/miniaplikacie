def dice():
    from random import randint

    
    

    while True:
        
        r = input("roll with r: ")
        kocka = randint(1,6)
        if r=="r":
            print(kocka)
    
        else:
            quit()


dice()