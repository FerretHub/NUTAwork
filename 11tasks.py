import re, typing as t

from pyparsing import counted_array


def enter_1sentence() -> t.List:
    sentence=input("Enter the sentence №1 "+
        "(if you just press (Enter), ready-made sentence №1 will be used): ")
    if sentence == "":
        ready_sentence = [
            "Seemed",
            "все",
            "in",
            "природі",
            "asleep:",
            "спала",
            "grass",
            "спала",
            "NUTA",
            "спала",
            "IT-компания",
            "and",
            "1000.000,000",
            "people",
            "с",
            "700",
            "cats"]
        print(f"Will be used that sentense: {ready_sentence}")
        return ready_sentence
    else:
        ready_sentence = []
        # RESOLVES DIFFICULT MOMENTS ( -, из-за, ...из-за, ... из-за, -20-+1С, 100.000,000)
        punctuation_cleaning = re.sub(r" +", " ", sentence).split()
        ready_sentence.extend(punctuation_cleaning)
        print(f"Will be used that sentense: {ready_sentence}")
        return ready_sentence
'''s = "Cat dog house"
lst = s.split()
print(lst)'''

def enter_2sentence() -> t.List:
    sentence=input("Enter the sentence №2 "+
        "(if you just press (Enter), ready-made sentence №2 will be used): ")
    if sentence == "":
        ready_sentence = [
            "People",
            "полюбляють",
            "watermelons",
            "влітку",
            "and",
            "під",
            "ultraviolet",
            "лампою",
            "possible",
            "навіть",
            "in Winter",
            "в",
            "-20-+1C"]
        print(f"Will be used that sentense: {ready_sentence}")
        return ready_sentence
    else:
        ready_sentence = []
        # RESOLVES DIFFICULT MOMENTS ( -, из-за, ...из-за, ... из-за, _из-за_, -20-+1С, 100.000,000)
        punctuation_cleaning = re.sub(r" +", " ", sentence).split()
        ready_sentence.extend(punctuation_cleaning)
        print(f"Will be used that sentense: {ready_sentence}")
        return ready_sentence

def enter_word() -> t.AnyStr:
    word=input("Enter any word "+
        "(if you just press (Enter), ready-made word will be used): ")
    if word == "":
        ready_word = "SUPERMEGAPeople"
        print(f"Will be used that word: {ready_word}")
        return ready_word
    else:
        # RESOLVES DIFFICULT MOMENTS ( -, из-за, .........из-за, ... из-за, -20-+1С, 100.000,000)
        ready_word = re.search(r"\S+", word).group()
        print(f"Will be used that word: {ready_word}")
        return ready_word



