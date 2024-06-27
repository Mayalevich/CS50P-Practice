a=input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
if a.strip()=="42":
    print("Yes")
elif a.lower()=="forty-two" or a.lower()=="forty two":
    print("Yes")
else:
    print("No")
