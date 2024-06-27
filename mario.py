a=int(input("side length of the sqaure?"))
b=a-1
for i in range(a):
    print("#"*(a-b))
    b=b-1

a=int(input("side length of the sqaure?"))
b=a-1
for i in range(a):
    print(" "*b + "#"*(a-b))
    b=b-1

