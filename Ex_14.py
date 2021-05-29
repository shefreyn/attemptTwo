mixedIn = input('Enter a sentence with a mix of upper and lowercase letters : ')
upper = 0
lower = 0
for ch in mixedIn:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1
print(f"Number of uppercase chars : {upper} and Number of lowercase chars : {lower}")