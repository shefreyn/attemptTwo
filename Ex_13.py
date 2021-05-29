mixedInput = input('Enter a mixed input of string and numbers : ')
letter = 0
number = 0
for ch in mixedInput:
    if ch.isdigit():
        number = number + 1
    elif ch.isalpha() :
        letter = letter + 1
    else :
        print()
print(f"Number of letter's: {letter} \n Number of numbers: {number}")
