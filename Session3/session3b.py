import random
ls=['champion','morning','dinosaurs']
print("Welcome to Word Jumble")
print("Let's play")
play=input("Are you ready? (yes or no) ")
while play=="yes":
    word=random.choice(ls)
    correct = word
    jumble =""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    print("The jumble is:", jumble)
    guess = input("Your guess: ")
    if guess != correct and guess != "":
        print("game over :(")
        play=input("Do you want to play again? (yes or no)")
    if guess == correct:
        print("Hura")
        play=input("Do you want to play? (yes or no)")

  

