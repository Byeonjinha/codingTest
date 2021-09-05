
def Selfnumber(startnum,n):
    natural=set(range(startnum,n))
    generate = set()
    for A in range(startnum,n):
        for B in str(A):
            A+=int(B)
        generate.add(A)

    selfnum=sorted(natural-generate)
    for A in selfnum:
        print(A)



Selfnumber(33,10001)

