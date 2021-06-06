passSugg = input('PassWord Requirements: \n1 - 6 characters Min & 12 Max  \n2 - One uppercase and One Lowercase  \n3 - One Number and one Special Char[#,$,&]\nEnter password Suggestions : ')
passlist = passSugg.split(',')
successPass = []
for x in range(len(passlist)):                            # Iterate through List
    passInput = passlist[x]                               #list value to variable
    print(f'Checking Pass.....({passInput})')
    if len(passInput) < 6 or len(passInput) > 12:         # Pass Length Check
        print('Pass length requirements do not meet !')
        continue
    for char in passInput:                                # boolean for uppercase in password
        charUpper = False
        if char.isupper() == True:
            charUpper = True
            break
        else : 
            continue
    for char in passInput:                                # boolean for lowercase in password
        charLower = False
        if char.islower() == True:
            charLower = True
            break
        else : 
            continue
    for char in passInput:                                # boolean for Number in password
        charNum = False
        if char.isalpha() == True:
            charNum = True
            break
        else : 
            continue
    for char in passInput:                                # boolean for symbol in password
        charSymbol = False
        if char == '@' or char == '!':
            charSymbol = True
            break
        else : 
            continue

    if charUpper == False:
        print('No upper CAse')
    elif charLower == False:
        print('No Lower Case')
    elif charNum == False:
        print('No numbers')
    elif charSymbol == False:
        print('No Special Characters')
    if charUpper == True and charLower == True and charNum == True and charSymbol == True:
        print(f'{passInput} works !!')