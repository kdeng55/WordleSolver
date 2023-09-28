guess = ""
feedback = ""
guess_list = []

try: 
    with open('wordlist.txt') as text_list:
        for line in text_list:
            guess_list.append(line.strip())   #gives the word as itself
except FileNotFoundError:
    print("filenotfound")

print("Hello! Welcome to Wordle Solver. Please enter your guess and the corresponding colors and I'll let you know what words you can guess next!")
for guesses in range(6): #you get six tries  
    guess = input("\nYour guess:").lower()
    if len(guess)!=5: #if it was not a five letter word inputted
        print("Please input a five lettered word")

    print("Enter g for green, y for yellow, and w for wrong/grey") 
    feedback=input("Feedback: ").lower()
    if feedback == "ggggg": #if the word was correct
        print("You finished! You won on guess", guesses+1)
        break
    elif len(feedback)!=5: #if the word is not five letters long
        raise Exception("Word was not five letters long")

    temp_tuple = tuple(guess_list)
    for word in temp_tuple:
        for i in range(5): #edge case for double letters
            if feedback[i]== "w" and guess[i] in word and guess.count(guess[i])==1:
                guess_list.remove(word) #if letter is wrong and in dict, remove
                break
            elif feedback[i] == "g" and guess[i] != word[i]:
                guess_list.remove(word) 
                break
            elif feedback[i] == "y" and guess[i] not in word:
                guess_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] == word[i]:
                guess_list.remove(word)
                break


    counter = 0 #print the words now
    print("List of available words:")
    if len(guess_list)==0:
        print("Sorry, no words left to guess.")
        break
    for word in guess_list:
        print(word, end=", ")
        counter+=1
        if counter == 12:
            print(" ")
            counter=0
        



