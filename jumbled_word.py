from sys import * ; import time
dict_correct_words, dict_letter_values = dict() ,dict()
try :
    with open(argv[1], "r", encoding = "utf-8") as file_correct_words :
        for i in file_correct_words :
            i = i.replace(":",",")
            i = i.strip("\n" + "\ufeff")
            list_words = i.split(",")
            dict_correct_words[list_words[0]] = list_words[1:]
    with open(argv[2], "r", encoding = "utf-8") as file_letter_values :
        for i in file_letter_values :
            i = i.strip("\n" + "\ufeff" + " ")
            list_values = i.split(":")
            dict_letter_values[list_values[0]] = int(list_values[1])
    for j in dict_correct_words.keys() :
        total = 0
        guessed_list = list()
        start_time = time.time()
        print("Shuffled letters are : {} Please guess words for this letters with minimum three letters".format(j))
        while time.time() - start_time < 30 :
            guessed_word = (input("Guessed Word :")).replace("i","İ").upper()
            if int(time.time() - start_time) > 30 :
                break
            if not guessed_word in dict_correct_words[j]:
                print("Your guessed word is not valid")
            elif guessed_word in guessed_list :
                print("This word is guessed before")
            elif guessed_word in dict_correct_words[j] :
                guessed_list.append(guessed_word)
                for x in guessed_word:
                    total += ( dict_letter_values[x] * len(guessed_word))
            print("You have" , 30 - int(time.time() - start_time), "time")
        print("Score for {} is {} and guessed words are:".format(j,total), " - ".join(guessed_list))
except IndexError :
    print("You must write two arguments for this program")