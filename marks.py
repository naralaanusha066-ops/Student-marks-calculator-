# Student Marks Calculator - Made by Anusha

print("--- Student Marks Calculator ---")

name = input("Student Name: ")
telugu = int(input("Telugu Marks: "))
english = int(input("English Marks: "))
maths = int(input("Maths Marks: "))
science = int(input("Science Marks: "))
social = int(input("Social Marks: "))

total = telugu + english + maths + science + social
percentage = total / 5

print("\nName:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A+ - Excellent!")
elif percentage >= 75:
    print("Grade: A - Very Good!")
elif percentage >= 60:
    print("Grade: B - Good!")
elif percentage >= 40:
    print("Grade: C - Pass!")
else:
    print("Grade: Fail - Try Again!")
