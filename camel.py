a=input("camelCase: ")
result =""
for i in a:
    if i.isupper():
        result=result+ "_" + i.lower()
    else:
        result=result+i
print(result)
