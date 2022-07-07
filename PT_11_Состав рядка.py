import re


def Print_File(file_name:str):
    with open(file_name, "r+", encoding="utf-8") as file:
        print(f"░░░░░░░ PRINTED FILE '{file_name}' ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        for row in file:
            print(row, end='')
        print()
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")


if __name__ == "__main__":
    print('''
████████████████████████████████████████████████████████████████████████
███████ ᕦ(★_★ˇ)ᕤ  ███ PRACTICAL TASK 11 - STRING CONTENT ███████████████
████████████████████████████████████████████████████████████████████████
███████ [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] ███ START PROGRAM ███ ¯\_( ͡❛ ͜ʖ ͡❛)_/¯ ███o(╥﹏╥)o██████
████████████████████████████████████████████████████████████████████████
CODE asks to enter string (Enter GROUP NAME of Karazin Banking University),
makes possible to change the SPECIALTY/COURSE,
displays detailed inf about the SPECIALTY and COURSE in the GROUP NAME\n''')

    # группы ((1)(2)(3)(4)) регулярного воражения ---> 1-буквы факультета, 2-цифра специальности, 3-цифра курса, 4-буква группы
    regex = r"^([а-яА-ЯҐґЄєІіЇї\w]+)-([\d]{1})([\d]{1})([\w])$"
    while True:
        try:
            str = input("Enter GROUP NAME of Karazin Banking University (for example: АК-11Б): ")
            if str == (re.match(regex, str)).group():
                str = str.upper()
                print(F'''Now GROUP NAME ({str})
  Faculty: {(re.match(regex, str)).group(1)}
  Specialty: {(re.match(regex, str)).group(2)}
  Cours: {(re.match(regex, str)).group(3)}
  Group: {(re.match(regex, str)).group(4)}\n''')
                break
            raise
        except:
            print("You entered the GROUP NAME incorrectly! ==> TRY AGAIN!")
            continue

    # в строке неиже указано только имя файла, т.к. этот-txt находится в этой же директории с ПРОГОЙ PT_11
    file_name = "specialties and courses.txt"
    while True:
        try:
            action = int(input('''What do you want to do with the file?
1 = update SPECIALTY in GROUP NAME
2 = update COURSE in GROUP NAME
3 = read full file
4 = read only detailed inf (about current SPECIALTY and COURSE) in GROUP NAME
5 = END PROGRAM EXECUTION!!!!!!!
Your choise?: '''))
            print()
            # 5 = (add/update) inf about current SPECIALTY in GROUP NAME
            # 6 = (add/update) inf about current COURSE in GROUP NAME

            if action == 1:
                i=0
                while i == 0:
                    last_correct_str = str
                    specialty = input(f"Past correct GROUP NAME ({str}) ---> New SPECIALTY (max specialties [1-->9]) for GROUP NAME: ")
                    if specialty == (re.match(r"^([\d]{1})$", specialty)).group():
                        str = str.replace((re.match(regex, str)).group(2), specialty, 1)
                        print(f"Now GROUP NAME ({str})\n")
                        i=1
                    else:
                        raise

            elif action == 2:
                i=0
                while i == 0:
                    last_correct_str = str
                    course = input(f"Past correct GROUP NAME ({str}) ---> New COURSE (courses [1-->6]) for GROUP NAME: ")
                    if course == (re.match(r"^([\d]{1})$", course)).group() and 0 < int(course) < 7:
                        str = str[:-2]+course+str[-1:]
                        print(f"Now current GROUP NAME: {str}\n")
                        i=1
                    else:
                        raise

            elif action == 3:
                Print_File(file_name)

            elif action == 4:
                print(f"░░░░░░░ DETAILED INF from '{file_name}' ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                with open(file_name, "r+", encoding="utf-8") as file:
                    print(f"IN GROUP NAME ({str})\n░░ 1st digit ({(re.match(regex, str)).group(2)}) after (-) is:") # вывод инф про СПЕЦИАЛЬНОСТЬ
                    contents = file.readlines()
                    switch = 0 # нужен для продолжения печати если нашлась СПЕЦИАЛЬНОСТЬ
                    switch_inf_printed = 0 # контролирует напечатается ли СПЕЦИАЛЬНОСТЬ, если останется = 0, то с пом этой перем выведется что инфы нет
                    for index, line in enumerate(contents):
                        if line == f'{(re.match(regex, str)).group(2)} - Specialty\n':
                            print(line[:-1])
                            switch = 1
                            switch_inf_printed = 1
                        elif switch == 1:
                            if re.search(r'[\d] - Course\n|[\d] - Specialty\n', line) or re.match(r'\n', line) or index == len(contents)-1:
                                switch = 0
                                switch_inf_printed = 0
                                break
                            print(line[:-1])
                        elif switch_inf_printed == 0 and index == len(contents)-1:
                            print(f"In file '{file_name}' no detailed inf about the SPECIALTY")
                            break
                            
                    print(f"░░ 2nd digit ({(re.match(regex, str)).group(3)}) after (-) is:") # вывод инф про КУРС
                    switch_inf_specialty_have = 0
                    for index, line in enumerate(contents):
                        if line == f'{(re.match(regex, str)).group(2)} - Specialty\n' or switch_inf_specialty_have == 1:
                            if line == f'{(re.match(regex, str)).group(3)} - Course\n':
                                print(line[:-1])
                                switch = 1
                                switch_inf_printed = 1
                            elif switch == 1:
                                if re.search(r'[\d] - Course\n|[\d] - Specialty\n', line) or re.match(r'\n', line) or index == len(contents)-1:
                                    switch = 0
                                    switch_inf_specialty_have = 0
                                    break
                                print(line[:-1])
                            elif switch_inf_printed == 0 and index == len(contents)-1:
                                print(f"In file '{file_name}' no detailed inf about the COURSE")
                                break
                            else:
                                switch_inf_specialty_have = 1
                        elif switch_inf_printed == 0 and index == len(contents)-1:
                            print(f"In file '{file_name}' no detailed inf about the COURSE")
                            break
                print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

            # elif action == 5:
            #     with open(file_name, "r+", encoding="utf-8") as file:
            #         contents = file.readlines()
            #         print(contents)

            #     for index, line in enumerate(contents):
            #         if line == f'{(re.match(regex, str)).group(2)} - Specialty\n': # поиск - если есть СПЕЦИАЛЬНОСТЬ ==> заменить описание
            #             print(line[:-1])
            #                 switch = 1
            #                 switch_inf_printed = 1
            #             elif switch == 1:
            #                 if re.search(r'[\d] - Course\n|[\d] - Specialty\n', line) or re.match(r'\n', line) or index == len(contents)-1:
            #                     switch = 0
            #                     switch_inf_printed = 0
            #                     break
            #                 print(line[:-1])
            #             elif switch_inf_printed == 0 and index == len(contents)-1:
            #                 print(f"In file '{file_name}' no detailed inf about the SPECIALTY")
            #                 break

            #         elif : # поиск - если нет СПЕЦИАЛЬНОСТИ ==> создать № СПЕЦИАЛЬНОСТИ и сделать описание


            #     with open(file_name, 'w', encoding="utf-8") as file:
            #         for s in contents:
            #             file.write(s)
                
            #     Print_File(file_name)

                # ///////////////////////////////////////////////////////////////////////////////////////////////////////

                # file.write(input("Enter what you want to write to the file:\n")+r"\n")
                # file.flush() # то что вы записали записалось в буфер и пока в файле не появится, пока он не будет закрыт или 2 решение
                # # эта строка сразу скинет с буфера в файл вами записанные данные
                # print()
                
                # contents = file.readlines()
                # contents[0] = 'some new text\n'
                # file.close()

                # with open(file_name, 'w') as file:
                #     file.writelines(['one', 'two'])
                
                # new_rows = []

                # i = 1
                # while i > 0 or i != '':
                #     new_row = input((f'Enter new row-{i}: '))
                #     if new_row != '':
                #         new_rows.append(new_row)
                #         i += 1
                #     else:
                #         i = ''

                # with open(file_name, 'w') as file:
                #     file.writelines("%s\n" % r for r in new_rows)

                # if str not in file: # добавление инф, если в переменной STR новые СПЕЦИАЛЬНОСТЬ и КУРС

                #     name_group = 
                #     input(f'''This is a new SPECIALTY and COURSE, please enter datailed inf!
                # about the SPECIALTY ({name_specialty}):\n''')
                #     input("about the COURSE ():\n")
                #     open file
                #     add in file

                # if str.group(0): # добавление инф, если в переменной STR новая только СПЕЦИАЛЬНОСТЬ

                # if str.group(2): # добавление инф, если в переменной STR новый только КУРС под определенную специальность

            # elif action == 6:
            #     pass

            elif action == 5:
                break

            else:
                raise
        except:
            print("At one of the stages you entered some nonsense! ===> TRY AGAIN!\n")
            if action == 1 or 2:
                str = last_correct_str
                print(f"GROUP NAME remained intact ({str})")
            continue
