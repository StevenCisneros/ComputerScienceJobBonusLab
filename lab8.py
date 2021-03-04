#Steven Cisneros
#Professor Nguyen
#CIS 103-20324-LEC
#12 March 2020

RANGE0 = 1000

RANGE1 = 3000

RANGE2 = 6000

RANGE3 = 6001

BONUS1 = 0

BONUS2 = 25

BONUS3 = 50

BONUS4 = 100

BONUS5 = 200

bonus = 0

last_name = input("Enter the last name: ")

first_name = input("Enter the first name: ")

tyString = input("Enter this year's units: ")
this_year = float(tyString)

lyString = input("Enter last year's units: ")
last_year = float(lyString)

if this_year > last_year:
    if this_year<=RANGE0:
        bonus = BONUS2
    else:
        if this_year<=RANGE1:
            bonus = BONUS3
        else:
            if this_year<=RANGE2:
                bonus = BONUS4
            else:
                this_year<=RANGE3
                bonus = BONUS5

else:
    bonus = BONUS1

print(last_name,",",first_name)

print("Bonus is $",bonus)
    


