b=50
c=0
print("Amount Due: "+str(b))
while b>0:
    a=int(input("Insert Coin:"))
    if a==25 or a==10 or a==5:
        b=b-a
        print("Amount Due: "+str(b))
        c=c+a
    else:
        print("Amount Due: "+str(b))
if c>=50:
    print("Change Owed: "+ str(c-50))
