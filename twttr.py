a = input("Input: ")
vowels = ["a","e","o","i","u","A","E","I","O","U"]
print("Output: ", end="")

for i in a:
    if i not in vowels:
        print(i, end="")

print("")
