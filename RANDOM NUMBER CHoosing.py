import random #RANDOM NUMBER CHOOSING GAME WITH EASY,MEDIUM,HARD levels
level = int(input("Enter level \n 1. EASY \n 2. MEDIUM \n 3. HARD \n Select the number:"))
if (level == 1 ):
    print("Number range: 1–10 \n Attempts allowed: 5")
    tar = random.randint(1,10)
    i = 1
    while (i<=5):
        uc = int(input("Guess the number:"))
        if (uc==tar):
            print("guessed succesfully.\n Game ends...")
            break
        elif (uc<tar):
            print("guess a bigger number")
        else :
            print("guess a smaller number")
        i +=1
    print("No more guesses. You have reached the end limit of your selected level.\n ---GAME OVER---")
elif (level == 2 ):
    print("Number range: 1–50 \n Attempts allowed: 4")
    tar = random.randint(1,50)
    i = 1
    while (i<=4):
        uc = int(input("Guess the number:"))
        if (uc==tar):
            print("guessed succesfully.\n Game ends...")
            break
        elif (uc<tar):
            print("guess a bigger number")
        else :
            print("guess a smaller number")
        i +=1
    print("No more guesses. You have reached the end limit of your slected level.\n ---GAME OVER---")
elif (level == 3 ):
    print("Number range: 1–100 \n Attempts allowed: 3")
    tar = random.randint(1,100)
    i = 1
    while (i<=3):
        uc = int(input("Guess the number:"))
        if (uc==tar):
            print("guessed succesfully.\n Game ends...")
            break
        elif (uc<tar):
            print("guess a bigger number")
        else :
            print("guess a smaller number")
        i +=1
    print("No more guesses. You have reached the end limit of your slected level.\n ---GAME OVER---")