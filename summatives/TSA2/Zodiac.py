month = int(input("Enter Month: "))
day = int(input("Enter Day: "))

months = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December',
}

if month <= 0 and day <= 0:
    print("[INVALID MONTH AND DAY] No Negative or Zero Inputs")
elif day <= 0:
    print("[INVALID DAY] No Negative or Zero Inputs")
elif month <= 0 or month >= 13:
    print("[INVALID MONTH]")

elif month == 1:
    if(day <= 19):
        print(f"{months[month]} {day} is Capricorn")
    elif(day <= 31):
        print(f"{months[month]} {day} is Aquarius")
    else:
        print(f"[INVALID DAY] There is no {day} in {months[month]}")

elif month == 2:
    if(day <= 18):
        print(f"{months[month]} {day} is Aquarius")
    elif(day <= 29):
        print(f"{months[month]} {day} is Pisces")
    else:
        print(f"[INVALID DAY] There is no {day} in {months[month]}")

elif month == 3:
    if(day <= 20):
        print(f"{months[month]} {day} is Pisces")
    elif(day <= 31):
        print(f"{months[month]} {day} is Aries")
    else:
        print(f"[INVALID DAY] There is no {day} in {months[month]}")

elif month == 4:
    if(day <= 19):
        print(f"{months[month]} {day} is Aries")
    elif(day <= 30):
        print(f"{months[month]} {day} is Taurus")
    else:
        print(f"[INVALID DAY] There is no {day} in {months[month]}")      

elif month == 5:
    if(day <= 20):
        print(f"{months[month]} {day} is Taurus")
    elif(day <= 31):
        print(f"{months[month]} {day} is Gemini")
    else:
        print(f"[INVALID DAY] There is no {day} in {months[month]}")        

elif month == 6:
    if(day <= 20):
        print(f"{months[month]} {day} is Gemini")
    elif(day <= 30):
        print(f"{months[month]} {day} is Cancer")
    else:
        print(f"[INVALID DAY] There is no {day} in {months[month]}")  

elif month == 7:
    if(day <= 22):
        print(f"{months[month]} {day} is Cancer")
    elif(day <= 31):
        print(f"{months[month]} {day} is Leo")
    else:
        print(f"[INVALID DAY] There is no {day} in {months[month]}")  

elif month == 8:
    if(day <= 22):
        print(f"{months[month]} {day} is Leo")
    elif(day <= 31):
        print(f"{months[month]} {day} is Virgo")
    else:
        print(f"[INVALID DAY] There is no {day} in {months[month]}")  

elif month == 9:
    if(day <= 22):
        print(f"{months[month]} {day} is Virgo")
    elif(day <= 30):
        print(f"{months[month]} {day} is Libra")
    else:
        print(f"[INVALID DAY] There is no {day} in {months[month]}")  

elif month == 10:
    if(day <= 22):
        print(f"{months[month]} {day} is Libra")
    elif(day <= 31):
        print(f"{months[month]} {day} is Scorpio")
    else:
        print(f"[INVALID DAY] There is no {day} in {months[month]}")  

elif month == 11:
    if(day <= 21):
        print(f"{months[month]} {day} is Scorpio")
    elif(day <= 30):
        print(f"{months[month]} {day} is Sagittarius")
    else:
        print(f"[INVALID DAY] There is no {day} in {months[month]}")  

elif month == 12:
    if(day <= 22):
        print(f"{months[month]} {day} is Sagittarius")
    elif(day <= 31):
        print(f"{months[month]} {day} is Capricorn")
    else:
        print(f"[INVALID DAY] There is no {day} in {months[month]}")  
