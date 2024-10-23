def percentage_grade_calc():
    percentage=0
    phy=float(input("Enter marks for Physics: "))
    chem=float(input("Enter marks for Chemistry: "))
    bio=float(input("Enter marks for Biology: "))
    math=float(input("Enter marks for Mathematics: "))
    comp=float(input("Enter marks for Computer: "))
    percentage = 100 * (phy+chem+bio+math+comp)/500

    print('Percentage: %f' % (percentage))

    if percentage>=90:
        print("Grade A")
    if percentage>=80:
        print("Grade B")
    if percentage>=70:
        print("Grade C")
    if percentage>=60:
        print("Grade D")
    if percentage>=40:
        print("Grade E")
    if percentage<40:
        print("Grade F")

percentage_grade_calc()