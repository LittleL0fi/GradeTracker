print("welcome " + name, "to your Grade Tracker")

grade1 = int(input("Enter your first grade: "))
print(f"your first grade is: {grade1}")

grade2 = int(input("Enter your second grade:"))
print(f"your second grade is: {grade2}")

grade3 = int(input("Enter your third grade:"))
print(f"your third grade is: {grade3}")


while grade1 < 0 or grade1 > 100:
    print("Error: Grade 1 is out of range. Please enter a grade between 0 and 100.")
    grade1 = int(input("Enter your first grade: "))

while grade2 < 0 or grade2 > 100:
    print("Error: Grade 2 is out of range. Please enter a grade between 0 and 100.")
    grade2 = int(input("Enter your second grade: "))

while grade3 < 0 or grade3 > 100:
    print("Error: Grade 3 is out of range. Please enter a grade between 0 and 100.")
    grade3 = int(input("Enter your third grade: "))
    
    average = (grade1 + grade2 + grade3) / 3
print(f" your average is: {average}")
if average >= 70:
    print("Congratulations! You passed.")
else:
    print("Sorry, you did not pass. Better luck next time.")
    
    
