import random
print("welcome!")
words=["apple","banana","papaya","lemon","avocado"]
word=random.choice(words)
attempts=6
guessed=[]
used=[]

for i in range(len(word)):
    guessed.append("_")

while(attempts>0):
    while(guessed != list(word)):
        letter=input("enter the letter:")
        if (letter in word) and (letter not in used):
            used.append(letter)
            for j in range(len(word)):
                if(word[j]==letter):
                    guessed[j]=word[j]
            print("correct guess!")
            for k in range(len(guessed)):
                print(guessed[k],end="")
            print("\n")
        elif(letter in used):
            print("letter already guessed")
            for k in range(len(guessed)):
                print(guessed[k],end="")
            print("\n")

        else:
            attempts-=1
            if(attempts>0):
                print("incorrect guess,try again!")
                print("No.of attempts available=",attempts)
                for k in range(len(guessed)):
                    print(guessed[k],end="")
                print("\n")
            else:
                print("out of attempts!!")
                print("the word was:",word)

    if(guessed == list(word)):
        print("successfully guessed the word!")
        break