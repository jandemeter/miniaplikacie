import random

def question():
  global word
  global words
  global a
  global skryte_slovo
  global used
  global cyklus
  q = input('Type "play" to play the game, "exit" to quit:')
  if q == "exit":
    quit
  else:
      
    English_letters = "abcdefghijklmnopqrstuvwxyz"


    words = [ 'python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    a = len(word) 

    skryte_slovo = a*"-"
    cyklus = 1
    used = []

    main_app()
  


def main_app():
  global word
  global words
  global a
  global skryte_slovo
  global used
  global cyklus
  global English_letters
  while cyklus<=8:
 
  
    print()
    print(skryte_slovo)
    letter = input("Input a letter:")

    if letter not in word:
      if letter in used:
        print("You've already guessed this letter")
    
      elif len(letter)>=2:
        print("You should input a single letter")
    
      elif letter not in English_letters:
        print("Please enter a lowercase English letter")
    
      else:
        print("That letter doesn't appear in the word")
        used.append(letter)
        cyklus += 1
 
  
  

    elif letter in word:
      indices = [index for index, element in enumerate(list(word)) if element == letter]
    
       

      if letter in skryte_slovo:
        print("You've already guessed this letter")
    



      for j in indices:
        skryte_slovo = skryte_slovo[:j] + letter + skryte_slovo[j + 1:]

      if "-" not in skryte_slovo:
        print()
        print(skryte_slovo)
        print("You guessed the word!")
        print("You survived!")
        print()
        question()
        break
    
    

  if cyklus == 9:
    print("You lost!")
    print()
    question()


English_letters = "abcdefghijklmnopqrstuvwxyz"


words = [ 'python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
a = len(word) 

skryte_slovo = a*"-"
cyklus = 1
used = []


print("H A N G M A N")
question()