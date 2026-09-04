sentence = input("Enter a sentence: ")
  letter_count = 0
for char in sentence:
  if char.isalpha():
    letter_count += 1
print("LETTERS", letter_count)
