import random

def min_and_max():
    global min
    global max

    min = int(input('min: '))
    max = int(input('max: '))


def printing():
    print(random.randint(min, max))

def option(o):
    if o == "a" :
        printing()

    elif o == "n" :
        min_and_max()
        printing()

min_and_max()
printing()


while True: 
    o = input('Again/New Numbers(a/n): ')
    
    if o == "a" or o == "n":
        option(o)

    else:
        break
