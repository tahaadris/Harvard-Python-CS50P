user_input = input("Input: ")
Output = ""

for alphabet in user_input:
    if alphabet in ["a","A","E","e","I","i","O","o","U","u"]:
        continue
    else:
        Output += alphabet
print("Output:" , Output)

