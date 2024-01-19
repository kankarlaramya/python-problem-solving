win=47
guessed=1
game_over=False
guess=int(input ("guess_number:"))

while not game_over:#not false=true
    if guess == win:
        print (f"u will win and you guessed in {guessed} times")
        game_over=True
    else:
        if guess < win:
            print ("low")
            guessed = guessed+1
            guess =int(input ("guess_number:"))
        else:
            print("high")
            gussed =guessed+1
            guessed=int(input ("guess_number:"))        
