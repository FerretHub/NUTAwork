from ipaddress import summarize_address_range
import random

def decorator(func):
    def wrap(*args):
        print("░░░░░░░ PRINTED ARRAY ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        func(*args)
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
    return wrap

@decorator
def Print_Array(array):
    for row in range(len(array)): # ищет строку массива с MAX длинной
                len_row = len(array[row])
                if row == 0:
                    max_len_row = len_row
                elif 0 < row < len(array) and max_len_row < len_row:
                    max_len_row = len_row
    
    for column in range(max_len_row): # печатает сверху массива номера столбцов
        if column == 0:
            print(f"{' '*(len(str(len(array)))+4)}{column+1}", end="")
        else:
            print(f"    {column+1}", end="")
    print()

    for row in range(len(array)):
        if row == 0:                    print(f"{row+1}{' '*len(str(len(array)-len(str(row+1))))} [{array[row]}")
        elif 0 < row < len(array)-1:    print(f"{row+1}{' '*len(str(len(array)-len(str(row+1))))}  {array[row]}")
        else:                           print(f"{row+1}{' '*len(str(len(array)-len(str(row+1))))}  {array[row]}]")

def Delete_Row_With_Min_Value(array):
    print("░░░░░░░ DELETING A ROW ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    count_rows = len(array) # для проверки если все строки будут пустые --- [[],[],[]], то ниодна не удалится

    switch_boolean_for_min_value = False # переключатель контроллер (проверяет, записывалось ли что-то 
    # в переменную min_value - нужно для того чтоб контролить в массиве первые пустые строки [[],[],[-20, 50]])

    for row in range(len(array)):
        if len(array[row]) == 0:
            continue
        else:
            minn = min(array[row])
            if switch_boolean_for_min_value == False:
                min_value = minn
                index_delete_row = row
                switch_boolean_for_min_value = True
            elif 0 < row < len(array):
                if minn < min_value:
                    min_value = minn
                    index_delete_row = row
        count_rows-1 # если все строки будут пустыми --- [[],[],[],...], 
        # то этот счетчик не отминусуется ==> ниче не удалится ==> выведется что НИЧЕ НЕ УДАЛЕНО! (см ниже)

    if count_rows > len(array):
        array.pop(index_delete_row)
        print(f"Will be deleted ({index_delete_row+1}) row with min value ({min_value})")
        Print_Array(array)
    else:
        print("ROW was not deleted because all rows are empty!\n")

def Add_Column(array):
    print("░░░░░░░ ADDING A COLUMN ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    while True:
        try:
            sum_len_rows = 0 # проверка, если в итоге эта переменная останется = 0, ==> в пустоту нечего добавить
            for row in array:
                sum_len_rows += len(row)
            if sum_len_rows == 0:
                print("Nowhere to add a new column, because there are no columns AT ALL!\n")
                break

            switch_add_column = int(input('''1 = manual mode
2 = auto-random mode
Your choice?: '''))
            if 1 > switch_add_column > 2:
                raise
            
            for row in range(len(array)): # ищет строку массива с MAX длинной
                len_row = len(array[row])
                if row == 0:
                    max_len_row = len_row
                elif 0 < row < len(array) and max_len_row < len_row:
                    max_len_row = len_row
            
            if switch_add_column == 1:
                column_K = int(input(f'''Enter K (= 1--->{max_len_row}) --- this is the № column after which
the new column will be inserted (where you will insert the available values): '''))
                if column_K < 1 or column_K > max_len_row:
                    raise

                for row in range(len(array)):
                    if column_K-1 == len(array[row])-1:
                        array[row].append(random.randint(value_A, value_B))
                        print(f"Added to row ({row+1}) column ({column_K+1}) with value ({array[row][column_K]})")
                    elif 0 <= column_K-1 < len(array[row]):
                        array[row].insert(column_K, random.randint(value_A, value_B))
                        print(f"Added to row ({row+1}) column ({column_K+1}) with value ({array[row][column_K]})")
                    elif column_K-1 > len(array[row])-1:
                        print(f"Add to row ({row+1}) column ({column_K+1}) impossible!")
                Print_Array(array)
                break

            elif switch_add_column == 2:
                column_K = random.randint(1, max_len_row)
                print(f'''Entered K (from range [1--->{max_len_row}]) = {column_K} --- this is the № column after which
the new column will be inserted (where you will insert the available values)''')

                for row in range(len(array)):
                    if column_K-1 == len(array[row])-1:
                        array[row].append(random.randint(value_A, value_B))
                        print(f"Added to row ({row+1}) column ({column_K+1}) with value ({array[row][column_K]})")
                    elif 0 <= column_K-1 < len(array[row]):
                        array[row].insert(column_K, random.randint(value_A, value_B))
                        print(f"Added to row ({row+1}) column ({column_K+1}) with value ({array[row][column_K]})")
                    elif column_K-1 > len(array[row])-1:
                        print(f"Add to row ({row+1}) column ({column_K+1}) impossible!")
                Print_Array(array)
                break
        except:
            print("At one of the stages you entered some nonsense! ===> TRY AGAIN!")
            continue

    


if __name__ == "__main__":
    print('''
████████████████████████████████████████████████████████████████████████
███████ ᕦ(★_★ˇ)ᕤ  ███ PRACTICAL TASK 8 - ARRAY CONVERSION ██████████████
████████████████████████████████████████████████████████████████████████
███████ [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] ███ START PROGRAM ███ ¯\_( ͡❛ ͜ʖ ͡❛)_/¯ ███o(╥﹏╥)o██████
████████████████████████████████████████████████████████████████████████
CODE creates an NxM dynamic array,
removes the row with the min value,
adds a new column after the column with № K\n''')

    array = []

    print("Enter range for randomizer(A ---> B)")
    value_A, value_B = int(input("A = ")), int(input("B = "))
    print()

    for i in range(n := int(input("Enter N(rows), preferably >1 = "))):
        array_columns = []
        for j in range(m := int(input(f"For {i+1}-row M(columns), [0--->10.000 :D] = "))):
            array_columns.append(random.randint(value_A, value_B))
        array.append(array_columns)

    Print_Array(array)
    Delete_Row_With_Min_Value(array)
    Add_Column(array)
