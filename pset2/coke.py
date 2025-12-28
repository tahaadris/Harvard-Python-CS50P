amount_due = 50

while amount_due > 0:
    print("Amount Due:", amount_due)
    user_input = int(input("Insert Coin: "))    
    if user_input in [25, 10, 5]:
        amount_due -= user_input

print("Change Owed:", abs(amount_due))