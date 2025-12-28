months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ").title().strip()
    try:
        if "/" in date:
            month , day , year = date.split("/")
            if (0 < int(month) <=12) and (0 < int(day) <= 31):
                month = int(month)
                day = int(day)
                year = int(year)
                break
        elif "," in date: 
            date = date.replace(",","")
            month , day , year = date.split(" ")
            if (month in months) and (0 < int(day) <= 31):
                month = months.index(month) + 1
                day = int(day)
                year = int(year)
                break
            
    except ValueError:
        pass
print(f"{year}-{month:02}-{day:02}")
