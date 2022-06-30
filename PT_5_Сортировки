import random


def Exchange_Bubble_Sort():
    for i in range(amount-1):
        print(f"Iteration {i+1}")
        for j in range(amount-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print(f"    Indices {j+1}<-->{j+2}: {array}")
            else:
                print(f"    Indices {j+1}    {j+2}: {array}")

def Selection_Sort():
    for i in range(amount-1):
        print(f"Iteration {i+1}")
        index_min_value = i
        j = i+1
        while j < amount:
            if array[j] < array[index_min_value]:
                index_min_value = j
            j += 1
        array[i], array[index_min_value] = array[index_min_value], array[i]
        print(f"    Indices {i+1}<-->{index_min_value+1}: {array}")

def Insertion_Sort():
    for i in range(1, amount):
        print(f"Iteration {i}")
        key = array[i]
        print(f"    key = index {i+1} = {array[i]}")
        j = i-1
        while j >= 0 and array[j] > key :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        print(f"    KEY insert in index {j+2}: {array}")


if __name__ == "__main__":
    print('''
████████████████████████████████████████████████████████████████████████
███████ ᕦ(★_★ˇ)ᕤ  ███ PRACTICAL TASK 5 - SORTING ███████████████████████
████████████████████████████████████████████████████████████████████████
███████ [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] ███ START PROGRAM ███ ¯\_( ͡❛ ͜ʖ ͡❛)_/¯ ███o(╥﹏╥)o██████
████████████████████████████████████████████████████████████████████████
CODE sorts random numbers using 1 of 3 sorting methods
1 - exchange (обменом - пузырьковая сортировка)
2 - selection (выбором)
3 - insertion (вставками)\n''')
    sort_methods = {
        '1': Exchange_Bubble_Sort,
        '2': Selection_Sort,
        '3': Insertion_Sort}

    while True:
        try:
            print("Enter range for randomizer(A ---> B)")
            value_A, value_B = int(input("A = ")), int(input("B = "))
            amount = int(input("Enter AMOUNT of numbers, what will be generated = "))
            array = [random.randint(value_A, value_B) for _ in range(amount)]
            print(f"Array created: {array}")
            break
        except:
            print("At one of the stages you entered some nonsense! ===> TRY AGAIN!")
            continue
    what_method = input("What sort method to use? (1 | 2 | 3): ")

    print(f"░░░░░░░ START {what_method} METHOD ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    sort_methods[what_method]()
    print(f'''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
RESULT: {array}
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n''')
