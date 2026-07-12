n = int(input("Enter number of students: "))
marks = []
print("Enter marks of each student:")
for i in range(n):
    m = int(input(f"Student {i+1}: "))
    marks.append(m)
max_mark = marks[0]
for i in range(1, n):
    if marks[i] > max_mark:
        max_mark = marks[i]
print("\nHighest mark in the class:", max_mark)
