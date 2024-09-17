from datetime import date

# 1:Function to calculate age:
def calc_age():
    while True:
        print("1->Press 1 to calculate age.")
        print("2->Press 'q' any time to go to main manu.")
        choice = input("Enter your choice : ")
        if choice == "1":
            # Getting the date of birth from user 
            birthDay   = input("Enter the day of birth   : ")
            if birthDay == 'q':
                break

            birthMonth = input("Enter the month of birth : ")
            if birthMonth == 'q':
                break

            birthYear  = input("Enter the year of birth  : ")
            if birthYear == 'q':
                break

            # Current date
            current_day   = date.today().day
            current_month = date.today().month
            current_year  = date.today().year

            # Calculating age
            age_day   = current_day   - int(birthDay)
            age_month = current_month - int(birthMonth)
            age_year  = current_year  - int(birthYear)

            print(f"Yor are of {age_year} years, {age_month} months and {age_day} days.\n")
        elif choice == 'q':
            break

# 2:Function to calculate rectangle area
def rect_area():
    #  # area of rectange = l * w
    while True:
        print("1->Press '1' To Calculate the Area of Ractangle.")
        print("2->Press 'q' any time to go to main manu.")
        choice = input("Enter your choice : ")
        if choice == '1':
            length = input("Enter length of rectagnle    : ")
            if length == "q":
                break

            width  = input("Enter the width of rectangle : ")
            if width == "q":
                break

            areaOfRect : float = float(length) * float(width)
            print(f"Area of rectangle is : {areaOfRect.__round__(2)}\n")

        elif choice == 'q':
            break

# 3:Function to calculate circle area
def circle_area():
    # a = π * r**2
    while True:
        print("1->Press '1' To Calculate the Area of Circle.")
        print("2->Press 'q' ant time to go to main manu.")
        choice = input("Enter your choice : ")
        if choice == '1':
            print("Value of 'π' is constant : 3.14156.")
            r = input("Enter Radius of Circle    : ")
            if r == "q":
                break
            areaOfCircle = (3.14156 * (float(r)**2))
            print(f"Area of rectangle is : {areaOfCircle.__round__(2)}\n")

        elif choice == 'q':
            break

# 4:Function to calculate cube area
def cube_area()->None:
    # a = 6a**2
    while True:
        print("1->Press '1' To Calculate total surface Area of Cube.")
        print("2->Press 'q' to go to main manu.")
        choice = input("Enter your choice : ")
        if choice == '1':
            a = input("Enter surface area of Cube    : ")
            if a == "q":
                break

            areaOfCube : float = (6 * (float(a)**2))
            print(f"Total surface Area of cube is : {areaOfCube.__round__(2)}\n")

        elif choice == "q":
            break

# 5:Function to calculate temperature:
def calc_temp():
    while True:
        print("1-> Choose .1. Calculate from Fahrenheit to Centigrade. ")
        print("2-> Choose .2. Calculate from Centigrade to Fahrenheit. ")
        print("3->Press 'q' any time to go to main manu.")
        choice = input("Enter your choice : ")

        if choice == "1" :
            f = input("Enter the temperature in Fahrenheit : ")
            if f == "q":
                break

            # Formula to calculate celcius from Fahrenheit
            # °C = (°F - 32) / 1.8
            c_temp : float = (float(f) - 32) / 1.8 
            print(f"\nTemperature in Centigrade is : {c_temp.__round__(2)} °C\n")

        elif choice == "2" :
            c = input("Enter the temperature in Centigrade : ")
            if c == "q":
                break

            # Formula to calculate celcius from 
            # °F = (°C * 1.8) + 32
            f_temp : float = (float(c) * 1.8) + 32
            print(f"\nTemperature in Fahrenheit is : {f_temp.__round__(2)} °F\n")
        
        elif choice == "q" :
            break

# 6:Function to calculate time
def calc_time()->None:
    while True:
        print("1->Press '1' To Calculate the seconds conversion.")
        print("2->Press 'q' any time to go to main manu.")
        choice = input("Enter your choice : ")
        if choice == '1':
            s = input("Enter the number of seconds    : ")
            if s == "q":
                break

            mins : int = int(s) // 60
            secs : int = int(s) % 60
            print(f"There are : {mins} Minutes and {secs} seconds in {s} seconds. \n")

        elif choice == 'q':
            break


# 7:Function to calculate percentage
def calc_pecentage():
    while True:
        print("1->Press '1' To Calculate the Area of Ractangle.")
        print("2->Press 'q' to go to main manu.")
        choice = input("Enter your choice : ")
        if choice == '1':
            percent = (input("Enter required percentage : "))
            if percent == 'q':
                break

            total   = (input("Enter the total number    : "))
            if total == 'q':
                break
            percentage : float  = ((float(percent) / float(100) * float(total) ))
            print(f"{percent} percent of {total} is : {percentage}\n")

        elif choice == 'q':
            break

# 8:Function to calculate BMI:
def calc_bmi():
    while True:
        print("1->Press 1 to calculate BMI.")
        print("2->Press 'q' any time to go to main manu.")
        choice = input("Enter your choice : ")
        if choice == "1":
            print("This programme is to calculate BMI of an individual : ")
            name   = input("Enter your name : ")
            if name == 'q':
                break

            weight = input("Enter your weight in kg(kilograms) : ")
            if weight == 'q':
                break

            height = input("Enter your height in exact feet    : ")
            if height == 'q':
                break

            #To convert the feet into meters
            sumInMeter = 3.28
            height : float = float(height) / float(sumInMeter)
            # print(height)

            # Formula to calculate BMI
            # bmi is equal to weight over height in meter squares
            bmi : float = float(weight) / float(height ** 2)
            print(f"{name.title()} your BMI index is : { bmi.__round__(3)} BMI.\n")
        elif choice == 'q':
            break

# 9:Function to calculate volume
def calc_volume()->None:
    # V = πr2h
    while True:
        print("1->Press '1' To Calculate the volume of Cylinder.")
        print("2->Press 'q' to go to main manu.")
        choice = input("Enter your choice : ")
        if choice == '1':
            print("Value of 'π' is constant     : 3.14156.")
            rad = input("Enter the Radius of Cylinder : ")
            if rad == 'q':
                break

            height = input("Enter the height of Cylinder : ")
            if height == 'q':
                break

            vol : float = float(3.14156) * float(rad) * float(rad) * float(height)
            print(f"Total Volume of Cylinder is  : {vol}\n")

        elif choice == 'q':
            break
