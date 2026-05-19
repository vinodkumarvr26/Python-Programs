limit = int(input("Enter the limit: "))
# Initialize the sum
sum = 0
for i in range(1, limit + 1):
  sum += i
print("The sum of natural numbers up to", limit, "is:", sum)
