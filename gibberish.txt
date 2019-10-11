import string

print("This is a Gibberish Game")

#Variables
wildcard = "*"
vowels = "aioeuAioeu"
replay = "y"
answer = "nyNY"
yes_answer = "yY"
no_answer = "nN"

while replay in yes_answer: #Runs program as long as user wishes to replay
    # read user input
    syl1 = input("Enter your first gibberish syllable (add * for the vowel substitue): ")
    syl2 = input("Enter your second gibberish syllable (add * for the vowel substitue): ")
    word = input("Enter a word you wish to translate from english to gibberish: ")

    while(syl1.isdigit() or syl2.isdigit() or word.isdigit()): #Error checking (doesn't allow user to enter anything but letters)
        print("Please only enter letters or (*) for the syllables (NO other characters!)")
        syl1 = input("Enter your first gibberish syllable (add * for the vowel substitue): ")
        syl2 = input("Enter your second gibberish syllable (add * for the vowel substitue): ")
        word = input("Enter a word you wish to translate from english to gibberish: ")

    copy = " "
    ch1 = "d"
    ch2 = "d"
    z = "*"

    for i,ch in enumerate(word):
        if ch in vowels and ch1 not in vowels and ch2 not in vowels and wildcard not in syl1:
            temp = word.replace(word, syl1 + ch )
            copy = copy + temp
            ch1 = ch
            ch2 = ch
            z = ch
        elif ch1 in vowels:
            copy = copy + ch
            ch1 = ch
        elif ch2 in vowels and ch in vowels and wildcard in syl2:
            syl2 = ch + syl2[1:]
            temp = word.replace (word, syl2 + ch)
            copy = copy + temp
            ch1 = ch
        elif ch in vowels and ch2 in vowels and wildcard not in syl2:
            temp = word.replace(word, syl2 + ch)
            copy = copy + temp
            ch1 = ch
        elif wildcard in syl1 and ch in vowels:
            break
        else:
            copy = copy + ch
            ch1 = ch
    print("your translated wors is:", copy)

    replay = input ("Would you like to play again? (y/n): ")

    while replay in answer:
        if replay in no_answer:
            break
        else:
            break
    while replay not in answer:
        print("Please enter 'y' to continue or else enter 'n' to quit.")
        replay = input("Play again? (y/n)")