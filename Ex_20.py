def logic(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j % 7 == 0:
            yield j 

for logic(n) in range(100):
    print(n)