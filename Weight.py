weight = float(input("Weight: "))
letter = input("(K)g or (L)bs: ")

if letter == "k" or letter == "K":
    weight *= 2.2
    print("Weight in Lbs: " + str(weight))
elif letter == "l" or letter == "L":
    weight /= 2.2
    print("Weight in Kg: " + str(weight))
else:
    print("Invalid letter!")
print ("Done!")