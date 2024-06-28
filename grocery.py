grocery = {}
while True:
    try:
        item = input().strip().lower()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1

    except EOFError:
        for key in sorted(grocery.keys()):
            print(f"{grocery[key]} {key.upper()}")
        break


