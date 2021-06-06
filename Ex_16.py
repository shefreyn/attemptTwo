accBalance = 0
endTrans = True
def inputfun():
    perform = input("Type 'D' to deposit and Type 'W' to withdraw : ")
    return perform

def withOdep(perform,accBalance):
    if perform == 'd':
        depositAmt = int(input('Enter Amount to be deposited : '))
        accBalance += depositAmt
    elif perform == 'w':
        withdrawAmt = int(input('Enter Amount to be withdrawed : '))
        accBalance -= withdrawAmt
    return accBalance

transOpt = 1
while transOpt == 1:
    transOpt = int(input('press 1 to perform a transaction or 2 to end : ')) 
    if transOpt == 2:
        break
    perform = inputfun()
    accBalance = withOdep(perform,accBalance)
    

print(f'Your Account balance is {accBalance}')