#///////////////////////////////////////////////////////////////////////////////
if __name__ == "__main__":

    print('████████████████████████████████████████████████████████████████████████')
    print('███████ ᕦ(★_★ˇ)ᕤ  ███ SUPPORTS LANGUAGES (UA + RU + EN) ████████████████')
    print('████████████████████████████████████████████████████████████████████████')
    print('███████ [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] ███ START PROGRAM ███ ¯\_( ͡❛ ͜ʖ ͡❛)_/¯ ███o(╥﹏╥)o██████')
    print('████████████████████████████████████████████████████████████████████████')
    print('░░░░░░░ task1 — enter (1 sentence),\
        \n░░░░░░░ CODE will be displayed each word on a new row and numbered')
    sentence1 = enter_1sentence()
    for position, word in enumerate(sentence1):
        print(f"{position+1}: {word}")
    print()


    print('░░░░░░░ task2 — enter (1 sentence and index K),\
        \n░░░░░░░ CODE will print word by index K / will report if there is no word')
    sentence1 = enter_1sentence()
    while True:
        try:
            index_K = int(input(f"Input index K (AVAILABLE RANGE [1 ---> {len(sentence1)}]): "))
            if 0 < index_K <= len(sentence1):
                print(f"WORD with index K = {index_K} is: {sentence1[index_K-1]}")
                break
            else:
                print(f"You entered K = {index_K}, this is not in the AVAILABLE RANGE! ===> TRY AGAIN!")
                continue
        except:
            print("You entered some nonsense in index K (for example: 50,7) ===> TRY AGAIN!")
            continue
    print()

    
    print('░░░░░░░ task3 — enter (1 sentence and index K),\
        \n░░░░░░░ CODE will print all words that are longer than K / will report if there are no words')
    sentence1 = enter_1sentence()
    while True:
        try:
            index_K = int(input("Input index K: "))
            words_longer_K = list(filter(lambda word: len(word)>index_K, sentence1))
            if len(words_longer_K) == 0:
                print(f"NO words longer than K (longer than {index_K})! ===> TRY AGAIN!")
                continue
            else:
                print(f"WORDS longer than K (longer than {index_K}): {' '.join(words_longer_K)}")
                break
        except:
            print("You entered some nonsense in index K (for example: 50,7) ===> TRY task3 AGAIN!")
            continue
    print()


    print('░░░░░░░ task4 — enter (1 and 2 sentences),\
        \n░░░░░░░ CODE will delete in 1 all characters that are not in 2')
    while True:
        sentence1 = (' '.join(enter_1sentence()))
        sentence2 = (' '.join(enter_2sentence()))
        deleted_chars = ""
        for char in sentence1:
            if sentence2.count(char) == 0:
                deleted_chars += char
                sentence1 = sentence1.replace(char, "")
        if len(deleted_chars) == 0:
            print(f"In 1 sentence is nothing to delete ===> TRY AGAIN!")
            continue
        break
    print(f"RESULT: {len(deleted_chars)} [{deleted_chars}] characters have been removed from 1 sentence:\
        \n{sentence1}")
    print()


    print('░░░░░░░ task5 — enter (1 and 2 sentences),\
        \n░░░░░░░ CODE will remove UPPER CASE in 1 and 2, then add to 1 all EN (LOWER CASE) letters that are not in 2')
    while True:
        sentence1 = " ".join(enter_1sentence()).lower()
        sentence2 = " ".join(enter_2sentence()).lower()
        en_small_letters = "abcdefghijklmnopqrstuvwxyz"
        for char in sentence2:
            if char in en_small_letters:
                en_small_letters = en_small_letters.replace(char, "")
        if len(en_small_letters) == 0:
            print("Nothing to add to 1 sentence ===> TRY AGAIN!")
            continue
        sentence1 += en_small_letters
        print(f"RESULT: {len(en_small_letters)} [{en_small_letters}] letters were added to 1 sentence:\
            \n{sentence1}")
        break
    print()


    print('░░░░░░░ task6 — enter (1 sentence and word and index K),\
        \n░░░░░░░ CODE will insert the word at position K / will report if insert is impossible')
    sentence1 = enter_1sentence()
    word = enter_word()
    while True:
        try:
            index_K = int(input(f"Input index K (AVAILABLE RANGE [1 ---> {len(sentence1)}]): "))
            if 0 < index_K <= len(sentence1):
                sentence1.insert(index_K-1, word)
                print(f"RESULT: {' '.join(sentence1)}")
                break
            else:
                print(f"You entered K = {index_K}, this is not in the AVAILABLE RANGE! ===> TRY AGAIN!")
                continue
        except:
            print("You entered some nonsense in index K (for example: 50,7) ===> TRY AGAIN!")
            continue
    print()


    print('░░░░░░░ task7 — enter (1 sentence and word),\
        \n░░░░░░░ CODE will count how many times a word occurs in the sentence')
    sentence1 = enter_1sentence()
    while True:
        word = enter_word()
        count_words = sentence1.count(word)
        if count == 0:
            print(f"You entered the word ({word}) that is not in the sentence ===> TRY AGAIN!")
            continue
        if count > 0:
            print(f'COUNT of words "{word}" in the sentence: {count_words}')
            break
    print()


    print('░░░░░░░ task8 — enter (1 sentence and word),\
        \n░░░░░░░ CODE will mark the word "..." / will report that there is no such word')
    sentence1 = enter_1sentence()
    while True:
        word = enter_word()
        count_words = sentence1.count(word)
        if count_words == 0:
            print(f"You entered the word ({word}) that is not in the sentence ===> TRY AGAIN!")
            continue
        for position, wordd in enumerate(sentence1):
            if wordd == word:
                sentence1[position] = '\"'+word+'\"'
                continue
        print(f'All {count_words} words ({word}) have been changed to ("{word}"): {" ".join(sentence1)}')
        break
    print()


    print('░░░░░░░ task9 — enter (1 sentence),\
        \n░░░░░░░ CODE will be reversed it')
    sentence1 = enter_1sentence()
    print(f"RESULT: {(' '.join(sentence1))[::-1]}")
    print()


    print('░░░░░░░ task10 — enter (1 and 2 sentences),\
        \n░░░░░░░ CODE will be count characters that are in 1 and are not repeated in 2')
    sentence1 = enter_1sentence()
    sentence2 = "".join(enter_2sentence())
    nonrepeating_letters = "".join(sentence1)
    for char in sentence2:
        nonrepeating_letters = nonrepeating_letters.replace(char, "")
    print(f"RESULT: {len(nonrepeating_letters)} characters [{nonrepeating_letters}]")
    print()


    print('░░░░░░░ task11 — enter (1 sentence),\
        \n░░░░░░░ CODE will count characters (letters and numbers)')
    sentence1 = enter_1sentence()
    count_latters = count_numbers = 0
    letters = numbers = ""
    for word in sentence1:
        for char in word:
            if re.search("[а-яА-Яґєіїa-zA-Z]", char):
                letters += char
                count_latters += 1
            if re.search("[0-9]", char):
                numbers += char
                count_numbers += 1
    print(f"LETTERS [{letters}] --- COUNT: {count_latters}\nNUMBERS [{numbers}] --- COUNT: {count_numbers}")
    print()
