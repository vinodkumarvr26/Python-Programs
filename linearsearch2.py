n = int(input("Enter number of students: "))
roll_numbers = []
print("Enter roll numbers of students:")
for i in range(n):
    roll = int(input("enter roll number  "))
    roll_numbers.append(roll)

# Read roll number to search
search_roll = int(input("Enter roll number to search: "))

# Linear Search using for-else
for roll in roll_numbers:
    if roll == search_roll:
        print("Student has submitted the assignment.")
        break
else:
    print("Student has not submitted the assignment.")
