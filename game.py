import random

while True:
    try:
        value=int(input("Level:"))
        if value>0 and value<100:
            value=random.randint(1, value)
            while True:
                guess=int(input("Guess:"))
                if guess < value:
                    print("Too small!")
                elif guess > value:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        else:
            continue

    except ValueError:
        continue
    break
