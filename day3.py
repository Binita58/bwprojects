# a = int(input("Enter your marks: "))
# if a < 0 or a > 100:
#     print("Invalid input! Please enter marks between 0 and 100.")
# else:
#     if a >= 80:
#         print("Distinction")
#     elif a >= 60:
#         print("First Division")
#     elif a >= 45:
#         print("Second Division")
#     elif a >= 32:
#         print("Third Division")
#     else:
#         print("Failed")


"""
a = input("Enter your marks: ")
if not a.isdigit():
    print("Please enter the number between 0-100.")
else:
    a = int(a)
    if a < 0 or a > 100:
        print("Invalid input! Please enter marks between 0 and 100.")
    else:
        if a >= 80:
            print("Distinction")
        elif a >= 60:
            print("First Division")
        elif a >= 45:
            print("Second Division")
        elif a >= 32:
            print("Third Division")
        else:
            print("Failed")

"""

# b= input("Enter your age ")
# if not b.isdigit():
#     print("Enter your age in number")
# else:
#     b=int(b)
#     if b>= 18 and b.is_dl and b.is_v:
#         print("You are eligible to drive")

# USING BOOLEAN AND NESTED IF
# has_license = input("Do you have a driving license?").lower()
# has_ride = input("Do you have your own ride?").lower()
# age = input("Enter your age ")
# if not age.isdigit():
#     print("Enter your age in number")
# elif age = int(age):

    # has_license = input("Do you have a driving license?").lower()
    # has_ride = input("Do you have your own ride?").lower()
    # is_license = True if license == "yes" else False
    # is_ride = True if ride == "yes" else False
    # if age>=18:
    # if has_license=="yes":
    #     if has_ride=="yes":
    #         print("You are allowed to drive alone")
    #     else:
    #         print("You have a license but not a ride")
    # else:
    #     print("You are not allowed to drive")


        

# Employee_Experience = input("Enter Employee_Experience: ")
# Employee_Performance = input("Enter Employee_Performance: ")
# Employee_Attendance = input("Enter Employee_Attendance: ")


# if (Employee_Experience.replace('.', '', 1).isdigit() and
#     Employee_Performance.replace('.', '', 1).isdigit() and
#     Employee_Attendance.replace('.', '', 1).isdigit()):
    
#     Employee_Experience = float(Employee_Experience)
#     Employee_Performance = float(Employee_Performance)
#     Employee_Attendance = float(Employee_Attendance)


#     if Employee_Experience >= 5:
#         if Employee_Performance >= 4.5:
#             if Employee_Attendance >= 95:
#                 print("Diamond")
#             else:
#                 print("Not eligible")
#         else:
#             print("Not eligible")

#     elif 2 <= Employee_Experience < 5:
#         if Employee_Performance >= 4:
#             if Employee_Attendance >= 85:
#                 print("Platinum")
#             else:
#                 print("Not eligible")
#         else:
#             print("Not eligible")

#     else:
#         print("Not eligible")

# else:
#     print("Please enter numeric values only!")


experience = 5
rating = 5.5
attendance = 95

if experience >= 5:
    if rating >= 4.5:
        if attendance >= 95:
            print("Your experience is",experience,"years", "rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Platinum")
        elif attendance >= 85:
            print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Gold")
        else:
            print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Silver")
    elif rating >= 3.5:
        if attendance >= 90:
            print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Silver")
        else:
            print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Bronze")
    else:
        print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is No Bonus")
        
elif experience >= 2:
    if rating >= 4:
        print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Silver")
    elif rating >= 3:
        print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Bronze")
    else:
        print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is No Bonus")
else:
    print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","You are not eligible")



'''Write a program that asks the user for three numbers and determines:
The largest number , The smallest number, Whether all three numbers are even, 
Whether the average is greater than 50

n1=int(input("Enter the first number "))
n2=int(input("Enter the second number "))
n3=int(input("Enter the third number "))
if n1>n2 and n1>n3:
    print("The largest number is n1")
elif n2>n1 and n2>n3:
    print("The largest number is n2")
else:
    print("The largest number is n3")
    if n1<n2 and n1<n3:
        print("The smallest number is n1")
    elif n2<n1 and n2<n3:
        print("The smallest number is n2")
    else:
        print("The smallest number is n3 ")
        if n1%2==0 and n2%2==0 and n3%2==0:
            print("All the numbers are even")
        else:
            print("Not all the numbers are even")
            avg=(n1+n2+n3)/3
            print("The average of the given numbers is ")
            if avg>50:
                print("The average of the numbers if greater than 50")
            else:
                print("The average of the numbers is less than 50")'''
    

