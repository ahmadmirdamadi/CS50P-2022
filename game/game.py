import random

while True:
    try:
        sath = int(input("enter sath: "))
        if sath > 0:
            break
    except:
        pass

rn = random.randint(1, sath)

while True:
    try:
        g = int(input("guess: "))
        if g > 0:
            if g < rn:
                print("Too small!")
            elif g > rn:
                print("Too large!")
            else:
                print("Just right!")
                break

    except:
        pass