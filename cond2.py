score = input("Enter Score: ")
try:
    fs = float(score)
    if fs >= 0.9:
        print("A")
    elif fs >= 0.8:
        print("B")
    elif fs >= 0.7:
        print("C")
    elif fs >= 0.6:
        print("D")
    elif fs < 0.6:
        print("F")
except:
    print("Error, please enter value between 0.0 and 1.0")
