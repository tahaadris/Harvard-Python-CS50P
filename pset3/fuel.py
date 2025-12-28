while True:
    fraction = input("Fraction: ")
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        percentage = x/y * 100
        if x < 0 or y < 0:
            continue
        if percentage <= 1 and x <= y:
            print("E")
            break
        elif percentage >= 99 and x <= y:
            print("F")
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else: 
        if x<=y:
            print(round(percentage),"%",sep="")
            break

        